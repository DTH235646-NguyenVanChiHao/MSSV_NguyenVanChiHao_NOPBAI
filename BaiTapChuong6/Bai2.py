from random import randrange

# --- Create random list ---
n = int(input("Nhập số phần tử: "))
lst = [randrange(0, 100) for _ in range(n)]
print("List ngẫu nhiên:", lst)

# --- Insert new value ---
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:", lst)

# --- Remove all occurrences ---
k = int(input("Mời nhập số để xóa: "))
while k in lst:         # more direct than count()
    lst.remove(k)
print("List sau khi xóa:", lst)

# --- Check palindrome ---
def is_palindrome(seq):
    for i in range(len(seq)//2):
        if seq[i] != seq[-i-1]:
            return False
    return True

if is_palindrome(lst):
    print("List đối xứng")
else:
    print("List không đối xứng")
