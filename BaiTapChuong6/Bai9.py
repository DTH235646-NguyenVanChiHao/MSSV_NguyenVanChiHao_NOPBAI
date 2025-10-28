import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- Dữ liệu đầu vào ---
M = [3,6,7,8,11,17,2,90,2,5,4,5,8]

# --- Tạo các danh sách kết quả ---
odd_nums       = [x for x in M if x % 2 == 1]
even_nums      = [x for x in M if x % 2 == 0]
prime_nums     = [x for x in M if is_prime(x)]
not_prime_nums = [x for x in M if not is_prime(x)]

# --- Xuất kết quả ---
print("Dãy số lẻ  :", odd_nums,  f"→ {len(odd_nums)} số")
print("Dãy số chẵn:", even_nums, f"→ {len(even_nums)} số")
print("Số nguyên tố:", prime_nums)
print("Không nguyên tố:", not_prime_nums)
