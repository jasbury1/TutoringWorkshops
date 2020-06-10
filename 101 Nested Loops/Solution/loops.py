

def main():
    matrix1 = [[1, 2, 5], [6, 3, 5], [2, 3, 6]]
    matrix2 = [[1, 2, 3, 5], [6, 3, 5, 6], [2, 3, 6], [3, 4, 5, 7]]
    matrix3 = [[1, 2], [3, 4]]
    matrix4 = []
    matrix5 = [[1, 2], [], [3, 4, 5]]

    vector1 = [2, 3, 4]

    scalar1 = 3
    
    print_matrix1(matrix2)
    print()
    print_matrix2(matrix2)
    print()
    print_matrix1(scalar_multiplication2(matrix2, 2))
    print()
    scalar_multiplication1(matrix2, 2)
    print_matrix1(matrix2)
    print()
    print(mat_vec_multiplication(matrix1, vector1))


'''
  This funtion should take a 2D list and print it out as a matrix.
  Use one space between each entry in each row
  You may not assume each row has the same amount of columns
  =================================================================
  Example runs:
  
  matrix = [[1, 2, 3, 5], [6, 3, 5, 6], [2, 3, 6], [3, 4, 5, 7]]

  will be printed as:

    1 2 3 5
    6 3 5 6
    2 3 6
    3 4 5 7

  =================================================================
'''
def print_matrix1(matrix):
    for row in matrix:
        row_str = ""
        for entry in row:
            row_str += str(entry) + " "
        print(row_str)

def print_matrix2(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

'''
  This funtion should take a matrix represented as a 2D list
  and multiply all entries by the value
  You may not assume each row has the same amount of columns
  =================================================================
  Example runs:
  
  matrix = [[1, 2, 5], [6, 3, 5], [2, 3, 6]]
  value = 3

  will return: [[3, 6, 15], [18, 9, 15], [6, 9, 18]]

  =================================================================
'''
def scalar_multiplication1(matrix, value):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = matrix[row][col] * value

def scalar_multiplication2(matrix, value):
    result = []

    for row in range(len(matrix)):
        new_row = []
        for col in range(len(matrix[row])):
            new_row.append(matrix[row][col] * value)
        result.append(new_row)
    return result


'''
  This funtion takes a matrix and multiplies it by the vector
  This works in math like the following:

    |a b c|   |x|       |ax + by + cz|
    |d e f| * |y|   =   |dx + ey + fz|
    |g h i|   |z|       |gx + hy + iz|

  You MAY assume the matrix and vector have the same # of rows

  =================================================================
  Example runs:
  
  matrix = [[1, 2, 5], [6, 3, 5], [2, 3, 6]]
  vector = [2, 3, 4]

  will return: [28, 41, 37]

  =================================================================
'''
def mat_vec_multiplication(matrix, vector):
    result = []
    for row in range(len(matrix)):
        counter  = 0
        for col in range(len(matrix[row])):
            counter += matrix[row][col] * vector[col]
        result.append(counter)
    return result

if __name__ == '__main__':
    main()
