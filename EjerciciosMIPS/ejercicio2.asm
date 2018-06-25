
    .data
        gg: .ascii "hola mundo"

    .text
.globl main
main:
        li $v0, 4
        la $a0, gg

        syscall


        ### Exit System Call ###
        li $v0,10
        syscall
