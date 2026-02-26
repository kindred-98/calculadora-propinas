import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from .services import dividir_cuenta
from .utils import formatear_moneda

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class TipCalculatorGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Propina")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        self.dark_mode = False
        self.historial = []

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.configurar_estilos()
        self.crear_widgets()

    # ==========================
    # ESTILOS
    # ==========================

    def configurar_estilos(self):
        if self.dark_mode:
            bg = "#1e1e1e"
            fg = "white"
        else:
            bg = "white"
            fg = "black"

        self.root.configure(bg=bg)
        self.style.configure("TFrame", background=bg)
        self.style.configure("TLabel", background=bg, foreground=fg)
        self.style.configure("TRadiobutton", background=bg, foreground=fg)

    # ==========================
    # WIDGETS
    # ==========================

    def crear_widgets(self):

        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(main_frame,
                  text="💰 Calculadora de Propina",
                  font=("Segoe UI", 16, "bold")).pack(pady=10)

        # INPUTS
        ttk.Label(main_frame, text="Monto total:").pack(anchor="w")
        self.monto_entry = ttk.Entry(main_frame)
        self.monto_entry.pack(fill="x", pady=5)

        ttk.Label(main_frame, text="Tipo de propina:").pack(anchor="w")

        self.tipo_var = tk.StringVar(value="porcentaje")

        ttk.Radiobutton(main_frame, text="Porcentaje",
                        variable=self.tipo_var,
                        value="porcentaje").pack(anchor="w")

        ttk.Radiobutton(main_frame, text="Fija",
                        variable=self.tipo_var,
                        value="fija").pack(anchor="w")

        ttk.Label(main_frame, text="Valor:").pack(anchor="w")
        self.valor_entry = ttk.Entry(main_frame)
        self.valor_entry.pack(fill="x", pady=5)

        ttk.Label(main_frame, text="Número de personas:").pack(anchor="w")
        self.personas_entry = ttk.Entry(main_frame)
        self.personas_entry.pack(fill="x", pady=5)

        ttk.Button(main_frame,
                   text="Calcular",
                   command=self.calcular).pack(pady=10)

        # ==========================
        # HISTORIAL
        # ==========================

        ttk.Label(main_frame,
                  text="📜 Historial",
                  font=("Segoe UI", 12, "bold")).pack(pady=10)

        columnas = ("Monto", "Propina", "Total", "Por Persona")

        self.tree = ttk.Treeview(main_frame,
                                 columns=columnas,
                                 show="headings",
                                 height=6)

        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)

        self.tree.pack()

        # ==========================
        # GRÁFICO
        # ==========================

        self.fig, self.ax = plt.subplots(figsize=(4, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        self.canvas.get_tk_widget().pack(pady=10)

    # ==========================
    # FUNCIONES
    # ==========================

    def actualizar_grafico(self, monto, propina):

        self.ax.clear()

        valores = [monto, propina]
        etiquetas = ["Monto", "Propina"]

        self.ax.pie(valores,
                    labels=etiquetas,
                    autopct="%1.1f%%")

        self.ax.set_title("Distribución del Pago")

        self.canvas.draw()

    def calcular(self):
        try:
            monto = float(self.monto_entry.get())
            tipo = self.tipo_var.get()
            valor = float(self.valor_entry.get())
            personas = int(self.personas_entry.get())

            resultado = dividir_cuenta(monto, tipo, valor, personas)

            # Agregar a historial
            self.tree.insert("",
                             tk.END,
                             values=(
                                 formatear_moneda(monto),
                                 formatear_moneda(resultado["propina"]),
                                 formatear_moneda(resultado["total"]),
                                 formatear_moneda(resultado["por_persona"])
                             ))

            # Actualizar gráfico
            self.actualizar_grafico(monto, resultado["propina"])

        except Exception as e:
            messagebox.showerror("Error", str(e))