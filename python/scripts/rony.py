# Python3 implementation of the approach
def reminder(x):
    c=0
    board=[x]
    for i in range(1,x):
        #if(x % i) == 1:
        print(x % i, i)
        if (x % i) != 1:
            board.insert(-1,i)

    print(board)
        #    c+=1
    for i in range(len(board)):
        for j in range(1,board[i]):
            new = board[i] % j
            print(board[i], ' mod ',j,' = ', new)

            # if (new)== 1 and board[i]:
            #     print(board[i])
            # if new != 1 and j not in board:
            #     board.insert(-1,j)

    return((board))
    #return c

print(reminder(7))
