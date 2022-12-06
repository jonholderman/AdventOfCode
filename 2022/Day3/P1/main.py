
def get_duplicate_chars(s1, s2):

    duplicate_chars = []
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in range(len(chars)):
        if chars[char] in s1:
            if chars[char] in s2:
                duplicate_chars.append(chars[char])

    return duplicate_chars

def get_compartment(rucksack, compartment_number):

    compartment = ""

    string_length = int(len(rucksack))
    mid_point = int(string_length / 2)

    if compartment_number == 1:
        compartment = rucksack[0:mid_point-1]
    elif compartment_number == 2:
        compartment = rucksack[mid_point:]

    return compartment

leter_dict = {
    'a': 1,  'b': 2,  'c': 3,  'd': 4,  'e': 5,  'f': 6,  'g': 7,  'h': 8,  'i': 9,  'j': 10, 'k': 11, 'l': 12, 'm': 13,
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 
    'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}

def convert_char_to_int(c):

    value = 0

    if c.islower():
        ord(c) - 96
    else: 
        ord(c) - 38

    return value

total_sum_of_priorities = 0

with open('input.txt') as file:
    for index, line in enumerate(file):

        sum_of_priorities = 0
        line_result = line.strip()

        first_compartment = get_compartment(line_result, 1)
        second_compartment = get_compartment(line_result, 2)

        duplicate_chars = get_duplicate_chars(first_compartment, second_compartment)

        for char in duplicate_chars:
            sum_of_priorities = sum_of_priorities + convert_char_to_int(char)

        total_sum_of_priorities = total_sum_of_priorities + sum_of_priorities

        print("Line Result: ", line_result)
        print("Line Split: ", first_compartment, " | ", second_compartment)
        print("Duplicate Chars: ", duplicate_chars)
        print("Sum of Priorities: ", sum_of_priorities)
        print("Total Sum of Priorities: ", total_sum_of_priorities)
        print("")

print("")
print("#####")
print("Total Sum of Priorities: ", total_sum_of_priorities)
print("")
