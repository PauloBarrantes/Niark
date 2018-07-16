.data 
l: .word 0:50
.text 
main: 
li $v1, 5
li $a1, 1
slt $a2, $a1, $v1
beq $a2, $0, Continuation1
li $v0, 1
li $a0,1
syscall
Continuation1:
li $a3, 8
li $t0,8
bne $a3,$t0,Continuation3
li $v0, 1
li $a0,2
syscall
Continuation3:
li $t1, 2
div $a3, $t1
mflo $t9
slt $t2, $v1, $t9
beq $t2, $0, Continuation5
li $v0, 1
li $a0,3
syscall
Continuation5:
la $t3, l
li $t5, 0
mul $t4, $t1, 4
add $t4, $t4, $t3
sw $t5, ($t4)
mul $t6, $t1, 4
add $t6, $t6, $t3
lw $t7, ($t6)
bgtz $t7, Continuation8
li $v0, 1
li $a0,4
syscall
Continuation8:
li $v0, 10
syscall
