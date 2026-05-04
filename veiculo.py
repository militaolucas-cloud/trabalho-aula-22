class Veiculo:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    def descrever(self):
        return f"{self._marca} {self._modelo} ({self._ano})"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self._num_portas = num_portas

    @property
    def num_portas(self):
        return self._num_portas

    def descrever(self):
        return f"{super().descrever()} - {self._num_portas} portas"


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self._cilindradas = cilindradas

    @property
    def cilindradas(self):
        return self._cilindradas

    def descrever(self):
        return f"{super().descrever()} - {self._cilindradas}cc"