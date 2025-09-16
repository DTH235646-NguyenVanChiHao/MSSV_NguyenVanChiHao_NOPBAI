def CheckPrime(x):
    """Return True if x is a prime number, otherwise False"""
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):   # chỉ cần kiểm tra đến căn bậc hai
        if x % i == 0:
            return False
    return True

# Dữ liệu đầu vào
s = "5;7;8;-2;8;11;-13;9;10"
arr = s.split(';')

sochan = 0
soam = 0
sont = 0
sum_val = 0

for x in arr:
    print(x)
    number = int(x)

    if number % 2 == 0:
        sochan += 1
    if number < 0:
        soam += 1
    if CheckPrime(number):
        sont += 1

    sum_val += number

print("Số chẵn =", sochan)
print("Số âm =", soam)
print("Số nguyên tố =", sont)
print("Trung bình =", sum_val / len(arr))
