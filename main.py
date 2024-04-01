import copy
import os
import pygame
import random
from dotenv import load_dotenv


def get_env(key, type):
  try:
    if type == int:
      value = int(os.getenv(key))
      if value <= 0:
        raise ValueError
      return value
    elif type == tuple:
      value = tuple(map(int, os.getenv(key).removeprefix('(').removesuffix(')').split(',')))
      if len(value) != 3:
        raise ValueError
      return value
    elif type == bool:
      value = os.getenv(key)
      if value != '0' and value != '1':
        raise ValueError
      return value == '1'
    elif type == list:
      if os.getenv(key) == "[]":
        return []
      value = [[int(j) for j in i] for i in [x.split(',') for x in os.getenv(key).removeprefix('[(').removesuffix(')]').split('),(')]]
      return value
  except ValueError:
    print(f"Invalid variable {key}.")
    exit()


def create_gosper_glider_gun(gun):
  [x, y] = gun
  grid[y+4][x] = 1
  grid[y+5][x] = 1
  grid[y+4][x+1] = 1
  grid[y+5][x+1] = 1
  grid[y+2][x+13] = 1
  grid[y+2][x+12] = 1
  grid[y+3][x+11] = 1
  grid[y+4][x+10] = 1
  grid[y+5][x+10] = 1
  grid[y+6][x+10] = 1
  grid[y+7][x+11] = 1
  grid[y+8][x+12] = 1
  grid[y+8][x+13] = 1
  grid[y+5][x+14] = 1
  grid[y+3][x+15] = 1
  grid[y+4][x+16] = 1
  grid[y+5][x+16] = 1
  grid[y+6][x+16] = 1
  grid[y+5][x+17] = 1
  grid[y+7][x+15] = 1
  grid[y+2][x+20] = 1
  grid[y+3][x+20] = 1
  grid[y+4][x+20] = 1
  grid[y+2][x+21] = 1
  grid[y+3][x+21] = 1
  grid[y+4][x+21] = 1
  grid[y+1][x+22] = 1
  grid[y+5][x+22] = 1
  grid[y][x+24] = 1
  grid[y+1][x+24] = 1
  grid[y+5][x+24] = 1
  grid[y+6][x+24] = 1
  grid[y+2][x+34] = 1
  grid[y+3][x+34] = 1
  grid[y+2][x+35] = 1
  grid[y+3][x+35] = 1


def create_double_block_laying_switch_engine(engine):
  [x, y] = engine
  grid[y][x] = 1
  grid[y][x+1] = 1
  grid[y][x+2] = 1
  grid[y][x+3] = 1
  grid[y][x+4] = 1
  grid[y][x+5] = 1
  grid[y][x+6] = 1
  grid[y][x+7] = 1
  grid[y][x+9] = 1
  grid[y][x+10] = 1
  grid[y][x+11] = 1
  grid[y][x+12] = 1
  grid[y][x+13] = 1
  grid[y][x+17] = 1
  grid[y][x+18] = 1
  grid[y][x+19] = 1
  grid[y][x+26] = 1
  grid[y][x+27] = 1
  grid[y][x+28] = 1
  grid[y][x+29] = 1
  grid[y][x+30] = 1
  grid[y][x+31] = 1
  grid[y][x+32] = 1
  grid[y][x+34] = 1
  grid[y][x+35] = 1
  grid[y][x+36] = 1
  grid[y][x+37] = 1
  grid[y][x+38] = 1


