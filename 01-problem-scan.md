# 01-problem-scan.md — Bài Cá Nhân (Phase 1 & 2)

*   **Họ và tên:** Nguyễn Quang Anh
*   **MSSV:** 2A202600608
*   **Lớp:** C401 (Nhóm: vin-no)

---

# 🔍 Phase 1 — SCAN: Quét Cơ Hội Ứng Dụng AI

Dưới đây là danh sách 5 bài toán/nút thắt cổ chai (bottlenecks) thực tế được tìm thấy thông qua hoạt động vận hành của các công ty thành viên thuộc Tập đoàn Vingroup bằng cách áp dụng **4 Lenses (Lặp lại, Tốn thời gian, AI-upgrade, Pain từ người khác)**:

| # | Subsidiary (Công ty thành viên) | Lens (Thấu kính) | Mô tả ngắn bài toán / Nút thắt cổ chai |
|---|----------------------------------|------------------|----------------------------------------|
| 1 | **Xanh SM (GSM)** | Tốn thời gian / Pain | Tài xế báo xe hết pin/sự cố pin khẩn cấp giữa đường cần cứu hộ di động hoặc đề xuất trạm sạc gần nhất có trụ trống. Điều phối viên phải kiểm tra thủ công nhiều nguồn dữ liệu (bản đồ, hệ thống trạm, định vị) để chỉ đường và điều phối, mất 15 phút/lượt. |
| 2 | **Vinhomes** | Lặp lại / AI-upgrade | Phân loại và tự động chuyển hướng các phản ánh, khiếu nại của cư dân (về vệ sinh, an ninh, kỹ thuật, điện nước) trên App Vinhomes Resident tới đúng Ban quản lý từng tòa nhà/phòng ban nghiệp vụ thay vì để nhân viên CSKH ngồi đọc và chia thủ công. |
| 3 | **Vinmec** | Tốn thời gian | Bác sĩ mất rất nhiều thời gian (20-30 phút/bệnh nhân) để tổng hợp các ghi chú lâm sàng, kết quả xét nghiệm thành văn bản tóm tắt hồ sơ xuất viện (Discharge Summary) bằng ngôn ngữ phổ thông dễ hiểu cho người bệnh. |
| 4 | **VinFast** | AI-upgrade | Khách hàng mô tả lỗi xe bằng tiếng Việt tự nhiên (ví dụ: *"xe đi qua gờ giảm tốc kêu cụp cụp ở bánh trước"* hoặc *"màn hình trung tâm thỉnh thoảng bị đen khi lùi"*), hệ thống tự động phân loại và map sang mã lỗi kỹ thuật chuẩn để nhân viên kỹ thuật tiếp nhận. |
| 5 | **Vinpearl** | Pain từ người khác | Bộ phận vận hành khách sạn phải quét thủ công hàng nghìn phản hồi của khách hàng trên các nền tảng đặt phòng trực tuyến (Booking.com, Agoda, Google Travel) để lọc ra các phàn nàn khẩn cấp cần xử lý ngay lập tức (phòng bẩn, thái độ nhân viên tệ, thiết bị hỏng). |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Dưới đây là 3 thẻ bài toán tiềm năng nhất được phân tích sơ bộ:

### 1. QUICK PROBLEM CARD #1: Xanh SM — Xử lý sự cố hết pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tài xế Xanh SM báo sự cố pin yếu/hết pin  │
│ giữa đường cần chỉ hướng trạm sạc trống hoặc cứu hộ khẩn.   │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (chờ đợi), Điều phối viên (quá tải) │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi hotline ──> 2. Điều phối viên định vị xe     │
│   ──> 3. Kiểm tra trụ sạc VinFast trống ──> 4. Viết SMS chỉ  │
│   đường gửi tài xế ──> 5. Điều xe cứu hộ pin (nếu dưới 5%).  │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 12 phút/lượt)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4            │
│ (Lấy định vị -> Tìm trạm sạc trống phù hợp -> Soạn SMS nháp) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút.      │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

### 2. QUICK PROBLEM CARD #2: Vinhomes — Phân loại phản ánh cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân loại và điều hướng phản ánh  │
│ của cư dân gửi qua App Vinhomes Resident về Ban quản lý.    │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH trực tổng đài phản ánh,  │
│ Cư dân Vinhomes (chờ phản hồi lâu).                         │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh ──> 2. CSKH trung tâm đọc thủ công  │
│   ──> 3. Phân loại theo thẻ lỗi ──> 4. Chuyển tiếp về Ban    │
│   Quản lý tòa nhà tương ứng trên phần mềm quản trị.          │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 5 phút/ticket)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (Trích xuất ý kiến cư dân -> Gắn nhãn phân loại -> Định hướng)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian điều hướng từ 2 tiếng ──> dưới 10 giây/ticket.│
│ Tỷ lệ phân loại chính xác đạt trên 92%.                     │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

### 3. QUICK PROBLEM CARD #3: Vinmec — Tóm tắt hồ sơ xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Trích xuất hồ sơ bệnh án để soạn tóm tắt  │
│ hướng dẫn xuất viện dễ hiểu cho bệnh nhân.                  │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị (quá tải thủ tục),     │
│ Bệnh nhân xuất viện (khó hiểu các thuật ngữ y học phức tạp). │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Đọc tóm tắt bệnh án ──> 2. Lọc thông tin thuốc/tái khám│
│   ──> 3. Soạn tờ tóm tắt tiếng Việt bình dân ──> 4. Ký duyệt│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 20 phút/lượt)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (Đọc dữ liệu lâm sàng -> Dịch thuật ngữ -> Draft tờ hướng dẫn)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian soạn thảo từ 25 phút ──> dưới 3 phút/bệnh án.│
│                                                             │
│ Quick Architecture: [x] LLM Feature (Có Human-In-The-Loop)  │
└─────────────────────────────────────────────────────────────┘
```
