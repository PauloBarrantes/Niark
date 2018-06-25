
    .data
    prompt:    .asciiz "Enter a number:  "
    string1: .asciiz "El numero es menor a 0"
    string2: .asciiz "El numero es mayor o igual a 0"
    .text
.globl main
main:
        li $v0, 4
        la $a0, prompt
        syscall

        li $v0, 5
        syscall

        move $t0, $v0
        li $t1, 0
        blt $t0, $t1, menor

        mayor:
            li $v0, 4
            la $a0, string2
            syscall
            j fin
        menor:
                li $v0, 4
                la $a0, string1
                syscall
        fin:


        ### Exit System Call ###
        li $v0,10
        syscall
