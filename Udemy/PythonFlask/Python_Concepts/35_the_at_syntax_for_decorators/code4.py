import functools

def deixar_seguro(funcao):
    @functools.wraps(funcao)
    def funcao_seguranca():
        if usuario['nivel_de_acesso'] == "admin":
            return funcao()
        else:
            return f"O usuário {usuario['nome']} não é administrador"
        
    return funcao_seguranca


@deixar_seguro
def acessar_senha_admin():
    return "1234"


usuario = {"nome": "João", "nivel_de_acesso": "admin"}

print(acessar_senha_admin.__name__)