grammar Fuzzy;

/*
 * Parser Rules
 */

compileUnit
	:	fuzzy_rule+ EOF                     # File
	;

fuzzy_rule
    :   expr '=>' ID 'is' ID                # FuzzyRule
    ;

expr
    :   ID 'is' ID                          # VarValue
    |   '(' expr ')'                        # Parens
    |   expr 'and' expr                     # And
    |   expr 'or' expr                      # Or
    |   'not' expr                          # Not
    ;

/*
 * Lexer Rules
 */

fragment LETTER		:	[a-zA-Z]			;
fragment DIGIT		:	[0-9]				;

ID
	:	LETTER (LETTER | DIGIT | '_')*
	;

COMMENT
	:	'/*' (COMMENT | .)*? '*/' -> skip
	;

WS
	:	[ \t\n\r]+ -> skip
	;
