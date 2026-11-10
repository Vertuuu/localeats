# Atividade 4: Testes Automatizados do LocalEats

**Unidade Curricular:** Qualidade de Software
**Projeto:** LocalEats — https://local-eats-unisenac.vercel.app/
**Modalidade:** Dupla

**Integrantes:**

- Éverton Lopes
- Lorenzo Maciel

---

## Estrutura

```
atividade-04/
├── atividade-04-testes-automatizados.md
├── relatorio-pytest.txt
├── requirements.txt
├── pytest.ini
├── pages/
│   ├── __init__.py
│   └── login_page.py          # Page Object da tela de acesso
├── src/
│   ├── __init__.py
│   └── regras_localeats.py
└── tests/
    ├── __init__.py
    ├── test_regras_localeats.py
    └── test_localeats.py
```

### Como executar

Dentro de `atividades/atividade-04`, no PowerShell:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

O `pytest.ini` já define o navegador (Chromium) e guarda screenshot e trace do Playwright em `evidencias/test-results/` quando um teste funcional falha.

---

## Identificação das responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Éverton Lopes | Unitário | Pedido acima do valor mínimo é aceito | `tests/test_regras_localeats.py::test_pedido_acima_do_minimo_e_aceito` |
| TU02 | Éverton Lopes | Unitário | Limite do valor mínimo (R$ 29,99, R$ 30,00 e R$ 30,01) | `tests/test_regras_localeats.py::test_pedido_no_limite_do_valor_minimo` |
| TU03 | Éverton Lopes | Unitário | Valor negativo gera `ValueError` | `tests/test_regras_localeats.py::test_pedido_com_valor_negativo_gera_erro` |
| TU04 | Lorenzo Maciel | Unitário | Quantidade dentro do intervalo é válida | `tests/test_regras_localeats.py::test_quantidade_dentro_do_intervalo_e_valida` |
| TU05 | Lorenzo Maciel | Unitário | Limites do intervalo (0, 1, 10 e 11) | `tests/test_regras_localeats.py::test_quantidade_nos_limites_do_intervalo` |
| TU06 | Lorenzo Maciel | Unitário | Quantidade negativa gera `ValueError` | `tests/test_regras_localeats.py::test_quantidade_negativa_gera_erro` |
| TF01 | Éverton Lopes | Funcional | Alternar para "Criar Conta" exibe o formulário de cadastro e oculta o de login | `tests/test_localeats.py::test_alternar_para_criar_conta_exibe_formulario_de_cadastro` |
| TF02 | Lorenzo Maciel | Funcional | Acesso sem sessão leva à tela de login, e "Entrar" com campos vazios não sai dela | `tests/test_localeats.py::test_entrar_sem_preencher_campos_mantem_usuario_no_login` |

TU02 e TU05 são parametrizados com `pytest.mark.parametrize` e aparecem no relatório como um item por valor de limite (13 itens coletados no total).

---

## Parte 1: Testes unitários e TDD

As duas funções estão em `src/regras_localeats.py`. Os limites ficam em constantes (`VALOR_MINIMO_PEDIDO`, `QUANTIDADE_MINIMA_ITENS`, `QUANTIDADE_MAXIMA_ITENS`) para que a regra seja lida no código sem número solto.

### TDD de Éverton Lopes

**Regra escolhida:** Regra 1 — `pedido_atingiu_valor_minimo(valor_pedido)`.

**Primeiro teste escrito:** `test_pedido_acima_do_minimo_e_aceito`, verificando que um pedido de R$ 50,00 retorna `True`.

**Por que o teste falhou inicialmente:** a função ainda não existia. O pytest interrompeu a coleta com `ImportError: cannot import name 'pedido_atingiu_valor_minimo' from 'src.regras_localeats'`.

**Implementação mínima realizada:** uma função que apenas retornava `True`, suficiente para o primeiro teste passar.

**Segundo teste escrito:** `test_pedido_no_limite_do_valor_minimo`, começando com R$ 29,99 esperando `False`. Ele falhou com `assert True is False`, porque a implementação mínima aceitava qualquer valor. Depois o teste foi parametrizado para cobrir também o valor exato de R$ 30,00 e R$ 30,01.

**Melhoria ou refatoração realizada:** a função passou a comparar com a constante `VALOR_MINIMO_PEDIDO` (`>=`, para que R$ 30,00 seja aceito) e a lançar `ValueError` para valor negativo, verificado pelo terceiro teste com `pytest.raises`.

### TDD de Lorenzo Maciel

**Regra escolhida:** Regra 3 — `quantidade_itens_valida(quantidade)`.

**Primeiro teste escrito:** `test_quantidade_dentro_do_intervalo_e_valida`, verificando que 3 itens retornam `True`.

**Por que o teste falhou inicialmente:** a função não existia, e a coleta parou com `ImportError: cannot import name 'quantidade_itens_valida' from 'src.regras_localeats'`.

**Implementação mínima realizada:** uma função que retornava sempre `True`.

**Segundo teste escrito:** `test_quantidade_nos_limites_do_intervalo`, parametrizado com 0, 1, 10 e 11. Os casos `zero` e `acima-do-limite` falharam, pois a implementação mínima aceitava tudo. Os casos 1 e 10 já passavam, o que mostrou que eles sozinhos não bastariam para forçar a regra.