def create_spacerake(spacerake):
  [x, y] = spacerake

  grid[y+15][x] = 1
  grid[y+17][x] = 1
  grid[y+18][x+1] = 1
  grid[y+18][x+2] = 1
  grid[y+18][x+3] = 1
  grid[y+18][x+4] = 1
  grid[y+17][x+4] = 1
  grid[y+16][x+4] = 1
  grid[y+15][x+3] = 1

  grid[y+5][x+8] = 1
  grid[y+6][x+8] = 1
  grid[y+6][x+7] = 1
  grid[y+7][x+6] = 1
  grid[y+8][x+7] = 1
  grid[y+8][x+8] = 1
  grid[y+8][x+9] = 1
  grid[y+8][x+10] = 1
  grid[y+8][x+11] = 1
  grid[y+9][x+8] = 1
  grid[y+9][x+9] = 1
  grid[y+9][x+10] = 1
  grid[y+9][x+11] = 1
  grid[y+10][x+11] = 1

  grid[y+1][x+9] = 1
  grid[y+2][x+9] = 1
  grid[y+1][x+10] = 1
  grid[y+2][x+10] = 1
  grid[y+3][x+10] = 1
  grid[y][x+11] = 1
  grid[y+2][x+11] = 1
  grid[y+3][x+11] = 1
  grid[y][x+12] = 1
  grid[y+1][x+12] = 1
  grid[y+2][x+12] = 1
  grid[y+1][x+13] = 1

  grid[y+1][x+17] = 1
  grid[y+3][x+17] = 1
  grid[y][x+18] = 1
  grid[y][x+19] = 1
  grid[y][x+20] = 1
  grid[y][x+21] = 1
  grid[y+1][x+21] = 1
  grid[y+2][x+21] = 1
  grid[y+3][x+20] = 1

  grid[y+6][x+17] = 1
  grid[y+6][x+18] = 1
  grid[y+7][x+16] = 1
  grid[y+8][x+16] = 1
  grid[y+9][x+15] = 1
  grid[y+9][x+16] = 1
  grid[y+10][x+16] = 1
  grid[y+10][x+17] = 1
  grid[y+7][x+19] = 1
  grid[y+8][x+19] = 1
  grid[y+9][x+19] = 1
  grid[y+9][x+18] = 1

  grid[y+15][x+17] = 1
  grid[y+17][x+17] = 1
  grid[y+14][x+18] = 1
  grid[y+14][x+19] = 1
  grid[y+14][x+20] = 1
  grid[y+14][x+21] = 1
  grid[y+15][x+21] = 1
  grid[y+16][x+21] = 1
  grid[y+17][x+20] = 1


load_dotenv()
WINDOW_WIDTH = get_env('WINDOW_WIDTH', int)
WINDOW_HEIGHT = get_env('WINDOW_HEIGHT', int)
GRID_WIDTH = get_env('GRID_WIDTH', int)
GRID_HEIGHT = get_env('GRID_HEIGHT', int)
CELL_BORDER_SIZE = get_env('CELL_BORDER_SIZE', int)
CELL_BORDER_COLOUR = get_env('CELL_BORDER_COLOUR', tuple)
DEAD_CELL_COLOUR = get_env('DEAD_CELL_COLOUR', tuple)
LIVE_CELL_COLOUR = get_env('LIVE_CELL_COLOUR', tuple)
STEP_DURATION = get_env('STEP_DURATION', int)
RANDOMISE_GRID = get_env('RANDOMISE_GRID', bool)
WRAP_AROUND_HORIZONTAL = get_env('WRAP_AROUND_HORIZONTAL', bool)
WRAP_AROUND_VERTICAL = get_env('WRAP_AROUND_VERTICAL', bool)
GOSPER_GLIDER_GUNS = get_env('GOSPER_GLIDER_GUNS', list)
SPACE_RAKES = get_env('SPACE_RAKES', list)
DOUBLE_BLOCK_LAYING_SWITCH_ENGINES = get_env('DOUBLE_BLOCK_LAYING_SWITCH_ENGINES', list)

CELL_SIZE = int(min(WINDOW_WIDTH / GRID_WIDTH, WINDOW_HEIGHT / GRID_HEIGHT))
GRID_X = (WINDOW_WIDTH - GRID_WIDTH * CELL_SIZE) / 2
GRID_Y = (WINDOW_HEIGHT - GRID_HEIGHT * CELL_SIZE) / 2

grid = []
for y in range(GRID_HEIGHT):
  row = []
  for x in range(GRID_WIDTH):
    row += [random.randint(0,1) if RANDOMISE_GRID else 0]
  grid += [row]
new_grid = copy.deepcopy(grid)

for gun in GOSPER_GLIDER_GUNS:
  create_gosper_glider_gun(gun)
for rake in SPACE_RAKES:
  create_spacerake(rake)
