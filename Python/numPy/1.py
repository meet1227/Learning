import numpy as np
# 1d array
one_d=np.array([1,2,3,4])
#2d array
two_d=np.array([[1,2,3,4],[4,3,2,1]])
#3d array
three_d=np.array([
                    [[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8]],
                    [[5,6,7,8,9,10,11,12],[12,11,10,9,8,7,6,5],[1,2,3,4,5,6,7,8]]
                ])
# print(one_d)
# print(two_d)
# print(three_d)


#access the array element
# print(one_d[2])
# print(two_d[1,2])
# print(three_d[1,2,7])



#Array slicing
# print(one_d[1:3])
# print(two_d[:2,3])
# print(three_d[1,1:3,2:5])



#numpy datatypes
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
# print(one_d.dtype)
temp_Array=np.array(['m','e','d'],dtype='S4')
# print(temp_Array)
# changing datatype
copy=three_d.astype('S')
# print(copy)



# shape
print(three_d.shape)
# reshape

# m=three_d.reshape(8,2,3)
# m[7,1,2]=1111
# print(m)
# print(three_d)


# m=three_d.reshape(6,2,-1)#unknown dimension,means do not specify the one dimension python will calculate it. 
# print(m)

# reshape return the view of original array so if any change in view it's affect the view ans -><-

# flattening arrays

# d=two_d.reshape(-1)
# print(d)


# iteration in numpy array

for x in np.nditer(three_d):
    print(x)