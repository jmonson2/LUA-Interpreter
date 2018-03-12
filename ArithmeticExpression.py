import Memory
import Id
import sys
import inspect
import ArithmeticOp
class ArithmeticExpression:

    def determine(self,text,index):
        mem = Memory.Memory()
        id = Id.Id()
        operators=ArithmeticOp.ArithmeticOp()
        #Determine arithmetic operation
        if("AssignmentStatement.py" in inspect.stack()[1][1]):
            
            if (operators.Contains(text,index)):
                result = operators.Operate(text,index)
                mem.Store(result)
                return index
        else:
            
            if(operators.Contains(text,index)):
                result = operators.Operate(text,index)
                return result
        #Determine id
        if (id.Include(text,index)):
            return mem.mem
        #Determine literal integer
        if (isinstance(int(text[index]),int)): #Determines if value stored at text[index] is an integer. If not, the
            if("AssignmentStatement.py" in inspect.stack()[1][1]): #Prevents storing memory for anything but assignment

                mem.Store(text[index])


            elif(inspect.stack()[1][3]=='sPrint'): #This determines if the sPrint method is calling ArithmeticExpression.determine
                return int(text[index])  #If it is, it returns what is stored in the memory so it can be printed.

            elif("ArithmeticExpression.py" in inspect.stack()[1][1]):
                return int(text[index])
            index+=1
            return(index)

