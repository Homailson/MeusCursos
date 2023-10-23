# Desevolvimento em Flask

## Criação de ambiente virtual e instalação

1- Tenha Python instalado na sua máquina

2- Entre na pasta do seu projeto pelo terminal e entre com:

```
    python -m venv venv
```

3- Ative seu ambiente virtual no mesmo diretório:

```
    .\venv\Scripts\activate
```

**Caso esteja com problemas de permissão para ativar o ambiente virtual no seu windows faça:**


```
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```


**No mesmo diretório e tente ativar novamente**

**Quando terminar de trabalhar no seu projeto, você pode desativar o ambiente virtual **


```
    deactivate
```

4- Instale o Flask no seu ambiente virtual:


```
    pip install flask
```

5- Em seu arquivo app.py, dentro do seu diretório raíz do projeto, importe o framework Flask:


```
    from flask import Flask
```

6- No seu arquivo app.py, coloque o seguinte código


```
    #Criando uma nova aplicação Flask
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello, world!"
```


7- Para rodar sua primeira aplicação flask temos que definir algumas variáveis de ambiente
**No windows ficará assim, usando powershell:**


```
    $env:FLASK_APP = "app.py"
```


**Depois assim:**


```
    $env:FLASK_DEBUG=1
```

8- Agora, basta apenas rodar o Flask:
    
    
```
    flask run
```