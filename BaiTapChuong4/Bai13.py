def tong_uoc(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def la_so_hoan_thien(n):
    return tong_uoc(n) == n

def la_so_thinh_vuong(n):
    return tong_uoc(n) > n

# Ví dụ kiểm tra
n = 12
print(f"Số {n} là số hoàn thiện? {la_so_hoan_thien(n)}")
print(f"Số {n} là số thịnh vượng? {la_so_thinh_vuong(n)}")

n = 6
print(f"Số {n} là số hoàn thiện? {la_so_hoan_thien(n)}")
print(f"Số {n} là số thịnh vượng? {la_so_thinh_vuong(n)}")
