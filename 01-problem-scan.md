# 01 — Problem Scan & Quick Cards (Bài cá nhân)

> **Lab 02: AI Product Scoping — Vin Smart Future (Vingroup)**
>
> Tài liệu này thể hiện tư duy tìm kiếm và đánh giá bài toán cá nhân trước khi thảo luận nhóm, bao gồm Phase 1 (SCAN) và Phase 2 (QUICK-ASSESS).

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Sử dụng **4 Lenses** để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Dưới đây là danh sách **6 bài toán/bottleneck** thực tế được xác định:

### 4 Lenses áp dụng:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày.
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên.
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn.
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn.

### 📝 List bài toán của tôi:

| # | Subsidiary (Công ty thành viên) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Vinmec** | Tốn thời gian | Bác sĩ mất 20-30 phút/bệnh nhân để soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary), phải trích xuất thủ công từ bệnh án điện tử, kết quả xét nghiệm, và ghi chú lâm sàng rồi viết lại bằng ngôn ngữ dễ hiểu cho bệnh nhân. |
| 2 | **Vinhomes** | Lặp lại | Nhân viên CSKH phải phân loại thủ công hàng trăm phản ánh/khiếu nại mỗi ngày từ App Vinhomes Resident (mất nước, hỏng thang máy, ồn ào, rác thải...) rồi chuyển đến đúng ban quản lý từng tòa nhà. Quy trình mất 10-15 phút/ticket và thường xuyên chuyển nhầm bộ phận. |
| 3 | **VinFast** | AI có thể tốt hơn | Khách hàng VinFast mô tả lỗi xe bằng tiếng Việt tự nhiên (ví dụ: *"xe đi qua gờ giảm tốc kêu lục cục ở bánh trước bên lái"*), nhân viên CSKH không có chuyên môn kỹ thuật phải tra cứu thủ công bảng mã lỗi rồi chuyển tiếp cho xưởng dịch vụ, gây chậm trễ 1-2 ngày phản hồi. |
| 4 | **Xanh SM** | Pain từ người khác | Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác so với vị trí thực tế, khiến khách phải chờ lâu, tăng tỉ lệ hủy chuyến (~12%), và làm giảm thu nhập của tài xế. |
| 5 | **Vinpearl** | Tốn thời gian | Bộ phận Sales phải đọc và xử lý thủ công hàng chục email đặt phòng theo đoàn (Group Booking) phức tạp từ các công ty lữ hành mỗi tuần, kiểm tra quỹ phòng trống, rồi soạn thảo báo giá phản hồi. Mỗi email mất 30-45 phút xử lý, gây chậm phản hồi và mất khách. |
| 6 | **Vinmec** | Pain từ người khác | Bệnh nhân gọi đến tổng đài Vinmec mô tả triệu chứng bệnh bằng ngôn ngữ tự nhiên (ví dụ: *"đau ngực lan ra vai trái, thỉnh thoảng khó thở"*), nhân viên tổng đài phải đoán chuyên khoa phù hợp để xếp lịch hẹn. Tỉ lệ phân loại sai chuyên khoa lên đến 18%, dẫn đến bệnh nhân phải đặt lại lịch khám. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn **top 3 bài toán** tiềm năng nhất từ danh sách SCAN: **#1 (Vinmec — Hồ sơ xuất viện), #2 (Vinhomes — Phân loại phản ánh cư dân), #6 (Vinmec — Phân loại lịch hẹn khám).**

---

