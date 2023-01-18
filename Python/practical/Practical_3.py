import numpy as np
np_arr=np.random.choice([2,4,6,7,9,30],size=[3,4,3])
print(np_arr)
np_arr_reshaped=np_arr.reshape(6,6)
print(np_arr_reshaped)
print(np_arr[1:,3,1:])