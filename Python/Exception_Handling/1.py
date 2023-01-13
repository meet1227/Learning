try:
    flag=int(input())
    if flag>0:
        k = 5//flag
    else:
        k=5//0
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print('unknown error')
else:
    print('result is',k)
finally:
    if flag>0:
        print('you entered correct option so u get answer')
    else:
        print('please try again')