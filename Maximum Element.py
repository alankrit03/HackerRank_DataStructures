if __name__=='__main__':
    stack=[0]
    for _ in range(int(input())):
        query=input().split()
        if int(query[0])==1:
            stack.append(max(int(query[1]),stack[-1]))
            #print(stack,query[1])
        elif int(query[0])==2:
            stack.pop()
        else:
            print((stack[-1]))

