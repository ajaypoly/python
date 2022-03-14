


def postfix(s):
    stack = []
    for i in s :
        if i.isdigit():
            stack.append(int(i))

        elif s.isalpha(): 
            return None  

        elif i== "+":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1+num2)

        elif i == "-":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1-num2)

        elif i == "/":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1/num2)
                                                             
        elif i == "*":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1*num2)

    return stack.pop()


