# 02-deep-dive-report.md — Báo Cáo Phân Tích Sâu (Phase 3 & 5)

*   **Tên nhóm:** vin-no
    1.  Nguyễn Quang Anh - MSSV: 2A202600608
    2.  Vũ Minnh Duy - MSSV: 2A202600806
    3.  Huỳnh An Nghiệp - MSSV: 2A202600853
---

# 🏗️ Phase 3 — DEEP-DIVE: Phân Tích Chi Tiết Bài Toán

## 3.1. Quyết định Lựa chọn Bài toán Nhóm
Nhóm quyết định chọn bài toán **"Xử lý sự cố pin yếu/hết pin thực địa của xe taxi điện Xanh SM"** để thực hiện thiết kế chi tiết giải pháp AI.

*   **Lý do lựa chọn:**
    *   **Tác động trực tiếp đến doanh thu:** Sự cố cạn kiệt pin giữa đường làm tắc nghẽn hoạt động của xe, gây stress cho tài xế và làm giảm 15% doanh thu của Xanh SM do hủy chuyến và xe không hoạt động thời gian thực.
    *   **Phù hợp với công nghệ hiện tại:** Việc đọc tọa độ, tra cứu trạm sạc trống và soạn thảo tin nhắn hướng dẫn rất phù hợp với mức kiến trúc **LLM Feature**. Rủi ro có thể kiểm soát hoàn toàn bằng cách áp dụng cơ chế con người duyệt trước khi gửi (Human-in-the-loop).
*   **Lý do loại bỏ các bài toán khác:**
    *   *Bài toán phân loại khiếu nại Vinhomes:* Rủi ro pháp lý cao, cần dữ liệu huấn luyện lớn về các điều khoản pháp lý và tranh chấp phí dịch vụ.
    *   *Bài toán tóm tắt hồ sơ Vinmec:* Môi trường y tế có dung sai lỗi cực kỳ thấp (vấn đề an toàn tính mạng), đòi hỏi hệ thống giám sát và phê duyệt y tế lâm sàng phức tạp chưa sẵn sàng ở giai đoạn này.

---

## 3.2. Problem Statement (6-field) — Tiêu Chuẩn Vin Smart Future

| Trường thông tin (Field) | Nội dung chi tiết |
|-------------------------|-------------------|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM. |
| **2. Current Workflow** | 1. Nhận cuộc gọi khẩn cấp báo hết pin từ tài xế.<br>2. Điều phối viên tra cứu vị trí GPS thủ công trên phần mềm nội bộ.<br>3. Mở dashboard bản đồ trạm sạc VinFast để tìm trụ trống gần nhất tương thích dòng xe.<br>4. Viết thủ công tin nhắn chỉ đường/hướng dẫn gửi qua App tài xế.<br>5. Liên hệ xe cứu hộ nếu mức pin cực kỳ khẩn cấp. |
| **3. Bottleneck** | Bước 3 & 4 (mất trung bình 12 phút/lượt): Tra cứu thủ công tính sẵn sàng của các trụ sạc tương thích cổng sạc xe (VF5/VFe34/VF8) và soạn thảo tin nhắn hướng dẫn bằng tiếng Việt thân thiện, rõ ràng dưới áp lực cuộc gọi dồn dập giờ cao điểm. |
| **4. Business Impact** | Hà Nội có trung bình 80 sự cố pin/ngày. Gây mất tổng cộng hơn 20 giờ làm việc thủ công/ngày của đội ngũ điều phối. Thời gian chờ đợi của tài xế lâu làm tăng tỉ lệ hủy chuyến của khách hàng và lãng phí tài nguyên xe. |
| **5. Success Metric** | 1. Giảm tổng thời gian xử lý sự cố từ **15 phút xuống dưới 3 phút**.<br>2. Đảm bảo tỷ lệ định vị đúng trạm sạc có trụ trống và đúng loại cổng sạc phù hợp đạt trên **98%**. |
| **6. Operational Boundary** | **ĐƯỢC PHÉP:** Tự động lấy tọa độ xe, truy vấn API trạm sạc VinFast và soạn thảo tin nhắn hướng dẫn dưới dạng nháp (draft).<br>**CẤM (Ranh giới đỏ):**<br>- CẤM tự ý gửi tin nhắn hướng dẫn cho tài xế mà không có điều phối viên duyệt (bắt buộc gắn thẻ `[DRAFT_ONLY]` đầu tin nhắn).<br>- CẤM đề xuất trạm sạc xa quá 5km khi pin dưới 5%. Thay vào đó, bắt buộc phải trả về JSON yêu cầu cứu hộ di động: `{"action": "dispatch_mobile_charger", "reason": "<explain_why>"}`. |

