import Id
import AssignmentStatement
import PrintStatement
import sys
import IfStatement
class Statement:

    def determineStatement(self,text,index):
        if_state = IfStatement.IfStatement()
        id = Id.Id()
        print_statement = PrintStatement.PrintStatement()
        #Determines if statement
        #if (text[index]=='if'):
           #index = if_state.determine(text,index):
        #Determines assignment statement
        if(id.Include(text,index)):
            index+=1 #Allows the determine statement to determine if there is a '=' present
            assign = AssignmentStatement.AssignmentStatement()
            index = assign.determine(text,index)
            return index

        #Determines while statement
        #Determines print statement
        if (text[index] == "print"):
            index+=1
            if text[index]== "(":
                index+=1
                index = print_statement.sPrint(text,index)
                return index
            else:
                sys.exit("Left paran not found.")


        #Determines repeat statement
