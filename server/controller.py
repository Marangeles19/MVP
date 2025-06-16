from model import CalculadoraModel

class CalculadoraController:
    def __init__(self, view):
        self.view = view
        self.model = CalculadoraModel()

    def sumar(self, a, b):
        try:
            a = float(a)
            b = float(b)
            resultado = self.model.sumar(a, b)
            self.view.mostrar_resultado(resultado)
        except ValueError:
            self.view.mostrar_resultado("Error: ingresa números válidos")
