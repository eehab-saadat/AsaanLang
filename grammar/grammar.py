# BNF SYNTAX GRAMMAR

# <variable_name> ::= <identifier>
# <identifier> ::= <letter> | <identifier> <letter> | <identifier> <digit>

# <program> ::= <block_statement>
# <block_statement> ::= <statement> | <statement> <block_statement>
# <statement> ::= <assignment_statement> | <print_statement> | <if_statement> | <while_statement>
# <assignment_statement> ::= <variable_name> = <expression> | <variable_name> = <string_expression> | <variable_name> = <condition_expression>
# <input_statement> ::= <type> <variable_name> = btao() | <variable_name> = btao()
# <print_statement> ::= likho <string_expression> | likho <variable_name>
# <if_statement> ::= agar (<condition_expression>) { <block_statement> } | agar (<condition_expression>) { <block_statement> } <elif_statement><else_statement> | agar (<condition_expression>) { <block_statement> } <else_statement>
# <elif_statement> ::= warnaagar (<condition_expression>) { <block_statement> }
# <else_statement> ::= warna { <block_statement> }
# <while_statement> ::= jabtak (<condition_expression>) { <block_statement> }
# <comment> ::= #<string_constant>

# <relational_operator> ::= keBrabar | keBrabarNahi | seChota | seBara | jitnaYaChota | jitnaYaBara 
# <logical_operator> ::= aur | ya | nahi

# <expression> ::= <term> | <term> + <expression> | <term> - <expression>
# <condition_expression> ::= <expression> <relational_operator> <expression> | <condition_expression> <logical_operator> <condition_expression> | <boolean_constant>
# <string_expression> ::= "<string_constant>" | "<string_expression> <string_constant>"
# <string_constant> ::= <letter> | <string_constant> <letter> | <digit> | <string_constant> <digit> | <special_character> | <string_constant> <special_character>

# <type> ::= number | lafz | ishariya | boolean
# <term> ::= <factor> | <factor> * <term> | <factor> / <term>
# <factor> ::= <variable_name> | <constant> | (<expression>)
# <constant> ::= <integer_constant> | <float_constant>
# <integer_constant> ::= <digit> | <integer_constant> <digit>
# <float_constant> ::= <integer_constant> . <integer_constant>

# <boolean_constant> ::= sahi | galat
# <keyword> ::= agar | warnaagar | warna | jabtak | likho | aur | ya | nahi
# <letter> ::= a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
# <special_character> ::= ! | @ | # | $ | % | ^ | & | * | ( | ) | _ | + | - | = | { | } | [ | ] | | | \ | : | ; | " | ' | < | > | , | . | ? | / | ~
# <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

# DEFINED CLASS NAMES
# KEYWORD, CONDITIONAL_EXP, ASSIGNMENT_STATEMENT, PRINT_STATEMENT, IF_STATEMENT, ELIF_STATEMENT, ELSE_STATEMENT, WHILE_STATEMENT

'''
Source Code:
number a hai 10
number b hai btao?
boolean c hai sahi
jabtak (a > 0 aur b < 10) {
    # Ek Tabsarah
    likho "Salam Duniya!"
    agar (a == 5) {
        likho "a is 5"
    } 
    warna agar (a == 6) {
        likho "a is 6"
    } 
    warna {
        likho "a is not 5 or 6"
    }
    a hai a - 1
}

Lexicalized AST:
[["number", "a", "hai", "10"], ["number", "b", "hai", "btao?"], ["boolean", "c", "hai", "sahi"],["jabtak", ["a", ">", "0", "aur", "b", "<", "10"]], [["# Ek Tabsarah"], ["likho", "Salam Duniya!"], ["agar", ["a", "==", "5"]], [["likho", "a is 5"]], ["warnaagar", ["a", "==", "6"]], [["likho", "a is 6"]], ["warna"], [["likho", "a is not 5 or 6"]], ["a", "hai", "a", "-", "1"]]]

Tokenized AST:
[["number", "a", KEYWORD, "10"], ["number", "b", KEYWORD, KEYWORD], ["boolean", "c", KEYWORD, BOOL_KW],[KEYWORD, CONDITIONAL_EXP], [COMMENT, [KEYWORD, "Salam Duniya!"], [KEYWORD, CONDITIONAL_EXP], [[KEYWORD, "a is 5"]], [KEYWORD, CONDITIONAL_EXP], [[KEYWORD, "a is 6"]], [KEYWORD], [[KEYWORD, "a is not 5 or 6"]], ["a", OPERATOR, "a", OPERATOR, "1"]]]

Parsed AST:
[ASSIGNMENT_STATEMENT, INPUT_STATEMENT, ASSIGNMENT_STATEMENT, WHILE_STATEMENT, [COMMENT, PRINT_STATEMENT, IF_STATEMENT, [PRINT_STATEMENT], ELIF_STATEMENT, [PRINT_STATEMENT], ELSE_STATEMENT, [PRINT_STATEMENT], ASSIGNMENT_STATEMENT]]

Target Code:
a = 10
b = 0
c = true
while a > 0 and b < 10:
    print("Salam Duniya!")
    if a == 5:
        print("a is 5")
    elif a == 6:
        print("a is 6")
    else:
        print("a is not 5 or 6")
    a = a - 1
'''