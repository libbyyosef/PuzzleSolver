from typing import List, Tuple, Set, Optional
import copy

# We define the types of a partial picture and a constraint (for type
# checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def helper_row_max_seen(row: int, picture: Picture, col: int,
                        color: int) -> int:
    counter1_row: int = 0
    counter2_row: int = 0
    for r1 in range(row + 1):
        if color == 0:
            if picture[r1][col] == color:
                counter1_row = 0
            else:
                counter1_row += 1
        else:
            if picture[r1][col] == color:
                counter1_row += 1
            else:
                counter1_row = 0

    for r2 in range(row + 1, len(picture)):
        if color == 0:
            if picture[r2][col] == color:
                return counter1_row + counter2_row
            else:
                counter2_row += 1
        else:
            if picture[r2][col] == color:
                counter2_row += 1
            else:
                return counter1_row + counter2_row
    return counter1_row + counter2_row


def helper_col_max_seen(row: int, picture: Picture, col: int,
                        color: int) -> int:
    counter1_col: int = 0
    counter2_col: int = 0
    for c1 in range(col):
        if color == 0:
            if picture[row][c1] == color:
                counter1_col = 0
            else:
                counter1_col += 1
        else:
            if picture[row][c1] == color:
                counter1_col += 1
            else:
                counter1_col = 0
    for c2 in range(col + 1, len(picture[0])):
        if color == 0:
            if picture[row][c2] == color:
                return counter1_col + counter2_col
            else:
                counter2_col += 1
        else:
            if picture[row][c2] == color:
                counter2_col += 1
            else:
                return counter1_col + counter2_col
    return counter1_col + counter2_col


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] == 0:
        return 0
    counter_row: int = helper_row_max_seen(row, picture, col, 0)
    counter_col: int = helper_col_max_seen(row, picture, col, 0)
    return counter_row + counter_col


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] == 0 or picture[row][col] == -1:
        return 0
    counter_row: int = helper_row_max_seen(row, picture, col, 1)
    counter_col: int = helper_col_max_seen(row, picture, col, 1)
    return counter_row + counter_col


def check_constraints(picture: Picture,
                      constraints_set: Set[Constraint]) -> int:
    new_list: list = []
    for r in constraints_set:
        new_list.append(r)
    result: int = 0
    for i in new_list:
        row = i[0]
        col = i[1]
        seen = i[2]
        max_seen = max_seen_cells(picture, row, col)
        min_seen = min_seen_cells(picture, row, col)
        if seen < min_seen or seen > max_seen:
            return 0
        elif min_seen == max_seen:
            result += 1
        else:
            continue
    if result == len(new_list):
        return 1
    else:
        return 2


def find_minus_one(picture: Picture) -> bool:
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if picture[i][j] == -1:
                return True
    return False


def create_board(m: int, n: int) -> Picture:
    picture: Picture = []
    for i in range(m):
        picture.append([])
        for j in range(n):
            picture[i].append(-1)
    return picture


def seen_1(picture: Picture, row, col) -> Picture:
    if row - 1 >= 0:
        picture[row - 1][col] = 0
    if row + 1 < len(picture):
        picture[row + 1][col] = 0
    if col - 1 >= 0:
        picture[row][col - 1] = 0
    if col + 1 <= len(picture[0]):
        picture[row][col + 1] = 0
    return picture


def placed_constraints(constraints_set: Set[Constraint], n: int,
                       m: int) -> Picture:
    picture: Picture = create_board(n, m)
    new_list = []
    for r in constraints_set:
        new_list.append(r)
    for i in new_list:
        row = i[0]
        col = i[1]
        seen = i[2]
        if seen == 0:
            picture[row][col] = 0
        elif seen == 1:
            picture = seen_1(picture, row, col)
            picture[row][col] = 1
        elif seen > 0:
            picture[row][col] = 1
    return picture


def solve_helper(picture: Picture, constraints_set: Set[Constraint],
                 index) -> Picture or None:
    if not find_minus_one(picture):
        return picture
    else:
        maxi = len(picture[0])
        row, col = index // maxi, index % maxi
        if picture[row][col] != -1:
            if solve_helper(picture, constraints_set, index + 1) is not None:
                return picture
            else:
                return None
        if check_constraints(picture, constraints_set) != 0:
            picture[row][col] = 0
            if check_constraints(picture, constraints_set) == 0:
                picture[row][col] = 1
            solve_helper(picture, constraints_set, index + 1)
            if not find_minus_one(picture):
                return picture
        else:
            return None


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> \
        Picture or None:
    new_picture: Picture = placed_constraints(constraints_set, n, m)
    picture = solve_helper(new_picture, constraints_set, 0)
    return picture


def helper_solutions(constraints_set: Set[Constraint], n: int, m: int,
                     picture) -> int:
    temp = copy.deepcopy(picture)
    if solve_helper(temp, constraints_set, 0) is None:
        return 0
    if not find_minus_one(picture):
        if check_constraints(picture, constraints_set) == 0:
            return 0
        else:
            return 1

    counter = 0
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if picture[i][j] != -1:
                continue
            else:
                for_1 = copy.deepcopy(picture)
                picture[i][j] = 0
                temp1 = copy.deepcopy(picture)
                if solve_helper(temp1, constraints_set, 0) is not None:
                    counter += helper_solutions(constraints_set, n, m,
                                                picture)
                for_1[i][j] = 1
                temp2 = copy.deepcopy(for_1)
                if solve_helper(temp2, constraints_set, 0) is not None:
                    counter += helper_solutions(constraints_set, n, m, for_1)
    return counter


def how_many_solutions(constraints_set: Set[Constraint], n: int,
                       m: int) -> int:
    if len(constraints_set) == 0:
        return 2 ** (n * m)
    picture: Picture = placed_constraints(constraints_set, n, m)
    temp = copy.deepcopy(picture)
    if not solve_helper(temp, constraints_set, 0):
        return 0
    return helper_solutions(constraints_set, n, m, picture)



def generate_puzzle(picture: Picture, ) -> Set[Constraint]:
    constraints_set: Set[Constraint] = set()
    new_set: set = set()

    for i in range(len(picture)):
        for j in range(len(picture[0])):
            seen=max_seen_cells(picture, i, j)
            constraints_set.add((i, j, seen))
    temp_set = copy.deepcopy(constraints_set)
    for constraint in constraints_set:
        temp_set.remove(constraint)
        if how_many_solutions(temp_set, len(picture), len(picture[
                                                                  0])) == 1 :
                continue
        else:
            new_set.add(constraint)
            temp_set.add(constraint)
    return new_set


