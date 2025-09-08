#is Prime

def isPrime(num):
    for i in range(2,n //2 +1):
        if num % i == 0:
            return False
        return True

n = int(input("Nhập số nguyên dương n: "))
if n < 2:
    print(f"{n} không phải là số nguyên tố.")       
else:
    if isPrime(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
#is Prime