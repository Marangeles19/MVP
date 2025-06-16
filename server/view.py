import tkinter as tk

class CalculadoraView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Calculadora MVP")
        self.root.geometry("300x200")

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Número 1:").grid(row=0, column=0, sticky="w")
        self.entry1 = tk.Entry(frame, width=20)
        self.entry1.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Número 2:").grid(row=1, column=0, sticky="w")
        self.entry2 = tk.Entry(frame, width=20)
        self.entry2.grid(row=1, column=1, pady=5)

        self.boton_sumar = tk.Button(frame, text="Sumar", command=self.on_sumar_clicked, width=20)
        self.boton_sumar.grid(row=2, column=0, columnspan=2, pady=10)

        self.resultado_label = tk.Label(frame, text="Resultado: ", fg="blue", font=("Arial", 12))
        self.resultado_label.grid(row=3, column=0, columnspan=2)

    def on_sumar_clicked(self):
        valor1 = self.entry1.get()
        valor2 = self.entry2.get()
        self.controller.sumar(valor1, valor2)

    def mostrar_resultado(self, resultado):
        self.resultado_label.config(text=f"Resultado: {resultado}")

    def iniciar(self):
        self.root.mainloop()
