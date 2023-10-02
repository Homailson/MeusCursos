

def acessar_senha_admin():
    return "1234"

def deixar_seguro(funcao):
    def funcao_seguranca():
        if usuario['nivel_de_acesso'] == "admin":
            return funcao()
        else:
            return f"O usuário {usuario['nome']} não é administrador"
        
    return funcao_seguranca


acessar_senha_admin = deixar_seguro(acessar_senha_admin)

usuario = {"nome": "João", "nivel_de_acesso": "convidado"}

print(acessar_senha_admin())
