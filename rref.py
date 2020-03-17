#specifications
M = int(input("matrix height: "))
N = int(input("matrix width: "))

#creating the matrix
matrix = []
print ("Enter values of matrix in rows from left to right, top to bottom.")
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input(f"({i + 1}, {j + 1}): ")))
    matrix.append(row)

#echelon forming the matrix
m = 0
n = 0
progress = 0
while 1:
    if matrix[m][n] == 0: #then we need to see if it's the bottom of the column
        if m == M: #then we need to see if it's the end of the matrix
            if n == N: #then it's done
                break
            else: #start in a new column at top of work zone
                m = progress
                n += 1
        else: #move down
            m += 1
    else: #do a step
        #divide row by leading coefficient
        for j in range(n, N):
            matrix[m][j] /= matrix[m][n]
        #bring row to top of work zone
        matrix[m], matrix[progress] = matrix[progress], matrix[m]
        m = progress
        #tally progress
        progress += 1
        if progress == M: #then it's done
            break
        for i in range(progress, M):
            k = matrix[i][n]
            for j in range(n, N):
                matrix[i][j] -= k * matrix[m][j]

#row reducing the matrix


#printing the output
print ("reduced row echelon form equivalent matrix:")
for m in range(M):
    print (matrix[m])
