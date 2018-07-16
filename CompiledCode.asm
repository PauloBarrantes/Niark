.data 
hola: .word 0:50
.text 
main: 
li $v1, 3
la $a1, hola
mul $a2, $v1, 4
add $a2, $a2, $a1
sw $a2, 0
li $v0, 10 
syscall 
