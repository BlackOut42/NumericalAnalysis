'''
    Gal Rabinovich 209064500
    Daniel Nekludov 321984619
'''
import numpy as np

def calculate_norm(mat):
    rows, cols = mat.shape
    max_row_sum = 0
    for i in range(rows):
        row_sum = sum(abs(mat[i, j]) for j in range(cols))
        if row_sum > max_row_sum:
            max_row_sum = row_sum
    return max_row_sum

def invert_matrix(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        print("Error: The matrix must be square to invert.")
        return None

    inverse_matrix = np.eye(rows)

    for i in range(rows):
        if np.isclose(matrix[i, i], 0):
            for k in range(i + 1, rows):
                if not np.isclose(matrix[k, i], 0):
                    matrix[[i, k]] = matrix[[k, i]]
                    inverse_matrix[[i, k]] = inverse_matrix[[k, i]]
                    break

        pivot = matrix[i, i]
        if np.isclose(pivot, 0):
            print("Error: Matrix is singular and cannot be inverted.")
            return None
        
        matrix[i] = matrix[i] / pivot
        inverse_matrix[i] = inverse_matrix[i] / pivot

        for j in range(rows):
            if i != j:
                factor = matrix[j, i]
                matrix[j] = matrix[j] - factor * matrix[i]
                inverse_matrix[j] = inverse_matrix[j] - factor * inverse_matrix[i]

    return inverse_matrix

def calculate_condition(matrix):
    temp_matrix = np.array(matrix)
    norm_original = calculate_norm(temp_matrix)
    inverse_matrix = invert_matrix(temp_matrix)
    if inverse_matrix is None:
        return None
    norm_inverse = calculate_norm(inverse_matrix)
    return norm_original * norm_inverse

def print_matrix_info(matrix):
    temp_matrix = np.array(matrix)
    inverse_matrix = invert_matrix(temp_matrix)

    if inverse_matrix is None:
        return False

    print("Original matrix:\n", matrix)
    print("Original matrix norm:", calculate_norm(matrix))
    print("\nInverse matrix:\n", inverse_matrix)
    print("Inverse matrix norm:", calculate_norm(inverse_matrix))
    condition_number = calculate_condition(matrix)
    if condition_number is not None:
        print("\nCondition number =", condition_number)
    return True

# Function to input a matrix from user
def input_matrix_from_user():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows <= 0 or cols <= 0:
                print("Error: Rows and columns must be positive integers.")
                continue
            matrix = np.zeros((rows, cols))
            print("Enter matrix elements row-wise:")
            for i in range(rows):
                for j in range(cols):
                    matrix[i, j] = float(input(f"Element [{i}, {j}]: "))
            return matrix
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")

print("Welcome to Matrix Operations Program")

while True:
    use_default = input("Do you want to use the default matrix? (yes/no): ").strip().lower()
    
    if use_default == 'yes':
        matrix = np.array([[1, -1, -2], [2, -3, -5], [-1, 3, 5]])
        break
    elif use_default == 'no':
        matrix = input_matrix_from_user()
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("\nMatrix selected:\n", matrix)
print_matrix_info(matrix)
