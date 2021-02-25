def two_stek_parser(term):
    list_of_term = []
    stek_for_operators = []
    stek_for_operands = []
    priority = {'+':1,'-':1,'*':2,':':2 }
    for i in range(0, len(term)):
        list_of_term.append(term[i])
    try:
        for i in range(len(list_of_term)):
            if list_of_term[i].isdigit() or list_of_term[i] == '.':
                if i > 0:
                    if list_of_term[i-1].isdigit() or list_of_term[i-1] == '.':
                        p = stek_for_operands.pop()
                        stek_for_operands.append(p + list_of_term[i])
                    else:
                        stek_for_operands.append(list_of_term[i])
                else:
                    stek_for_operands.append(list_of_term[i])

                try:
                    for l in stek_for_operands:
                        c = float(l)
                except Exception:
                        print('Someting Wrong with coma, like a "1..5.6" ')
                        break

            else:

                if list_of_term[i] == '(':
                    stek_for_operators.append(list_of_term[i])


                elif len(stek_for_operators) == 0:
                    stek_for_operators.append(list_of_term[i])

                elif stek_for_operators[-1] == '(':

                    stek_for_operators.append(list_of_term[i])


                elif list_of_term[i] == ')':
                    while stek_for_operators[-1] != '(':
                        y = stek_for_operands.pop()
                        x = stek_for_operands.pop()
                        z = stek_for_operators.pop()
                        if z == '+':
                            stek_for_operands.append(float(x) + float(y))
                        elif z == '-':
                            stek_for_operands.append(float(x) - float(y))
                        elif z == '*':
                            stek_for_operands.append(float(x) * float(y))
                        elif z == ':':
                            stek_for_operands.append(float(x) / float(y))
                    stek_for_operators.pop()


                elif priority.get(list_of_term[i]) > priority.get(stek_for_operators[-1]):

                    stek_for_operators.append(list_of_term[i])

                else:
                    while len(stek_for_operators) > 0 and stek_for_operators[-1] != '(' and priority.get(list_of_term[i]) <= priority.get(stek_for_operators[-1]) :
                        y = stek_for_operands.pop()
                        x = stek_for_operands.pop()
                        z = stek_for_operators.pop()
                        if z == '+':
                            stek_for_operands.append(float(x) + float(y))
                        elif z == '-':
                            stek_for_operands.append(float(x) - float(y))
                        elif z == '*':
                            stek_for_operands.append(float(x) * float(y))
                        elif z == ':':
                            try:
                                stek_for_operands.append(float(x) / float(y))
                            except ZeroDivisionError:
                                print("pls, dont")
                                break
                    stek_for_operators.append(list_of_term[i])


        if len(stek_for_operators) == 2:
            while len(stek_for_operators) > 1:
                y = stek_for_operands.pop()
                x = stek_for_operands.pop()
                z = stek_for_operators.pop()
                if z == '+':
                    stek_for_operands.append(float(x) + float(y))
                elif z == '-':
                    stek_for_operands.append(float(x) - float(y))
                elif z == '*':
                    stek_for_operands.append(float(x) * float(y))
                elif z == ':':
                    try:
                        stek_for_operands.append(float(x) / float(y))
                    except ZeroDivisionError:
                        print("pls, dont")


        elif len(stek_for_operators) == 1:
            y = stek_for_operands.pop()
            x = stek_for_operands.pop()
            z = stek_for_operators.pop()
            if z == '+':
                stek_for_operands.append(float(x) + float(y))
            elif z == '-':
                stek_for_operands.append(float(x) - float(y))
            elif z == '*':
                stek_for_operands.append(float(x) * float(y))
            elif z == ':':
                try:
                    stek_for_operands.append(float(x) / float(y))
                except ZeroDivisionError:
                    print("pls, dont")

        return stek_for_operands[0]
    except Exception:
        return print("Someting wrong")







#term = input()
#print(two_stek_parser(term))


