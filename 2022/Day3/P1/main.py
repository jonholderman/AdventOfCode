
def get_duplicate_chars(s1, s2):

    duplicate_chars = []

    for i in range(len(s1)):
        for j in range(len(s2)):

            left = s1[i]
            right = s2[j]
            if left == right:
                duplicate_chars.append(left)

            

    return duplicate_chars

leter_dict = {
    'a': 1, 'b': 2, 'c': 3,'d': 4, 'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 
    'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}

total_sum_of_priorities = 0

with open('sample.txt') as file:
    for index, line in enumerate(file):

        sum_of_priorities = 0

        line_result = line.strip()
        string_length = int(len(line_result))
        mid_point = int(string_length / 2)

        first_compartment = line_result[0:mid_point-1]
        second_compartment = line_result[mid_point:]

        duplicate_chars = get_duplicate_chars(first_compartment, second_compartment)

        print("Line Result: ", line_result)
        print("1st: ", first_compartment)
        print("2nd: ", second_compartment)
        print("Duplicate Chars: ", duplicate_chars)

        for char in duplicate_chars:
            sum_of_priorities = sum_of_priorities + leter_dict[char]
        
        print("Sum of Priorities: ", sum_of_priorities)
        print("")

        total_sum_of_priorities = total_sum_of_priorities + sum_of_priorities

print("")
print("#####")
print("Total Sum of Priorities: ", total_sum_of_priorities)
print("")
