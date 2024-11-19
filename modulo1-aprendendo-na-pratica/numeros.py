# Inteiro
numero_inteiro = 4;
print("Inteiro", numero_inteiro);

# Real com ponto flutuante
numero_real = 3.14;
print("Real com ponto flutuante");

# type()
print("Tipo da variavel inteiro: ", type(numero_inteiro));
print("Tipo da variavel real: ", type(numero_inteiro));

# ======== Operadores aritméticos ========
num1 = 5;
num2 = 2;

# Soma
soma = num1 + num2;
print("A soma de ", num1, "+", num2, " = ", soma);
print("Resultado da soma em float: ", float(soma));

# Subtração
subtracao = num1 - num2;
print("A subtracao de ", num1, "-", num2, " = ", subtracao);

# Multiplicação
multiplicacao = num1 * num2;
print("A multiplicacao de ", num1, "*", num2, " = ", multiplicacao);

#Divisão
divisao = num1 / num2;
print("A divisao de ", num1, "/", num2, " = ", divisao);
print("Tipo da variavel do resultado da divisao: ", type(divisao));
print("Resultado da divisao em inteiro: ", int(divisao));

#Divisão resultando em inteiro
divisao_int = num1 // num2;
print("A divisao de ", num1, "//", num2, " = ", divisao_int);

# Módulo
modulo = num1 % num2;
print("O módulo de ", num1, "%", num2, " = ", modulo);
