
    .data
    prompt1:     .asciiz "Digite el primer numero:  "
    prompt2:     .asciiz "Digite el segundo numero:  "
    prompt3:     .asciiz "Digite el tercer numero:  "

    string1:    .asciiz "Promedio:  "
    saltolinea: .asciiz "\n"
    .text
.globl main
main:
    ##Pedimos el primer numero
        li $v0, 4
        la $a0, prompt1
        syscall

        li $v0, 5
        syscall

        move $t0, $v0
    ##Pedimos el segundo numero
        li $v0, 4
        la $a0, prompt2
        syscall

        li $v0, 5
        syscall
        move $t1, $v0
    ##Pedimos el tercer numero
        li $v0, 4
        la $a0, prompt3
        syscall

        li $v0, 5
        syscall
        move $t2, $v0
    ## Calculamos el promedio
        add $t0, $t0, $t1
        add $t0, $t0,$t2
        li  $t4, 3
        div $t0, $t4
        mflo $t0

        li $v0, 4
        la $a0, string1
        syscall

        li $v0, 1
        move $a0, $t0
        syscall
        ### Exit System Call ###
        li $v0,10
        syscall
