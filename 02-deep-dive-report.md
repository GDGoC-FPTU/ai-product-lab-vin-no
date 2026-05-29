# 02 — Deep-Dive Report (Báo cáo nhóm)

> **Lab 02: AI Product Scoping — Vin Smart Future (Vingroup)**

### 👥 Thông tin nhóm
| Họ và Tên | MSSV |
|-----------|------|
| *(Điền tên thành viên 1)* | *(Điền MSSV)* |
| *(Điền tên thành viên 2)* | *(Điền MSSV)* |
| *(Điền tên thành viên 3)* | *(Điền MSSV)* |

---

# 🗳️ Quyết định lựa chọn bài toán Deep-Dive

Nhóm quyết định chọn bài toán **"Card #3 — Vinmec: Trợ lý phân loại lịch hẹn khám theo triệu chứng"** để thực hiện Deep-Dive.

## Lý do lựa chọn và loại bỏ các thẻ khác:

| Thẻ | Quyết định | Lý do |
|-----|-----------|-------|
| **Card #1 — Vinmec Soạn hồ sơ xuất viện** | ❌ Loại | Mặc dù tác động ROI lớn, bài toán yêu cầu tích hợp sâu vào 3 hệ thống y tế riêng biệt (HIS/LIS/PACS) — chi phí kỹ thuật ban đầu quá cao và cần sự phê duyệt phức tạp từ phòng IT bệnh viện. Phù hợp hơn cho giai đoạn scale-up sau khi đã có kinh nghiệm triển khai AI. |
| **Card #2 — Vinhomes Phân loại phản ánh cư dân** | ❌ Loại | Rủi ro thấp nhưng tác động kinh doanh cũng thấp hơn so với y tế. Ngoài ra, bài toán phân loại text thuần túy có thể giải quyết hiệu quả bằng cách kết hợp Rule-based router + keyword matching trước khi cần LLM. |
| **Card #3 — Vinmec Phân loại lịch hẹn khám** | ✅ **Chọn** | Tác động trực tiếp đến trải nghiệm bệnh nhân (18% sai chuyên khoa), chi phí tổn thất rõ ràng (~240 triệu VNĐ/tháng), và giải pháp LLM có lợi thế vượt trội so với rule-based trong việc hiểu ngôn ngữ tự nhiên tiếng Việt mô tả triệu chứng. Scope pilot hẹp, dễ đo lường. |

---

# 🏗️ Phase 3 — DEEP-DIVE: Vinmec — Trợ lý phân loại lịch hẹn khám theo triệu chứng

## 3.1. Current-State Workflow Mapping

> **📎 Sơ đồ quy trình hiện tại:** Xem file [04-workflow-diagram.png](04-workflow-diagram.png)

**Mô tả quy trình hiện tại (4 bước, 7-8 phút/cuộc gọi):**

| Bước | Mô tả | Ai thực hiện | Thời gian | Ghi chú |
|------|-------|-------------|-----------|---------|
| **1** | Bệnh nhân gọi tổng đài Vinmec hoặc nhắn tin qua App mô tả triệu chứng bằng tiếng Việt tự nhiên | Bệnh nhân | — | Input: mô tả bằng ngôn ngữ tự nhiên (thường mơ hồ, viết tắt) |
| **2** | Nhân viên tổng đài nghe/đọc mô tả triệu chứng, tra cứu bảng phân loại triệu chứng – chuyên khoa (bản giấy hoặc file Excel ~200 dòng) | Nhân viên tổng đài | ⏱ **5 phút** 🔴 | **BOTTLENECK:** Nhân viên thiếu kiến thức y khoa chuyên sâu. Triệu chứng mơ hồ có thể thuộc nhiều chuyên khoa (VD: "đau bụng" → Nội tiêu hóa / Ngoại / Sản / Tiết niệu) |
| **3** | Chọn chuyên khoa và bác sĩ phù hợp, xếp lịch hẹn vào hệ thống HIS | Nhân viên tổng đài | ⏱ 2 phút | 🔄 **Handoff:** Chuyển giao giữa tổng đài → HIS → chuyên khoa |
| **4** | Gửi tin xác nhận lịch hẹn cho bệnh nhân qua SMS/App | Nhân viên tổng đài | ⏱ 1 phút | Output: SMS/push notification xác nhận |

