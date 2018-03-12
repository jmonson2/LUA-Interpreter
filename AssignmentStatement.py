import sys
import ArithmeticExpression
import ArithmeticOp
class AssignmentStatement:

    def determine(self,text,index):
        if (text[index]!="="):
            sys.exit("Assignment operator not found, terminated program.")



        index+=1 #This allows us to push the correct value to determine if the grammar after '=' is correct.

        a_expr = ArithmeticExpression.ArithmeticExpression()
        a_op = ArithmeticOp.ArithmeticOp()
        if (a_op.Contains(text,index)):
            a_expr.determine(text,index)
            return index + 3
        #else:
        index = a_expr.determine(text,index)
        return index

