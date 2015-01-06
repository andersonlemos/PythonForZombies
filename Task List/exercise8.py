# coding: utf-8

valorPorHora = float(raw_input("Digite o valor da Hora trabalhada : "))
quantidadeDeHorasTrabalhadas = float(raw_input('Horas trabalhadas : '))

salarioBruto = quantidadeDeHorasTrabalhadas * valorPorHora
impostoDeRenda = (salarioBruto * 0.11)
inss = (salarioBruto * 0.08)
sindicato = (salarioBruto * 0.05)

salarioLiquido = salarioBruto - impostoDeRenda - inss - sindicato

print ('+ Salario Bruto : R$ %5.2f ' % salarioBruto)
print ('- IR  : R$ %5.2f ' % impostoDeRenda)
print ('- INSS  : R$ %5.2f ' % inss)
print ('- SINDICATO  : R$ %5.2f ' % sindicato)
print ('= Salario Liquido  : R$ %5.2f ' % salarioLiquido)