n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    while True:
        x = float(input(f"Nhập phần tử thứ {i}: "))
        # kiểm tra quy tắc tăng dần : X[-1] - THE LAST ELEMENT
        if i == 0 or x > lst[-1]:
            lst.append(x)
            break
        else:
            print(" Số này không lớn hơn số trước. Hãy nhập lại!")

print("Dãy số tăng dần:", lst)
