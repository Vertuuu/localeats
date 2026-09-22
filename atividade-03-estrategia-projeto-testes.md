# Atividade 3: Estratégia e Projeto de Testes no LocalEats

**Unidade Curricular:** Qualidade de Software
**Metodologia:** Problem-Based Learning (PBL)
**Projeto:** LocalEats — https://local-eats-unisenac.vercel.app/
**Elemento de Competência:** EC4 — Planejar e projetar testes selecionando técnicas adequadas.

**Integrantes:**

- Éverton Lopes — funcionalidade sob sua responsabilidade: **Criar conta**
- Lorenzo Maciel — funcionalidade sob sua responsabilidade: **Pesquisar restaurantes**

> As funcionalidades mantidas aqui são as mesmas exploradas na Atividade 1, e os requisitos de qualidade formulados naquela atividade são a base de teste utilizada neste documento.

---

## Tarefa 1: Análise e priorização de riscos

### Critério de priorização adotado

A probabilidade e o impacto foram classificados em três níveis. A probabilidade considera o que já foi observado na exploração da Atividade 1 e a ausência de validação declarada; o impacto considera a consequência para o usuário e para o negócio caso a falha ocorra em produção.

| | Impacto Baixo | Impacto Médio | Impacto Alto |
|---|---|---|---|
| **Probabilidade Alta** | P3 | P2 | P1 |
| **Probabilidade Média** | P3 | P2 | P1 |
| **Probabilidade Baixa** | P3 | P3 | P2 |

O impacto pesa mais do que a probabilidade na definição da prioridade. A decisão é deliberada: o LocalEats é o canal principal de contato entre o usuário e o restaurante, e uma falha de impacto alto compromete o uso do produto mesmo quando ocorre com pouca frequência. P1 é executado obrigatoriamente, P2 é executado quando houver tempo disponível no ciclo e P3 é executado por amostragem.

### Riscos identificados

| ID | Funcionalidade | Integrante | Risco (o que pode falhar e qual a consequência) | Prob. | Impacto | Prioridade |
|---|---|---|---|---|---|---|
| RSC-01 | Criar conta | Éverton Lopes | O cadastro aceitar e-mail em formato inválido (sem "@", sem domínio, sem parte local ou com espaço) e criar a conta assim mesmo. O usuário fica sem canal de recuperação de senha e de contato, e o e-mail, que é a chave usada para impedir duplicidade, deixa de ser confiável | Alta | Alto | **P1** |
| RSC-02 | Criar conta | Éverton Lopes | A regra de tamanho mínimo da senha não ser aplicada corretamente no limite, permitindo o cadastro com senha mais curta do que o exigido. Credenciais fracas aumentam o risco de acesso indevido ao histórico de pedidos, que é a necessidade implícita levantada na Atividade 1 | Média | Alto | **P1** |
| RSC-03 | Criar conta | Éverton Lopes | A recusa do cadastro ser comunicada de forma que o usuário não identifique a causa: mensagem em idioma diferente do restante da interface e posicionada longe do campo correspondente. O usuário repete a tentativa sem corrigir o dado certo ou abandona o cadastro | Alta | Médio | **P2** |
| RSC-04 | Pesquisar restaurantes | Lorenzo Maciel | A busca retornar restaurantes que não correspondem ao termo informado, por casar fragmentos de texto em vez do valor pesquisado. A lista deixa de ser confiável e o usuário é levado a restaurantes fora do que procurou | Média | Alto | **P1** |
| RSC-05 | Pesquisar restaurantes | Lorenzo Maciel | A busca deixar de encontrar restaurantes existentes por diferença de acentuação ou de caixa no termo digitado ("saudavel" em vez de "Saudável"). O usuário conclui que não há opção disponível quando há | Média | Médio | **P2** |
| RSC-06 | Pesquisar restaurantes | Lorenzo Maciel | A ausência de resultados não ser comunicada, ou ser comunicada sem indicar a causa quando a busca é combinada com o filtro de especialidade. O usuário não distingue "não existe" de "a aplicação falhou" | Baixa | Médio | **P3** |

### Justificativa da probabilidade atribuída

