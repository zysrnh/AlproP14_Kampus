xT=[[-2,2.5,0.5],
    [-1,0.5,1.5]];
zX=[[0,0,0],
    [0,0,0]];
for i in range(2):
    for j in range(3):
        print(xT[i][j], end=" ");
    print("");
temp=xT[2-1][3-1];
xT[2-1][3-1]=xT[1-1][2-1];
xT[1-1][2-1]=temp;
for i in range(2):
    for j in range(3):
        zX[i][j]=xT[i][j];
print(" ");
for i in range(2):
    for j in range(3):
        print(zX[i][j], end=" ");
    print("");
        