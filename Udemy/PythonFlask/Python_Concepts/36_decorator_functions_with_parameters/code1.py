import functools

def deixar_seguro(funcao):
    @functools.wraps(funcao)
    def funcao_seguranca(*args, **kwargs):
        if usuario['nivel_de_acesso'] == "admin":
            return funcao(*args, **kwargs)
        else:
            return f"O usuário {usuario['nome']} não é administrador"
        
    return funcao_seguranca


@deixar_seguro
def acessar_senha(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

usuario = {"nome": "João", "nivel_de_acesso": "admin"}

print(acessar_senha("billing"))