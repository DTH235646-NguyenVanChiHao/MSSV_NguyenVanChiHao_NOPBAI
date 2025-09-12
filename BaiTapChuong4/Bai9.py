#*****************************
import math

# Nhập n
n = int(input("Nhập n: "))

S = 0
# Tính từ 1 đến n
for i in range(1, n + 1):
    S = math.sqrt(i + S)

print("Giá trị căn bậc hai lồng nhau =", S)
