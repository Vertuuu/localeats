# Atividade 2: Organização da Qualidade no LocalEats

**Unidade Curricular:** Qualidade de Software
**Metodologia:** Problem-Based Learning (PBL)
**Projeto:** LocalEats — https://local-eats-unisenac.vercel.app/
**Elemento de Competência:** EC2 — Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

**Integrantes:**

- Éverton Lopes
- Lorenzo Maciel

---

## Tarefa 1: Diagnóstico da situação

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Não existe um critério compartilhado para considerar uma funcionalidade pronta. Cada integrante entrega no ponto que julga suficiente | Funcionalidades são dadas como concluídas sem verificação equivalente entre si, o que faz defeitos chegarem ao usuário e gera retrabalho já com a versão publicada. A equipe também perde a previsibilidade das entregas, porque "pronto" significa coisas diferentes a cada item |
| A qualidade é tratada como atribuição exclusiva do QA, e parte da equipe entende que somente ele deve testar | O teste se concentra no fim do fluxo e transforma o QA em gargalo. Defeitos de requisito e de implementação só aparecem quando a correção é mais cara, e o desenvolvedor deixa de verificar o próprio trabalho porque presume que alguém verificará depois |
| Defeitos são encontrados, mas não há registro nem acompanhamento padronizado, e algumas atividades não possuem responsável definido, inclusive a aprovação da disponibilização de uma nova versão | Sem registro, o mesmo defeito reaparece e não há histórico para priorizar correções ou justificar decisões. Sem responsável definido, atividades ficam duplicadas ou órfãs, e a publicação de uma versão passa a depender de acordo informal, o que dilui a responsabilidade quando algo falha em produção |

### A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA?

Não. O QA concentra a competência em técnicas de teste e em avaliação da qualidade, mas não tem como compensar sozinho decisões tomadas antes dele. Um critério de aceitação mal definido nasce no refinamento, um erro de validação nasce na implementação e uma versão publicada sem verificação nasce no processo de liberação. Se a responsabilidade for exclusiva do QA, ele vira um ponto único de verificação no fim do fluxo, encarece a correção e ainda assim não impede o defeito de existir. A qualidade é construída por todos os papéis ao longo do desenvolvimento, e o QA atua para tornar essa construção observável e verificável.

---

## Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Éverton Lopes | QA (analista de qualidade) | Participar do refinamento propondo cenários de teste antes da implementação; planejar e executar os testes do sistema; registrar defeitos com evidência e passos de reprodução; acompanhar o defeito até o fechamento; verificar se os critérios de aceitação foram atendidos antes da liberação; manter e evoluir a automação de testes | Técnicas de projeto de teste (partição de equivalência, valor limite, teste exploratório); escrita de casos de teste e de critérios verificáveis; automação de testes funcionais e de interface; leitura de logs e de requisições para isolar a causa do defeito; noções de API e de banco de dados; modelo de qualidade do produto da ISO/IEC 25010 | Comunicação objetiva ao reportar defeito, descrevendo o comportamento sem atribuir culpa; pensamento crítico para questionar requisito ambíguo ainda no refinamento; colaboração com o desenvolvedor na reprodução do problema; organização para manter o registro atualizado; capacidade de sustentar tecnicamente uma recomendação de não liberar |
| Éverton Lopes | DevOps | Manter o pipeline que executa build, testes automatizados e publicação; garantir a separação e a equivalência entre os ambientes; executar a disponibilização da versão aprovada; assegurar a possibilidade de retorno a uma versão anterior; manter monitoramento e logs que permitam detectar falha em produção | Versionamento e estratégia de branches; configuração de pipeline de integração e entrega contínua; automação de build e de publicação; gestão de configuração e de credenciais; monitoramento, coleta de logs e métricas de disponibilidade; procedimento de retorno de versão | Disciplina de processo para não abrir exceção na publicação; atenção a risco e antecipação de impacto; comunicação rápida e clara durante incidente; disponibilidade para apoiar os demais papéis na configuração de ambiente |
| Lorenzo Maciel | Responsável pelo produto | Definir e comunicar os critérios de aceitação de cada funcionalidade; representar a necessidade do usuário nas decisões de escopo; priorizar a correção dos defeitos frente às novas funcionalidades; decidir sobre a disponibilização da versão com base no que foi verificado | Escrita de histórias e de critérios de aceitação verificáveis; técnicas de priorização considerando valor e risco; leitura de indicadores de uso e de defeitos; compreensão do domínio de pedidos e restaurantes do LocalEats; noções de qualidade em uso para avaliar o impacto de um defeito no usuário | Decisão sob incerteza e disposição para assumir a responsabilidade pela liberação; comunicação com pessoas de perfis diferentes; foco no usuário ao avaliar um defeito; capacidade de recusar escopo quando a verificação não foi concluída |
| Lorenzo Maciel | Desenvolvedor | Implementar a funcionalidade conforme os critérios de aceitação acordados; escrever e manter os testes unitários do código que produz; revisar o código de outro desenvolvedor; corrigir os defeitos priorizados; sinalizar risco técnico e ambiguidade de requisito ainda no refinamento | Linguagem e framework utilizados na aplicação; escrita de testes unitários e uso de dublês de teste; tratamento de erro e validação de entrada, tanto no cliente quanto no servidor; boas práticas de revisão de código; noções de segurança aplicáveis a autenticação e sessão | Receber crítica em revisão de código sem tratá-la como julgamento pessoal; atenção a detalhe na verificação do próprio trabalho antes de submetê-lo; transparência ao comunicar impedimento ou atraso; colaboração com o QA na reprodução e no fechamento do defeito |

