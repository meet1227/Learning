import csv
import os
print('please select bellow option')
print('     1. write')
print('     2. Copy')
x=int(input())
header_list=['User_Id','Name','Date']
try:
    match  x:
        case 1:
            print('Enter the file name')
            file_name=input()
            f=open(file_name,'a')
            writer = csv.writer(f)
            if os.path. getsize(file_name) == 0:
                writer.writerow(header_list)
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