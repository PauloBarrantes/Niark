
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGNACION BREAK CASE COMA COMENTARIO CORCHETEDER CORCHETEIZQ DECREMENTAR DECVARIABLE DIFERENTE DIV DOUBLE ELSE FALSE FOR FUNCTION IF IGUAL IMPORT INCREMENTAR INT MAYOR MAYORIGUAL MENOR MENORIGUAL MULT NEWLINE NOMBRE OR PARDER PARIZQ PRINT PRIVATE PUBLIC PUNTOYCOMA READ RESTA RETURN STRING SUMA SWITCH TABULACION TRUE VOID WHILEexpression : PUBLIC expressionexpression : PRIVATE expression\n    domain : PRIVATE\n           | PUBLIC\n    \n    return : VOID\n           | FUNCTION\n    \n    expression : domain return NOMBRE PARIZQ parameter PARDER NEWLINE\n    \n    parameter : empty\n              | NOMBRE parametro_extra\n\n    \n    parametro_extra : COMA NOMBRE parametro_extra\n                    | empty\n    expression : TRUE expressionexpression : FALSE expression\n    expression : IF PARIZQ PARDER\n    expression : ELSE expression\n    expression :  t NOMBRE\n    \n    expression : FOR PARIZQ DECVARIABLE ASIGNACION INT PUNTOYCOMA condition PUNTOYCOMA incdec NOMBRE PARDER NEWLINE\n    \n    condition_operator : DIFERENTE\n              | IGUAL\n              | MAYOR\n              | MAYORIGUAL\n              | MENOR\n              | MENORIGUAL\n    \n    condition : variabletypes condition_operator variabletypes\n    \n    variabletypes : NOMBRE\n                  | DOUBLE\n                  | INT\n                  | STRING\n    \n    incdec : INCREMENTAR\n           | DECREMENTAR\n    expression : WHILE expressionexpression : RETURN expressionexpression : PRINT expressionexpression : READ expressionexpression : IMPORT expressionexpression : SWITCH expressionexpression : CASE expressionexpression : BREAK expressionexpression : TABULACION expressionexpression : COMA expressionexpression : INT expressionexpression : DOUBLE expressionexpression : STRING expressionexpression : PUNTOYCOMA expressionexpression : DECVARIABLE expressionexpression : IGUAL expressionexpression : MENOR expressionexpression : MAYOR expressionexpression : MAYORIGUAL expressionexpression : MENORIGUAL expressionexpression : ASIGNACION expressiont : SUMA expressionexpression : RESTA expressionexpression : INCREMENTAR expressionexpression : DECREMENTAR expressionexpression : MULT expressionexpression : DIV expressionexpression : CORCHETEIZQ expressionexpression : CORCHETEDER expressionexpression : COMENTARIO expressionexpression : NEWLINE expressionexpression : AND expressionexpression : OR expressionexpression : DIFERENTE expressionempty : '
    
