op_stack = []  # To take hold of all the operations done
S = []
for _ in range(int(input())):
    op = input().split()

    if op[0] == '1':
        S.extend(list(op[1]))
        op_stack.append((1, len(op[1])))

    elif op[0] == '2':
        temp = S[len(S) - int(op[1]):]
        S = S[:len(S) - int(op[1])]
        op_stack.append((2, temp))

    elif op[0] == '3':
        # print(S,op[1])
        print(S[int(op[1]) - 1])

    else:
        last_op = op_stack.pop()
        if last_op[0] == 1:
            S = S[:len(S) - last_op[1]]
        else:
            S = S + last_op[1]
        # print(S)