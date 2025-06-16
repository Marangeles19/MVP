from controller import CalculadoraController
from view import CalculadoraView

if __name__ == "__main__":
    view = CalculadoraView(None)
    controller = CalculadoraController(view)
    view.controller = controller
    view.iniciar()
