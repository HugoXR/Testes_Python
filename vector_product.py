a = [1,2, 3]
b = [3,2, 1]
C = []

for k in range(len(a)):
    for i in range(len(a)):
        for j in range(len(b)):
            if(i != k and j != k and i != j):
                if k == (len(a) - (len(a) - 1)):
                    C.append(a[i]*b[j] - a[j]*b[i]) 
                else:
                    C.append(a[j]*b[i] - a[i]*b[j]) 

D = [C[i] for i in range(len(C)) if i % 2 != 0]  

print(D)
