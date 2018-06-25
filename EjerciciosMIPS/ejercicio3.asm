
    .data


    .text
.globl main
main:
        li $t1, 1
        li $t2, 2
        add $t3, $t1,$t2
        li $v0, 1 ##Recordar siempre cambiar el número del system call
        move $a0, $t3

        syscall


        ### Exit System Call ###
        li $v0,10
        syscall
