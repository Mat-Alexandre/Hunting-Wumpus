# Mundo de Wumpus
Trabalho da disciplina de Intelligência Artificial.

-- EM PROGRESSO --
* Disclaimer: As imagens e sons utilizadas na versão 'Extra' possuem direitos autorais.
Sendo feito o uso das mesma apenas a fim de aprendizado.

É uma caverna que consiste em salas conectadas por passagens.
Em algum lugar na caverna, está o wumpus.
O wumpus pode ser atingido por um agente, mas o agente só tem uma flecha.
Algumas salas contêm poços sem fundo. O monstro devora qualquer guerreiro que entrar em sua
sala. Somente o wumpus não cai nos poços.
A única vantagem nesse ambiente é a possibilidade de encontrar um
monte de ouro.

## Definição do ambiente de tarefa:
### Medida de desempenho:
- +1.000 por pegar o ouro,
- -1.000 se cair em um poço ou for devorado pelo wumpus,
- -1 para cada ação executada e
- -10 pelo uso da flecha.–

### Ambiente:
- Uma malha 4 x 4 de salas.
- O agente sempre começa no quadrado identificado como [1, 1]
- As posições do wumpus e do ouro são escolhidas ao acaso.
- Cada quadrado (menos o inicial) pode ser um poço (probabilidade de 0,2).

### Definição do ambiente de tarefa:
#### Atuadores:
- O agente pode mover-se para frente, virar à esquerda 90º ou à direita 90º.
- O agente morrerá se entrar em um quadrado com um poço ou um wumpus vivo.
- A ação Agarrar pode ser usada para levantar um objeto no mesmo quadrado do agente.
- A ação Atirar pode ser usada uma vez para atirar uma flecha.

#### Sensores:
- O agente perceberá um fedor no quadrado contendo o wumpus e nos quadrados adjacentes (não em diagonal).
- O agente perceberá uma brisa nos quadrados adjacentes a um poço.
- O agente perceberá um resplendor no quadrado onde está o ouro.
- Quando caminhar para uma parede, o agente perceberá um impacto.
- Quando o wumpus é morto, ele emite um grito triste que pode ser percebido em qualquer lugar da caverna.
- As percepções serão dadas ao agente sob a forma de uma lista de cinco símbolos.