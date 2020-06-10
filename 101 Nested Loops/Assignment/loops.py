

def main():
    # Some test variables are created for you. Be sure to create more,
    # and call your functions with these variables to test them out

    matrix1 = [[1, 2, 5], [6, 3, 5], [2, 3, 6]]
    matrix2 = [[1, 2, 3, 5], [6, 3, 5, 6], [2, 3, 6], [3, 4, 5, 7]]
    matrix3 = [[1, 2], [3, 4]]

    vector1 = [2, 3, 4]

    scalar1 = 3


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
def print_matrix(matrix):
    pass

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
def scalar_multiplication(matrix, value):
    pass

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
    pass

if __name__ == '__main__':
    main()
