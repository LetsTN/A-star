import sys
from grid import Grid
from a_star import A_star

def main():
  matrix_path = sys.argv[1]
  start_arg = sys.argv[2].split(',')
  end_arg = sys.argv[3].split(',')

  start = (int(start_arg[0]), int(start_arg[1]))
  end = (int(end_arg[0]), int(end_arg[1]))

  matrix = Grid(matrix_path).get_grid()

  result, matrix = A_star(matrix, start, end).find_path()

  print("Mapa da trajetória (maracado com 'x'):")
  for line in matrix:
    print(line)

  print()
  print("Lista com as coordenadas:")
  print(result)


if __name__ == "__main__":
  main();