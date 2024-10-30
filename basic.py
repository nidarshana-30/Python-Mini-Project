"""rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))

rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))

# Check if multiplication is possible (columns of A must equal rows of B)
if cols_A != rows_B:
    print("Matrix multiplication is not possible with these dimensions.")
else:
    # Input matrix A
    print("Enter the elements of matrix A row by row:")
    A = [[int(input()) for _ in range(cols_A)] for _ in range(rows_A)]

    # Input matrix B
    print("Enter the elements of matrix B row by row:")
    B = [[int(input()) for _ in range(cols_B)] for _ in range(rows_B)]

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Multiply matrices
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    # Print the result
    print("Resultant Matrix:")
    for row in result:
        print(row)

A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]

# Get dimensions
rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

# Initialize the result matrix with zeros
result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

# Multiply matrices
for i in range(rows_A):
    for j in range(cols_B):
        for k in range(cols_A):
            result[i][j] += A[i][k] * B[k][j]

# Print the result
print("Resultant Matrix:")
for row in result:
    print(row)"""


attempts = 3  # Allow 3 attempts

for _ in range(attempts):
    password = input("Enter your password: ")
    has_upper = False
    has_lower = False
    has_digit = False

    # Check each character in the password
    if len(password) >= 8:
        for char in password:
            if char.isupper():  # Check for an uppercase letter
                has_upper = True
            if char.islower():  # Check for a lowercase letter
                has_lower = True
            if char.isdigit():  # Check for a digit
                has_digit = True
        
        # Validate all criteria
        if has_upper and has_lower and has_digit:
            print("Password accepted.")
            break  # Exit the loop if the password is valid
    else:
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one digit. Please try again.")
        continue     