## Card #1 — Vinmec: Tự động soạn thảo tóm tắt hồ sơ xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Bác sĩ Vinmec mất quá nhiều thời gian soạn thảo  │
│ tóm tắt hồ sơ xuất viện (Discharge Summary) cho bệnh nhân  │
│ bằng cách trích xuất thủ công từ nhiều nguồn dữ liệu y tế. │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau? Bác sĩ điều trị (quá tải hành chính),         │
│ Bệnh nhân (chờ đợi lâu để nhận giấy xuất viện)             │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Bác sĩ mở bệnh án điện tử, đọc toàn bộ lịch sử       │
│      khám và điều trị của bệnh nhân                         │
│   → 2. Tra cứu và tổng hợp kết quả xét nghiệm, chẩn đoán  │
│        hình ảnh (X-quang, MRI, siêu âm) từ nhiều hệ thống  │
│   → 3. Đọc lại ghi chú lâm sàng hằng ngày của điều dưỡng   │
│        và bác sĩ trực                                       │
│   → 4. Viết tay bản tóm tắt xuất viện bằng ngôn ngữ dễ     │
│        hiểu cho bệnh nhân (chẩn đoán, thuốc, lịch tái khám)│
│   → 5. Trưởng khoa ký duyệt và in ấn giao cho bệnh nhân    │
│                                                             │
│ Bước nào tốn nhất? Bước 2-4 (⏱ 20-30 phút/bệnh nhân)       │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 và 4       │
│ (Tự động trích xuất dữ liệu y tế → Tổng hợp → Draft bản   │
│  tóm tắt xuất viện bằng ngôn ngữ bệnh nhân hiểu được)      │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian soạn hồ sơ xuất viện từ 25 phút ──> dưới    │
│ 5 phút/bệnh nhân. Độ chính xác nội dung y khoa ≥ 95%.       │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
│ (LLM trích xuất và tổng hợp dữ liệu y tế, draft bản tóm   │
│  tắt. Bắt buộc Bác sĩ/Trưởng khoa review trước khi in.)    │
└─────────────────────────────────────────────────────────────┘
```

---

## Card #2 — Vinhomes: Phân loại & Điều hướng phản ánh cư dân tự động

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Nhân viên CSKH Vinhomes phải phân loại thủ công   │
│ hàng trăm phản ánh/khiếu nại mỗi ngày từ App cư dân,       │
│ chuyển đến đúng ban quản lý tòa nhà tương ứng.              │
│ Công ty thành viên: [x] Vinhomes                             │
│                                                             │
│ Ai đang đau? Nhân viên CSKH (xử lý quá tải, nhầm lẫn),     │
│ Cư dân (chờ đợi phản hồi 8-12 tiếng, bị chuyển nhầm)       │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh qua App Vinhomes Resident          │
│      (text tự do + ảnh/video đính kèm)                      │
│   → 2. Nhân viên CSKH đọc nội dung, phân loại thủ công      │
│        vào 1 trong ~15 danh mục (điện, nước, thang máy,     │
│        PCCC, vệ sinh, an ninh, tiếng ồn, bãi xe, v.v.)     │
│   → 3. Tra cứu ban quản lý phụ trách đúng tòa nhà và       │
│        chuyển tiếp ticket kèm ghi chú ưu tiên               │
│   → 4. Soạn tin nhắn phản hồi xác nhận cho cư dân           │
│                                                             │
│ Bước nào tốn nhất? Bước 2-3 (⏱ 10-15 phút/ticket)          │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 và 4       │
│ (AI tự động đọc nội dung phản ánh → Phân loại danh mục →    │
│  Xác định tòa nhà → Route đến đúng ban quản lý → Draft     │
│  tin nhắn xác nhận cho cư dân)                               │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian phân loại ticket từ 12 phút ──> dưới 30 giây.│
│ Tỉ lệ chuyển đúng ban quản lý đạt ≥ 95% (hiện tại ~82%).   │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
│ (LLM phân loại nội dung phản ánh và route tự động.           │
│  Các ticket ưu tiên cao như PCCC/An ninh cần nhân viên      │
│  xác nhận trước khi đóng.)                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## Card #3 — Vinmec: Trợ lý phân loại lịch hẹn khám theo triệu chứng

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Nhân viên tổng đài Vinmec phải đoán chuyên khoa   │
│ phù hợp khi bệnh nhân mô tả triệu chứng bằng ngôn ngữ tự  │
│ nhiên qua điện thoại, dẫn đến tỉ lệ phân loại sai ~18%.    │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau? Nhân viên tổng đài (thiếu kiến thức y khoa),   │
│ Bệnh nhân (phải đặt lại lịch khám khi bị xếp sai khoa)     │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Bệnh nhân gọi tổng đài Vinmec hoặc nhắn tin qua App   │
│      mô tả triệu chứng bằng ngôn ngữ tự nhiên              │
│   → 2. Nhân viên tổng đài nghe/đọc mô tả, tra cứu bảng     │
│        phân loại triệu chứng – chuyên khoa (bản giấy/Excel) │
│   → 3. Chọn chuyên khoa và bác sĩ phù hợp, xếp lịch hẹn   │
│        vào hệ thống HIS (Hospital Information System)        │
│   → 4. Gửi tin xác nhận lịch hẹn cho bệnh nhân qua SMS/App │
│                                                             │
│ Bước nào tốn nhất? Bước 2 (⏱ 5-8 phút/cuộc gọi)            │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2               │
│ (AI phân tích mô tả triệu chứng bằng tiếng Việt → Gợi ý    │
│  top 3 chuyên khoa phù hợp nhất kèm mức độ tự tin → Nhân   │
│  viên tổng đài chọn và xác nhận)                             │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm tỉ lệ phân loại sai chuyên khoa từ 18% ──> dưới 5%.   │
│ Giảm thời gian xử lý cuộc gọi từ 7 phút ──> dưới 3 phút.   │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
│ (LLM phân tích triệu chứng và gợi ý chuyên khoa.            │
│  Nhân viên tổng đài BẮT BUỘC xác nhận trước khi xếp lịch.  │
│  Trường hợp triệu chứng nguy hiểm/khẩn cấp: tự động        │
│  escalate đến bác sĩ trực cấp cứu.)                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Lý do lựa chọn top 3 và loại bỏ các bài toán khác:

| Bài toán bị loại | Lý do loại bỏ |
|---|---|
| **#3 — VinFast chẩn đoán lỗi xe** | Dữ liệu mã lỗi kỹ thuật ô tô rất đặc thù và cần độ chính xác cực cao (liên quan an toàn xe). Rule-based mapping với cơ sở dữ liệu mã lỗi OBD-II có thể giải quyết hiệu quả hơn LLM trong giai đoạn đầu. |
| **#4 — Xanh SM gợi ý điểm đón** | Đây là bài toán thuần tối ưu hóa GPS/bản đồ, phù hợp với giải pháp Rule-based + thuật toán tối ưu lộ trình hơn là sử dụng LLM. Không cần xử lý ngôn ngữ tự nhiên. |
| **#5 — Vinpearl Group Booking** | Mặc dù tốn thời gian nhưng số lượng email Group Booking mỗi tuần chưa đủ lớn (~20-30 email) để justify chi phí triển khai và duy trì hệ thống AI. Có thể bắt đầu bằng template email chuẩn hóa trước. |
