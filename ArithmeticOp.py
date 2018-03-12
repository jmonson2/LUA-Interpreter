import sys
class ArithmeticOp:
        op = ['+','-','*','/']

        def Contains(self,text,index):
            i = 0
            for operators in ArithmeticOp.op:
                    if(ArithmeticOp.op[i]==text[index]):
                        return True 
                    i+=1

            return False
        
        def Operate(self,text,index):
            oper = text[index]
            num1 = int(text[index+1])
            num2 = int(text[index+2])
         
            if (oper == '+'):
                result = num1 + num2

            elif (oper == '-'):
                result = num1 - num2

            elif (oper == '*'):
                result = num1 * num2

            elif (oper == '/'):
                result = num1/num2

            else:
               sys.exit("Arithmetic Operaator invalid, program terminated.")

            return result


            