**Tổng thời gian thủ công:** ⏱ **7-8 phút/cuộc gọi**

**Tỉ lệ phân loại sai chuyên khoa:** ~**18%** → Bệnh nhân phải đặt lại lịch khám, lãng phí thời gian và slot bác sĩ.

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên tổng đài đặt lịch hẹn khám tại Vinmec (Call Center). Mỗi nhân viên xử lý trung bình 50-70 cuộc gọi/ngày. Nhân viên không có chuyên môn y khoa, chỉ được đào tạo cơ bản về bảng phân loại triệu chứng. |
| **2. Current Workflow** | Bệnh nhân gọi tổng đài hoặc nhắn tin qua App Vinmec mô tả triệu chứng bằng tiếng Việt tự nhiên (ví dụ: *"đau ngực lan ra vai trái, hay khó thở khi leo cầu thang"*). Nhân viên tổng đài nghe/đọc mô tả, tra cứu bảng phân loại triệu chứng – chuyên khoa (bản giấy hoặc file Excel ~200 dòng), chọn chuyên khoa và bác sĩ phù hợp, xếp lịch hẹn vào HIS, rồi gửi tin xác nhận. 4 bước, mất 7 phút/cuộc gọi. |
| **3. Bottleneck** | Bước 2 (mất 5 phút): Nhân viên phải diễn giải mô tả triệu chứng bệnh nhân bằng ngôn ngữ thông thường (thường mơ hồ, trùng lặp giữa nhiều chuyên khoa) rồi tra cứu bảng Excel dài. Ví dụ: *"đau bụng"* có thể thuộc Nội tiêu hóa, Ngoại tổng quát, Sản phụ khoa, hoặc Tiết niệu. Thiếu kiến thức y khoa khiến tỉ lệ sai ~18%. |
| **4. Business Impact** | Với ~300 cuộc gọi đặt lịch/ngày tại một cơ sở Vinmec, 18% sai chuyên khoa = **~54 bệnh nhân/ngày** phải đặt lại lịch → mất thời gian, giảm NPS (Net Promoter Score), và chiếm slot lịch hẹn của bệnh nhân khác. Chi phí xử lý lại mỗi ca sai: ~150.000 VNĐ (chi phí tổng đài + giờ bác sĩ lãng phí). Tổn thất ước tính: ~8 triệu VNĐ/ngày/cơ sở = **~240 triệu VNĐ/tháng**. |
| **5. Success Metric** | 1. Giảm tỉ lệ phân loại sai chuyên khoa từ **18% xuống dưới 5%**. <br> 2. Giảm thời gian xử lý cuộc gọi từ **7 phút xuống dưới 3 phút**. <br> 3. Tỉ lệ bệnh nhân hài lòng với lịch hẹn lần đầu ≥ **92%** (hiện tại ~82%). |
| **6. Operational Boundary** | AI được phép phân tích mô tả triệu chứng bằng tiếng Việt và gợi ý **top 3 chuyên khoa** phù hợp nhất kèm mức độ tự tin (confidence score). **CẤM:** AI không được tự động xếp lịch mà KHÔNG có nhân viên tổng đài xác nhận lựa chọn cuối cùng (HITL bắt buộc). AI không được đưa ra chẩn đoán bệnh hay khuyến nghị điều trị. Nếu triệu chứng có dấu hiệu **cấp cứu** (đau ngực dữ dội, khó thở nặng, mất ý thức, chảy máu nhiều), AI phải **auto-escalate đến bác sĩ trực cấp cứu** ngay lập tức thay vì xếp lịch hẹn thông thường. |

---

## 3.3. Future-State Flow & AI Fit

> **📎 Sơ đồ quy trình tương lai:** Xem file [04-workflow-diagram.png](04-workflow-diagram.png)

* **AI Fit:** Chọn **LLM Feature** — LLM hiểu ngôn ngữ tự nhiên tiếng Việt rất tốt, có thể phân tích triệu chứng mô tả mơ hồ và ánh xạ sang chuyên khoa chính xác hơn bảng Excel tĩnh. Rule-based không khả thi vì biến thể ngôn ngữ quá đa dạng (hàng nghìn cách diễn đạt khác nhau cho cùng một triệu chứng).

