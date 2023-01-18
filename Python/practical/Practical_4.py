import numpy as np
li=[]
print('Enter the elements:')
for i in range(10):
    x=int(input())
    li.append(x)
np_arr=np.array(li)
print('Your numpy Array is:',np_arr)
print('Reverse numpy Array:',np_arr[::-1])
print('Sum of Array element:',np.sum(np_arr))