"""
Not Complete
"""


input = [[1,2,3],[4,5,6],[7,8,9]]
r = int(len(input))
c = r
output = [[0]*c]*r
op = []
for i in range(c):
    for j in range(r):
        output[0][0] = input[r-1-j][i]

print("---------------------------")

for i in range(r):
    for j in range(c):
        print(output[i][j])

