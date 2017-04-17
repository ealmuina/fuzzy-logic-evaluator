grammar Fuzzy;

/*
 * Parser Rules
 */

compileUnit
    : '[' 'model' ']' model EOF                             # File
    ;

model
	:   mod='Sugeno' sugeno_rule+                           # Sugeno

	|   mod='Mamdani' '[' 'defuzzy' ']'
        defuzzy=('Centroid' | 'Bisecter' | 'Mean of Max')
        mamdani_tsukamoto_rule+                             # Mamdani

	|   mod='Tsukamoto' mamdani_tsukamoto_rule+             # Tsukamoto
	;

sugeno_rule
    :   logic_expr '=>' ID '=' arithmetic_expr              # SRule
    ;

mamdani_tsukamoto_rule
    :   logic_expr '=>' ID 'is' ID                          # MTRule
    ;

logic_expr
    :   ID 'is' ID                                          # LVarValue
    |   '(' logic_expr ')'                                  # LParens
    |   logic_expr 'and' logic_expr                         # LAnd
    |   logic_expr 'or' logic_expr                          # LOr
    |   'not' logic_expr                                    # LNot
    ;

arithmetic_expr
    :   ID                                                  # AVar
    |   NUMBER                                              # ANumber
    |   '(' arithmetic_expr ')'                             # AParens
    |   arithmetic_expr op='**' arithmetic_expr             # AArithmetic
    |   arithmetic_expr op=('*' | '/') arithmetic_expr      # AArithmetic
    |   arithmetic_expr op=('+' | '-') arithmetic_expr      # AArithmetic
    |   '-' arithmetic_expr                                 # ANeg
    ;

/*
 * Lexer Rules
 */

fragment LETTER		:	[a-zA-Z]			                ;
fragment DIGIT		:	[0-9]				                ;

NUMBER
    :   DIGIT+ ('.' DIGIT+)?
    ;

ID
	:	LETTER (LETTER | DIGIT | '_')*
	;

COMMENT
	:	'/*' (COMMENT | .)*? '*/' -> skip
	;

WS
	:	[ \t\n\r]+ -> skip
	;
