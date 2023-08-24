import pandas as pd
import numpy as np

arr1 = np.array([[int(x) for x in input().split()] for i in range(3)])
print(arr1)
print()

arr2 = np.array([[int(x) for x in input().split()] for i in range(4)])
print(arr2)
print()

arr3=np.zeros((len(arr1)*len(arr2[0])),int)
arr3=arr3.reshape((len(arr1),len(arr2[0])))

for i in range(len(arr1)):
    for j in range(len(arr2[0])):
        for k in range(len(arr2)):
            arr3[i][j]+=arr1[i][k]*arr2[k][j]


print(arr3)