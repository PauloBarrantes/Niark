.data 
.text 
main: 
li $v1, 5
li $a1, 1
slt $a2, $a1, $v1
beq $a2, $0, 1Continuation
li $v0, 1 
li $a0,5
syscall 
1Continuation:
li $a3, 10
li $t0,6
bne $a3,$t0,3Continuation
li $v0, 1 
li $a0,6
syscall 
3Continuation:
li $t1, 2
div $a3, $t1
mflo $t9
slt $t2, $v1, $t9
beq $t2, $0, 5Continuation
li $v0, 1 
li $a0,7
syscall 
5Continuation:
li $v0, 10 
syscall 
