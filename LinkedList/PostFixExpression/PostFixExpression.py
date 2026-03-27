def postExpression(s):
    stack = []

    for ch in s:
        print("Processing:", ch)

        if ch.isdigit():
            stack.append(int(ch))
        else:
            a = stack.pop()
            b = stack.pop()

            if ch == '+':
                stack.append(b + a)
            elif ch == '-':
                stack.append(b - a)
            elif ch == '*':
                stack.append(b * a)
            elif ch == '/':
                stack.append(int(b / a))
        print("Stack:", stack)
    return stack[0]


print(postExpression("23*456+-5--"))   
