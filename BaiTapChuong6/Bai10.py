from typing import List


def input_matrix(rows: int, cols: int, name: str) -> List[List[int]]:
    print(f"Enter matrix {name}:")
    matrix = []
    for i in range(rows):
        while True:
            row = list(map(int, input(f"  Row {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"⚠️  Please enter exactly {cols} numbers.")
    return matrix



def add_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    rows, cols = len(A), len(A[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(A[i][j] + B[i][j])
        result.append(new_row)
    return result



def transpose_matrix(M: List[List[int]]) -> List[List[int]]:
    rows, cols = len(M), len(M[0])
    result = []
    for j in range(cols):          # each column becomes a row
        new_row = []
        for i in range(rows):
            new_row.append(M[i][j])
        result.append(new_row)
    return result



m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

# Input matrices
A = input_matrix(m, n, "A")
B = input_matrix(m, n, "B")

# Process
C   = add_matrices(A, B)      # A + B
A_T = transpose_matrix(A)     # Transpose of A
B_T = transpose_matrix(B)     # Transpose of B

# Output results
print("\nMatrix A:", A)
print("Matrix B:", B)
print("A + B   :", C)
print("A Transpose:", A_T)
print("B Transpose:", B_T)