- **RSC-01 (Alta):** na exploração da Atividade 1 não foi observada qualquer crítica de formato de e-mail, e a interface de serviço pública da aplicação trata o campo de e-mail como texto livre, sem tipo específico de endereço eletrônico. Não há, portanto, validação declarada na qual confiar.
- **RSC-02 (Média):** a regra observada na Atividade 1 é "senha com mais de três caracteres". O valor exato do limite e o comportamento no limite não estão documentados, e regras de tamanho mínimo são um ponto clássico de erro de implementação (uso de `>` onde deveria haver `>=`).
- **RSC-03 (Alta):** o comportamento já foi observado e registrado com evidência na Atividade 1 — a mensagem "Email already registered" apareceu em inglês, acima do formulário e não junto ao campo de e-mail. O risco não é hipotético; o que se verifica aqui é sua extensão aos demais casos de recusa.
- **RSC-04 (Média):** a busca da Atividade 1 com o termo "Centro" retornou apenas restaurantes daquela localização, que é o comportamento desejado. O risco permanece porque a regra de correspondência não está especificada: não há definição de que a busca deva casar o termo inteiro, e consultas à interface de serviço da aplicação retornam resultados também para fragmentos de palavra.
- **RSC-05 (Média):** as localizações e especialidades cadastradas incluem valores acentuados ("Saudável", "Hambúrguer"), e o usuário digita sem acento com frequência.
- **RSC-06 (Baixa):** a mensagem "Nenhum restaurante encontrado." já foi observada e funcionou no caso simples. Restou verificar a combinação com o filtro de especialidade, ainda não exercitada.

---

## Tarefa 2: Técnicas de teste selecionadas e sua aplicação

Todas as técnicas escolhidas são de **caixa-preta**, aplicadas no **nível de sistema** e pela **interface web**. A equipe não tem acesso ao código-fonte da aplicação, e os requisitos da Atividade 1 estão formulados em termos de comportamento observável pelo usuário, o que torna as técnicas baseadas na especificação as adequadas para esta etapa.

| Integrante | Risco atendido | Técnica escolhida | Por que esta técnica |
|---|---|---|---|
| Éverton Lopes | RSC-01 | Partição de equivalência | O e-mail admite um número infinito de entradas. A técnica reduz esse conjunto a classes que a aplicação deve tratar do mesmo modo, garantindo cobertura das formas de invalidez sem repetir casos equivalentes entre si |
| Éverton Lopes | RSC-02 | Análise de valor limite | O risco está em uma regra de tamanho com um limite numérico definido. O defeito típico não ocorre no meio da faixa, e sim exatamente na fronteira entre aceitar e recusar, que é onde a técnica concentra os casos |
| Éverton Lopes | RSC-03 | Teste baseado em experiência (exploratório guiado por checklist) | A qualidade da mensagem é um atributo de usabilidade e não pode ser derivada de partições de entrada: o que se avalia é idioma, posicionamento, clareza e preservação dos dados digitados. O roteiro é um checklist aplicado a cada recusa produzida pelos demais casos, o que evita execução duplicada |
| Lorenzo Maciel | RSC-04 e RSC-05 | Partição de equivalência | O termo de busca também tem domínio infinito. As classes separam o que deve retornar resultados do que não deve, e isolam as variações de escrita (caixa, acento, fragmento) que o requisito precisa tratar de forma equivalente |
| Lorenzo Maciel | RSC-06 | Tabela de decisão | O resultado da busca não depende de uma entrada isolada, e sim da combinação entre o termo digitado e o filtro de especialidade selecionado. A tabela de decisão torna explícitas todas as combinações de condições e evita que uma delas fique sem caso de teste |

### Aplicação 1 — Partição de equivalência no campo E-mail (Éverton, RSC-01)

| Classe | Tipo | Descrição | Representante escolhido |
|---|---|---|---|
| CE-01 | Válida | E-mail bem formado e ainda não cadastrado | `everton.qa01@teste.com` |
| CE-02 | Inválida (regra de negócio) | E-mail bem formado e já cadastrado | e-mail utilizado na Atividade 1 |
| CE-03 | Inválida (formato) | Sem o caractere "@" | `evertonteste.com` |
| CE-04 | Inválida (formato) | Com "@", sem domínio | `everton@` |
| CE-05 | Inválida (formato) | Com domínio, sem parte local | `@teste.com` |
| CE-06 | Inválida (formato) | Contendo espaço no meio do endereço | `everton qa@teste.com` |
| CE-07 | Inválida (obrigatoriedade) | Campo vazio | (em branco) |

