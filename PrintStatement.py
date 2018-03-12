import ArithmeticExpression
import sys
class PrintStatement:

    def sPrint(self,text,index):
        a_expr = ArithmeticExpression.ArithmeticExpression()

        print(a_expr.determine(text,index))

        while(text[index] != ")"):
            index+=1
        return index+1