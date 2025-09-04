# Chương trình minh họa các cách nhập dữ liệu từ bàn phím trong Python

# 1. Nhập chuỗi cơ bản
name = input("Nhập tên của bạn: ")
print("Xin chào,", name)

# 2. Nhập số nguyên (cần ép kiểu int)
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi của bạn là:", age)

# 3. Nhập nhiều giá trị và tách bằng split()
a, b = input("Nhập hai số nguyên, cách nhau bằng khoảng trắng: ").split()
a = int(a)
b = int(b)
print("Tổng của", a, "và", b, "là:", a + b)

# 4. Nhập nhiều giá trị và ép kiểu ngay bằng map()
x, y, z = map(float, input("Nhập ba số thực, cách nhau bằng khoảng trắng: ").split())
print("Trung bình của ba số là:", (x + y + z) / 3)

# 5. Nhập danh sách số nguyên
numbers = list(map(int, input("Nhập các số nguyên, cách nhau bằng khoảng trắng: ").split()))
print("Danh sách bạn vừa nhập là:", numbers)
print("Tổng các phần tử trong danh sách =", sum(numbers))
