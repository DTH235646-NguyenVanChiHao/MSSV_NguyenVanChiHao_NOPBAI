import random

N = int(input("Nhập số lượng phần tử N: "))
lst = []
while len(lst) < N:
    num = random.randrange(0, 100)   # tạo số từ 0 đến 99
    if num not in lst:               # chỉ thêm nếu chưa có
        lst.append(num)

print("List ngẫu nhiên (không trùng):", lst)
