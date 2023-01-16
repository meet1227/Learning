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

# copy=three_d.astype('S')
# print(copy,'hello')
# print(three_d)


# shape

# print(three_d.shape)




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

# for x in np.nditer(three_d):
#     print(x)



# # Iterating Array With Different Data Types

# for x in np.nditer(three_d,flags=['buffered'], op_dtypes=['S']):
#     print(x)




# # iterating with different step size
# for x in np.nditer(three_d[::,::,::2]):
#     print(x)


# # Enumerated Iteration Using ndenumerate()
# for id,x in np.ndenumerate(three_d):
#     print(id,x)


# #########



#     # Joining NumPy Arrays


# three_dm=np.array([
#                     [[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8]],
#                     [[5,6,7,8,9,10,11,12],[12,11,10,9,8,7,6,5],[1,2,3,4,5,6,7,8]]
#                 ])

# three_dp=np.array([
#                     [[35,6,4,67,45,7,4,65],[5,6,3,7,4,3,2,1],[5,6,8,3,5,6,7,8]],
#                     [[9,3,7,8,9,10,11,12],[12,11,10,9,8,7,6,5],[1,2,3,4,5,6,7,8]]
#                 ])



# print('first',three_dm)
# print('second',three_dp)
# print('both')

# # # concetinate function

# # # dm=np.concatenate((three_dm,three_dp),axis=0)
# # # dm=np.concatenate((three_dm,three_dp),axis=1)
# # # dm=np.concatenate((three_dm,three_dp),axis=2)
# # print(dm)

# # # stack function

# # dm=np.stack((three_dm,three_dp), axis=0)
# # dm=np.stack((three_dm,three_dp), axis=1)
# # dm=np.stack((three_dm,three_dp), axis=2)
# # print(dm)

# # # hstack
# # # vstack
# # # dstack functions..

# # dm=np.hstack((three_dm,three_dp))
# # print('hstack',dm)
# # dm=np.vstack((three_dm,three_dp))
# # print('vstack',dm)
# # dm=np.dstack((three_dm,three_dp))
# # print('dstack',dm)




# ###################

##############

# Splitting NumPy Arrays

three_dm=np.array([
                     [[1,2,3,4,5,6,7,8],[8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8]],
                     [[5,6,7,8,9,10,11,12],[12,11,10,9,8,7,6,5],[1,2,3,4,5,6,7,8]]
                 ])
print(three_dm)
dm = np.array_split(three_dm, 4)
print('splited',dm)


