if __name__ == '__main__':
    N = int(input())
ans_List=[]
for i in range(N):
    lst=input().split()
    if lst[0]=='insert':
        ans_List.insert(int(lst[1]),int(lst[2]))
    elif lst[0]=='print':
        print(ans_List)
    elif lst[0]=='remove':
        ans_List.remove(int(lst[1]))
    elif lst[0]=='append':
        ans_List.append(int(lst[1]))
    elif lst[0]=='sort':
        ans_List.sort()
    elif lst[0]=='pop':
        ans_List.pop()
    elif lst[0]=='reverse':
        ans_List.reverse()
