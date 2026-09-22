# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

**Unidade Curricular:** Qualidade de Software
**Metodologia:** Problem-Based Learning (PBL)
**Projeto:** LocalEats — https://local-eats-unisenac.vercel.app/
**Elemento de Competência:** EC1 — Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Integrantes:**

- Éverton Lopes
- Lorenzo Maciel

---

## Tarefa 1: Fundamentos da qualidade

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Localizar restaurantes por especialidade ou localização, por meio da pesquisa e dos filtros disponíveis na aplicação | Usuário consumidor | O usuário não encontra opções relevantes e abandona a aplicação; os restaurantes cadastrados perdem visibilidade |
| Explícita | Registrar um pedido e posteriormente consultá-lo na área "Meus Pedidos" | Usuário consumidor e restaurante parceiro | A aplicação deixa de cumprir sua finalidade principal; pedidos sem rastreabilidade geram retrabalho e reclamações |
| Implícita | As credenciais e a sessão do usuário devem ser protegidas, com senha não exposta e sessão encerrada ao sair do sistema | Usuário consumidor e operador da plataforma | Acesso indevido ao histórico de pedidos, exposição de dados pessoais, risco legal e perda de confiança na plataforma |
| Implícita | Favoritos e pedidos devem permanecer consistentes entre sessões e dispositivos | Usuário consumidor | O usuário refaz trabalho já realizado, desconfia da confiabilidade do sistema e deixa de utilizar o recurso |

### Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade?

Sim. A qualidade não se mede pela simples presença das funcionalidades, mas pelo grau em que elas atendem às necessidades declaradas e às implícitas. O LocalEats pode ter cadastro, favoritos e pedidos funcionando e ainda assim ser inadequado se a sessão não for encerrada corretamente ao sair do sistema: a necessidade explícita "entrar no sistema" estaria atendida, mas a necessidade implícita de proteção da sessão, não. Na prática, outra pessoa com acesso ao mesmo dispositivo visualizaria o histórico de pedidos do usuário. O comportamento seria funcionalmente correto e, ainda assim, de baixa qualidade.

---

## Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Éverton Lopes | Criar conta | **Utilização esperada:** acessar o LocalEats, clicar em "Criar Conta", preencher Nome Completo, E-mail e Senha com mais de três caracteres e clicar em "Registrar". **Utilização alternativa:** repetir o mesmo fluxo informando um e-mail já cadastrado anteriormente. | **Esperada:** a conta foi criada e a aplicação apresentou diretamente a home com o usuário autenticado, exibindo "Olá, Teste" no canto superior direito e o menu Explorar, Meus Favoritos e Meus Pedidos. O fluxo não passou pela tela de login. **Alternativa:** a aplicação exibiu a mensagem "Email already registered" acima do formulário e não criou a conta. A mensagem foi apresentada em inglês, enquanto os demais rótulos da tela estão em português, e não foi posicionada junto ao campo de e-mail. Os dados informados permaneceram preenchidos. | [everton-criar-conta-sucesso-home-logada.png](./evidencias/everton-criar-conta-sucesso-home-logada.png) · [everton-criar-conta-email-ja-registrado.png](./evidencias/everton-criar-conta-email-ja-registrado.png) |
| Lorenzo Maciel | Pesquisar restaurantes | **Utilização esperada:** acessar a home, inserir o termo "Centro" no campo de busca e clicar em "Buscar". **Utilização alternativa:** repetir o fluxo com o termo "Teste", que não corresponde a nenhuma especialidade ou localização cadastrada. | **Esperada:** a aplicação retornou restaurantes cuja localização exibida é "Centro" (Restaurante Sabor 1, Restaurante Sabor 7 e Restaurante Sabor 9), com especialidades distintas entre si (Japonesa, Italiana e Mexicana), com o filtro de especialidade mantido em "Todos". A página não retornou ao topo após a busca, deixando o título parcialmente encoberto pelo cabeçalho fixo. **Alternativa:** a aplicação exibiu a mensagem "Nenhum restaurante encontrado." em português, alinhada à esquerda abaixo dos filtros, e nenhum card foi listado. O termo permaneceu no campo de busca. | [lorenzo-pesquisar-localizacao-centro.png](./evidencias/lorenzo-pesquisar-localizacao-centro.png) · [lorenzo-pesquisar-termo-inexistente.png](./evidencias/lorenzo-pesquisar-termo-inexistente.png) |

---

## Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Éverton Lopes | O cadastro deve impedir a criação de conta com e-mail já registrado e informar o motivo ao usuário por meio de mensagem apresentada no mesmo idioma da interface e associada ao campo correspondente | Usabilidade → Proteção contra erro do usuário | O cadastro é o primeiro contato do usuário com o LocalEats e é o ponto em que um erro de preenchimento tem maior custo de correção. A exploração mostrou que a duplicidade é bloqueada, o que já protege contra o erro, mas a mensagem "Email already registered" aparece em inglês em uma interface em português e afastada do campo de e-mail. Isso reduz a chance de o usuário compreender de imediato qual dado precisa ser alterado, obrigando-o a deduzir a causa da recusa | Executar uma série de cadastros com entradas inválidas (e-mail já registrado, e-mail sem "@", domínio ausente, senha curta e campos obrigatórios em branco) e registrar, para cada caso, se a criação foi bloqueada, se a mensagem identifica o campo e o motivo, em qual idioma ela é apresentada e a que distância do campo ela é posicionada. Comparar o número de casos com mensagem em português e associada ao campo com o total de casos testados |
| Lorenzo Maciel | A pesquisa deve retornar apenas restaurantes cuja especialidade ou localização corresponda ao termo buscado e, quando não houver correspondência, informar explicitamente a ausência de resultados | Adequação funcional → Correção funcional | No LocalEats a busca é o caminho principal para o usuário chegar ao restaurante desejado, e o resultado precisa ser fiel ao termo informado para que a lista seja confiável. Na exploração, o termo "Centro" retornou apenas restaurantes dessa localização, mesmo com especialidades diferentes entre si, e o termo inexistente produziu a mensagem "Nenhum restaurante encontrado." em vez de uma tela vazia sem explicação. O requisito formaliza essa condição, que precisa se manter para qualquer termo, e não apenas para os casos verificados | Executar buscas com termos válidos de especialidade e de localização, conferindo em cada card retornado se a especialidade ou o bairro exibido corresponde ao termo, e contar quantos resultados divergiram do total retornado. Repetir com termos inexistentes, com erros de digitação, com variação de maiúsculas e acentos e com o campo vazio, registrando em quais casos a mensagem de ausência de resultados foi apresentada |

---

## Uso de inteligência artificial

**Ferramenta utilizada:**
Claude (Anthropic).

**Como foi utilizada:**
Apoio na redação das necessidades explícitas e implícitas da Tarefa 1, na organização dos registros de exploração da Tarefa 2 a partir dos passos e das capturas de tela produzidos pelos integrantes, e na formulação dos requisitos de qualidade e dos critérios de avaliação da Tarefa 3.

**Como as respostas foram verificadas:**
O grupo revisou cada trecho gerado antes de incorporá-lo ao documento. As descrições da exploração foram conferidas contra as capturas de tela produzidas pelos integrantes, e o que não podia ser comprovado pela interface foi removido ou reescrito.
