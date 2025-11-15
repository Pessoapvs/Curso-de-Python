<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Curso de Python — README</title>
  
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">
        <!-- Python logo oficial -->
        <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" style="max-width:80px;max-height:80px">
      </div>
      <div>
        <h1>Curso de Python — Meu Aprendizado</h1>
        <p class="lead">Repositório com exercícios, projetos e anotações do meu curso de Python. Ideal para quem está começando ou quer revisar conceitos práticos.</p>
        <div class="badges">
          <img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python badge">
          <img src="https://img.shields.io/badge/Status-Em%20Progresso-yellow" alt="status badge">
        </div>
      </div>
    </header>

    <section>
      <h2>O que tem aqui?</h2>
      <div class="grid">
        <div class="card">
          <h3>Conteúdo</h3>
          <ul>
            <li>Exercícios básicos (variáveis, operadores, controle de fluxo)</li>
            <li>Projetos pequenos (calculadora, conversores, tabuada, jogos simples)</li>
            <li>Anotações e dicas práticas</li>
            <li>Scripts voltados para segurança da informação (com responsabilidade)</li>
          </ul>
        </div>
        <div class="card">
          <h3>Estrutura do repositório</h3>
          <pre>/
├─ README.html  (visualização em HTML)
├─ exercicios/
│  ├─ basicos.py
│  └─ tabuada.py
├─ projetos/
│  └─ projeto_exemplo/
└─ assets/
   └─ imagens/
</pre>
        </div>
      </div>
    </section>

    <section>
      <h2>Galeria</h2>
      <div class="images">
        <!-- Imagens de exemplo (livres) -->
        <img src="https://images.unsplash.com/photo-1581093588401-5b0a2d5f8b76?auto=format&fit=crop&w=800&q=60" alt="Exemplo 1">
        <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=60" alt="Exemplo 2">
      </div>
    </section>

    <section>
      <h2>Como usar</h2>
      <ol>
        <li>Clone o repositório: <code>git clone https://github.com/seu-usuario/seu-repo.git</code></li>
        <li>Entre na pasta e execute os scripts com <code>python3 nome_do_arquivo.py</code></li>
        <li>Leia os comentários e teste modificações — prática é tudo!</li>
      </ol>
    </section>

    <section>
      <h2>Exemplo rápido (tabuada)</h2>
      <pre><code>n = int(input('Digite um número inteiro: '))
for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')
</code></pre>
    </section>

    <footer>
      <p>Feito com ❤️ e Python. Se quiser, posso gerar também a versão <code>README.md</code> atualizada com estes conteúdos em Markdown ou te ajudar a adicionar badges e GIFs.</p>
      <p>Contato: <a href="mailto:seu-email@example.com">seu-email@example.com</a></p>
    </footer>
  </div>
</body>
</html>

