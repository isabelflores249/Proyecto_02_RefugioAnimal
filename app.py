import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from shiny import App, render, ui

# ---- 1. Cargar dataset ----
df = pd.read_csv(r"C:\Users\ESTUDIANTE\Downloads\refugio.csv")

# ---- 2. Definir primera página (gráfica y tabla) ----
page1 = ui.navset_card_underline(
    ui.nav_panel("Gráfico", ui.output_plot("hist")),
    ui.nav_panel("Tabla", ui.output_data_frame("data")),
    footer=ui.input_select(
        "var", 
        "Selecciona variable:", 
        choices=["Animal Type", "Sex upon Outcome", "Outcome Type"]
    ),
    title="Datos del Austin Animal Center"
)

# ---- 3. Estructura general de la app ----
app_ui = ui.page_navbar(
    ui.nav_spacer(),  # Empuja los paneles hacia la derecha
    ui.nav_panel("Análisis", page1),
    ui.nav_panel("Acerca de", "Aplicación Shiny con datos del refugio de animales."),
    title="Refugio de Animales 🐶🐱"
)

# ---- 4. Servidor ----
def server(input, output, session):
    @render.plot
    def hist():
        p = sns.countplot(data=df, x=input.var(), color="#007bc2", edgecolor="white")
        p.set(title=f"Distribución por {input.var()}", xlabel=input.var(), ylabel="Cantidad")
        plt.xticks(rotation=45)
        return p

    @render.data_frame
    def data():
        return df[[input.var()]].head(20)

# ---- 5. Crear app ----
app = App(app_ui, server)
