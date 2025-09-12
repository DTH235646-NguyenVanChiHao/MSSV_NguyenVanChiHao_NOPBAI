def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s

# ------------------------
# Trường hợp 1
def case1():
    global val
    val = 5
    print("Case 1:")
    print(sum1(5))  # 5
    print(sum2())   # 5 (val -> 0)
    print(sum3())   # 0 (vì val = 0)
    print()

# Trường hợp 2
def case2():
    global val
    val = 5
    print("Case 2:")
    print(sum1(5))  # 5
    print(sum3())   # 5 (val = 5)
    print(sum2())   # 5 (val -> 0)
    print()

# Trường hợp 3
def case3():
    global val
    val = 5
    print("Case 3:")
    print(sum2())   # 5 (val -> 0)
    print(sum1(5))  # 5
    print(sum3())   # 0 (vì val = 0)
    print()

# ------------------------
# Gọi cả 3 trường hợp
case1()
case2()
case3()
