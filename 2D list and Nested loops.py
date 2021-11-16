#2dimentional list 
number_grid = [
    [1,2,3],            #row 0
    [5,6,7],            #row 1
    [5,7,8],            #row 2 
    [0]
]

print(number_grid[0][0])
print(number_grid[2][1])

for row in number_grid: 
    #for row in row:
        print (row)

for row in number_grid: 
    for col in row:
        print (col)


