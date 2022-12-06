f = open("input.txt", "r")
rawInput = f.read()

tmpData = rawInput.split("\n")
tmpData2 = []

containing_pairs = 0


for data_piece in tmpData:
   tmpData2.append(data_piece.split(","))

def does_contain(a, b):
  a = a.split("-")
  b = b.split("-")
  a_start = int(a[0])  
  a_end = int(a[1])
  b_start = int(b[0])
  b_end = int(b[1])

  return a_start <= b_start and a_end >= b_end

for pair in tmpData2:
  if does_contain(pair[0], pair[1]) or does_contain(pair[1], pair[0]):
      containing_pairs = containing_pairs + 1

print(containing_pairs)

def does_overlap(a, b):
  a = a.split("-")
  b = b.split("-")
  a_start = int(a[0])
  a_end = int(a[1])
  b_start = int(b[0])
  b_end = int(b[1])

  return a_start <= b_start and a_end >= b_start or b_start <= a_start and b_end >= a_end

overlapping_pairs = 0

for pair in tmpData2:
  if does_overlap(pair[0], pair[1]) or does_overlap(pair[1], pair[0]):
    overlapping_pairs = overlapping_pairs + 1

print(overlapping_pairs)