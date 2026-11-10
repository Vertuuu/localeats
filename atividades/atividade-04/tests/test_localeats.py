import re

from playwright.sync_api import expect

from pages.login_page import LoginPage


# Responsável: Éverton Lopes
def test_alternar_para_criar_conta_exibe_formulario_de_cadastro(page):
    login = LoginPage(page)
    login.acessar()

    login.abrir_criar_conta()

    expect(login.formulario_cadastro).to_be_visible()
    expect(login.campo_nome).to_be_visible()
    expect(login.botao_registrar).to_be_visible()
    expect(login.formulario_login).to_be_hidden()
    expect(login.aba_criar_conta).to_have_class(re.compile(r"\bactive\b"))
    expect(login.aba_entrar).not_to_have_class(re.compile(r"\bactive\b"))


# Responsável: Lorenzo Maciel
def test_entrar_sem_preencher_campos_mantem_usuario_no_login(page):
    login = LoginPage(page)
    login.acessar()
    # Sem sessão, a página inicial redireciona para a tela de acesso.
    expect(page).to_have_url(re.compile(r"/static/login\.html$"))
    expect(login.titulo).to_be_visible()

    login.enviar_login()

    # A validação nativa do navegador bloqueia o envio do formulário vazio.
    assert login.campo_email_login.evaluate("campo => campo.validity.valueMissing") is True
    expect(page).to_have_url(re.compile(r"/static/login\.html$"))
    expect(login.mensagem_erro).to_be_hidden()
    expect(login.formulario_login).to_be_visible()
