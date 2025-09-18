# Alunos
# Luiz Carlos Souza - 06003531
# Nathan de Brito Oliveira - 06003437
# Thiago Dutra da Silva - 06003665
# Rondineli da Silva Oliveira Moreira - 06005959
# Eduardo de Cunto - 06004790

# ToolKit
Este é um projeto de um toolkit com diversas funcionalidades relacionadas a conceitos de computação.

# Funcionalidades
O menu principal oferece as seguintes opções:

## 1. Verificador de Alfabeto e Cadeia
Descrição: Esta opção verifica se um símbolo ou uma cadeia de caracteres pertence a um alfabeto pré-definido Σ={a,b}.

## Funcionamento:

O programa primeiro solicita um único símbolo e verifica se ele pertence ao alfabeto.

Em seguida, solicita uma cadeia de caracteres e verifica se todos os caracteres da cadeia pertencem ao alfabeto.

Caso a cadeia contenha caracteres inválidos, eles serão exibidos.

## 2. Classificador de Problemas (T/I/N) por JSON
Descrição: Classifica uma lista de problemas computacionais como Tratável (T), Intratável (I) ou Não computável (N).

## Funcionamento:

Uma lista de problemas é carregada a partir de uma estrutura JSON interna.

Para cada problema, o programa exibe o nome e a descrição, e solicita ao usuário que o classifique como T, I ou N.

O programa então informa se a resposta está correta e, ao final, apresenta um resumo do desempenho do usuário.

## 3. Decisor: termina com 'b'?
Descrição: Esta funcionalidade determina se uma cadeia de caracteres inserida pelo usuário termina com a letra 'b'.

## Funcionamento:

O programa solicita que o usuário digite uma cadeia.

Ele então verifica se o último caractere da cadeia é 'b' e exibe o resultado da verificação (SIM ou NÃO).

A ferramenta também lida com o caso de uma cadeia vazia, informando que ela não termina com 'b'.

## 4. Avaliador Proposicional
Descrição: Avalia o valor-verdade de fórmulas de lógica proposicional envolvendo as proposições P, Q e R.

## Funcionamento:

O usuário escolhe um tipo de fórmula para avaliar (Conjunção e Disjunção, Implicações, ou Negações e Mistas).

O programa solicita os valores lógicos (True/False) para P, Q e R.

Os resultados das avaliações das fórmulas são exibidos.

Opcionalmente, o usuário pode visualizar a tabela-verdade completa para as fórmulas selecionadas.

## 5. Reconhecedor L_par_a e a*b*
Descrição: Reconhece se uma cadeia de caracteres pertence a uma de duas linguagens formais.

## Funcionamento:

O usuário escolhe entre duas linguagens para o reconhecimento:

L_par_a: Cadeias com um número par de 'a's.

a*b*: Cadeias formadas por zero ou mais 'a's seguidos por zero ou mais 'b's.

Após a inserção de uma cadeia, o programa verifica se ela pertence ao alfabeto {a, b}.

Por fim, o programa executa o reconhecimento de acordo com a linguagem escolhida e exibe se a cadeia é "ACEITA" ou "REJEITA".

## 0. Sair
Descrição: Encerra a execução do programa.