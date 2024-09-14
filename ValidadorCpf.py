
print("Digite o CPF:")

cpfDigitado = input()

CpfSepardosEsp = cpfDigitado.replace("-", ".")

NumerosCpf = CpfSepardosEsp.split(".")
NumerosCpfStr = ''.join(NumerosCpf)

FinalDigitado = NumerosCpf.pop(3)

NumerosCpfSemFinal = ''.join(NumerosCpf)


# MULTIPLICA PELOS VALORES E OBTEM A SOMA
Multiplicador = 10
ResultadoDigito1 = 0
for digito in NumerosCpfSemFinal:
    ResultadoDigito1 += int(digito) * Multiplicador
    Multiplicador -= 1

# MULTIPLICA A SOMA POR 10

ResultadoDigito1Por10 = ResultadoDigito1 * 10

# DEFINE O VALOR DO PRIMEIRO NUMERO

primeiroNumero = ResultadoDigito1Por10 % 11
primeiroNumero = primeiroNumero if primeiroNumero <= 9 else 0


#                   SEGUNDO NUMERO
# ADICIONA O PRIEMIRO NUMERO NO FINAL DOS 9 PRIMEIROS DIGITOS DO CPF
NumerosCpfPara2digito = NumerosCpfSemFinal + str(primeiroNumero)

# MULTIPLICA PELOS VALORES E OBTEM A SOMA

Multiplicador = 11
ResultadoDigito2 = 0
for digito in NumerosCpfPara2digito:
    ResultadoDigito2 += int(digito) * Multiplicador
    Multiplicador -= 1

# MULTIPLICA A SOMA POR 10
ResultadoDigito2Por10 = ResultadoDigito2 * 10

# DEFINE O VALOR DO SEGUNDO NUMERO

SegundoNumero = ResultadoDigito2Por10 % 11
SegundoNumero = SegundoNumero if SegundoNumero <= 9 else 0

# VALIDA O CPF
ultimosDigitos = str(primeiroNumero) + str(SegundoNumero)
CpfCalculado = NumerosCpfSemFinal + ultimosDigitos

if NumerosCpfStr == CpfCalculado: 
    print(cpfDigitado+ " É válido!!")
else:
     print(cpfDigitado+ " Não é válido!!")


