.data
	var1:		.word 1
	str: 		.asciiz "\nhola mundo"
  str2:   .asciiz "\nResultado de la suma ="
  mensajeInput1:   .asciiz "\nIngrese un numero entero: "
	mensajeInput2:   .asciiz "\nIngrese un numero positivo: "
	mensajeOutput:   .asciiz "Vamos a contar!\n"
	tryAgain:   .asciiz "\nEse numero no es positivo."
  mayIgCero:   .asciiz "\nNumero mayor o igual a cero"
  menorACero:   .asciiz "\nNumero menor a cero"
	separador: .asciiz ", "

.text
.globl main
  main:

			## Imprimimos un 1 ##

	li $v0, 1
	li $a0, 1
	syscall

			## Imprimimos "hola mundo" ##

	li $v0, 4
	la $a0, str
	syscall

			## Calculamos la suma 1+2 ##

  li $t1, 1
  li $t2, 2
  add $t0 $t1 $t2

			## Imprimimos "Resultado de la suma = " ##

  la $a0, str2
	syscall

			## Imprimimos el resultado de la suma (3) ##

  li $v0, 1
  move $a0, $t0
  syscall

			## Imprimimos mensaje de input ##

  li $v0, 4
  la $a0, mensajeInput1
  syscall

			## Pedimos entero al usuario y guardamos en $t0 ##

  li $v0, 5
  syscall
  move $t0, $v0

			## Comparamos valor ingresado, imprimimos mensaje según corresponda ##

  bge	$t0,$zero,mayorIgACero
  li $v0, 4
  la $a0, menorACero
  syscall
  j ejercicio5

mayorIgACero:
  li $v0, 4
  la $a0, mayIgCero
  syscall

ejercicio5:

			## Imprimimos mensaje de input ##

  li $v0, 4
  la $a0, mensajeInput2
  syscall

			## Pedimos entero al usuario y guardamos en $t0 ##

	li $v0, 5
	syscall
	move $t0, $v0

			## Revisamos que sea mayor que 1, si no lo es, pedimos numero nuevamente ##

	li $t1, 1
	bge $t0,$t1, entradaValida

	li $v0, 4
	la $a0, tryAgain
	syscall

	j ejercicio5

			## Si es mayor a 1, imprimimos los numeros desde 1 hasta el valor ingresado ##

entradaValida:

	li $v0, 4
	la $a0, mensajeOutput
	syscall

	li $t1, 0

ciclo:

	addi $t1, 1
	li $v0, 1
	move $a0, $t1
	syscall

	beq $t1, $t0, ejercicio6

	li $v0, 4
	la $a0, separador
	syscall

	j ciclo

ejercicio6:
	


fin:
  li $v0, 10
  syscall
