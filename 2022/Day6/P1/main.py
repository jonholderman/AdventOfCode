def has_duplicates(arr):
    dup = {x for x in arr if arr.count(x) > 1}

    if len(dup) > 0:
        return True
    else:
        return False

def marker_pos(signal, size):
    marker = ""
    for pos, char in enumerate(signal):
        marker = (marker + char)[-size:]
        if len(set(marker)) == size:
            return pos + 1

with open('input.txt') as file:
    for index, line in enumerate(file):

        line_result = line.strip()

        p1 = marker_pos(line_result, 4)
        p2 = marker_pos(line_result, 14)

        print("Part 1: ", p1)
        print("Part 2: ", p2)