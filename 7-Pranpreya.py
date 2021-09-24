# Assignment 6: Use stacks to check integrity of parenthesis
# Pranpreya Samasutthi (st122602)


def stack(mytest):
    #  list of opening and closing brackets
    open_b = ['(', '{', '[']
    close_b = [')', '}', ']']
    mystack = []

    for i in mytest:
        #  When you encounter a opening parenthesis, push it to the stack
        if i in open_b:
            mystack.append(i)
        #  When you encounter a closing parenthesis,
        #  and if it matches to the top of the stack, pop the stack,
        #  else, return "not ok"
        elif i in close_b:
            # mystack[3] -> ] -> index of close = 2
            # so index of open = 2 -> [
            # mystack[3-1] -> [
            # open_b[index] == mystack[len(mystack) - 1] -> [ == [ -> pop
            index = close_b.index(i)
            if (len(mystack) > 0) and (open_b[index] == mystack[len(mystack) - 1]):
                mystack.pop()
            else:
                return "Not okay"
    # if the stack is not empty, return "not ok"
    # otherwise, "ok"
    if mystack:
        return "Not okay"
    return "OK"


print('{[[]]{()}} ', stack('{[[]]{()}}'))
print('[{} ', stack('[{}'))