Um representante por classe é suficiente, porque a hipótese da técnica é que a aplicação trata igualmente todos os valores de uma mesma classe. Não foram criados casos adicionais com outros e-mails bem formados, que pertenceriam à mesma classe CE-01.

### Aplicação 2 — Análise de valor limite no campo Senha (Éverton, RSC-02)

Regra sob teste, conforme observado na Atividade 1: a senha deve ter **mais de três caracteres**, ou seja, o menor valor aceito é **4**.

| Valor (nº de caracteres) | Posição em relação ao limite | Classe | Resultado esperado |
|---|---|---|---|
| 0 | Fora da faixa (campo vazio) | Inválida | Cadastro bloqueado, campo obrigatório sinalizado |
| 3 | Limite inferior inválido | Inválida | Cadastro bloqueado, com mensagem informando o tamanho mínimo |
| 4 | Limite inferior válido | Válida | Conta criada |
| 5 | Imediatamente acima do limite válido | Válida | Conta criada |

Os valores 3 e 4 são o par crítico: são eles que revelam um erro de comparação na implementação da regra. Os valores 0 e 5 confirmam o comportamento das faixas adjacentes. **Se o limite da regra mudar**, apenas esta tabela precisa ser refeita: os valores passam a ser o novo limite inválido, o novo limite válido e seus vizinhos imediatos, e os casos CT-EV-07 e CT-EV-08 são atualizados. Os demais casos do projeto não são afetados.

### Aplicação 3 — Partição de equivalência no campo de busca (Lorenzo, RSC-04 e RSC-05)

| Classe | Tipo | Descrição | Representante escolhido |
|---|---|---|---|
| CB-01 | Válida | Termo igual a uma localização cadastrada | `Centro` |
| CB-02 | Válida | Termo igual a uma especialidade cadastrada | `Japonesa` |
| CB-03 | Válida | Termo válido com caixa diferente da cadastrada | `japonesa` |
| CB-04 | Válida | Termo válido digitado sem acento | `saudavel` |
| CB-05 | Inválida (sem correspondência) | Termo que não corresponde a nenhuma especialidade ou localização | `Teste` |
| CB-06 | Limite / ambígua | Fragmento de uma palavra cadastrada | `cent` |
| CB-07 | Limite | Campo contendo apenas espaço em branco | `" "` |
| CB-08 | Limite | Campo vazio | (em branco) |

As classes CB-03 e CB-04 são tratadas como válidas porque o usuário não tem como saber a grafia exata armazenada; exigir a digitação idêntica transferiria a ele um conhecimento que a aplicação deveria absorver. As classes CB-06 e CB-07 estão marcadas como limite porque o requisito atual não define a regra de correspondência para fragmentos nem o tratamento do espaço em branco — ver a decisão registrada no item "Pontos em aberto" do plano.

### Aplicação 4 — Tabela de decisão para busca combinada com filtro (Lorenzo, RSC-06)

**Condições:** C1 — termo informado no campo de busca; C2 — o termo corresponde a alguma especialidade ou localização cadastrada; C3 — filtro de especialidade diferente de "Todos" selecionado; C4 — existe restaurante que satisfaz simultaneamente o termo e o filtro.

| Regra | C1 | C2 | C3 | C4 | Ação esperada | Caso |
|---|---|---|---|---|---|---|
| R1 | N | — | N | — | Exibir a lista completa de restaurantes, sem mensagem de erro | CT-LO-08 |
| R2 | S | S | N | — | Exibir somente os restaurantes correspondentes ao termo | CT-LO-01, CT-LO-02 |
| R3 | S | N | N | — | Exibir a mensagem de ausência de resultados, sem nenhum card listado | CT-LO-05 |
| R4 | S | S | S | S | Exibir somente os restaurantes que atendem ao termo **e** à especialidade selecionada | CT-LO-09 |
| R5 | S | S | S | N | Exibir a mensagem de ausência de resultados, mantendo visíveis o termo e o filtro aplicados | CT-LO-10 |
| R6 | N | — | S | — | Exibir somente os restaurantes da especialidade selecionada | CT-LO-11 |

As combinações em que C2 é indiferente ("—") foram consolidadas porque a condição não altera a ação quando não há termo informado. Essa consolidação reduz as dezesseis combinações teóricas a seis regras efetivas, sem perder nenhuma ação distinta.

