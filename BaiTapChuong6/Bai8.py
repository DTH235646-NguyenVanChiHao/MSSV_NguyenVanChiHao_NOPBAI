n = int(input("Nhập số lượng phần tử: "))
M = []

for i in range(n):
    value = float(input(f"Nhập M[{i}]: "))
    M.append(value)

# Sắp xếp giảm dần
M.sort(reverse=True)

print("Dãy sau khi sắp xếp giảm dần:", M)
