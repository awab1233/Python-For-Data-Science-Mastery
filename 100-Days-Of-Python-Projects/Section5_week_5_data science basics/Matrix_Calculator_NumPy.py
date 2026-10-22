import numpy as np

def get_matrix():
    try: 
        row = int(input("enter the number of rows: "))
        column = int(input("enter the number of columns: "))
        print("enter the elements of the matrix separated by spaces: ")
        elements =[]        
        for _ in range(row):
            row = list(map(float, input().split()))
            if len(row) != column:
                raise ValueError("Number of elements in the row does not match the specified number of columns.")
            elements.append(row)
        return np.array(elements)

    except ValueError as e:
        print("ERROR", e)  
        return None

def matrix_operations(A,B):
    print("\nmatrix A:", A)
    print("\nmatrix B:", B)

    try:
        print("\n addition:\n", A + B)
    except ValueError:
        print("ERROR: Matrices must have the same dimensions for addition.")

    try:
        print("\n subtraction:\n", A - B)
    except ValueError:
        print("ERROR: Matrices must have the same dimensions for addition.")

    try:
        print("\n multiplication:\n", A * B)
    except ValueError:
        print("ERROR: Matrices must have compatible dimensions for multiplication.")

    try:
        print("\n dot product:\n",np.dot(A,B))
    except ValueError:
        print("ERROR: Matrices must have compatible dimensions for dot product.")
    
    print("\n transpose of A:\n", A.T)
    print("\n transpose of B:\n", B.T)

    try:
        print("\ndeterminant of A:\n", np.linalg.det(A))
    except np.linalg.LinAlgError:
        print("ERROR: Matrix A is singular and does not have a determinant.")
    
    try:
        print("\ndeterminant of B:\n", np.linalg.det(B))
    except np.linalg.LinAlgError:
        print("ERROR: Matrix B is singular and does not have a determinant.")

    try: 
        print("\ninverse of A:\n", np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("ERROR: Matrix A is singular and does not have an inverse.")
    
    try:
        print("\ninverse of B:\n", np.linalg.inv(B))
    except np.linalg.LinAlgError:
        print("ERROR: Matrix B is singular and does not have an inverse.")


def main():
    print("Welcome to the Matrix Calculator!")
    print("=================================")
    
    print("Enter matrix A:")
    A = get_matrix()
    if A is None:
        return
    
    print("Enter matrix B:")
    B = get_matrix()
    if B is None:
        return
    
    matrix_operations(A,B)

main()