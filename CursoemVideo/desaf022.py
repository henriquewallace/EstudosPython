nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('O seu nome em letras minúsculas é {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separar = nome.split()
print('Seu segundo nome é {} e ele tem {} letras'.format(separar[1], len(separar[1])))













