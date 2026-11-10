"""Page Object da tela de acesso do LocalEats (static/login.html)."""

URL_LOCALEATS = "https://local-eats-unisenac.vercel.app/"


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.titulo = page.get_by_text("Bem-vindo ao app de Qualidade de Software")
        self.aba_entrar = page.locator("#showLoginBtn")
        self.aba_criar_conta = page.get_by_role("button", name="Criar Conta")
        self.formulario_login = page.locator("#loginForm")
        self.formulario_cadastro = page.locator("#registerForm")
        self.campo_email_login = page.get_by_placeholder("teste@teste.com")
        self.botao_entrar = self.formulario_login.get_by_role("button", name="Entrar")
        self.campo_nome = page.get_by_placeholder("Seu nome")
        self.botao_registrar = page.get_by_role("button", name="Registrar")
        self.mensagem_erro = page.locator("#errorMsg")

    def acessar(self):
        self.page.goto(URL_LOCALEATS)

    def abrir_criar_conta(self):
        self.aba_criar_conta.click()

    def abrir_entrar(self):
        self.aba_entrar.click()

    def enviar_login(self):
        self.botao_entrar.click()
