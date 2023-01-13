import csv
import os
print('please select bellow option')
print('     1. write')
print('     2. Copy')
x=int(input())
try:
    match  x:
        case 1:
            file_name=input()
            f=open(file_name,'a')
            writer = csv.writer(f)
            print('Please Enter the number of rows')
            r_Count=int(input())
            for i in range(r_Count):
                li=[]
                j=0
                print('User_id:')
                li.append(input())
                print('Name:')
                li.append(input())
                print('Date')
                li.append(input())
                writer.writerow(li)
        case 2:
            file_name=input()
            f=open(file_name,'r')
            reader= csv.reader(f)
            fc=open(''+file_name+'_copy.csv','w')
            writer=csv.writer(fc)
            writer.writerows(reader)
except FileNotFoundError:
    print('please chack filename')
except:
    print('unknown exception')
finally:
    if os.path.exists(file_name):
        f.close()
    if os.path.exists(''+file_name+'_copy.csv'):
        fc.close()