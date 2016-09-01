# -*- coding: UTF-8 -*-
"""
电脑 = x = 1
人 = o = -1
"""
gameover = False

ai_first = False
steps = 0
win = 0

turn_to_ai = False

pc = False
turn = False

table = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

better_pos = [[2, 2],
              [1, 1],
              [1, 3],

              [3, 1],
              [3, 3],
              [1, 2],

              [2, 1],
              [2, 3],
              [3, 2],
              ]


def printtable():
    for row in range(3):
        print(" " + table[row][0] + " | " + table[row][1] + " | " + table[row][2])

        if not row == 2:
            print("-" * 11)


def get_row_value(row):
    s = 0
    for i in range(3):
        if table[row][i] == ' ':
            s += 0
        elif table[row][i] == 'o':
            s += -1
        elif table[row][i] == 'x':
            s += 1
    return s


def get_col_value(col):
    s = 0
    for i in range(3):
        if table[i][col] == ' ':
            s += 0
        elif table[i][col] == 'o':
            s += -1
        elif table[i][col] == 'x':
            s += 1
            pass
    return s


def get_dia_value(dia):
    s = 0
    # '\' 斜行
    if dia == 0:
        for i in range(3):
            if table[i][i] == ' ':
                s += 0
            elif table[i][i] == 'o':
                s += -1
            elif table[i][i] == 'x':
                s += 1
    # '/' 斜行
    elif dia == 1:
        for i in range(3):
            if table[i][3-1-i] == ' ':
                s += 0
            elif table[i][3-1-i] == 'o':
                s += -1
            elif table[i][3-1-i] == 'x':
                s += 1
    return s


def get_line_score():
    res_array = [-10, -10, -10, -10, -10, -10, -10, -10]
    for i in range(8):
        if int(i/3) == 0:
            res_array[i] = (get_row_value(i % 3))
        if int(i/3) == 1:
            res_array[i] = (get_col_value(i % 3))
        if int(i/3) == 2:
            res_array[i] = (get_dia_value(i % 3))
    return res_array


def judge():
    res_arr = get_line_score()
    # print('judge()', res_arr)
    for i in range(len(res_arr)):
        if abs(res_arr[i]) == 3:
            global gameover
            gameover = True
            global steps
            steps = 0
            global win
            if ai_first:
                if steps % 2 == 1:
                    win = 1
                else:
                    win = -1
            else:
                if steps % 2 == 0:
                    win = 1
                else:
                    win = -1
            print('game over')
            if win == 1:
                print("|**** computer win ****|")
            elif win == -1:
                print("|**** computer win ****|")

    if steps == 9:
        gameover = True
        steps = 0
        print('game over')
        print("|**** 平局 ****|")


def find_goal(res_arr, v):
    for i in range(len(res_arr)):
        if res_arr[i] == v:
            print('|v| = 2:(v, i, arr[i])', v, i, res_arr[i])
            if int(i/3) == 0:
                for j in range(3):
                    if (table[int(i % 3)][j]) == ' ':
                        return [i+1, j+1]
            elif int(i/3) == 1:
                for j in range(3):
                    if (table[j][int(i % 3)]) == ' ':
                        return [j+1, int(i % 3)+1]
            elif int(i/3) == 2:
                # '\'
                if i % 3 == 0:
                    for j in range(3):
                        if table[j][j] == ' ':
                            return [j+1, j+1]
                # '/'
                if i % 3 == 1:
                    for j in range(3):
                        if table[j][3-1-j] == ' ':
                            return [j+1, (3-1-j)+1]
    else:
        return []


def cal_position():
    print('cal_position()')
    res_arr = get_line_score()
    # 找我方2连
    p = find_goal(res_arr, 2)
    if len(p) == 2:
        print("p_2", p)
        return p
    # 如果我方没有2连就找敌方2连
    p = find_goal(res_arr, -2)
    if len(p) == 2:
        print("p_-2", p)
        return p
    # 如果没有2连，不管那么多啦！直接根据最优位置放置棋子
    for i in range(len(better_pos)):
        p = better_pos[i]
        if table[p[0]-1][p[1]-1] == ' ':
            better_pos.remove(better_pos[i])
            print("p_%d", i, p)
            return p
    else:
        print("不可能！如果你看到我，证明出bug了！")

while not pc:
    ch = input("请输入1选择跟AI对战\n")
    if ch == '1':
        pc = True
    elif not ch == 1:
        print("乖，听话，选1")

first_flag = False
while not first_flag:
    first = input("请选择1：电脑先下 或者 2：您先下：\n")
    if first not in ['1', '2']:
        print("乖，请选 1 或 2 不要乱选")
    elif str(first) == '1':
        ai_first = True
        turn_to_ai = True
        first_flag = True
        break
    elif str(first) == '2':
        ai_first = False
        first_flag = True
        break

while not gameover:
    if turn_to_ai:
        pos = cal_position()
        table[int(pos[0])-1][int(pos[1])-1] = "x"
        steps += 1
        printtable()
        judge()
        turn_to_ai = False
    else:
        pos = input('input your choise by row and col (e.g. 13):\n')
        if not pos[0] in ["1", "2", "3"] or not pos[1] in ["1", "2", "3"]:
            print("numbers not in range")
        elif table[int(pos[0]) - 1][int(pos[1]) - 1] != " ":
            print("cell are already used")
        else:
            table[int(pos[0]) - 1][int(pos[1]) - 1] = "o"
            steps += 1
            printtable()
            judge()
            turn_to_ai = True
