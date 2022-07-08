n=int(input("Enter Kahyyam/Pascal triangle lenght: "))
KP=[[1 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(1,i):
        KP[i][j]=KP[i-1][j-1]+KP[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(KP[i][j], end=" ")
    print()
    