---

## Tarefa 3: Casos de teste elaborados

### Éverton Lopes — Criar conta

| ID | Risco | Técnica | Pré-condição | Dados de entrada | Passos | Resultado esperado |
|---|---|---|---|---|---|---|
| CT-EV-01 | RSC-01 | Partição (CE-01) | Usuário não autenticado; e-mail ainda não cadastrado | Nome: `Everton QA`; E-mail: `everton.qa01@teste.com`; Senha: `Senha123` | 1. Acessar a aplicação. 2. Clicar em "Criar Conta". 3. Preencher os três campos. 4. Clicar em "Registrar" | Conta criada e usuário autenticado; a home é exibida com a saudação do usuário no cabeçalho e o menu Explorar, Meus Favoritos e Meus Pedidos |
| CT-EV-02 | RSC-01, RSC-03 | Partição (CE-02) | Existir conta previamente cadastrada com o e-mail utilizado | E-mail já registrado; demais campos válidos | 1 a 4 idem CT-EV-01 | Cadastro bloqueado; mensagem apresentada no idioma da interface, associada ao campo E-mail, informando que o endereço já está em uso; os dados digitados permanecem preenchidos |
| CT-EV-03 | RSC-01 | Partição (CE-03) | Usuário não autenticado | E-mail: `evertonteste.com`; demais campos válidos | 1 a 4 idem CT-EV-01 | Cadastro bloqueado; mensagem indicando que o e-mail está em formato inválido, associada ao campo E-mail |
| CT-EV-04 | RSC-01 | Partição (CE-04) | Usuário não autenticado | E-mail: `everton@`; demais campos válidos | 1 a 4 idem CT-EV-01 | Cadastro bloqueado com mensagem de formato inválido |
| CT-EV-05 | RSC-01 | Partição (CE-05) | Usuário não autenticado | E-mail: `@teste.com`; demais campos válidos | 1 a 4 idem CT-EV-01 | Cadastro bloqueado com mensagem de formato inválido |
| CT-EV-06 | RSC-01 | Partição (CE-06) | Usuário não autenticado | E-mail: `everton qa@teste.com`; demais campos válidos | 1 a 4 idem CT-EV-01 | Cadastro bloqueado com mensagem de formato inválido |
| CT-EV-07 | RSC-02 | Valor limite (3) | Usuário não autenticado; e-mail inédito | Senha: `abc` (3 caracteres); demais campos válidos | 1 a 4 idem CT-EV-01 | Cadastro bloqueado; mensagem informando o tamanho mínimo exigido para a senha |
| CT-EV-08 | RSC-02 | Valor limite (4) | Usuário não autenticado; e-mail inédito | Senha: `abcd` (4 caracteres); demais campos válidos | 1 a 4 idem CT-EV-01 | Conta criada e usuário autenticado |
| CT-EV-09 | RSC-01, RSC-02 | Partição (CE-07 e senha vazia) | Usuário não autenticado | Todos os campos em branco | 1. Acessar "Criar Conta". 2. Clicar em "Registrar" sem preencher | Cadastro bloqueado; cada campo obrigatório não preenchido é sinalizado individualmente |
| CT-EV-10 | RSC-03 | Exploratório guiado por checklist | Ter executado ao menos os casos CT-EV-02 a CT-EV-07 | As recusas produzidas pelos casos anteriores | Para cada recusa observada, registrar: (a) o idioma da mensagem; (b) a distância entre a mensagem e o campo correspondente; (c) se a mensagem identifica o campo e o motivo; (d) se os dados digitados foram preservados; (e) se o foco foi levado ao campo com erro | Em 100% das recusas a mensagem está em português, identifica o campo e o motivo, é exibida junto ao campo correspondente e os dados válidos já digitados são preservados. Qualquer desvio é registrado como defeito de usabilidade com a captura de tela correspondente |

### Lorenzo Maciel — Pesquisar restaurantes

