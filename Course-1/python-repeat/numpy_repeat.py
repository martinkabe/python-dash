import numpy as np

mylist = [1,2,3,4]
np_array = np.array(mylist)
print(f"{np_array}, type of {type(np_array)}")

arr = np.arange(0,10)
print(arr)

print(np.zeros((5,5)))
print(np.ones((5,5)))

print(np.random.randint(0,100))

print(np.random.randint(0,100,(5,5)))

print(np.linspace(0,10,101))

np.random.seed(101)
print(np.random.randint(0,100,(5,5)))

print(np.argmax(np_array))

arr = np.array([1,2,3,4,5,6])
print(arr.reshape(2,3))

mat = np.arange(0,100).reshape(10,10)
print(mat)
print(mat[5,2])

print(mat[:,2])

print(mat[mat>50])
