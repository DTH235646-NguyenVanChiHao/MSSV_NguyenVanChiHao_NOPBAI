# Chương trình minh họa các loại lỗi và cách bắt lỗi trong Python

print("=== 1. Lỗi cú pháp (Syntax Error) ===")
print("Ví dụ: print('Hello'  # thiếu dấu ngoặc đóng -> SyntaxError")
print("👉 Lỗi này không chạy được, nên mình chỉ minh họa, không thực thi.\n")

print("=== 2. Lỗi logic (Logic Error) ===")
a, b = 10, 0
print("Mình muốn tính tổng a + b, nhưng lại viết nhầm thành a - b")
print("Kết quả:", a - b)  # Sai logic
print("👉 Lỗi logic khó phát hiện vì chương trình vẫn chạy bình thường.\n")

print("=== 3. Lỗi runtime (Runtime Error) ===")
try:
    x = 10 / 0  # chia cho 0
except ZeroDivisionError as e:
    print("Gặp lỗi Runtime:", e, "\n")

print("=== 4. Bắt lỗi với try-except ===")
try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    print("Thương a/b =", a / b)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except ValueError:
    print("Lỗi: Bạn phải nhập số nguyên!")
except Exception as e:
    print("Có lỗi khác xảy ra:", e)
