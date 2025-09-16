# Nhập một chuỗi từ người dùng
s = input("Nhập chuỗi: ")

print("\n--- Kết quả xử lý ---")

# 1. Độ dài
print("Độ dài chuỗi:", len(s))

# 2. Xóa khoảng trắng 2 đầu
print("strip():", s.strip())

# 3. Chữ thường và chữ hoa
print("lower():", s.lower())
print("upper():", s.upper())

# 4. Viết hoa chữ cái đầu tiên
print("capitalize():", s.capitalize())
print("title():", s.title())

# 5. Tách và nối chuỗi
words = s.split()
print("split():", words)
print("join():", " ".join(words))

# 6. Thay thế chuỗi con
print("replace():", s.replace("a", "@"))

# 7. Tìm kiếm chuỗi con
print("find('a'):", s.find("a"))

# 8. Kiểm tra bắt đầu/kết thúc
print("startswith('H'):", s.startswith("H"))
print("endswith('!'):", s.endswith("!"))

# 9. Kiểm tra dạng chuỗi
print("isdigit():", s.isdigit())
print("isalpha():", s.isalpha())
print("isalnum():", s.isalnum())