| ID | Risco | Técnica | Pré-condição | Dados de entrada | Passos | Resultado esperado |
|---|---|---|---|---|---|---|
| CT-LO-01 | RSC-04 | Partição (CB-01) / Regra R2 | Home carregada; filtro de especialidade em "Todos" | Termo: `Centro` | 1. Digitar o termo no campo de busca. 2. Clicar em "Buscar". 3. Conferir cada card retornado | Todos os cards retornados exibem a localização "Centro"; nenhum restaurante de outra localização é listado; restaurantes de especialidades diferentes podem aparecer, desde que a localização corresponda |
| CT-LO-02 | RSC-04 | Partição (CB-02) / Regra R2 | Home carregada; filtro em "Todos" | Termo: `Japonesa` | 1 a 3 idem CT-LO-01 | Todos os cards retornados exibem a especialidade "Japonesa"; nenhum restaurante de outra especialidade é listado |
| CT-LO-03 | RSC-05 | Partição (CB-03) | Ter executado CT-LO-02 e registrado o conjunto retornado | Termo: `japonesa` | 1 a 3 idem CT-LO-01 | O conjunto de restaurantes retornado é idêntico ao de CT-LO-02 |
| CT-LO-04 | RSC-05 | Partição (CB-04) | Existir restaurante com especialidade "Saudável" | Termo: `saudavel` | 1 a 3 idem CT-LO-01 | São retornados os restaurantes de especialidade "Saudável"; a ausência de acento no termo não altera o resultado |
| CT-LO-05 | RSC-06 | Partição (CB-05) / Regra R3 | Home carregada; filtro em "Todos" | Termo: `Teste` | 1 a 2 idem CT-LO-01 | Nenhum card é listado e a mensagem "Nenhum restaurante encontrado." é exibida; o termo permanece no campo de busca |
| CT-LO-06 | RSC-04 | Partição (CB-06) | Home carregada; filtro em "Todos" | Termo: `cent` | 1 a 3 idem CT-LO-01 | Nenhum restaurante sem relação com o fragmento é retornado: todo card listado deve conter o fragmento na especialidade ou na localização exibida. O caso também registra qual regra de correspondência a aplicação adota (termo completo ou fragmento), para que seja especificada — ver "Pontos em aberto" |
| CT-LO-07 | RSC-04 | Partição (CB-07) | Home carregada; filtro em "Todos" | Termo: um único espaço em branco | 1 a 3 idem CT-LO-01 | O espaço é tratado como busca sem termo e a lista completa é exibida; o espaço não é usado como texto a ser casado com o conteúdo dos campos |
| CT-LO-08 | RSC-06 | Regra R1 | Home carregada; filtro em "Todos" | Campo de busca vazio | 1. Clicar em "Buscar" sem digitar nada | A lista completa de restaurantes é exibida, sem mensagem de erro e sem mensagem de ausência de resultados |
| CT-LO-09 | RSC-06 | Regra R4 | Existir restaurante italiano localizado no Centro | Termo: `Centro`; filtro: `Italiana` | 1. Digitar o termo e clicar em "Buscar". 2. Selecionar o filtro "Italiana". 3. Conferir cada card | Somente restaurantes que atendem às duas condições são exibidos (localização "Centro" e especialidade "Italiana") |
| CT-LO-10 | RSC-06 | Regra R5 | Escolher uma combinação sem interseção na base atual | Termo: `Centro`; filtro: especialidade inexistente naquela localização | 1 a 2 idem CT-LO-09 | Nenhum card é listado e a mensagem de ausência de resultados é exibida; o termo digitado e o filtro selecionado permanecem visíveis, permitindo ao usuário identificar a causa |
| CT-LO-11 | RSC-06 | Regra R6 | Home carregada | Campo de busca vazio; filtro: `Italiana` | 1. Selecionar o filtro "Italiana" sem digitar termo | Somente restaurantes de especialidade "Italiana" são exibidos |

---

## Tarefa 4: Relação entre funcionalidade, risco, técnica e casos de teste

