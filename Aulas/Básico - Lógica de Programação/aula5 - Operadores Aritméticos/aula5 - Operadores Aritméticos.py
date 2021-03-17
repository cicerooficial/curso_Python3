"""
Operadores aritméticos

+   - Adição
-   - Subtração
*   - Multiplicação
/   - Divisão quebrada (ponto flutuante)
//  - Divisão arredondada (inteiro)
**  - Exponenciação número elevado à outro
%   - Resto da divisão
()  - Alterar a precedência dos operadores

Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na hora de realizar contas mais complexas
(de maior para menor precedência).

( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro
** - Depois vem a exponenciação
* / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo
+  - - Por fim, soma e subtração
Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

"""

print('Adição', 10+10)
print('Subtração',10-10)
print('Multiplicação',10*10)
print('Divisão quebrada',10.5/3)
print('Divisão arredondada',10//3)
print('Exponenciação',2**10)
print('Resto da divisão',10%3)
print('Alterar a precedência',5+2*10)
print('Alterar a precedência',(5+2)*10)

