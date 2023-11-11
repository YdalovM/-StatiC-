# 1
# class Snowflakes:
# def __init__(self, count):
# self.count = count

# def __add__(self, n):
# self.count += n
# return self

# def __sub__(self, n):
# self.count -= n
# return self

# def __mul__(self, n):
# self.count *= n
# return self

# def __truediv__(self, n):
# self.count /= n
# return self

# def makeSnow(self, n_in_row):
# rows = self.count // n_in_row
# remainder = self.count % n_in_row
# snowflake_row = '*' * n_in_row
# snowflake_pattern = (snowflake_row + '\n') * rows + '*' * remainder
# return snowflake_pattern

# 3
# class Robot:
# def __init__(self, x, y):
# self.x = max(0, min(x, 100))
# self.y = max(0, min(y, 100))
# self.path_coords = [(self.x, self.y)]

# def move(self, commands):
# for command in commands:
# if command == 'N':
# self.y = min(self.y + 1, 100)
# elif command == 'S':
# self.y = max(self.y - 1, 0)
# elif command == 'E':
# self.x = min(self.x + 1, 100)
# elif command == 'W':
# self.x = max(self.x - 1, 0)
# self.path_coords.append((self.x, self.y))

# return (self.x, self.y)

# def path(self):
# if len(self.path_coords) == 1:
# return [(self.x, self.y)]
# else:
# return self.path_coords

# 4
# class Talking:
# def __init__(self, name):
# self.name = name
# self.yes_count = 0
# self.no_count = 0
# self.answered_yes_last = True

# def to_answer(self):
# if self.answered_yes_last:
# self.yes_count += 1
# self.answered_yes_last = False
# return "more"
# else:
# self.no_count += 1
# self.answered_yes_last = True
# return "meow"

# def number_yes(self):
# return self.yes_count
#
# def number_no(self):
# return self.no_count

# 2
# class Snowflake:
# def __init__(self, size):
# if size % 2 == 0:
# raise ValueError("Размер снежинки должен быть нечетным")
# self.size = size
# self.grid = [[' ' for _ in range(size)] for _ in range(size)]
# self.initialize_snowflake()

# def initialize_snowflake(self):
# center = self.size // 2
# self.grid[center][center] = '*'

# def thaw(self, steps):
# for _ in range(steps):
# self.remove_outer_layer()

# def remove_outer_layer(self):
# for i in range(self.size):
# self.grid[0][i] = ' '
# self.grid[self.size - 1][i] = ' '
# self.grid[i][0] = ' '
# self.grid[i][self.size - 1] = ' '

# def freeze(self, n):
# new_size = self.size + 2 * n
# new_grid = [[' ' for _ in range(new_size)] for _ in range(new_size)]
# offset = n
# for i in range(self.size):
# for j in range(self.size):
#     new_grid[i + offset][j + offset] = self.grid[i][j]
# self.size = new_size
# self.grid = new_grid

# def thicken(self):
# new_grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
# for i in range(self.size):
# for j in range(self.size):
#     if self.grid[i][j] == '*':
#         new_grid[i][j - 1] = '*'
#         new_grid[i][j] = '*'
#         new_grid[i][j + 1] = '*'
# self.grid = new_grid

# def show(self):
# for row in self.grid:
# print(''.join(row))