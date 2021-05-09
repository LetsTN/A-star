# A*

## Como executar o código
  Abrir o terminal e ir até a pasta onde está o código.
  Depois, é só executar com:

  ```sh
    python3 main.py mapa.txt 0,0 9,8
  ```

  Onde ```mapa.txt``` é o arquivo com o mapa, ```0,0``` é a posição inicial e ```9,8``` é a posição final.

## Saída
  O código irá retornar, pelo próprio terminal, a seguinte saída:
  
  ```sh
    Mapa da trajetória (maracado com 'x'):
    ['x', '0', '1', '0', '0', '0', '0', '0', '0', '0']
    ['x', '0', '1', '0', '0', '0', '0', '0', '0', '0']
    ['x', 'x', '0', '0', '0', '0', '0', '0', '0', '0']
    ['0', 'x', 'x', 'x', '0', '1', '0', '0', '0', '0']
    ['1', '1', '1', 'x', '0', '1', '0', '0', '0', '0']
    ['0', '0', '0', 'x', 'x', '1', '0', '0', '0', '0']
    ['0', '0', '0', '0', 'x', 'x', '0', '0', '1', '1']
    ['0', '0', '0', '0', '0', 'x', 'x', 'x', '0', '0']
    ['0', '0', '0', '0', '1', '1', '1', 'x', '0', '0']
    ['0', '0', '0', '0', '0', '0', '0', 'x', 'x', '0']

    Lista com as coordenadas:
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (5, 4), (6, 4), (6, 5), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7), (9, 8)]
  ```

## Sobre o algoritmo A*
  O algoritmo A* é um algoritmo guloso para **Busca de caminhos**, procurando o melhor caminho de um vértice inicial até um vértice final em um grafo ou matriz.

  Ele escolhe esse caminho a cada iteração, procurando a melhor escolha possível de acordo com algum critério, normalmente chamado de heurística.

  Para ser mais eficiente, ele armazena os nós não explorados em uma **franja**. A cada iteração, vai-se acrescentando na franja os estados sucessores ao estado atual, e depois é procurado qual deles é o mais promissor, para assim ir montando o caminho.

## Heurística escolhida
  A heurística escolhida para esse trabalho foi a **Distância Euclidiana**, dada pela função:

  ![equation](http://www.sciweavers.org/tex2img.php?eq=%20%5Csqrt%7B%28i_%7Bfinal%7D-%20i_%7Binicial%7D%29%5E%7B2%7D%2B%28j_%7Bfinal%7D-j_%7Binicial%7D%29%5E%7B2%7D%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

## Resumo do algoritmo desenvolvido
  - Primeiro, no arquivo ```main.py```, são buscados o nome do arquivo com o mapa, a posição inicial e a posição final;

  - Ainda no ```main.py```, é instanciada uma Grid, que irá abrir e ler o arquivo com o mapa para convertê-lo em uma matriz (lista de listas);

  - Feita essa conversão, é então chamado o A*, instanciado de uma classe A_star. O cálculo do melhor caminho é feito da  seguinte forma:
    
    - Começando do ponto inicial, são inicializados os dicionários de distância do objetivo (```dist_objective```), distância percorrida (```dist_traveled```), distância valores calculados da heuristica (```heuristic```) e os nós percorridos em ordem (```before```), também como a lista de nós percorridos no geral (```states```) e a lista de franja (```fringe```);

    - Feito isso, começa-se a fazer as iterações, buscando os próximos nós (cima, baixo, esquerda e direita), analisando qual deles é o mais promissor com base na distância até o objetivo e adicionando-o ao dicionário e lista de nós percorridos, até chegar ao objetivo final;

    - Chegado o último nó, é feito um mapa do resultado (colocando um 'x' em cada nó do caminho), montada uma lista de respostas à partir do dicionário de nós percorridos, retornando ambos ao ```main.py```;

  - De volta ao ```main.py```, tudo é finalizado com o retorno via terminal tanto da matriz de resposta quanto da lista com o caminho.
