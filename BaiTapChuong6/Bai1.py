from random import randrange
import math




def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("=== Chương trình xử lý List ===")
n = int(input("Nhập số phần tử: "))

# Tạo list ngẫu nhiên
lst = [randrange(-100, 100) for _ in range(n)]
print("List ngẫu nhiên là:", lst)

# Thêm giá trị mới
value = int(input("Mời bạn thêm số mới: "))
lst.append(value)
print("List sau khi thêm:", lst)

# Đếm số xuất hiện
k = int(input("Bạn muốn đếm số nào: "))
count_k = lst.count(k)
print(f"Số {k} xuất hiện {count_k} lần trong list")

# Đếm và tính tổng các số nguyên tố
prime_numbers = [x for x in lst if check_prime(x)]
print(f"Có {len(prime_numbers)} số nguyên tố trong list")
print(f"Tổng các số nguyên tố = {sum(prime_numbers)}")

# Sắp xếp list
lst.sort()
print("List sau khi sort:", lst)

# Xóa list (không in sau khi xóa)
del lst
print("List đã được xóa khỏi bộ nhớ.")
