import LexicalAnalyzer
import Id
import sys
import Statement
class Parser:



    def Parse(self):
        id = Id.Id()
        statement = Statement.Statement()
        index=0
        file = open("test.lua")
        filetext = file.read()
        text = filetext.split() #Uses delimiter SPACE to separate the words into a list ; Stores in list split_text
        file.close()
#Begins initial checks
        if(text.pop(0)!="function"):
            sys.exit("function not found, program terminated.")

        id.Include(text,0)
        text.pop(0)

        if(text.pop(0)!='('):
            sys.exit("Left paran not found, program terminated.")

        if(text.pop(0)!=')'):
            sys.exit("Right paran not found, program terminated.")

#Ends initial checks
        while text[index]!="end":
            index = statement.determineStatement(text,index)
        return


