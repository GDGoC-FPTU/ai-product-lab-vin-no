# 01 — Problem Scan & Quick Cards (Bài cá nhân)

> **Lab 02 — AI Product Scoping (Vin Smart Future)**
> Vai trò: AI Product Engineer tại Vin Smart Future, khảo sát cơ hội tối ưu bằng AI cho các công ty thành viên Vingroup.
> *Nhóm: Vin nô — Họ tên / MSSV: Huỳnh An Nghiệp — 26A202600853*

---

## 🔍 Phase 1 — SCAN: Quét cơ hội qua 4 Lenses

Dùng 4 thấu kính (Lặp lại / Tốn thời gian / AI-upgrade / Stakeholder Pain) quét qua vận hành thực tế của các công ty thành viên Vingroup. Ghi nhận 6 bài toán (≥5 theo yêu cầu).

| # | Subsidiary | Lens | Mô tả ngắn bài toán | Tổn thất ước tính |
|---|------------|------|---------------------|-------------------|
| 1 | **Vinmec** | Tốn thời gian | Bác sĩ soạn thủ công **tóm tắt hồ sơ xuất viện (discharge summary)** dễ hiểu cho bệnh nhân từ bệnh án điện tử, đơn thuốc và kết quả xét nghiệm. | 20–30 phút/bệnh nhân; mỗi khoa ~40 ca/ngày → bác sĩ quá tải, chậm trả hồ sơ. |
| 2 | **Vinmec** | Pain từ người khác | Điều dưỡng tổng đài phải đọc mô tả triệu chứng tự do của khách để gợi ý đúng chuyên khoa đặt lịch (Tim mạch vs Hô hấp vs Tiêu hóa). | Đặt sai khoa → khách phải khám lại, khiếu nại, tốn 1 lượt khám. |
| 3 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công sự cố hết pin/sạc của tài xế trên đường (tra vị trí, tìm trạm trống, soạn chỉ dẫn). | ~15 phút/lượt; ~80 sự cố/ngày tại Hà Nội → rò rỉ doanh thu do xe nằm chờ. |
| 4 | **Vinhomes** | Lặp lại | Phân loại & điều hướng phản ánh cư dân (mất nước, hỏng đèn, ồn ào…) từ App Resident về đúng ban quản lý từng tòa. | CSKH phản hồi rập khuôn, mất ~12 giờ định tuyến thủ công. |
| 5 | **VinFast** | Lặp lại | Đối chiếu hóa đơn sạc điện hằng tuần từ hàng nghìn trụ sạc đối tác với số liệu tài chính. | Nhân viên tài chính mất nhiều giờ so khớp, dễ sai lệch số. |
| 6 | **Vinpearl** | AI-upgrade | Tổng hợp review Booking/Agoda/Google Map để lọc phàn nàn khẩn cấp ("phòng bẩn", "thái độ tệ") gửi Manager. | Phản hồi review chậm → ảnh hưởng điểm đánh giá & đặt phòng. |

**Nhận định chọn lọc cá nhân:** 3 bài toán có giá trị & độ rõ ràng cao nhất là **#1 (Vinmec — Discharge Summary)**, **#3 (Xanh SM — Sự cố pin)**, **#4 (Vinhomes — Phản ánh cư dân)** → đưa vào 3 Quick Cards.

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

