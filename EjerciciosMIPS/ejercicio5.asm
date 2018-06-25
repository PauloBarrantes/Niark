
    .data
    prompt:     .asciiz "Digite un numero positivo:  "
    string1:    .asciiz "Eso no es número positivo"

    string2:    .asciiz "Vamos a contar de 1 hasta "
    saltolinea: .asciiz "\n"
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
            li $v0, 1
            move $a0, $t0
            syscall
            li $v0, 4
            la $a0, saltolinea
            syscall
            ###
            li $t1,0
            loop:
                bgt $t1, $t0, afuera
                li $v0, 1
                move $a0, $t1
                syscall
                addi $t1, 1
                li $v0, 4
                la $a0, saltolinea
                syscall
                j loop

            afuera:

            j fin
        menor:
                li $v0, 4
                la $a0, string1
                syscall
        fin:


        ### Exit System Call ###
        li $v0,10
        syscall
