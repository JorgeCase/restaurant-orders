<body>
  <h1 align="center">Restaurant Orders</h1>
  <h2 align="center">Descrição</h2>
  <p align="center">Este projeto consiste em uma ferramenta de construção de cardápios para um restaurante. A ferramenta visa facilitar a geração de cardápios considerando restrições alimentares e disponibilidade de ingredientes em estoque.</p>

  <h2 align="center">Habilidades Desenvolvidas</h2>
  <p align="center">No desenvolvimento deste projeto foram utilizadas as seguintes habilidades:</p>
  <ul>
    <li>Manipulação de estruturas de dados <b>Hashmap</b> utilizando as classes <b>Dict</b> e <b>Set</b> do Python.</li>
    <li>Utilização da biblioteca <b>Pandas</b> e sua estrutura de dados <b>DataFrame</b>.</li>
    <li>Testes de software para garantir a qualidade e robustez do código.</li>
    <li>Conhecimentos de orientação a objetos (<b>POO</b>) para a implementação da ferramenta.</li>
  </ul>

  <h2 align="center">📁 Acesso ao Projeto</h2>
  <div>
    <dl>
        <dt>Para acessar o projeto faça o clone do repositório.</dt>
        <dd>No terminal utilize o comando: <code>git clone git@github.com:JorgeCase/restaurant-orders.git</code></dd>
        <dd>Entre na pasta do repositório que você acabou de clonar: <code>cd restaurant-orders</code></dd>
        <dt>Crie um ambiente virtual para o projeto com o comando:</dt>
        <dd><code>python3 -m venv .venv && source .venv/bin/activate</code></dd>
        <dt>Para ver a aplicação rodando use o comando:</dt>
        <dd><code>python3 -m uvicorn app:app</code></dd>
    </dl>
  </div>
  <h4 align="center">Este projeto é um dos requisitos para a formação de Desenvolvimento Web da Trybe</h4>
  <p>O projeto finaliza a <b>Seção 6 - Estrutura de Dados II: Hashmaps e Sets</b> do Módulo de Ciência da Computação e possuía <b>quatro</b> requisitos obrigatórios e <b>dois</b> requisitos optativos. Neste projeto obtive <b>100% de aprovação</b>.</p>
  <p>Lista de requisitos obrigatórios:</p>
  <ul>
    <li>Implementar testes para a classe <code>Ingredient</code>, previamente implementada.</li>
    <li>Implementar testes para a classe <code>Dish</code>, previamente implementada.</li>
    <li>Implementar a classe <code>MenuData</code> responsável pelo mapeamento de pratos e ingredientes baseado no arquivo <code>csv</code> disponibilizado.</li>
    <li>Implementar o método <code>get_main_menu</code> dentro da classe <code>MenuBuilder</code> para geração dos cardápios.</li>
  </ul>
  <p>Lista de requisitos optataivos:</p>
  <ul>
      <li>Implementar os métodos <code>check_recipe_availability</code> e <code>consume_recipe</code> para fazer a gestão de estoque de ingredientes.</li>
      <li>Complementar a implementação do método <code>get_main_menu</code> para gerar os cardápios baseados no estoque.</li>
  </ul>

  <div align="center">
    <h4 align="center">Para mais informações sobre a formação de Desenvolvimento Web da Trybe, clique no link abaixo.</h4>
    <a href='https://www.betrybe.com/'>Curso de Desenvolvimento Web Trybe</a>
  </div>
</body>
