# Chương trình minh họa ý nghĩa các toán tử: /, //, %, **, and, or, is

print("=== Toán tử / (chia thực) ===")
print("10 / 4 =", 10 / 4)
print("8 / 2 =", 8 / 2)

print("\n=== Toán tử // (chia lấy nguyên) ===")
print("10 // 4 =", 10 // 4)
print("9 // 2 =", 9 // 2)
print("-9 // 2 =", -9 // 2)

print("\n=== Toán tử % (chia lấy dư) ===")
print("10 % 4 =", 10 % 4)
print("9 % 2 =", 9 % 2)
print("20 % 5 =", 20 % 5)

print("\n=== Toán tử ** (lũy thừa) ===")
print("2 ** 3 =", 2 ** 3)
print("5 ** 2 =", 5 ** 2)
print("9 ** 0.5 =", 9 ** 0.5)

print("\n=== Toán tử and (logic AND) ===")
print("True and True =", True and True)
print("True and False =", True and False)
print("5 > 3 and 10 > 2 =", 5 > 3 and 10 > 2)

print("\n=== Toán tử or (logic OR) ===")
print("True or False =", True or False)
print("False or False =", False or False)
print("5 < 3 or 10 > 2 =", 5 < 3 or 10 > 2)

print("\n=== Toán tử is (so sánh object) ===")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a is b =", a is b)   # so sánh object (False)
print("a == b =", a == b)   # so sánh giá trị (True)
print("a is c =", a is c)   # cùng object (True)
