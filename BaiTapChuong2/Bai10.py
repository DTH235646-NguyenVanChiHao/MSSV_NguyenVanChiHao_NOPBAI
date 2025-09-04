# Câu 10: Viết ngắn gọn lại các lệnh

# (a) x = x + 1
print("=== (a) x = x + 1 ===")
x = 10
x = x + 1
print("Biểu thức gốc: x = x + 1 =", x)
x = 10
x += 1
print("Biểu thức rút gọn: x += 1 =", x, "\n")

# (b) x = x / 2
print("=== (b) x = x / 2 ===")
x = 10
x = x / 2
print("Biểu thức gốc: x = x / 2 =", x)
x = 10
x /= 2
print("Biểu thức rút gọn: x /= 2 =", x, "\n")

# (c) x = x - 1
print("=== (c) x = x - 1 ===")
x = 10
x = x - 1
print("Biểu thức gốc: x = x - 1 =", x)
x = 10
x -= 1
print("Biểu thức rút gọn: x -= 1 =", x, "\n")

# (d) x = x + y
print("=== (d) x = x + y ===")
x, y = 10, 5
x = x + y
print("Biểu thức gốc: x = x + y =", x)
x, y = 10, 5
x += y
print("Biểu thức rút gọn: x += y =", x, "\n")

# (e) x = x - (y + 7)
print("=== (e) x = x - (y + 7) ===")
x, y = 20, 5
x = x - (y + 7)
print("Biểu thức gốc: x = x - (y + 7) =", x)
x, y = 20, 5
x -= (y + 7)
print("Biểu thức rút gọn: x -= (y + 7) =", x, "\n")