**Mô tả quy trình tương lai (4 bước, ~2 phút/cuộc gọi):**

| Bước | Mô tả | Ai thực hiện | Thời gian | Ghi chú |
|------|-------|-------------|-----------|---------|
| **1** | Bệnh nhân gọi/nhắn tin mô tả triệu chứng bằng tiếng Việt | Bệnh nhân | — | Không thay đổi |
| **2** | 🔵 **AI** phân tích triệu chứng → Gợi ý top 3 chuyên khoa phù hợp nhất kèm confidence score | 🔵 AI (LLM) | ⏱ **10 giây** | Nếu phát hiện triệu chứng **cấp cứu** → auto-escalate ngay đến bác sĩ trực |
| **3** | 🟢 Nhân viên tổng đài xem gợi ý AI, xác nhận chuyên khoa → Xếp lịch hẹn HIS | 🟢 Human (HITL) | ⏱ 1 phút | HITL bắt buộc: nhân viên luôn có quyền quyết định cuối cùng |
| **4** | Gửi tin xác nhận lịch hẹn cho bệnh nhân qua SMS/App | Hệ thống | ⏱ 30 giây | Tự động sau khi nhân viên xác nhận |

**Tổng thời gian mới:** ⏱ **~2 phút/cuộc gọi** (giảm **71%** so với 7 phút)

**Fallback:** ↩️ Nếu AI confidence < 60% cho cả top 3 gợi ý, chuyển về nhân viên y tế có chuyên môn hỗ trợ phân loại thủ công.

🔵 = AI Step &nbsp;&nbsp; 🟢 = Human Step (HITL) &nbsp;&nbsp; ↩️ = Fallback

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:

| # | Câu hỏi | Đánh giá |
|---|---------|----------|
| 1 | Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? | ✅ Có: Logs cuộc gọi tổng đài Vinmec + lịch sử đặt lịch trên HIS (hàng trăm nghìn bản ghi). Có thể trích xuất tập training từ dữ liệu lịch sử. |
| 2 | Rủi ro khi AI sai có nằm trong tầm kiểm soát? | ✅ Có: Nhân viên tổng đài BẮT BUỘC xác nhận trước khi xếp lịch (HITL). Triệu chứng cấp cứu auto-escalate. Fallback khi confidence thấp. |
| 3 | Stakeholders sẵn sàng thay đổi quy trình? | ⚠️ Cần thuyết phục: Nhân viên tổng đài cần thời gian làm quen với giao diện gợi ý AI. Đề xuất training 2 buổi trước khi pilot. |

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:

[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.

### Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):

> **Bài toán đáp ứng đủ 3 tiêu chí GO:**
>
> 1. **Tác động kinh doanh rõ ràng:** 18% phân loại sai → ~54 bệnh nhân/ngày phải đặt lại lịch → tổn thất ~240 triệu VNĐ/tháng/cơ sở. Giải pháp AI có thể giảm tỉ lệ sai xuống <5%, tiết kiệm ước tính ~180 triệu VNĐ/tháng.
>
> 2. **Khả thi kỹ thuật cao:** LLM (Gemini 2.5 Flash) đã chứng minh khả năng phân tích ngôn ngữ tự nhiên tiếng Việt xuất sắc. Chi phí API Gemini ước tính: ~300 cuộc gọi/ngày × 30 ngày × ~500 VNĐ/cuộc = **~4.5 triệu VNĐ/tháng** — rất thấp so với chi phí tổn thất 240 triệu VNĐ. ROI > 40x.
>
> 3. **Ranh giới an toàn được kiểm soát:** HITL bắt buộc (nhân viên xác nhận), auto-escalate cấp cứu, và fallback khi confidence thấp đảm bảo rủi ro y tế được giảm thiểu tối đa.
>
> **Scope Pilot đề xuất:** Triển khai thử tại **Tổng đài Vinmec Times City, Hà Nội** trong **4 tuần**, chỉ áp dụng cho 5 chuyên khoa phổ biến nhất (Nội khoa, Tim mạch, Cơ xương khớp, Tai Mũi Họng, Da liễu). Đo lường tỉ lệ phân loại đúng so với baseline trước khi scale-up.
