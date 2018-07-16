.data 
.text 
main: 
li $v1, 5
li $a1, 0
Loop1:
li $v0, 1
li $a0,1
syscall
addi $a1, 1j Loop1
ExitLoop1:
li $v0, 10
syscall
