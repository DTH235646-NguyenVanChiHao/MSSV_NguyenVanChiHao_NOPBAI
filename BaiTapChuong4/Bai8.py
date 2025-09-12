#*****************************
import math

# Nhập a và x
a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

# Kiểm tra điều kiện
if a > 0 and a != 1 and x > 0:
    log_ax = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {log_ax}")
else:
    print("Điều kiện không hợp lệ: yêu cầu x > 0, a > 0 và a != 1")
