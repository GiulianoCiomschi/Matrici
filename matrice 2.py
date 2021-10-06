matrice=[[2,6,3,1,8],
        [9,7,1,3,1],
        [8,9,14,14,4],
        [21,7,16,12,20],
        [25,20,23,32,21]]
sum_linii=[]
sum_coloane=[0,0,0,0,0]
d_principala=[]
d_secundara=[]
for i in range(len(matrice)):
    sum_linii.append(sum(matrice[i]))
    for j in range(len(matrice[0])):
        sum_coloane[i]+=matrice[j][i]
    print("Suma linii",i,"=", sum_linii[i])
    print("Suma coloanei",i,"=",sum_coloane[i])
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i==j:
            d_principala.append(matrice[i][j])
print(f"Elementele diagonalei principale sunt: {d_principala}")
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if (i+j)==(len(matrice)-1):
            d_secundara.append(matrice[i][j])
print(f"Elementele diagonalei secundare sunt: {d_secundara}")

    

