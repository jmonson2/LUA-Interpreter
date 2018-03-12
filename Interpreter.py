#Interpreter starts the parser. The parser reads through the program and passes the current string to the
#necessary class. The classes will handle the processing until a new block is found. Once a new block is found, it
#returns back to the parser, and the parser will again determine the necessary class.

#The Lexical Analyzer is used for lexemes only.

#Execution is handled through the same classes, but through different methods. In execution, memory can be accessed
#and stored.




import Parser

class Interpreter:
    p = Parser.Parser()
    p.Parse()
