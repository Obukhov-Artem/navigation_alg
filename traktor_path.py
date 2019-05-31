import copy


class Traktor_path():
    def __init__(self, matrix, null_postion=(0, 0), final_postion=(0, 0)):
        self.matrix = matrix
        pozIn, pozOut = null_postion, final_postion
        path = self.transform_lab(self.matrix)
        eval = self.evalution_lab(path)
        eval_final = eval * 2
        path[pozIn[0]][pozIn[1]] = 1
        s_w = 1
        iter_num = 0
        while eval != eval_final and iter_num < 5:
            pozOuts = self.next_finish(path, pozIn)
            iter_num += 1
            eval = self.evalution_lab(path)
            variants = []
            for pos in pozOuts:
                path2 = self.found(path, pos, s_w)
                for p in path2:
                    if self.evalution_lab(p) <= eval:
                        variants.append([self.evalution_lab(p), pos, p])
            variants = sorted(variants, key=lambda x: x[0])
            if variants:
                path = copy.deepcopy(variants[0][2])
                pos = variants[0][1]

                path, s_w = self.transform_matrix(path)

            else:
                break
        turns, out = self.get_finish(path)
        self.matrix = path
        self.path = self.printPath(self.matrix, out)
        self.matrix_print =  "\n".join(",".join("{:^3}".format(line) for line in pp) for pp in self.matrix)

    def get_path(self):
        return self.path

    def get_matrix_str(self):
        return self.matrix_print

    def get_matrix(self):
        return self.matrix

    def found(self, pathArr_0, finPoint, start_w=1):
        pathArr = copy.deepcopy(pathArr_0)
        weight = start_w
        paths = []
        xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(len(pathArr) * len(pathArr[0])):
            weight += 1
            for y in range(len(pathArr)):
                for x in range(len(pathArr[y])):
                    if pathArr[y][x] == (weight - 1):
                        for x1, y1 in xy:
                            try:
                                if pathArr[y + y1][x + x1] == -1:
                                    pathArr[y + y1][x + x1] -= 1
                            except Exception:
                                pass
                        move = []
                        try:
                            if x <= finPoint[1]:
                                move.append((x < (len(pathArr[y]) - 1)
                                             and pathArr[y][x + 1] == 0, y, x + 1))
                                move.append((x < (len(pathArr[y]) - 1)
                                             and y < (len(pathArr) - 1)
                                             and pathArr[y][x + 1] <= -1
                                             and pathArr[y + 1][x] == 0, y + 1, x))
                                move.append((x < (len(pathArr[y]) - 1)
                                             and y > 0
                                             and pathArr[y][x + 1] <= -1
                                             and pathArr[y - 1][x] == 0, y - 1, x))
                            if x > finPoint[1]:
                                move.append((x > 0 and pathArr[y][x - 1] == 0, y, x - 1))
                                move.append((x > 0 and pathArr[y][x - 1] <= -1
                                             and y < (len(pathArr) - 1)
                                             and pathArr[y + 1][x] == 0, y + 1, x))
                                move.append((x > 0 and pathArr[y][x - 1] <= -1
                                             and y > 0
                                             and pathArr[y - 1][x] == 0, y - 1, x))
                            if y <= finPoint[0]:
                                move.append((y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0, y + 1, x))
                                move.append((y < (len(pathArr) - 1)
                                             and pathArr[y + 1][x] <= -1
                                             and x > 0
                                             and pathArr[y][x - 1] == 0, y, x - 1))
                                move.append((y < (len(pathArr) - 1)
                                             and pathArr[y + 1][x] <= -1
                                             and x < (len(pathArr[y]) - 1)
                                             and pathArr[y][x + 1] == 0, y, x + 1))
                            if y > finPoint[0]:
                                move.append((y > 0 and pathArr[y - 1][x] == 0, y - 1, x))
                                move.append((y > 0 and pathArr[y - 1][x] <= -1
                                             and pathArr[y][x - 1] == 0, y, x - 1))
                                move.append((y > 0 and pathArr[y - 1][x] <= -1
                                             and pathArr[y][x + 1] == 0, y, x + 1))
                        except Exception:
                            pass
                        if not move:
                            move = [(y > 0 and pathArr[y - 1][x] == 0, y - 1, x),
                                    (y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0, y + 1, x),
                                    (x > 0 and pathArr[y][x - 1] == 0, y, x - 1),
                                    (x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0, y, x + 1)]
                        v = 0
                        for m, yy, xx in set(move):
                            if m:
                                if v > 0:
                                    pathArr2 = copy.deepcopy(pathArr)
                                    pathArr2[yy][xx] = weight
                                    paths.extend(self.found(pathArr2, finPoint, start_w=weight))
                                else:

                                    pathArr[yy][xx] = weight
                                    v += 1
                                    break
        paths.append(copy.deepcopy(pathArr))
        return paths

    def printPath(self, pathArr, finPoint):
        y = finPoint[0]
        x = finPoint[1]
        weight = pathArr[y][x]
        result = list(range(weight))
        while (weight):
            weight -= 1
            if y > 0 and pathArr[y - 1][x] == weight:
                y -= 1
                result[weight] = 'down'
            elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
                result[weight] = 'up'
                y += 1
            elif x > 0 and pathArr[y][x - 1] == weight:
                result[weight] = 'right'
                x -= 1
            elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
                result[weight] = 'left'
                x += 1
        return result[1:]

    def transform_lab(self, labirint):
        for i in range(len(labirint)):
            for j in range(len(labirint[i])):

                if labirint[i][j] != 0:
                    labirint[i][j] = -1
        return labirint

    def transform_matrix(self, labirint):
        return labirint, max(max(i for i in j) for j in labirint)

    def evalution_lab(self, labirint):
        eval = sum([sum([i for i in j if i < 0]) for j in labirint])
        return eval

    def check_edge(self,point, lab):
        y, x = point
        r = 0
        mass = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for mx, my in mass:
            if y + my >= 0 and y + my < len(lab) and x + mx >= 0 and x + mx < len(lab[0]):
                if lab[y + my][x + mx] == -1:
                    r += 1
        if r <= 1:
            return True
        return False

    def next_finish(self, labirint, start_pos):
        y0, x0 = start_pos

        mass_edge = []
        delta = 3
        for i in range(max(y0 - delta, 0), min(y0 + delta, len(labirint))):
            for j in range(0, len(labirint[i])):
                if labirint[i][j] == -1:
                    if self.check_edge((i, j), labirint):
                        mass_edge.append([i, j])

        for i in range(0, len(labirint)):
            for j in range(max(x0 - delta, 0), min(x0 + delta, len(labirint[i]))):
                if labirint[i][j] == -1:
                    if self.check_edge((i, j), labirint) and [i, j] not in mass_edge:
                        mass_edge.append([i, j])
        mass_edge = sorted(mass_edge, key=lambda x: (abs(x[1] - x0), abs(x[0] - y0)))

        return mass_edge

    def get_finish(self, labirint):
        y, x = 0, 0
        value = 0
        for i in range(len(labirint)):
            for j in range(len(labirint[i])):
                if labirint[i][j] > value:
                    value = labirint[i][j]
                    y, x = i, j
        return value, (y, x)


labirint = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
a = Traktor_path(labirint,(10, 1),(5,5))
print(a.get_path())
print(a.get_matrix())
print(a.get_matrix_str())