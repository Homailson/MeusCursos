# O método estático em Python é utilizado quando você precisa de uma função associada a uma classe,
# mas que não precisa acessar ou modificar atributos da instância. Em outras palavras, ele não depende
# do estado da instância, apenas da classe em si.

class Veiculo:

    quantidade_veiculos = 0

    def __init__(self, tipo, modelo, marca, numero_passageiros, tipo_de_combustivel):
        self.modelo = modelo
        self.marca = marca
        self.numero_passageiros = numero_passageiros
        self.tipo_combustivel = tipo_de_combustivel
        self.tipo = tipo
        Veiculo.quantidade_veiculos += 1

    def __repr__(self) -> str:
        return f"<Veículo: {self.tipo}, {self.modelo}, {self.marca}, {self.numero_passageiros}, {self.tipo_combustivel}>"
    

    @staticmethod
    def total_veiculos():
        return Veiculo.quantidade_veiculos




carro1 = Veiculo("moto", "XR", "honda","2", "gasolina")
carro2 = Veiculo("moto", "CG", "honda","2", "gasolina")


print(carro1)
print(carro2)
print(Veiculo.total_veiculos())

