import re
#                 [M]     [V]     [L]
# [G]             [V] [C] [G]     [D]
# [J]             [Q] [W] [Z] [C] [J]
# [W]         [W] [G] [V] [D] [G] [C]
# [R]     [G] [N] [B] [D] [C] [M] [W]
# [F] [M] [H] [C] [S] [T] [N] [N] [N]
# [T] [W] [N] [R] [F] [R] [B] [J] [P]
# [Z] [G] [J] [J] [W] [S] [H] [S] [G]
#  1   2   3   4   5   6   7   8   9 

cargo = []
cargo.append(["Z", "T", "F", "R", "W", "J", "G"])
cargo.append(["G", "W", "M"])
cargo.append(["J", "N", "H", "G"])
cargo.append(["J", "R", "C", "N", "W"])
cargo.append(["W", "F", "S", "B", "G", "Q", "V", "M"])
cargo.append(["S", "R", "T", "D", "V", "W", "C"])
cargo.append(["H", "B", "N", "C", "D", "Z", "G", "V"])
cargo.append(["S", "J", "N", "M", "G", "C"])
cargo.append(["G", "P", "N", "W", "C", "J", "D", "L"])

def move_9000(amount, source, destination):
    for step in range(amount):
        transport = cargo[source-1].pop()
        cargo[destination-1].append(transport)

def move_9001(amount, source, destination):

    flip = -abs(amount)
    transport = cargo[source-1]
    items_to_move = transport[flip:]

    for item in items_to_move:
        cargo[source-1].pop()
        cargo[destination-1].append(item)

def show_top_cargo():

    for stack in cargo:
        print(stack.pop(), end="")

def part_one():

    with open('input.txt') as file:
        for index, line in enumerate(file):

            line_result = line.strip()
            result = re.search(r"move (\d+) from (\d+) to (\d+)", line_result)

            amount = int(result.group(1))
            source = int(result.group(2))
            destination = int(result.group(3))

            move_9000(amount, source, destination)

def part_two():

    with open('input.txt') as file:
        for index, line in enumerate(file):

            line_result = line.strip()
            result = re.search(r"move (\d+) from (\d+) to (\d+)", line_result)

            amount = int(result.group(1))
            source = int(result.group(2))
            destination = int(result.group(3))

            move_9001(amount, source, destination)

#part_one()
#show_top_cargo()
part_two()
show_top_cargo()