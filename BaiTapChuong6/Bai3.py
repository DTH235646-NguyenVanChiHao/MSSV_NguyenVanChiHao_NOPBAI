from random import randrange

def create_matrix(rows, cols):
    return [[randrange(100) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()

def get_row(matrix, r):
    if 0 <= r < len(matrix):
        return matrix[r]
    else:
        return []

def get_col(matrix, c):
    if matrix and 0 <= c < len(matrix[0]):
        return [row[c] for row in matrix]
    else:
        return []

def max_in_matrix(matrix):
    max_value = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
    return max_value

# --- Main program ---
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

D = create_matrix(m, n)
print("Ma trận ngẫu nhiên:")
print_matrix(D)

r = int(input("Mời bạn nhập dòng muốn xuất: "))
print("Dòng đã chọn:", get_row(D, r))

c = int(input("Mời bạn nhập cột muốn xuất: "))
print("Cột đã chọn:", get_col(D, c))

print("Số lớn nhất trong ma trận =", max_in_matrix(D))