> **Sobre certificações:** certificações como a CTFL do ISTQB podem ser úteis para nivelar o vocabulário de teste dentro da equipe e apoiar o desenvolvimento profissional, mas não substituem a experiência prática no produto nem devem ser exigidas como condição para o exercício dos papéis descritos acima.

---

## Tarefa 3: Matriz de responsabilidades

**R** — Responsável (executa) · **A** — Aprovador (responde pelo resultado) · **C** — Consultado · **I** — Informado

| Atividade de qualidade | Responsável pelo Produto | Desenvolvedor | QA | DevOps |
|---|---|---|---|---|
| Definir critérios de aceitação | R, A | C | R | I |
| Revisar requisitos | A | R | R | C |
| Implementar a funcionalidade | I | R, A | C | I |
| Revisar o código | I | R, A | C | C |
| Criar testes unitários | I | R, A | C | I |
| Planejar e executar testes do sistema | C | C | R, A | I |
| Registrar e acompanhar defeitos | C | R | R, A | R |
| Priorizar a correção dos defeitos | R, A | C | C | I |
| Aprovar a disponibilização da versão | A | I | C | R |

Observações sobre a distribuição:

- O registro de defeito é R para três papéis porque qualquer integrante que encontre um problema deve registrá-lo. O acompanhamento até o fechamento permanece com o QA, que responde pelo resultado.
- A aprovação da versão ficou com o responsável pelo produto, e a execução da publicação com o DevOps. Isso separa quem decide de quem opera e responde ao ponto do contexto em que não estava claro quem pode aprovar a disponibilização.

### Lacuna ou conflito encontrado

O desenvolvedor aparece como R e A simultaneamente em três atividades consecutivas: implementar a funcionalidade, revisar o código e criar testes unitários. Nas duas últimas isso configura um conflito, porque quem produz o código é também quem aprova a verificação do próprio código. A revisão perde a função de controle independente e passa a depender apenas da disciplina individual, exatamente o cenário em que funcionalidades chegam ao usuário com defeitos.

Enquanto a equipe não tiver uma liderança técnica, a correção possível é normativa: a revisão deve ser executada obrigatoriamente por um desenvolvedor diferente do autor, e nenhuma alteração pode ser aprovada por quem a escreveu. Essa regra precisa estar registrada na definição de pronto, e não depender de combinação informal.

### Práticas recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Definição de pronto acordada pela equipe, aplicada a toda funcionalidade antes de ser considerada concluída: critérios de aceitação verificados, testes unitários escritos para o código novo, revisão de código realizada por um desenvolvedor diferente do autor, defeitos encontrados registrados na ferramenta e nenhum defeito de severidade alta em aberto | Ausência de critério compartilhado para considerar uma funcionalidade pronta; conflito da revisão de código aprovada pelo próprio autor; defeitos identificados sem registro | Responsável pelo Produto, Desenvolvedor, QA, DevOps |
| Refinamento com as três visões antes do início do desenvolvimento, em que responsável pelo produto, desenvolvedor e QA discutem a mesma funcionalidade e o QA apresenta os cenários alternativos e os casos inválidos que pretende verificar, ainda na especificação | Concentração da qualidade no QA e no fim do fluxo; requisitos ambíguos que só aparecem como defeito depois da implementação; custo alto de correção tardia | Responsável pelo Produto, Desenvolvedor, QA |

---

## Uso de inteligência artificial

**Ferramenta utilizada:**
Claude (Anthropic).

**Como foi utilizada:**
Apoio na redação do diagnóstico da Tarefa 1, na descrição das responsabilidades e competências dos papéis da Tarefa 2 e na montagem inicial da matriz RACI e das práticas recomendadas da Tarefa 3.

**Como as respostas foram verificadas:**
O grupo revisou cada trecho gerado antes de incorporá-lo ao documento. A matriz foi conferida linha a linha contra as regras da atividade, verificando que toda atividade possui ao menos um R e um único A, e a distribuição foi ajustada ao tamanho e à realidade da equipe do LocalEats.
