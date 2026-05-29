"""Sinh sơ đồ Current-State Workflow cho bài toán Vinmec (04-workflow-diagram.png).

Chạy: python extras/make_diagram.py
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

plt.rcParams["font.family"] = "DejaVu Sans"

STEPS = [
    ("Bước 1\nMở EMR đọc\nchẩn đoán, XN,\nđơn thuốc", "Bác sĩ", "4 phút", False),
    ("Bước 2\nLọc thông tin\ncần đưa cho\nbệnh nhân", "Bác sĩ", "3 phút", False),
    ("Bước 3\nViết tay tóm tắt\n+ dặn dò\nthuốc/tái khám", "Bác sĩ", "12 phút", True),
    ("Bước 4\nRà soát số liệu,\nliều thuốc,\nngày tái khám", "Bác sĩ", "6 phút", True),
    ("Bước 5\nIn, ký &\nbàn giao\nbệnh nhân", "ĐD/Bác sĩ", "3 phút", False),
]

fig, ax = plt.subplots(figsize=(15, 5.2))
ax.set_xlim(0, 100)
ax.set_ylim(0, 40)
ax.axis("off")

ax.text(50, 38.2, "Vinmec — Quy trình soạn Tóm tắt Hồ sơ Xuất viện (Current-State, thủ công)",
        ha="center", va="center", fontsize=15, fontweight="bold")

box_w, box_h, gap = 16.0, 16.0, 2.8
x0 = 2.0
y_box = 14.0
centers = []

for i, (text, actor, t, is_bottleneck) in enumerate(STEPS):
    x = x0 + i * (box_w + gap)
    cx = x + box_w / 2
    centers.append((x, cx))
    face = "#ffe5e5" if is_bottleneck else "#e8f0fe"
    edge = "#d93025" if is_bottleneck else "#1a73e8"
    lw = 2.6 if is_bottleneck else 1.6
    box = FancyBboxPatch((x, y_box), box_w, box_h,
                         boxstyle="round,pad=0.3,rounding_size=1.2",
                         linewidth=lw, edgecolor=edge, facecolor=face)
    ax.add_patch(box)
    ax.text(cx, y_box + box_h - 3.2, text, ha="center", va="top",
            fontsize=9.3, fontweight="bold")
    ax.text(cx, y_box + 3.4, f"Actor: {actor}", ha="center", va="center", fontsize=8.2)
    ax.text(cx, y_box + 1.3, f"Time: {t}", ha="center", va="center", fontsize=8.6,
            color="#d93025" if is_bottleneck else "#202124", fontweight="bold")
    if is_bottleneck:
        # Chấm đỏ + nhãn Bottleneck
        ax.add_patch(Circle((cx - 5.0, y_box + box_h + 1.7), 0.7,
                            color="#d93025", zorder=5))
        ax.text(cx - 3.7, y_box + box_h + 1.7, "Bottleneck", ha="left", va="center",
                fontsize=9, color="#d93025", fontweight="bold")

# Mũi tên + nhãn Handoff giữa các bước
handoff_steps = {0, 1, 3}  # handoff sau bước 1, 2, 4
for i in range(len(STEPS) - 1):
    x_left = centers[i][0] + box_w
    x_right = centers[i + 1][0]
    arr = FancyArrowPatch((x_left, y_box + box_h / 2),
                          (x_right, y_box + box_h / 2),
                          arrowstyle="-|>", mutation_scale=18,
                          linewidth=1.8, color="#5f6368")
    ax.add_patch(arr)
    if i in handoff_steps:
        mid = (x_left + x_right) / 2
        ax.text(mid, y_box + box_h / 2 + 2.0, "Handoff", ha="center", va="center",
                fontsize=8.2, color="#9334e6", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#f3e8fd",
                          edgecolor="#9334e6", linewidth=1.0))

# Chú thích (legend)
ax.add_patch(Circle((3.0, 6.0), 0.7, color="#d93025", zorder=5))
ax.text(4.2, 6.0, "Bottleneck: Bước 3 (viết tay) & Bước 4 (rà số liệu) — chiếm 18/28 phút",
        ha="left", va="center", fontsize=10, color="#d93025")
ax.text(2.3, 3.4, "[Handoff]", ha="left", va="center", fontsize=9,
        color="#9334e6", fontweight="bold")
ax.text(8.5, 3.4, "= điểm chuyển giao thông tin (EMR → bản viết → bản in ký → bệnh nhân)",
        ha="left", va="center", fontsize=10, color="#5f6368")

# Tổng thời gian
ax.text(98, 5.0, "TỔNG THỜI GIAN: ~28 phút / bệnh nhân",
        ha="right", va="center", fontsize=12.5, fontweight="bold", color="#188038",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#e6f4ea", edgecolor="#188038"))

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "04-workflow-diagram.png")
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
print(f"Saved: {out}")