| Funcionalidade | Requisito de qualidade (Atividade 1) | Risco | Prioridade | Técnica | Casos de teste |
|---|---|---|---|---|---|
| Criar conta | O cadastro deve impedir a criação de conta inválida ou duplicada e informar o motivo no mesmo idioma da interface, junto ao campo correspondente | RSC-01 | P1 | Partição de equivalência | CT-EV-01 a CT-EV-06, CT-EV-09 |
| Criar conta | idem | RSC-02 | P1 | Análise de valor limite | CT-EV-07, CT-EV-08, CT-EV-09 |
| Criar conta | idem | RSC-03 | P2 | Exploratório guiado por checklist | CT-EV-10 (sobre as recusas de CT-EV-02 a CT-EV-07) |
| Pesquisar restaurantes | A pesquisa deve retornar apenas restaurantes cuja especialidade ou localização corresponda ao termo e informar explicitamente a ausência de resultados | RSC-04 | P1 | Partição de equivalência | CT-LO-01, CT-LO-02, CT-LO-06, CT-LO-07 |
| Pesquisar restaurantes | idem | RSC-05 | P2 | Partição de equivalência | CT-LO-03, CT-LO-04 |
| Pesquisar restaurantes | idem | RSC-06 | P3 | Tabela de decisão | CT-LO-05, CT-LO-08, CT-LO-09, CT-LO-10, CT-LO-11 |

**Como ler a cadeia:** a funcionalidade define o que o usuário precisa fazer; o requisito de qualidade da Atividade 1 define a condição que torna esse uso adequado; o risco descreve o que impediria essa condição de ser cumprida e quanto isso custaria; a técnica é escolhida pela natureza do risco — domínio de entrada amplo leva à partição de equivalência, regra com limite numérico leva à análise de valor limite, combinação de condições leva à tabela de decisão e atributo de usabilidade leva ao teste baseado em experiência; e os casos são a aplicação concreta da técnica sobre aquele risco. Nenhum caso deste documento existe sem um risco que o justifique, e nenhum risco ficou sem caso associado.

---

## Tarefa 5: Decisões gerais do plano de testes

### Objetivo

Verificar se as funcionalidades Criar conta e Pesquisar restaurantes do LocalEats atendem aos requisitos de qualidade formulados na Atividade 1, concentrando o esforço nos riscos de maior prioridade e produzindo evidência suficiente para apoiar a decisão de liberação descrita na matriz RACI da Atividade 2.

### Escopo

| Incluído | Excluído nesta etapa |
|---|---|
| Criar conta e Pesquisar restaurantes, testadas pela interface web, em nível de sistema e por técnicas de caixa-preta | Meus Favoritos, Meus Pedidos e avaliação de restaurantes |
| Verificação funcional e verificação de usabilidade das mensagens de erro do cadastro | Testes de desempenho, de carga e de segurança ofensiva |
| Execução manual com registro de evidência em captura de tela | Automação de testes, testes unitários e testes de compatibilidade entre navegadores e dispositivos móveis |

A exclusão de favoritos e pedidos é uma decisão de priorização, e não de irrelevância: são funcionalidades que dependem de conta criada e de restaurante localizado, ou seja, os dois fluxos incluídos neste plano são pré-condição delas.

### Base de teste

Requisitos de qualidade e evidências de exploração da Atividade 1; matriz de responsabilidades e definição de pronto da Atividade 2; comportamento observado na aplicação publicada.

### Ambiente e dados de teste

- **Ambiente:** aplicação publicada em https://local-eats-unisenac.vercel.app/, acessada por navegador desktop atualizado. Não existe ambiente de homologação separado, o que é registrado abaixo como risco do projeto de teste.
- **Massa de dados:** contas criadas com padrão de e-mail identificável (`<integrante>.qa<sequencial>@teste.com`), para que os registros gerados pelos testes sejam distinguíveis dos demais. Os restaurantes utilizados são os já existentes na base do ambiente.
- **Dependência de dados:** os casos CT-LO-01 a CT-LO-11 dependem do conteúdo cadastrado. Antes da execução, o conjunto de especialidades e localizações disponíveis é conferido e registrado, e os termos dos casos são ajustados caso algum valor não exista mais.

### Abordagem

Teste baseado em risco. Os casos associados a riscos P1 são executados sempre e primeiro; os P2 são executados na sequência; os P3 são executados por amostragem quando o tempo permitir. Cada caso é executado uma vez por ciclo, e os casos afetados por uma correção são reexecutados após a nova versão ser publicada.

### Critérios de entrada

- Funcionalidades implantadas e ambiente acessível.
- Casos de teste revisados por um integrante diferente de quem os elaborou, conforme a regra de revisão independente estabelecida na Atividade 2.
- Massa de dados conferida.

### Critérios de saída

- 100% dos casos ligados a riscos P1 executados, com resultado registrado.
- Nenhum defeito de severidade alta em aberto nas funcionalidades em escopo.
- Todos os defeitos encontrados registrados com passos de reprodução e evidência.
- Ao menos 80% dos casos ligados a riscos P2 executados.

