.data 
.text 
main: 
li $v1, 5
li $a1, 1
slt $a2, $a1, $v1
beq $a2, $zero, Continuation1
li $v0, 1
li $a0,5
syscall 
Continuation1:
li $a3, 10
li $t0,6
bne $a3,$t0,Continuation3
li $v0, 1
li $a0,6
syscall 
Continuation3:
li $t1, 2
div $a3, $t1
mflo $t9
slt $t2, $v1, $t9
beq $t2, $zero, Continuation5
li $v0, 1
li $a0,7
syscall 
Continuation5:
li $v0, 10
syscall 