**Melhoria ou refatoração realizada:** a regra foi implementada como `QUANTIDADE_MINIMA_ITENS <= quantidade <= QUANTIDADE_MAXIMA_ITENS`, com `ValueError` para quantidade negativa, verificado por `test_quantidade_negativa_gera_erro`. Antes dessa verificação, -1 teria sido tratado como `False`, sem distinguir quantidade zero de entrada inválida.

---

## Parte 2: Testes funcionais com Playwright

### Exploração do sistema

Ao acessar o endereço do LocalEats sem sessão, a aplicação redireciona para `/static/login.html`, com o texto "Bem-vindo ao app de Qualidade de Software" e duas abas: **Entrar** e **Criar Conta**. As demais telas (Explorar, Meus Favoritos, Meus Pedidos) só ficam acessíveis com usuário autenticado.

Os testes funcionais foram escritos sobre essa tela para não depender de credenciais no repositório e para não criar contas novas no ambiente compartilhado da turma a cada execução. Os locators usam os textos e placeholders exibidos na interface (`get_by_role("button", name="Criar Conta")`, `get_by_placeholder("Seu nome")`, `get_by_text(...)`), e os ids apenas onde o texto se repete, como o botão "Entrar", que existe na aba e no formulário.

A tela é encapsulada no Page Object `pages/login_page.py`, e os testes descrevem só a ação e o resultado esperado.

Nenhum teste usa `time.sleep`. As assertions com `expect` do Playwright aguardam automaticamente o estado esperado, até o tempo limite.

### TF01 — Éverton Lopes

Acessa o LocalEats, clica na aba **Criar Conta** e verifica que:

- o formulário de cadastro, o campo "Seu nome" e o botão "Registrar" ficam visíveis;
- o formulário de login fica oculto;
- a aba "Criar Conta" recebe a classe `active` e a aba "Entrar" deixa de tê-la.

### TF02 — Lorenzo Maciel

Acessa o LocalEats sem sessão e verifica que:

- a URL passa a ser `/static/login.html` e o título de boas-vindas é exibido;
- ao clicar em **Entrar** com os campos vazios, o campo de e-mail fica com `validity.valueMissing` verdadeiro, ou seja, a validação nativa do navegador (`required`) bloqueou o envio;
- a URL continua na tela de login, a mensagem de erro da aplicação não aparece e o formulário de login segue visível.

---

## Diferenciais implementados

- Terceiro teste unitário por integrante (TU03 e TU06), para entrada negativa.
- `pytest.raises` para verificar as exceções.
- `pytest.mark.parametrize` nos testes de limite (TU02 e TU05).
- Page Object Model (`pages/login_page.py`).
- Screenshot e trace do Playwright gravados automaticamente quando um teste funcional falha (`--screenshot only-on-failure --tracing retain-on-failure`).

---

## Explicação individual

**Éverton Lopes — TU02 (`test_pedido_no_limite_do_valor_minimo`):** o defeito mais provável nessa regra é trocar `>=` por `>`, o que recusaria um pedido de exatamente R$ 30,00. Por isso o teste verifica os três pontos em torno do limite: um centavo abaixo, o valor exato e um centavo acima. Se alguém trocar o operador, o caso `exatamente-o-minimo` falha e aponta o problema direto no nome do caso.

**Lorenzo Maciel — TF02 (`test_entrar_sem_preencher_campos_mantem_usuario_no_login`):** o teste confirma duas proteções da tela de acesso. A primeira é que, sem sessão, a página inicial leva ao login. A segunda é que o formulário vazio não chega a ser enviado. Para isso o teste não depende só de "nada mudou na tela": ele lê `validity.valueMissing` do campo de e-mail, que mostra que o bloqueio veio da validação do navegador, e confirma que a mensagem de erro da aplicação continua oculta, o que indica que nenhuma requisição de login foi tratada.

---

## Relatório da execução

O arquivo [relatorio-pytest.txt](./relatorio-pytest.txt) foi gerado com:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

Resultado: 13 itens coletados e 13 aprovados (TU01 a TU06, contando cada valor parametrizado, e TF01 e TF02 no Chromium).

---

## Uso de inteligência artificial

**Ferramenta utilizada:**
Claude (Anthropic), pelo Claude Code.

**Como a ferramenta foi utilizada:**
Apoio na exploração da tela de acesso do LocalEats, na escrita das funções e com o ciclo do TDD, na criação do Page Object e na redação deste documento.

**Uma sugestão que precisou ser alterada ou rejeitada:**
A primeira ideia para os testes funcionais era automatizar o cadastro e a pesquisa de restaurantes. Ela foi rejeitada porque o cadastro criaria uma conta nova no ambiente compartilhado da turma a cada execução, e a pesquisa exigiria guardar credenciais no repositório. Os testes ficaram na tela de acesso, que é estável e pública. Também foi removida uma linha de assertion sem efeito que tinha ficado no TF02 na primeira versão.

**Como o código sugerido foi verificado:**
Cada etapa do TDD foi executada com o pytest, e a falha de cada primeiro teste foi conferida antes da implementação. Os textos, placeholders e ids usados nos locators foram conferidos na própria página do LocalEats. A suíte completa foi executada e o relatório confere com a tabela de responsabilidades.
