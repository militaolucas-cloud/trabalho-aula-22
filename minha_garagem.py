from veiculo import Veiculo, Carro, Moto

# Crie pelo menos 3 veículos (dados inventados por você)
v1 = Carro("Toyota", "Corolla", 2022, 4)
v2 = Moto("Honda", "CG 160", 2021, 160)
v3 = Carro("Ford", "Fiesta", 2018, 4)

garagem = [v1, v2, v3]

# Percorrer e imprimir
for v in garagem:
    print(v.descrever())

# Contar quantos são carros e motos
carros = [v for v in garagem if isinstance(v, Carro)]
motos = [v for v in garagem if isinstance(v, Moto)]

print(f"Carros: {len(carros)} | Motos: {len(motos)}")