### Critérios de suspensão e retomada

A execução é suspensa se a aplicação ficar indisponível ou se um defeito bloqueante impedir a criação de conta, já que parte dos casos depende de usuário autenticado. A execução é retomada após a publicação da correção, reexecutando o caso que originou a suspensão e os casos que dependiam dele.

### Responsabilidades

Mantidas conforme a matriz RACI da Atividade 2: o QA responde pelo planejamento, pela execução dos testes de sistema e pelo acompanhamento dos defeitos até o fechamento; o desenvolvedor corrige os defeitos priorizados; o responsável pelo produto prioriza as correções e aprova a liberação; o DevOps executa a publicação. Neste plano, cada integrante executa os casos da funcionalidade sob sua responsabilidade, e a revisão dos casos é feita pelo outro integrante.

### Registro de defeitos e evidências

Cada defeito é registrado com identificador, caso de teste de origem, passos de reprodução, resultado esperado, resultado obtido, severidade e captura de tela. As evidências seguem o padrão de nomenclatura já adotado no repositório na Atividade 1 — `evidencias/<integrante>-<caso>-<situacao>.png` — para que a rastreabilidade entre documento e evidência permaneça direta.

### Riscos do projeto de teste

| Risco do projeto | Mitigação adotada |
|---|---|
| O ambiente é compartilhado e não há função de exclusão de conta, então cada execução deixa dados residuais | Usar e-mails sequenciais identificáveis e nunca reutilizar o mesmo e-mail entre execuções, exceto no caso que exige duplicidade |
| Não existe ambiente de homologação separado do ambiente publicado | Restringir os testes a operações que não alterem dados de outros usuários e concentrar a criação de dados no fluxo de cadastro |
| A base de restaurantes pode ser alterada entre ciclos, invalidando os dados esperados | Conferir e registrar o conjunto de especialidades e localizações no início de cada ciclo |
| O tempo de teste disponível pode ser reduzido | Critério de repriorização definido abaixo |

### Critério de repriorização se o tempo for reduzido

Mantêm-se os casos ligados a RSC-01, RSC-02 e RSC-04, que são os riscos P1: CT-EV-01, CT-EV-03, CT-EV-07, CT-EV-08, CT-EV-09, CT-LO-01, CT-LO-02 e CT-LO-06. São suspensos primeiro os casos P3 da tabela de decisão (CT-LO-08, CT-LO-10 e CT-LO-11) e, em seguida, os casos P2 de variação de escrita (CT-LO-03 e CT-LO-04). O checklist de usabilidade CT-EV-10 não é descartado, porque é executado sobre recusas que os casos P1 já produzem e tem custo adicional próximo de zero.

### Pontos em aberto a confirmar com o responsável pelo produto

1. **Regra de correspondência da busca:** o requisito não define se o termo deve casar o valor completo da especialidade ou da localização, ou se fragmentos também devem retornar resultados. Enquanto a regra não for decidida, o caso CT-LO-06 verifica apenas a condição mínima — que nenhum resultado sem relação com o termo seja exibido — e o comportamento observado é registrado para subsidiar a decisão.
2. **Valor exato do tamanho mínimo da senha:** a regra utilizada ("mais de três caracteres") vem da exploração da Atividade 1 e não de uma especificação escrita. Ao ser confirmada ou alterada, apenas a tabela de valor limite e os casos CT-EV-07 e CT-EV-08 precisam ser revisados.

---

## Uso de inteligência artificial

**Ferramenta utilizada:**
Claude (Anthropic).

**Como foi utilizada:**
Apoio na estruturação da análise de riscos da Tarefa 1, na redação da justificativa das técnicas da Tarefa 2, na organização das tabelas de casos de teste da Tarefa 3 e na consolidação das decisões do plano de testes da Tarefa 5.

**Como as respostas foram verificadas:**
O grupo revisou cada trecho antes de incorporá-lo ao documento. Os riscos foram confrontados com as evidências já produzidas na Atividade 1, os dados de teste da busca foram conferidos contra as especialidades e localizações efetivamente cadastradas na aplicação, e as afirmações que não podiam ser sustentadas pela interface ou pelos artefatos anteriores foram removidas ou registradas como ponto em aberto.
