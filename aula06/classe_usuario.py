class Usuario :
    def __init__ (self, nome_usuario, senha, nivel_acesso):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.nivel_acesso = nivel_acesso

    def login (self,nome_usuario, senha):
        if self.nome_usuario == nome_usuario and self.senha == senha:
            print ("Você está Logado\n Seja Bem Vindo")
        else:
            print ("Nome de usuário ou senha Incorretos")

    def alterar_senha (self, nome_usuario , nova_senha):
        if self.nome_usuario == nome_usuario:
            self.senha = nova_senha
            print ("Senha Alterada")
        else:
            print ("Usuário Inexistente")

def logout (self):
    nome_usuario = ""
    senha = ""
    nivel_acesso = ""
    print ("Você Saiu Do Sistema")
