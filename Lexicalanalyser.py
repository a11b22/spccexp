#lexical analysis

import re

TOKENS = [
    ('IDENTIFIER', r'[a-zA-Z_]\w*'), 
    ('CONSTANT', r'\d+(\.\d+)?'),     
    ('LITERAL', r'\".*?\"'),          
    ('OPERATOR', r'\+|\-|\*|\/|=|==|!=|<|>|<=|>=|&&|\|\|'), 
    ('PUNCTUATOR', r'\(|\)|\{|\}|\[|\]|,|;'),            
    ('WHITESPACE', r'\s+'),          
    ('NEWLINE', r'\n'),                
]

def lexer(input_string):
    tokens = []
    position = 0
    
    while position < len(input_string):
        match = None
        for token_type, regex_pattern in TOKENS:
            regex = re.compile(regex_pattern)
            match = regex.match(input_string, position)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE' and token_type != 'NEWLINE':
                    tokens.append((token_type, value))
                position = match.end()  
                print(f"Matched: {token_type} - '{value}'")
                break
        
        if not match:
            raise ValueError(f'Invalid character at position {position}')
    
    return tokens

# User input for the code
input_string = input("Enter the code: ")
tokens = lexer(input_string)
for token in tokens:
    print(token)


'''
Expected output:
Enter the code: a=b+c
'''
