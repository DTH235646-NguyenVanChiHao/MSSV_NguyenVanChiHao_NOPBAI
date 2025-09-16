def xu_ly_chuoi(s):
    nguyen_am = "aeiouAEIOU"

    dem_inhoa = 0
    dem_inthuong = 0
    dem_so = 0
    dem_kytu = 0
    dem_space = 0
    dem_nguyen_am = 0
    dem_phu_am = 0

    for ch in s:
        if ch.isupper():
            dem_inhoa += 1
        elif ch.islower():
            dem_inthuong += 1

        if ch.isdigit():
            dem_so += 1
        elif ch.isspace():
            dem_space += 1
        elif not ch.isalnum():
            dem_kytu += 1

        if ch.isalpha():
            if ch in nguyen_am:
                dem_nguyen_am += 1
            else:
                dem_phu_am += 1

    print("Số chữ IN HOA:", dem_inhoa)
    print("Số chữ in thường:", dem_inthuong)
    print("Số chữ số:", dem_so)
    print("Số ký tự đặc biệt:", dem_kytu)
    print("Số khoảng trắng:", dem_space)
    print("Số nguyên âm:", dem_nguyen_am)
    print("Số phụ âm:", dem_phu_am)


# --- Chạy thử ---
s = input("Nhập chuỗi: ")
xu_ly_chuoi(s)
