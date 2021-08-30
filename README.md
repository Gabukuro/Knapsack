# Problema da Mochila com Algoritmos Genéticos

## O que são Algoritmos Genéticos ?

Algoritmos Genéticos são técnicas utilizadas para tarefas de busca e otimização, ou seja, a busca pelo ótimo, ou mais próximo disso o possível. Este algoritmo é inspirado na teoria da evolução, de Charles Darwin, ele reflete o processo de evolução natural onde os indivíduos mais adaptados são selecionados para reprodução e assim gerar uma próxima geração melhor que a anterior.

### Noção da seleção natural

O processo de seleção natural começa com a seleção dos indivíduos mais adaptados de uma população, estes devem gerar descendentes que irão herdar as características de seus pais e compor a próxima geração. Esse processo se repete até encontrar a geração "ótima".

Esta noção é aplicada para encontrar a melhor entre diversas soluções para um determinado problema.

São cinco fases consideradas em um algoritmo genético.

1. População inicial
2. Pontuar os indivíduos
3. Seleção de indivíduos
4. Cruzamento
5. Mutação

## Descrição do problema

Você ficara isolado na natureza selvagem. A única coisa que poderá levar é uma mochila que suporta no máximo 30 kg. Você possui diversos itens de sovrevivência, cada um possui "pontos de sobrevivência" (dados para cada item de acordo com a tabela).
Seu objetivo é maximizar os pontos de sobrevivência.

|      Item      |Peso|Pontos|
|----------------|----|------|
| Saco de dormir | 15 |  15  |
| Corda          |  3 |   7  |
| Canivete       |  2 |  10  |
| Tocha          |  5 |   5  |
| Garrafa        |  9 |   8  |
| Comida         | 20 |  17  |

## Resolvendo o problema

### 1. População Inicial