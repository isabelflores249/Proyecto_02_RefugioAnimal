#Nombre del archivo: app_animales_interactiva.py

#Establecemos los paquetes a utilizar:

import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, ui, render, reactive

# Interfaz (ui)

app_ui = ui.page_fluid(
    ui.h2("Desarrollo de la Aplicación Shiny en Python"), #Aqui estamos haciendo que lea el archivo csv que deseamos que lea.

    ui.help_text(
        "Descripcion: Suba un archivo (.csv) y elija el tipo de gráfico que quiere visualizar."
    ),

    ui.layout_sidebar(
        ui.sidebar(
            ui.input_file("file1", "Archivo (.csv)", multiple=False, accept=[".csv"]),
            ui.input_select("var1", "Variable 1", choices=[]),
            ui.input_select("var2", "Variable 2", choices=[]),
            ui.input_radio_buttons(
                "tipo_grafico",
                "Tipo de gráfico",
                choices=[
                    "Histograma",
                    "Gráfico de barras comparativas",
                    "Gráfico de pie"
                ],
                selected="Histograma"
            ),
        ),
        ui.output_plot("grafico")
    )
)

# Servidor 

def server(input, output, session):


    @reactive.Calc #Queremos que el reactivo lea el .csv
    def df():
        file = input.file1()
        if file is None:
            return None
        try:
            return pd.read_csv(file[0]["datapath"])
        except Exception as e:
            print("Error al leer el CSV:", e)
            return None

    
    @reactive.effect
    @reactive.event(input.file1) # El efecto en este caso debe ser actualizar opciones de variables para cuando carguemos el .csv
    def actualizar_selectores():
        data = df()
        if data is not None:
            columnas = data.columns.tolist()
            columnas_categoricas = [
                c for c in columnas if data[c].dtype == "object" or data[c].nunique() < 20
            ]
            ui.update_select("var1", choices=columnas_categoricas)
            ui.update_select("var2", choices=["(ninguna)"] + columnas_categoricas)

    
    @output
    @render.plot
    def grafico():
        data = df() # Esta parte es la encargada de cargar los graficos que queremos usar: Histograma, Grafico comparativo (de barras) y grafico de pie.
        if data is None:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, "Subí un archivo CSV para comenzar.", ha="center", va="center")
            ax.axis("off")
            return fig

        var1 = input.var1()
        var2 = input.var2()
        tipo = input.tipo_grafico()

        fig, ax = plt.subplots(figsize=(8, 5))

        try:
#1. Histograma
            if tipo == "Histograma" and var1:
                conteo = data[var1].value_counts().sort_index()
                ax.bar(conteo.index, conteo.values, color="skyblue", edgecolor="black")
                ax.set_title(f"Frecuencia de {var1}")
                ax.set_xlabel(var1)
                ax.set_ylabel("Conteo")
                plt.xticks(rotation=45, ha="right")

#2. Grafico de barras comparativas
            elif tipo == "Grafico de barras comparativas" and var1 and var2 and var2 != "(ninguna)":
                tabla = pd.crosstab(data[var1], data[var2])
                tabla.plot(kind="bar", ax=ax, stacked=False, edgecolor="black")
                ax.set_title(f"{var1} vs {var2}")
                ax.set_xlabel(var1)
                ax.set_ylabel("Conteo")
                plt.xticks(rotation=45, ha="right")
                ax.legend(title=var2)

#3. Gráfico de pie
            elif tipo == "Gráfico de pie" and var1:
                conteo = data[var1].value_counts().head(10)
                ax.pie(
                    conteo.values,
                    labels=conteo.index,
                    autopct="%1.1f%%",
                    startangle=90,
                    colors=plt.cm.Paired.colors
                )
                ax.set_title(f"Distribución de {var1}")
                ax.axis("equal")

            else:
                ax.text(0.5, 0.5, "Seleccione variables válidas", ha="center", va="center")

        except Exception as e:
            ax.clear()
            ax.text(0.5, 0.5, f"Error: {e}", ha="center", va="center")

        plt.tight_layout()
        return fig

app = App(app_ui, server)