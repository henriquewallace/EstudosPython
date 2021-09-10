horaEntrada = int(input('Hora de entrada: '))
horaSaida = int(input('Hora de saída: '))
valorHora = 8
valorDiaria = 30
horaTotal = horaSaida - horaEntrada
# Se o cliente permanecer mais de 10 horas ele vai pagar o valor da diária
if horaTotal < 10:
    valorTotalEstacionamento = (horaSaida - horaEntrada) * valorHora
else:
    valorTotalEstacionamento = valorDiaria
print(valorTotalEstacionamento)