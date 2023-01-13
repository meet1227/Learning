#swaping the first element with last one

import os
def exchange(li):
    x=li[0]
    li[0]=li[-1]
    li[-1]=x
    return li
if __name__=='__main__':
    Exchange_list=input().split()
    Exchange_list=exchange(Exchange_list)
    print(Exchange_list)