
# Country Game API

Esse projeto é o complemento de um projeto anterior de jogo. Nele é formulado uma série de pontos, então desenvolvi essa API como banco do leaderbord dos jogadores.




## Iniciar Projeto

Para reutilizar o código no seu leaderboard, basta fazer um fork e seguir os seguintes passos:

```
git clone https://github.com/SEUNOME/country-game-api
cd country-game-api
source start_project
```

Isso vai ativar o ambiente virtual e instalar as dependências necessárias.
Pode também fazer testes com o Pytest, apenas digitando no terminal `pytest`

## Para rodar a API localmente, utilize:
`uvicorn cgapi.api:api --reload`
## Documentação da API

#### Retorna todos os players

```http
  GET /players/
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Gerado**. O id do player |
| `name`      | `string` | **Obrigatório**. O nome do player |
| `points`      | `int` | **Obrigatório**. A pontuação do player em questão |
| `date`      | `datetime` | **Gerado**. Horário em que foi enviado a pontuação |

#### Adiciona um player

```http
  POST /players/
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `name`      | `string` | **Obrigatório**. O nome do player |
| `points`      | `int` | **Obrigatório**. A pontuação do player em questão |

PS.: Caso o jogador já tenha registrado algum placar, seu nome será substituído pelo seu novo placar. Não é o ideal, pois qualquer pessoa poderia substituir aquela pontuação, no entando, como se trata de um jogo simples, acredito que não seja um problema por enquanto. A intenção do projeto é justamente experimentar as funcionalidades aprendidas.
