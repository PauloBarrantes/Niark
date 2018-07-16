.data 
.text 
main: 
li $v1, 5
li $a1, 1
slt $a2, $a1, $v1
beq $a2, $0, 1Continuation:
li $v0, 1 
li $a0,5
syscall 
1Continuation:
li $a3, 10
li $v0, 1 
li $a0,6
syscall 
3Continuation:
li $t0, 2
div $a3, $t0
mflo $t9
slt $t1, $v1, $t9
beq $t1, $0, 5Continuation:
li $v0, 1 
li $a0,7
syscall 
5Continuation:
li $v0, 10 
syscall 
