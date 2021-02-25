def two_stek_parser(term):
    list_of_term = []
    stek_for_operators = []
    stek_for_operands = []
    priority = {'+':1,'-':1,'*':2,'/':2}
    for i in range(0, len(term)):
        list_of_term.append(term[i])

    for i in list_of_term:
        if i.isdigit():
            print(list_of_term)
            print(list_of_term.index(i), 'gg')
            if list_of_term.index(i) > 0:
                if list_of_term[list_of_term.index(i)-1].isdigit():
                    print('ff',list_of_term[list_of_term.index(i)-1])
                    p = stek_for_operands.pop()
                    stek_for_operands.append(p + i)
                else:
                    stek_for_operands.append(i)

            else:
                stek_for_operands.append(i)
            print(stek_for_operands)
        else:
            if len(stek_for_operators) == 0:
                stek_for_operators.append(i)

            else:
                if priority.get(i) > priority.get(stek_for_operators[-1]):
                    stek_for_operators.append(i)
                    print(stek_for_operators)
                else:
                    #if len(stek_for_operators) == 1:
                        #x = stek_for_operands.pop()
                        #print(x)
                        #y = stek_for_operands.pop()
                        #print(y)
                        #z = stek_for_operators.pop()
                        #if z == '-':
                            #stek_for_operands.append(float(y) - float(x))
                        #elif z == '+':
                            #stek_for_operands.append(float(y) + float(x))
                        #elif z == '*':
                            #stek_for_operands.append(float(y) * float(x))
                        #elif z == '/':
                            #stek_for_operands.append(float(y) / float(x))
                    #else:
                    while priority.get(i) <= priority.get(stek_for_operators[-1]):
                        print(stek_for_operators,6)
                        if len(stek_for_operators) == 1:
                            break
                        x = stek_for_operands.pop()
                        print(x)
                        y = stek_for_operands.pop()
                        print(y)
                        z = stek_for_operators.pop()
                        if z == '-':
                            stek_for_operands.append(float(y) - float(x))
                        elif z == '+':
                            stek_for_operands.append(float(y) + float(x))
                        elif z == '*':
                            stek_for_operands.append(float(y) * float(x))
                        elif z == '/':
                            stek_for_operands.append(float(y) / float(x))
                    stek_for_operators.append(i)

    return print(float(stek_for_operands[0]),' ', str(stek_for_operators[0]),' ', float(stek_for_operands[1]))






term = input()
print(two_stek_parser(term))



