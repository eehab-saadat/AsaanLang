# imports
from modules.models.errors import ERROR

# For Lexical Code Analysis
class Lexer:
    source_code = "" # source code
    index = 0 # index of the current character
    char = "" # current character
    
    bracket_stack = [] # for checking brackets
    operators = ["+", "-", "*", "/", "%"] # for checking operators

    def __init__(self, source_code: str): # constructor
        self.source_code = source_code # set source code
        self.char = source_code[self.index] # set current character
    
    def lexicalize(self) -> list: # lexicalizes the code, returns the list of statements & code blocks
        expr_list = [] # list of statements & code blocks
        statement = [] # list of tokens

        while (self.index < len(self.source_code)): # while not EOF
            if (self.char.isalpha()): # for fetching keywords
                statement.append(self.getWord()) # append the keyword to the statement
            elif (self.char.isdigit()): # for fetching numbers
                 statement.append(self.getNumber()) # append the number to the statement
            elif (self.char in self.operators): # for fetching operators
                statement.append(self.char) # append the operator to the statement
                self.move() # move to the next character
            elif (self.char == '"'): # for fetching strings
                statement.append(self.getString()) # append the string to the statement
            elif (self.char == "#"): # for fetching comments
                statement.append(self.getComment()) # append the comment to the statement
            elif (self.char == "\n"): # for adding statements
                if len(statement) > 0: # if the statement is not empty
                    expr_list.append(statement) # append the statement to the list of statements
                statement = [] # reset the statement
                self.move() # move to the next character
            elif (self.char == " "): # for skipping spaces
                self.move() # move to the next character
            elif (self.char == "(" or self.char == "{"): # for fetching code blocks
                self.bracket_stack.append(self.char) # append the bracket to the stack
                if self.char == "(": # start of conditional, round opening bracket
                    self.move() # move to the next character
                    item = self.lexicalize() # get the conditional recursively
                    statement.append(item) # append the conditional to the statement
                    expr_list.append(statement) # append the statement to the list of statements
                    statement = [] # reset the statement
                if self.char == "{": # start of code block, curly opening bracket
                    self.move() # move to the next character
                    if len(statement) > 0: # if the statement is not empty
                        expr_list.append(statement) # append the statement to the list of statements
                        statement = [] # reset the statement
                    item = self.lexicalize() # get the code block recursively
                    expr_list.append(item) # append the code block to the list of statements
                self.move() # move to the next character
            elif (self.char == ")" or self.char == "}"): # for closing conditionals or code blocks
                if len(self.bracket_stack) == 0: # if the stack is empty
                    raise ERROR("error", "bracket ka ghalat istemaal") # raise syntax error for unbalanced brackets
                else:
                    if (self.char == ")"): # end of conditional, round closing bracket
                        self.bracket_stack.pop() # pop the opening bracket from the stack
                        return statement # return the statement
                    elif (self.char == "}"): # end of code block, curly closing bracket
                        if len(statement) > 0: # if the statement is not empty
                            expr_list.append(statement) # append the statement to the list of statements
                        self.bracket_stack.pop() # pop the opening bracket from the stack
                        return expr_list # return the list of statements
                    else: # if the bracket is not a closing bracket
                        raise ERROR("error", "bracket band krna bhool gaye") # raise error
            else:
                raise ERROR("error", "syntax ki ghalti") # raise syntax error
                
        if (len(statement) > 0): # if the statement is not empty
            expr_list.append(statement) # append the statement to the list of statements

        return expr_list # return the list of statements
    
    def move(self) -> None: # moves to the next character
        self.index += 1 # increment the index
        if self.index < len(self.source_code): # if not EOF
            self.char = self.source_code[self.index] # set the current character

    def getWord(self) -> str: # fetches a keyword
        word = "" # the keyword
        while ((self.index < len(self.source_code)) and (self.char.isalnum() or self.char == "_" or self.char == "?")): # while not EOF and the character is alphanumeric or underscore or question mark
            word += self.char # append the character to the keyword
            self.move() # move to the next character
        return word # return the keyword
    
    def getNumber(self) -> str: # fetches a number or a float
        number = "" # the number 
        while (self.char.isdigit() or self.char == ".") and self.index < len(self.source_code): # while not EOF and the character is a digit or a dot
            number += self.char # append the character to the number
            self.move() # move to the next character
        if self.char != " ": # if the character is not a space
            pass
            #raise ERROR("error", "number ki jagha harf ka istemaal") # raise syntax error 
        return number # return the number
    
    def getString(self) -> str: # fetches a string
        string = "" # the string
        quotesClosed = False # whether the quotes are closed or not
        while self.index < len(self.source_code) and not quotesClosed: # while not EOF and the quotes are not closed
            self.move() # move to the next character
            if self.char == '"': # if the character is a quote
                quotesClosed = True # set quotesClosed to True
                self.move() # move to the next character
            else: # if the character is not a quote
                string += self.char # append the character to the string
        if not quotesClosed: # if the quotes are not closed
            raise ERROR("error", "vaveyn ya \"\" ka istemaal nahi kiya") # raise syntax error
        return string # return the string
    
    def getComment(self) -> str: # fetches a comment
        comment = "" # the comment
        while self.index < len(self.source_code) and self.char != "\n": # while not EOF and the character is not a newline
            comment += self.char # append the character to the comment
            self.move() # move to the next character
        return comment # return the comment