for engine in DOUBLE_BLOCK_LAYING_SWITCH_ENGINES:
  create_double_block_laying_switch_engine(engine)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(CELL_BORDER_COLOUR)

  for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
      pygame.draw.rect(
        screen,
        LIVE_CELL_COLOUR if grid[y][x] == 1 else DEAD_CELL_COLOUR,
        pygame.Rect(
          GRID_X + CELL_SIZE * x + CELL_BORDER_SIZE,
          GRID_Y + CELL_SIZE * y + CELL_BORDER_SIZE,
          CELL_SIZE - CELL_BORDER_SIZE,
          CELL_SIZE - CELL_BORDER_SIZE
        ),
        CELL_SIZE
      )

  pygame.display.flip()

  for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
      new_grid[y][x] = grid[y][x]
      live_neighbour_count = 0
      if y > 0 and x > 0 and grid[y-1][x-1] == 1:
        live_neighbour_count += 1
      if y > 0 and grid[y-1][x] == 1:
        live_neighbour_count += 1
      if y > 0 and x < GRID_WIDTH-1 and grid[y-1][x+1] == 1:
        live_neighbour_count += 1
      if x > 0 and grid[y][x-1] == 1:
        live_neighbour_count += 1
      if x < GRID_WIDTH-1 and grid[y][x+1] == 1:
        live_neighbour_count += 1
      if y < GRID_HEIGHT-1 and x > 0 and grid[y+1][x-1] == 1:
        live_neighbour_count += 1
      if y < GRID_HEIGHT-1 and grid[y+1][x] == 1:
        live_neighbour_count += 1
      if y < GRID_HEIGHT-1 and x < GRID_WIDTH-1 and grid[y+1][x+1] == 1:
        live_neighbour_count += 1

      if y == 0 and x == 0:
        if grid[GRID_HEIGHT-1][GRID_WIDTH-1] == 1 and WRAP_AROUND_HORIZONTAL and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[GRID_HEIGHT-1][0] == 1 and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[GRID_HEIGHT-1][1] == 1 and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[0][GRID_WIDTH-1] == 1 and WRAP_AROUND_HORIZONTAL:
          live_neighbour_count += 1
        if grid[1][GRID_WIDTH-1] == 1 and WRAP_AROUND_HORIZONTAL:
          live_neighbour_count += 1
      elif y == 0 and x == GRID_WIDTH-1:
        if grid[GRID_HEIGHT-1][GRID_WIDTH-2] == 1 and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[GRID_HEIGHT-1][GRID_WIDTH-1] == 1 and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[GRID_HEIGHT-1][0] == 1 and WRAP_AROUND_HORIZONTAL and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[0][0] == 1 and WRAP_AROUND_HORIZONTAL:
          live_neighbour_count += 1
        if grid[1][0] == 1 and WRAP_AROUND_HORIZONTAL:
          live_neighbour_count += 1
      elif y == GRID_HEIGHT-1 and x == 0:
        if grid[GRID_HEIGHT-2][GRID_WIDTH-1] == 1 and WRAP_AROUND_HORIZONTAL:
          live_neighbour_count += 1
        if grid[GRID_HEIGHT-1][GRID_WIDTH-1] == 1 and WRAP_AROUND_HORIZONTAL:
          live_neighbour_count += 1
        if grid[0][GRID_WIDTH-1] == 1 and WRAP_AROUND_HORIZONTAL and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[0][0] == 1 and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[0][1] == 1 and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
      elif y == GRID_HEIGHT-1 and x == GRID_WIDTH-1:
        if grid[GRID_HEIGHT-2][0] == 1 and WRAP_AROUND_HORIZONTAL:
          live_neighbour_count += 1
        if grid[GRID_HEIGHT-1][0] == 1 and WRAP_AROUND_HORIZONTAL:
          live_neighbour_count += 1
        if grid[0][0] == 1 and WRAP_AROUND_HORIZONTAL and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[0][GRID_WIDTH-1] == 1 and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
        if grid[0][GRID_WIDTH-2] == 1 and WRAP_AROUND_VERTICAL:
          live_neighbour_count += 1
      elif y == 0 and WRAP_AROUND_VERTICAL:
        if grid[GRID_HEIGHT-1][x-1] == 1:
          live_neighbour_count += 1
        if grid[GRID_HEIGHT-1][x] == 1:
          live_neighbour_count += 1
        if grid[GRID_HEIGHT-1][x+1] == 1:
          live_neighbour_count += 1
      elif y == GRID_HEIGHT-1 and WRAP_AROUND_VERTICAL:
        if grid[0][x-1] == 1:
          live_neighbour_count += 1
        if grid[0][x] == 1:
          live_neighbour_count += 1
        if grid[0][x+1] == 1:
          live_neighbour_count += 1
      elif x == 0 and WRAP_AROUND_HORIZONTAL:
        if grid[y-1][GRID_WIDTH-1] == 1:
          live_neighbour_count += 1
        if grid[y][GRID_WIDTH-1] == 1:
          live_neighbour_count += 1
        if grid[y+1][GRID_WIDTH-1] == 1:
          live_neighbour_count += 1
      elif x == GRID_WIDTH-1 and WRAP_AROUND_HORIZONTAL:
        if grid[y-1][0] == 1:
          live_neighbour_count += 1
        if grid[y][0] == 1:
          live_neighbour_count += 1
        if grid[y+1][0] == 1:
          live_neighbour_count += 1

      if grid[y][x] == 0:
        if live_neighbour_count == 3:
          new_grid[y][x] = 1
      elif grid[y][x] == 1:
        if live_neighbour_count < 2 or live_neighbour_count > 3:
          new_grid[y][x] = 0

  grid = copy.deepcopy(new_grid)

  clock.tick(60)

  pygame.time.wait(STEP_DURATION)

pygame.quit()