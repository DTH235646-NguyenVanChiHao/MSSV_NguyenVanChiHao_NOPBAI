# Nhập tháng
month = int(input("Nhập tháng (1-12): "))

# Kiểm tra và xác định quý
if 1 <= month <= 3:
    quarter = 1
elif 4 <= month <= 6:
    quarter = 2
elif 7 <= month <= 9:
    quarter = 3
elif 10 <= month <= 12:
    quarter = 4
else:
    quarter = None   # Tháng không hợp lệ

# Xuất kết quả
if quarter:
    print(f"Tháng {month} thuộc quý {quarter} trong năm.")
else:
    print("Tháng không hợp lệ! Vui lòng nhập từ 1 đến 12.")