_lr_action_items = {'PUBLIC':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'PRIVATE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'TRUE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'FALSE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'IF':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'ELSE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'FOR':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'WHILE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'RETURN':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'PRINT':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'READ':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'IMPORT':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'SWITCH':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'CASE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'BREAK':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'TABULACION':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'COMA':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,95,104,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,100,100,]),'INT':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,94,103,114,115,116,117,118,119,120,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,98,106,106,-18,-19,-20,-21,-22,-23,]),'DOUBLE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,103,114,115,116,117,118,119,120,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,110,110,-18,-19,-20,-21,-22,-23,]),'STRING':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,103,114,115,116,117,118,119,120,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,111,111,-18,-19,-20,-21,-22,-23,]),'PUNTOYCOMA':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,98,106,107,108,110,111,124,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,103,-27,113,-25,-26,-28,-24,]),'DECVARIABLE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,56,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,92,]),'IGUAL':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,106,108,109,110,111,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-27,-25,116,-26,-28,]),'MENOR':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,106,108,109,110,111,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-27,-25,119,-26,-28,]),'MAYOR':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,106,108,109,110,111,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-27,-25,117,-26,-28,]),'MAYORIGUAL':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,106,108,109,110,111,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-27,-25,118,-26,-28,]),'MENORIGUAL':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,106,108,109,110,111,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-27,-25,120,-26,-28,]),'ASIGNACION':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,92,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,94,]),'RESTA':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'INCREMENTAR':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,113,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,122,]),'DECREMENTAR':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,113,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,123,]),'MULT':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'DIV':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'CORCHETEIZQ':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'CORCHETEDER':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'COMENTARIO':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'NEWLINE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,102,126,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,105,127,]),'AND':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'OR':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'DIFERENTE':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,106,108,109,110,111,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-27,-25,115,-26,-28,]),'SUMA':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'$end':([1,45,46,50,51,52,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,91,105,127,],[0,-1,-2,-61,-12,-13,-15,-16,-45,-51,-41,-44,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,-43,-46,-47,-48,-49,-50,-53,-54,-55,-56,-57,-58,-59,-60,-62,-63,-64,-14,-7,-17,]),'VOID':([2,3,4,],[-4,-3,48,]),'FUNCTION':([2,3,4,],[-4,-3,49,]),'PARIZQ':([8,11,90,],[53,56,93,]),'NOMBRE':([10,45,46,47,48,49,50,51,52,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,100,103,105,114,115,116,117,118,119,120,121,122,123,127,],[55,-1,-2,90,-5,-6,-61,-12,-13,-15,-16,-45,-51,-41,-44,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-42,-43,-46,-47,-48,-49,-50,-53,-54,-55,-56,-57,-58,-59,-60,-62,-63,-64,-52,-14,95,104,108,-7,108,-18,-19,-20,-21,-22,-23,125,-29,-30,-17,]),'PARDER':([53,93,95,96,97,99,101,104,112,125,],[91,-65,-65,102,-8,-9,-11,-65,-10,126,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[1,45,46,50,51,52,54,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,]),'domain':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'t':([0,2,3,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'return':([4,],[47,]),'parameter':([93,],[96,]),'empty':([93,95,104,],[97,101,101,]),'parametro_extra':([95,104,],[99,112,]),'condition':([103,],[107,]),'variabletypes':([103,114,],[109,124,]),'condition_operator':([109,],[114,]),'incdec':([113,],[121,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> PUBLIC expression','expression',2,'p_PUBLIC','parser.py',6),
  ('expression -> PRIVATE expression','expression',2,'p_PRIVATE','parser.py',10),
  ('domain -> PRIVATE','domain',1,'p_FUNCDOMAIN','parser.py',15),
  ('domain -> PUBLIC','domain',1,'p_FUNCDOMAIN','parser.py',16),
  ('return -> VOID','return',1,'p_FUNCRETURN','parser.py',22),
  ('return -> FUNCTION','return',1,'p_FUNCRETURN','parser.py',23),
  ('expression -> domain return NOMBRE PARIZQ parameter PARDER NEWLINE','expression',7,'p_FUNCTION','parser.py',29),
  ('parameter -> empty','parameter',1,'p_PARAMETRO','parser.py',35),
  ('parameter -> NOMBRE parametro_extra','parameter',2,'p_PARAMETRO','parser.py',36),
  ('parametro_extra -> COMA NOMBRE parametro_extra','parametro_extra',3,'p_PARAMETRO_EXTRA','parser.py',43),
  ('parametro_extra -> empty','parametro_extra',1,'p_PARAMETRO_EXTRA','parser.py',44),
  ('expression -> TRUE expression','expression',2,'p_TRUE','parser.py',48),
  ('expression -> FALSE expression','expression',2,'p_FALSE','parser.py',52),
  ('expression -> IF PARIZQ PARDER','expression',3,'p_IF','parser.py',57),
  ('expression -> ELSE expression','expression',2,'p_ELSE','parser.py',62),
  ('expression -> t NOMBRE','expression',2,'p_OPERATION','parser.py',67),
  ('expression -> FOR PARIZQ DECVARIABLE ASIGNACION INT PUNTOYCOMA condition PUNTOYCOMA incdec NOMBRE PARDER NEWLINE','expression',12,'p_FOR','parser.py',72),
  ('condition_operator -> DIFERENTE','condition_operator',1,'p_CONDITION_OPERATOR','parser.py',78),
  ('condition_operator -> IGUAL','condition_operator',1,'p_CONDITION_OPERATOR','parser.py',79),
  ('condition_operator -> MAYOR','condition_operator',1,'p_CONDITION_OPERATOR','parser.py',80),
  ('condition_operator -> MAYORIGUAL','condition_operator',1,'p_CONDITION_OPERATOR','parser.py',81),
  ('condition_operator -> MENOR','condition_operator',1,'p_CONDITION_OPERATOR','parser.py',82),
  ('condition_operator -> MENORIGUAL','condition_operator',1,'p_CONDITION_OPERATOR','parser.py',83),
  ('condition -> variabletypes condition_operator variabletypes','condition',3,'p_CONDITON','parser.py',89),
  ('variabletypes -> NOMBRE','variabletypes',1,'p_VARIABLETYPES','parser.py',95),
  ('variabletypes -> DOUBLE','variabletypes',1,'p_VARIABLETYPES','parser.py',96),
  ('variabletypes -> INT','variabletypes',1,'p_VARIABLETYPES','parser.py',97),
  ('variabletypes -> STRING','variabletypes',1,'p_VARIABLETYPES','parser.py',98),
  ('incdec -> INCREMENTAR','incdec',1,'p_INCDEC','parser.py',104),
  ('incdec -> DECREMENTAR','incdec',1,'p_INCDEC','parser.py',105),
  ('expression -> WHILE expression','expression',2,'p_WHILE','parser.py',109),
  ('expression -> RETURN expression','expression',2,'p_RETURN','parser.py',113),
  ('expression -> PRINT expression','expression',2,'p_PRINT','parser.py',117),
  ('expression -> READ expression','expression',2,'p_READ','parser.py',121),
  ('expression -> IMPORT expression','expression',2,'p_IMPORT','parser.py',125),
  ('expression -> SWITCH expression','expression',2,'p_SWITCH','parser.py',129),
  ('expression -> CASE expression','expression',2,'p_CASE','parser.py',133),
  ('expression -> BREAK expression','expression',2,'p_BREAK','parser.py',137),
  ('expression -> TABULACION expression','expression',2,'p_TABULACION','parser.py',141),
  ('expression -> COMA expression','expression',2,'p_COMA','parser.py',145),
  ('expression -> INT expression','expression',2,'p_INT','parser.py',149),
  ('expression -> DOUBLE expression','expression',2,'p_DOUBLE','parser.py',153),
  ('expression -> STRING expression','expression',2,'p_STRING','parser.py',157),
  ('expression -> PUNTOYCOMA expression','expression',2,'p_PUNTOYCOMA','parser.py',161),
  ('expression -> DECVARIABLE expression','expression',2,'p_DECVARIABLE','parser.py',165),
  ('expression -> IGUAL expression','expression',2,'p_IGUAL','parser.py',169),
  ('expression -> MENOR expression','expression',2,'p_MENOR','parser.py',173),
  ('expression -> MAYOR expression','expression',2,'p_MAYOR','parser.py',177),
  ('expression -> MAYORIGUAL expression','expression',2,'p_MAYORIGUAL','parser.py',181),
  ('expression -> MENORIGUAL expression','expression',2,'p_MENORIGUAL','parser.py',185),
  ('expression -> ASIGNACION expression','expression',2,'p_ASIGNACION','parser.py',189),
  ('t -> SUMA expression','t',2,'p_SUMA','parser.py',193),
  ('expression -> RESTA expression','expression',2,'p_RESTA','parser.py',197),
  ('expression -> INCREMENTAR expression','expression',2,'p_INCREMENTAR','parser.py',201),
  ('expression -> DECREMENTAR expression','expression',2,'p_DECREMENTAR','parser.py',205),
  ('expression -> MULT expression','expression',2,'p_MULT','parser.py',209),
  ('expression -> DIV expression','expression',2,'p_DIV','parser.py',213),
  ('expression -> CORCHETEIZQ expression','expression',2,'p_CORCHETEIZQ','parser.py',217),
  ('expression -> CORCHETEDER expression','expression',2,'p_CORCHETEDER','parser.py',221),
  ('expression -> COMENTARIO expression','expression',2,'p_COMENTARIO','parser.py',225),
  ('expression -> NEWLINE expression','expression',2,'p_NEWLINE','parser.py',229),
  ('expression -> AND expression','expression',2,'p_AND','parser.py',233),
  ('expression -> OR expression','expression',2,'p_OR','parser.py',237),
  ('expression -> DIFERENTE expression','expression',2,'p_DIFERENTE','parser.py',241),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',245),
]