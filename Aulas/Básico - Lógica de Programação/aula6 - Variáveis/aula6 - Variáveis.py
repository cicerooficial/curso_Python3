"""
Variáveis
1. Iniciar com letra;
2. Sempre com letras minúsculas;
3. Pode conter números;
4. Separar com _.
"""

nome        = 'Henrique'        #str-String
idade       = 26                #int
altura      = 1.70              #float
e_maior     = idade > 18        #bool
peso        = 80                #int
imc         = peso // altura**2

print('Nome: ',nome)
print('Idade: ',idade)
print('Altura: ',altura)
print('É maior: ',e_maior)

print(nome, 'tem', idade, 'de idade e seu IMC é:', imc)
