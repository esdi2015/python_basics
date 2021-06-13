
class Matrix:
    def __init__(self, list_of_lists):
        self.matrix_data = list_of_lists

    def __str__(self):
        result = []
        for row in self.matrix_data:
            result.append(', '.join(map(str, row)))
        result = '\n'.join(result)
        return result

    def __add__(self, other):
        _new_list = []
        for i, row in enumerate(self.matrix_data):
            _new_row = []
            for j, r in enumerate(row):
                _new_row.append(self.matrix_data[i][j] + other.matrix_data[i][j])
            _new_list.append(_new_row)
        return Matrix(_new_list)


if __name__ == '__main__':
    matrix_data = [[2, 3, 4], [5, 4, 3]]
    matrix = Matrix(matrix_data)
    print('matrix')
    print(matrix)

    matrix_data_1 = [[1, 1, 1], [1, 1, 1]]
    matrix_1 = Matrix(matrix_data_1)
    print('matrix_1')
    print(matrix_1)

    matrix_sum = matrix + matrix_1
    print('matrix_sum')
    print(matrix_sum)

