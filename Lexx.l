%{
#include <stdio.h>
%}

%%

[0-9]+          { printf("INTEGER: %s\n", yytext); }
[a-zA-Z]+       { printf("IDENTIFIER: %s\n", yytext); }
[ \t\n]         { /* ignore whitespace */ }
.               { printf("Invalid character: %s\n", yytext); }

%%
int yywrap(){
return 1;
}

int main() {
    yylex();
    return 0;
}
