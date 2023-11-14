# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid 
def validate( block_data ):
num = grid[1][1]
b=0
  # Check whether the centre block is a bomb, a number, or an invalid input
  # Skip bombs, send an error on invalid input, verify numbers

if num == -1:
  StopIteration

for i in range(3):
  for j in range(3):
    if (i, j) == (1, 1):
      continue
    if  grid[i][j] == -1:
      b = b+1

if num == b:
   print("Valid middle block")
else:
   print("Invalid middle block")

 


grid = [
  [-1,1,0],
  [1,1,0],
  [0,0,0]
]

print (validate(grid))
