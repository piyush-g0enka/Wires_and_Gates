#!/usr/bin/env python3
from typing import List

WIRE_CHARACTERS = {'|', '-'}
INPUT_CHARACTERS = ('A', 'B')
GATE_CHARACTER = 'G'
OUTPUT_CHARACTER = 'X'


# Representation of a NAND gate

class NANDGate():
    def __init__(self, position):
        self.value = None
        self.left = None
        self.right = None
        self.position = position


def get_board(opname: str) -> str:
    # Read board from file

    with open(f"./circuits/{opname}.txt") as f:
        return f.read()


def gridify_board(board: str) -> List[List[str]]:
    # Return 2D char array representation of board

    return list(list(line) for line in board.split('\n'))


def evaluate_function(board: str, *inputs: bool) -> bool:
    # Given a board string, evaluate the boolean function with the
    # given inputs

    # dictionary to map character values to input
    character_dict = {}

    for character, value in zip(INPUT_CHARACTERS, inputs):
        character_dict[character] = value

    grid = gridify_board(board)

    ############## PRE-PROCESS GRID #################

    grid_height = len(grid)

    max_width = 0
    for row in grid:
        max_width = max(max_width, len(row))

    for row_i in range(0, grid_height):
        row_width = len(grid[row_i])
        grid[row_i].extend(" " * (max_width - row_width))

    grid_width = max_width

    ############## FIND OUTPUT CHARACTER POSITION #################

    output_coords = None

    for row_i in range(0, grid_height):
        for col_i in range(0, grid_width):
            if OUTPUT_CHARACTER == grid[row_i][col_i]:
                output_coords = (col_i, row_i)

    ############## TRAVERSE CIRCUIT #################

    # Get last NAND gate coordinates
    nand_gate_coords = find_nand_gate(grid, output_coords)
    output_gate = NANDGate(nand_gate_coords)
    output = traverse_circuit(grid, output_gate, character_dict)

    return output


# Gets the location of NAND gate associated with Output
def find_nand_gate(grid, output_coords):

    x, y = output_coords

    output_row = grid[y]

    for x_itr in range(x, 0, -1):
        if output_row[x_itr] == GATE_CHARACTER:
            return (x_itr, y)


# Traverses through the circuit from an output to an input G-->A / G-->G / G-->B
def find_input(grid, gate_coords, direction):

    x, y = gate_coords

    current_x = x

    if direction == "left":
        current_y = y-1
    else:
        current_y = y+1

    visited = set()

    # Traverse the wires till we come across a GATE/INPUT character
    while (grid[current_y][current_x] in WIRE_CHARACTERS):

        if (current_x, current_y) not in visited:

            visited.add((current_x, current_y))
            if ((current_x-1) >= 0) and (grid[current_y][current_x-1] in WIRE_CHARACTERS) and (current_x-1, current_y) not in visited:
                current_x -= 1

            elif ((current_y-1) >= 0) and (grid[current_y-1][current_x] in WIRE_CHARACTERS) and (current_x, current_y-1) not in visited:
                current_y -= 1

            elif ((current_y+1) < len(grid)) and (grid[current_y+1][current_x] in WIRE_CHARACTERS) and (current_x, current_y+1) not in visited:
                current_y += 1

            else:
                return (current_x-1, current_y)


# DFS traversal From X ---> A,B
def traverse_circuit(grid, node, ip_dict):

    x, y = node.position

    # Evaluate Left input
    if node.left is None:
        left_ip = find_input(grid, node.position, "left")

        x, y = left_ip
        character = grid[y][x]
        if character != GATE_CHARACTER:
            left_val = ip_dict[character]

        else:
            node.left = NANDGate(left_ip)
            left_val = traverse_circuit(grid, node.left, ip_dict)

    # Evaluate Right input
    if node.right is None:
        right_ip = find_input(grid, node.position, "right")
        x, y = right_ip
        character = grid[y][x]
        if character != GATE_CHARACTER:
            right_val = ip_dict[character]
        else:
            node.right = NANDGate(right_ip)
            right_val = traverse_circuit(grid, node.right, ip_dict)

    # Compute output using NAND Logic
    if (left_val == True and right_val == True):
        node.value = False

    else:
        node.value = True

    return node.value


if __name__ == "__main__":

    pass
