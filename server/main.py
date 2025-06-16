from presenter import CalculadoraPresenter
from view import CalculadoraView

if __name__ == "__main__":
    view = CalculadoraView(None)
    presenter = CalculadoraPresenter(view)
    view.presenter = presenter
    view.iniciar()
