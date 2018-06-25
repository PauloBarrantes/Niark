.data
	var1:		.word 1
	str: 		.asciiz "\nhola mundo"
  str2:   .asciiz "\nResultado de la suma = "
  mensajeInput:   .asciiz "\nIngrese un numero entero: "
  mayIgCero:   .asciiz "\nNumero mayor o igual a cero"
  menorACero:   .asciiz "\nNumero menor a cero"

.text
.globl main
  main:

#Imprimimos un 1
	li $v0, 1
	li $a0, 1
	syscall

#Imprimimos "hola mundo"
	li $v0, 4
	la $a0, str
	syscall

#Calculamos la suma 1+2
  li $t1, 1
  li $t2, 2
  add $t0 $t1 $t2

#Imprimimos "Resultado de la suma = "
  la $a0, str2
	syscall

#Imprimimos el resultado de la suma (3)
  li $v0, 1
  move $a0, $t0
  syscall

#Imprimimos mensaje de input
  li $v0, 4
  la $a0, mensajeInput
  syscall

#Pedimos entero al usuario y guardamos en $t0
  li $v0, 5
  syscall
  move $t0, $v0

#Comparamos valor ingresado, imprimimos mensaje según corresponda
  bge	$t0,$zero,mayorIgACero
  li $v0, 4
  la $a0, menorACero
  syscall
  j fin

mayorIgACero:
  li $v0, 4
  la $a0, mayIgCero
  syscall


fin:
  li $v0, 10
  syscall
