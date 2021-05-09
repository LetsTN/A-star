from math import pow, sqrt


class A_star:
  def __init__(self, matrix, start, end):
    self.matrix = matrix
    self.start = start
    self.end = end
    self.path_found = False


  def find_path(self):
    dist_objective = {}
    dist_traveled = {}
    heuristic = {}
    before = {}
    states = []

    dist_traveled[self.start] = 0
    dist_objective[self.start] = self.calc_dist_objective(self.start, self.end) 
    heuristic[self.start] = dist_traveled[self.start] + dist_traveled[self.start]
    before[self.start] = None

    fringe = []
    fringe.append(self.start)
    while len(fringe) != 0:
      most_promising = self.find_most_promising(fringe, heuristic)
      state = fringe.pop(most_promising)

      if state == self.end:
        self.path_found = True
        break

      next_states = self.find_next(state)
      states.append(state)

      for i in range (0, len(next_states)):	
        next_state = next_states[i]
        if next_state not in states and next_state not in fringe:
          fringe.append(next_state)
          if next_state not in heuristic.keys():
            dist_objective[next_state] = self.calc_dist_objective(next_state, self.end)
            dist_traveled[next_state] = dist_traveled[state] + 1
            heuristic[next_state] = dist_objective[next_state] + dist_traveled[next_state]
            before[next_state] = state

    response_path = []
    response_path.append(self.end)
    state = self.end
    while before[state] != None:
      self.matrix[state[0]][state[1]] = 'x'
      response_path.append(before[state])
      state = before[state]
    self.matrix[state[0]][state[1]] = 'x'
    response_path = response_path[::-1]

    return response_path, self.matrix;

  def find_next(self, current_pos):
    i = current_pos[0]
    j = current_pos[1]
    m = len(self.matrix)
    n = len(self.matrix[0])
    next = []

    if i > 0 and self.matrix[i-1][j] != '1': # cima
      next.append ((i-1, j))
    if i+1 < m and self.matrix[i+1][j] != '1': # baixo
      next.append ((i+1, j))
    if j > 0 and self.matrix[i][j-1] != '1': # esquerda
      next.append ((i, j-1))
    if j+1 < n and self.matrix[i][j+1] != '1': # direita
      next.append ((i, j+1))

    return next

  def calc_dist_objective(self, start, end):
    i_start = start[0]
    j_start = start[1]

    i_end = end[0]
    j_end = end[1]

    dist = ((i_end - i_start)**2 + (j_end - j_start)**2)**(1/2)
    return dist

  def find_most_promising(self, fringe, heuristic):
    most_promissing = None
    most_promissing_value = 1000000000
    most_promissing_index = 0
    current_intex = 0

    for state in fringe:
      if heuristic[state] < most_promissing_value:
        most_promissing = state
        most_promissing_value = heuristic[state]
        most_promissing_index = current_intex
      current_intex = current_intex + 1

    return most_promissing_index