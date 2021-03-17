nome        = 'Henrique'        #str-String
idade       = 26                #int
altura      = 1.70              #float
e_maior     = idade > 18        #bool
peso        = 80                #int
imc         = peso // altura**2

print(nome, 'tem', idade, 'de idade e seu IMC é:', imc)
#Para uso de código mais elegível, pode-se utilizar as formatações abaixo:

print(f'{nome} tem {idade} de idade e seu IMC é: {imc}')
print(f'{nome} tem {idade} de idade e seu IMC é: {imc:.2f}')
print('{} tem {} de idade e seu IMC é: {}'.format(nome, idade, imc))
print('{0} tem {1} de idade e seu IMC é: {2}'.format(nome, idade, imc))
print('{n} tem {i} de idade e seu IMC é: {imc}'.format(n=nome, i=idade, imc=imc))