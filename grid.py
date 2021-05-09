class Grid:
  
  def __init__(self, matrix_path):
    self.matrix = self.buid_grid(matrix_path)

  def buid_grid(self, matrix_path):
    matrix = []

    with open(matrix_path, 'r') as matrix_file:
      line = matrix_file.readline().rstrip('\n')
      while line != '':
        matrix_line = line.split(' ')

        matrix.append(matrix_line)
        line = matrix_file.readline().rstrip('\n')
    
    return matrix
  
  def get_grid(self):
    return self.matrix


