import functools



def deixar_seguro(nivel_de_acesso):
    def decorador(funcao):
        @functools.wraps(funcao)
        def funcao_seguranca(*args, **kwargs):
            if usuario['nivel_de_acesso'] == nivel_de_acesso:
                return funcao(*args, **kwargs)
            else:
                return f"O usuário {usuario['nome']} não possui acesso do {nivel_de_acesso}"
            
        return funcao_seguranca
    return decorador

@deixar_seguro("admin")
def acessar_senha_admin():
    return "admin: 1234"

@deixar_seguro("convidado")
def acessar_senha_dashboard():
    return "user: user_password"


usuario = {"nome": "João", "nivel_de_acesso": "admin"}

print(acessar_senha_admin())
print(acessar_senha_dashboard())