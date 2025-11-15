<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Curso de Python — README</title>
  <style>
    :root{--bg:#0f1724;--card:#0b1220;--accent:#ffd43b;--muted:#94a3b8}
    body{font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; background:linear-gradient(180deg,#071020 0%, #091226 100%); color:#e6eef8; margin:0; padding:40px}
    .container{max-width:900px;margin:0 auto;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));padding:28px;border-radius:12px;box-shadow:0 8px 30px rgba(2,6,23,0.6)}
    header{display:flex;gap:16px;align-items:center}
    .logo{width:96px;height:96px;display:flex;align-items:center;justify-content:center;background:rgba(255,255,255,0.02);border-radius:12px;padding:8px}
    h1{margin:0;font-size:1.6rem}
    p.lead{color:var(--muted);margin-top:8px}
    .badges img{height:22px;margin-right:8px}
    section{margin-top:22px}
    .grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
    .card{background:var(--card);padding:12px;border-radius:10px}
    .images{display:flex;gap:10px;flex-wrap:wrap}
    .images img{width:calc(50% - 5px);border-radius:8px}
    code{background:rgba(0,0,0,0.3);padding:4px 6px;border-radius:6px;color:#ffe9b2}
    pre{background:#051025;padding:12px;border-radius:8px;overflow:auto}
    footer{margin-top:18px;color:var(--muted);font-size:0.9rem}
    a{color:var(--accent);text-decoration:none}
    @media(max-width:640px){.grid{grid-template-columns:1fr}.images img{width:100%}}
  </style>
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
