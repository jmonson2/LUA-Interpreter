import sys
class RelativeOp:
    op = ['<=','<','>=','>','==','~=']

    def Contains(self,text,index):
        i = 0
        for operators in RelativeOp.op:
            if(ArithmeticOp.op[i]==text[index]):
                return True
            i+=1

        return False

    def Operate(self,text,index):
        oper = text[index]
        num1 = int(text[index+1])
        num2 = int(text[index+2])

        if (oper == '<='):
            if (num1 <= num2):
                return True
            else:
                return False

        if (oper == '<'):
            if (num1 < num2):
                return True
            else:
                return False

        if (oper == '>='):
            if (num1 >= num2):
                return True
            else:
                return False

        if (oper == '>'):
            if (num1 > num2):
                return True
            else:
                return False

        if (oper == '=='):
            if (num1 == num2):
                return True
            else:
                return False

        if (oper == '~='):
            if (num1 != num2):
                return True
            else:
                return False
        else:
            sys.exit("Invalid Relative Operator, program terminated.")