### Quick Problem Card #1 — Vinmec: Soạn tóm tắt hồ sơ xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                         │
│ Bài toán: Bác sĩ Vinmec mất nhiều thời gian soạn thủ công     │
│ bản tóm tắt xuất viện dễ hiểu cho bệnh nhân từ EMR.           │
│ Công ty thành viên: [x] Vinmec                                │
│                                                              │
│ Ai đang đau (Actor)? Bác sĩ điều trị / điều dưỡng (quá tải   │
│ giấy tờ); bệnh nhân (nhận giấy ra viện trễ, khó hiểu).        │
│                                                              │
│ Workflow thủ công hiện tại (5 bước):                         │
│  1. Mở EMR đọc chẩn đoán, diễn tiến, xét nghiệm              │
│  → 2. Lọc thông tin cần đưa cho bệnh nhân                    │
│  → 3. Viết tay tóm tắt + dặn dò thuốc/tái khám              │
│  → 4. Rà soát số liệu, liều thuốc, ngày tái khám            │
│  → 5. In, ký, bàn giao cho bệnh nhân                         │
│                                                              │
│ Bước tốn nhất? Bước 3 & 4 (⏱ ~20 phút/bệnh nhân)            │
│ AI nhảy vào ở bước nào? Bước 3 (draft tóm tắt) + hỗ trợ      │
│ rà soát số liệu ở bước 4 (bác sĩ vẫn duyệt cuối).            │
│                                                              │
│ Metric thành công: Giảm thời gian soạn từ ~20 phút → dưới    │
│ 5 phút/bệnh nhân; 0 sai lệch số liệu lâm sàng (bác sĩ duyệt).│
│                                                              │
│ Quick Architecture: [x] LLM Feature (trích xuất + draft)     │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #2 — Xanh SM: Xử lý sự cố pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                         │
│ Bài toán: Tài xế báo hết pin giữa đường, cần chỉ dẫn trạm    │
│ sạc trống hoặc điều xe cứu hộ.                                │
│ Công ty thành viên: [x] Xanh SM (GSM)                        │
│                                                              │
│ Ai đang đau? Tài xế (chờ đợi), điều phối viên (quá tải).     │
│                                                              │
│ Workflow thủ công (5 bước):                                  │
│  1. Nhận cuộc gọi → 2. Tra vị trí GPS xe                     │
│  → 3. Tra trạm sạc trống phù hợp → 4. Soạn tin chỉ dẫn       │
│  → 5. Gọi cứu hộ nếu pin cạn                                 │
│                                                              │
│ Bước tốn nhất? Bước 3 & 4 (⏱ ~12 phút/lượt)                 │
│ AI nhảy vào ở bước 3–4 (tra trạm + draft chỉ dẫn).          │
│                                                              │
│ Metric: Giảm thời gian xử lý từ 15 phút → dưới 3 phút.       │
│ Quick Architecture: [x] LLM Feature                          │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #3 — Vinhomes: Phân loại phản ánh cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                         │
│ Bài toán: Phân loại & điều hướng phản ánh cư dân từ App      │
│ Resident về đúng ban quản lý từng tòa nhà.                    │
│ Công ty thành viên: [x] Vinhomes                             │
│                                                              │
│ Ai đang đau? Tổng đài CSKH, ban quản lý tòa, cư dân chờ lâu. │
│                                                              │
│ Workflow thủ công (4 bước):                                  │
│  1. Nhận phản ánh trên App → 2. Đọc & phân loại thủ công     │
│  → 3. Định tuyến tới ban phụ trách → 4. Phản hồi cư dân      │
│                                                              │
│ Bước tốn nhất? Bước 2 & 3 (⏱ phản hồi trung bình ~12 giờ)   │
│ AI nhảy vào ở bước 2 (phân loại nhãn) + 3 (gợi ý định tuyến).│
│                                                              │
│ Metric: Tự phân loại đúng >85% phản ánh dưới 10 giây.        │
│ Quick Architecture: [x] LLM Feature (có thể kèm Rule router) │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Đề xuất cá nhân để Deep-Dive

Tôi đề xuất nhóm chọn **Card #1 — Vinmec: Soạn tóm tắt hồ sơ xuất viện** vì:
- **Giá trị rõ ràng:** giải phóng 15–25 phút/bệnh nhân cho bác sĩ — nguồn lực khan hiếm nhất của bệnh viện.
- **AI Fit gọn:** chủ yếu là trích xuất + viết lại văn bản (LLM Feature), không cần Agent tự trị.
- **Ranh giới an toàn dạy được:** y tế bắt buộc Human-in-the-loop (bác sĩ duyệt) và cấm bịa số liệu — môi trường lý tưởng để stress-test ranh giới prompt.
