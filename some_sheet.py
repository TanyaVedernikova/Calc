term = input()



def check(term):

    symbols = ['(', ')','(-']


    good_operators = ['+', '-', '*', '/', '.', ',', '(', ')']
    good_operands = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    bad_operators = ['+*','*+','-*','*-','+:',':+','-:',':-', '/0','++', '--', '**', '::', '(+', '(*', '(-', '(:', '+)', '*)', '-)', ':)']

    for i in bad_operators:
        if i in term:
            print("No, dont use it")
        
    for i in range(len(term)):
        if term[i] not in good_operators:
            if term[i] not in good_operands:
                print("no, uoy use word")


check(term)