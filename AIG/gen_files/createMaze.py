from PIL import Image
from PIL import ImageDraw
import os
import numpy as np
import random as R

SUCCESS = 1
FAILURE = -1
END = 0


class MazeGen():  # 'x' means rows and 'y' means cols
    def __init__(self, x: int, y: int):
        self.sets = []
        self.walls = {}
        self.x, self.y = x, y
        self.steps = 0
        self.opposite = {
            'N': 'S',
            'S': 'N',
            'E': 'W',
            'W': 'E'
        }
        for row in range(self.y):
            for col in range(self.x):
                temp_set = {(row, col)}
                self.sets.append(temp_set)
                temp_walls = {
                    'N': 1,
                    'E': 1,
                    'S': 1,
                    'W': 1
                }
                if col == 0:
                    temp_walls['W'] = -1
                elif col == self.x - 1:
                    temp_walls['E'] = -1

                if row == 0:
                    temp_walls['N'] = -1
                elif row == self.y - 1:
                    temp_walls['S'] = -1

                self.walls[(row, col)] = temp_walls

    def find_set(self, y, x):
        for myset in self.sets:
            if tuple((y, x)) in myset:
                return myset

    def break_wall(self, x1: int, y1: int, wall: str, *, debug=False):
        if debug:
            points, rows = self.debug_points()

        if self.walls[(y1, x1)][wall] == -1:
            return SUCCESS

        set1 = self.find_set(y1, x1)
        index1 = self.sets.index(set1)
        y, x = 0, 0

        if wall == "N":
            y -= 1
        elif wall == "E":
            x += 1
        elif wall == "S":
            y += 1
        elif wall == "W":
            x -= 1

        x2, y2 = x1 + x, y1 + y

        if tuple((y2, x2)) in set1:
            return SUCCESS
        self.sets.pop(index1)
        set2 = self.find_set(y2, x2)
        points2, rows2 = self.debug_points()
        for point in set2:
            set1.add(point)
        self.sets.pop(self.sets.index(set2))

        self.sets.append(set1)

        self.walls[(y1, x1)][wall] = 0
        self.walls[(y2, x2)][self.opposite[wall]] = 0

        if len(self.sets) <= 1:
            return END
        return SUCCESS

    def randomize_point(self):
        return R.randint(0, self.y - 1), R.randint(0, self.x - 1)

    def randomize_wall(self):
        return R.choice(["N", "E", "S", "W"])

    def generate(self):
        result = 1
        while result != END:
            self.steps += 1
            y, x = self.randomize_point()
            wall = self.randomize_wall()
            result = self.break_wall(y, x, wall)
        self.walls[(0, R.randint(0, self.x - 1))]["N"] = 2
        self.walls[(self.y - 1, R.randint(0, self.x - 1))]["S"] = 2
        return self.get_board()

    def get_steps(self):
        return self.steps

    def debug_points(self):
        points, rows = 0, len(self.sets)
        for row in self.sets:
            points += len(row)
        return points, rows

    def get_board(self):
        result = []
        for row in range(self.y):
            result.append([])
            for col in range(self.x):
                result[row].append(self.walls[(row, col)])
        return result


###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
def createMaze(x: int, y: int):
    instance = MazeGen(x, y)
    return instance.generate()


def createImage(maze: list, *, px=30, width=4):
    rows, cols = len(maze), len(maze[0])

    image = Image.new("RGB", (cols * px, rows * px), color=(255, 255, 255))
    drawer = ImageDraw.Draw(image)
    filler = (255, 0, 0)
    for i in range(rows):
        for j in range(cols):
            if maze[i][j]["N"] in [1, -1]:
                drawer.line([(px * j, px * i), (px * j + px - 1, px * i)], fill=filler, width=width)
            if maze[i][j]["E"] in [1, -1]:
                drawer.line([(px * j + px - 1, px * i), (px * j + px - 1, px * i + px - 1)], fill=filler, width=width)
            if maze[i][j]["S"] in [1, -1]:
                drawer.line([(px * j, px * i + px - 1), (px * j + px - 1, px * i + px - 1)], fill=filler, width=width)
            if maze[i][j]["W"] in [1, -1]:
                drawer.line([(px * j, px * i), (px * j, px * i + px - 1)], fill=filler, width=width)
            if maze[i][j]["N"] in [2]:
                drawer.line([(px * j, px * i), (px * j + px - 1, px * i)], fill=(0, 0, 255), width=width)
            if maze[i][j]["S"] in [2]:
                drawer.line([(px * j, px * i + px - 1), (px * j + px - 1, px * i + px - 1)], fill=(0, 0, 255),
                            width=width)

    path = os.path.split(os.getcwd())[0]
    path += "/timathon/AIG/static/assets/img/"
    image.save(f"{path}maze.png")


def run(x: int, y: int, px=30):
    maze = createMaze(x, y)
    createImage(maze, px=px)


