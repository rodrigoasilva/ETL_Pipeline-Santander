# ETL_Pipeline-Santander
Repositório criado para realização de um desafio do Bootcamp da Santander de 2023. O desafio consiste em criar todas as etapas de Extração, Transformação e Carregamento do pipeline de um ETL comum utilizando Python.


## Extract

Foi escolhida uma planilha com dados sobre a recompensa dos 160 maiores valores de One Piece. 

[A planilha foi baixada no Kaggle nesse link](https://www.kaggle.com/datasets/umeshkumar017/list-of-one-piece-bounties) 

Dentro dessa planilha estão os nomes das maiores recompensas, o índice em ordem descrescente e o valor da recompensa individual.

Para o processo de extração, foram escolhidos as recompensas de todos do bando dos Chapéus de Palha de acordo com a seguinte lista:

> ### Bando do Chapéu de Palha
> - Monkey D. Luffy
> - Roronoa Zoro
> - Vinsmoke Sanji
> - Jinbe
> - Franky
> - Brook
> - Nami
> - Usopp
> - Tony Tony Chopper
> - Nico Robin



## Transform

Para essa etapa de tratamento dos dados, as recompensas foram normalizadas para um valor número, e foi tirada a média e o desvio de cada recompensa em relação à média da tripulação.

## Load

Foi criado um novo DataFrame com apenas os integrantes do bando do Chapéus de Palha e este é retornado ao final do código.