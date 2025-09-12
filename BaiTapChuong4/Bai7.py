#*****************************
import math

# Nhập tọa độ 2 điểm
x1, y1 = map(float, input("Nhập tọa độ A (x1 y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ B (x2 y2): ").split())

# Tính độ dài AB
AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Độ dài đoạn AB =", AB)
