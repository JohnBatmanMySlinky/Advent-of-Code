import sys

dat = [x.replace('(', '( ').replace(')', ' )').replace('\n', '').split(' ') for x in sys.stdin]

ops = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b)
}

def SHUNT(ls):
    '''
    # thanks brilliant's shunting yard algorithm page
    if number add to beginning of queue

    if its an operator
        if higher order operator in stack, pop those to queue
        then add to stack

    add left bracket add to stack
        if it's right bracket, pop operators till left bracket

    brackets don't go to queue
    '''

    queue = []
    operator = []
    for each in ls:
        if each not in ops.keys() and each != '(' and each != ')':
            queue.append(each)

        if each in ops.keys():
            if operator:
                precedence = each == "*" and operator[-1] == "+"
                while operator and operator[-1] in ops.keys() and precedence:
                    queue.append(operator.pop())
            operator.append(each)

        if each == '(':
            operator.append(each)

        if each == ')':
            while operator and operator[-1] != ")":
                popped = operator.pop()
                if popped != "(":
                    queue.append(popped)
                else:
                    break           # i missed this break and it took way too long to find

    while operator:
        queue.append(operator.pop())
    return(queue)

def RPN(shunted):
    # moderately stolen from
    # https://blog.klipse.tech/python/2016/09/22/python-reverse-polish-evaluator.html
    queue = []
    for each in shunted:
        if each in ops:
            b = queue.pop()
            a = queue.pop()
            queue.append(ops[each](a,b))
        else:
            queue.append(int(each))
    return(queue)

answer = 0
for each in dat:
    answer += RPN(SHUNT(each))[0]
print('part1: ' + str(answer))


