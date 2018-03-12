import sys
import Id
class LexicalAnalyzer:



    def AnalyzeStart(self,text):
        id = Id.Id()



    def Analyze(self,text,index): #This method is to determine which object to use first. Once an object is created,
                                  #the text and index is pushed to the object in which the object carries out execution.
                                  #Once the object is finished with its execution, it returns to this Analyze method to
                                  #determine what needs to be executed next.
       self.index=index
       while (index<len(text)):
           #print(text[index])
           
           #Insert Logic Here Above
           index+=1