---

## 3.3. Quy trình tương lai (Future-State Flow) & AI Fit

*   **Mức độ AI Fit:** Chọn mức **LLM Feature** (Quy trình nghiệp vụ có cấu trúc cố định, LLM tham gia xử lý bước đọc dữ liệu thô và sinh văn bản tự nhiên, không dùng Agent tự trị để đảm bảo kiểm soát an toàn).
*   **Quy trình tương lai:**
    1.  **Driver Call:** Tài xế gọi báo sự cố.
    2.  **🔵 AI Step (Auto-Pull & Draft):** Hệ thống tự động lấy tọa độ GPS xe và danh sách trạm sạc gần nhất còn trụ trống. LLM nhận đầu vào này cùng thông tin pin để sinh tin nhắn hướng dẫn chỉ đường.
        *   *Nếu Pin < 5%:* LLM kích hoạt Rule 2, trả về JSON yêu cầu xe cứu hộ.
        *   *Nếu Pin >= 5%:* LLM soạn thảo tin nhắn hướng dẫn, bắt buộc đính kèm tag `[DRAFT_ONLY]` ở đầu.
    3.  **🟢 Human Step (HITL):** Điều phối viên xem tin nhắn nháp (hoặc lệnh cứu hộ), chỉnh sửa nếu cần và bấm nút phê duyệt để gửi đi.
    4.  **↩️ Fallback Plan (Dự phòng):** Nếu mô hình gặp lỗi (không phản hồi hoặc định dạng sai), hệ thống tự động cảnh báo và điều phối viên sẽ chuyển sang tra cứu và soạn tin nhắn thủ công trên phần mềm như quy trình cũ.

---

# 🏁 Phase 5 — EVALUATE: Đánh Giá Khả Thi & Quyết Định

### AI Readiness Checklist

1.  **Value (Giá trị kinh doanh):** `[YES]` - Giảm thời gian chết của xe taxi, tăng hiệu suất hoạt động và giảm tải cho điều phối viên.
2.  **Baseline (Cơ sở so sánh):** `[YES]` - Quy trình cũ xử lý mất 15 phút, tỷ lệ lỗi thủ công trong giờ cao điểm là 8%.
3.  **Eval (Dữ liệu đánh giá):** `[YES]` - Có sẵn logs lịch sử các cuộc gọi báo sự cố và lịch sử điều vận trạm sạc.
4.  **Tolerance (Mức độ chấp nhận sai sót):** `[YES]` - Vì có chốt chặn con người duyệt (HITL) và cơ chế dự phòng (Fallback) nên dung sai lỗi của AI được kiểm soát an toàn.
5.  **Operations (Vận hành & Kỹ thuật):** `[YES]` - Đội ngũ kỹ sư Vin Smart Future làm chủ mã nguồn, có hệ thống giám sát log cuộc gọi.

**Điểm đánh giá sẵn sàng:** **5 / 5 (YES)**

---

### Quyết định của Ban Giám đốc Vin Smart Future:
`[x] GO (Bắt đầu xây dựng Prototype)`

**Lý giải quyết định (Justification):**
*   **Về mặt kỹ thuật:** Nguyên mẫu prompt đã được chạy stress-test thử nghiệm thành công với Gemini 2.5 Flash. Mô hình bảo vệ ranh giới an toàn cực kỳ tốt, phản ứng nhạy bén với trường hợp pin dưới 5% để đề xuất xe cứu hộ và giữ vững tag `[DRAFT_ONLY]` khi bị tấn công prompt bypass.
*   **Hiệu quả chi phí:** Sử dụng mô hình nhẹ `gemini-2.5-flash` có chi phí API cực kỳ thấp (~0.00015 USD/lượt xử lý). Thời gian phát triển giải pháp ngắn vì kiến trúc thuộc dạng LLM Feature đơn giản, không cần xây dựng hệ thống Agent tự trị phức tạp. Thời gian hoàn vốn (ROI) ước tính trong vòng 1.5 tháng sau khi triển khai thực địa.
