#!/usr/bin/python

def main():
    """
    ▄▄▄▄▄                  ▄           ▄▄▄▄▄ 
    █   ▀█  ▄▄▄    ▄ ▄▄  ▄▄█▄▄           █   
    █▄▄▄█▀ ▀   █   █▀  ▀   █             █   
    █      ▄▀▀▀█   █       █             █   
    █      ▀▄▄▀█   █       ▀▄▄         ▄▄█▄▄

    """

    input = open("input.txt")

    chosen_numbers = [int(x) for x in input.readline().rstrip().split(",")]
    boards = []
    number_board_map = {}
    board_input = [x.rstrip() for x in input.readlines()]
    board_input_index = 1

    input.close()

    for x in range(len(board_input) // 6):
        board = []
        board_row_index = 0

        for y in range(5):
            board.append([int(x) for x in board_input[board_input_index].split()])

            for x in range(len(board[board_row_index])):
                if board[board_row_index][x] in number_board_map:
                    number_board_map[board[board_row_index][x]].append([board_input_index // 6, board_row_index, x])
                else:
                    number_board_map[board[board_row_index][x]] = [[board_input_index // 6, board_row_index, x]]

            board_row_index += 1
            board_input_index += 1

        boards.append(board)
        board_input_index += 1

    first_winning_board = get_winning_boards(chosen_numbers, number_board_map, boards)

    print(first_winning_board[0][1])

    """
    ▄▄▄▄▄                  ▄           ▄▄▄▄▄  ▄▄▄▄▄ 
    █   ▀█  ▄▄▄    ▄ ▄▄  ▄▄█▄▄           █      █   
    █▄▄▄█▀ ▀   █   █▀  ▀   █             █      █   
    █      ▄▀▀▀█   █       █             █      █   
    █      ▀▄▄▀█   █       ▀▄▄         ▄▄█▄▄  ▄▄█▄▄

    """

    boards.pop(first_winning_board[0][0])

    for x in number_board_map:
        for y in range(len(number_board_map[x]) - 1, -1, -1):
            if number_board_map[x][y][0] == first_winning_board[0][0]:
                number_board_map[x].pop(y)
            elif number_board_map[x][y][0] > first_winning_board[0][0]:
                number_board_map[x][y][0] -= 1

    while len(boards) > 1:
        next_winning_boards = get_winning_boards(chosen_numbers, number_board_map, boards)
        next_winning_board_indices = set()
        board_pop_offset = 0

        for x in next_winning_boards:
            next_winning_board_indices.add(x[0])
            boards.pop(x[0] - board_pop_offset)
            board_pop_offset += 1

        for x in number_board_map:
            for y in range(len(number_board_map[x]) - 1, -1, -1):
                if number_board_map[x][y][0] in next_winning_board_indices:
                    number_board_map[x].pop(y)
                else:
                    smaller_winning_board_indices = [z for z in next_winning_board_indices if z < number_board_map[x][y][0]]
                    number_board_map[x][y][0] -= len(smaller_winning_board_indices)

    print(get_winning_boards(chosen_numbers, number_board_map, boards)[0][1])

def get_winning_boards(chosen_numbers, number_board_map, boards):
    winning_boards = []

    while len(chosen_numbers) > 0:
        x = chosen_numbers[0]
        winning_board_found = False

        if x in number_board_map:
            for y in number_board_map[x]:
                boards[y[0]][y[1]][y[2]] = -1

            for y in number_board_map[x]:
                column_matched = True
                row_matched = True

                # check if the entire row or column in the current board has been matched
                for z in range(5):
                    if boards[y[0]][y[1]][z] != -1:
                        row_matched = False
                        break

                if row_matched == True:
                    winning_board_found = True
                    unmarked_number_sum = 0

                    for z in boards[y[0]]:
                        for q in z:
                            unmarked_number_sum += q if q != -1 else 0

                    winning_boards.append((y[0], unmarked_number_sum * x))

                    continue

                for z in range(5):
                    if boards[y[0]][z][y[2]] != -1:
                        column_matched = False
                        break

                if column_matched == True:
                    winning_board_found = True
                    unmarked_number_sum = 0

                    for z in boards[y[0]]:
                        for q in z:
                            unmarked_number_sum += q if q != -1 else 0

                    winning_boards.append((y[0], unmarked_number_sum * x))

                    continue

            number_board_map.pop(x)

        chosen_numbers.pop(0)

        if winning_board_found == True:
            break

    return winning_boards

if __name__ == "__main__":
    main()