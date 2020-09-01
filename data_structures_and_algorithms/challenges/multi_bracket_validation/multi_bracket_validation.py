def multi_bracket_validation(input):
    '''
    This function takes a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced.
    '''
    open_brackets = ['[', '{', '(']
    close_brackets = [']', '}', ')']
    brackets = []
    for i in input:
        if i in open_brackets:
            brackets.append(i)
        elif i in close_brackets:
            closed = close_brackets.index(i)
            if len(brackets) > 0 and open_brackets[closed] == brackets[len(brackets) - 1]:
                brackets.pop()
            else:
                return False
        
    if len(brackets) == 0:
        return True
    else:
        return False