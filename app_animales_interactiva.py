#paquetes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shiny import App, ui, render, reactive

plt.style.use("_mpl-gallery")
# ui
app_ui = ui.page_fluid(
    ui.h2("Desarrollo de la Aplicación Shiny en Python"),

    ui.layout_sidebar(
        ui.sidebar(
            ui.input_file("file1", "Subir archivo CSV", multiple=False, accept=[".csv"]), #Como la importancia de la aplicacion de Shiny para python es que se puedan visualizar las variables de los CSVs en 4 tipos de graficos diferentes 
                                                                                          #(no es de suma importancia que el Dataset a utilizar sea el escogido por los participantes del proyecto), decidimos en que el usuario ingrese el archivo que desee visualizar, 
            ui.input_select("var_x", "Variable X", choices=[]),                           #igualmente para facilitar al usuario sobre no tener que establecer la ubicacion del archivo en su propia computadora en el .py file y en la consola para cuando quiera visualizar el Shiny.
            ui.input_select("var_y", "Variable Y", choices=[]),

            ui.input_radio_buttons(
                "tipo",
                "Tipo de gráfico",
                choices=[
                    "Histograma",
                    "Gráfico de dispersión",
                    "Diagrama de caja",
                    "Gráfico de Pie",
                ],
                selected="Histograma"
            ),
        ),
        ui.output_plot("grafico")
    )
)

#server
def server(input, output, session):

    
    @reactive.calc #Primera parte donde leemos el .csv
    def df():
        file = input.file1()
        if file is None:
            return None

        try:
            return pd.read_csv(file[0]["datapath"])
        except Exception as e:
            print("Error al leer CSV:", e)
            return None

    
    @reactive.Effect
    @reactive.event(input.file1)
    def actualizar_selectores():
        data = df()
        if data is not None:
            columnas = data.columns.tolist()

            num_cols = [c for c in columnas if np.issubdtype(data[c].dtype, np.number)]
            cat_cols = [c for c in columnas if data[c].dtype == "object"]

            ui.update_select("var_x", choices=columnas)
            ui.update_select("var_y", choices=["(ninguna)"] + columnas)

    
    # Graficos
    
    @output
    @render.plot
    def grafico():
        data = df()

        if data is None:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, "Suba un archivo .CSV", ha="center", va="center")
            ax.axis("off")
            return fig

        var_x = input.var_x()
        var_y = input.var_y()
        tipo = input.tipo()

        fig, ax = plt.subplots(figsize=(6, 4))

        try:

            
            # Histograma
            
            if tipo == "Histograma":
                x = data[var_x].dropna()

                ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")
                ax.set_title(f"Histograma de {var_x}")

            
            # Gráfico de dispersión
            
            elif tipo == "Gráfico de dispersión" and var_y != "(ninguna)":
                x = data[var_x].dropna()
                y = data[var_y].dropna()

                tamaños = np.random.uniform(15, 80, len(x))
                colores = np.random.uniform(15, 80, len(x))

                ax.scatter(x, y, s=tamaños, c=colores, vmin=0, vmax=100)
                ax.set_title(f"Gráfico de dispersión: {var_x} vs {var_y}")
                ax.set_xlabel(var_x)
                ax.set_ylabel(var_y)

            
            # Diagrama de caja
            
            elif tipo == "Diagrama de caja":
                valores = data[var_x].dropna()

                ax.boxplot([valores],
                           positions=[4],
                           widths=1.5,
                           patch_artist=True,
                           showmeans=False,
                           showfliers=False,
                           medianprops={"color": "white", "linewidth": 1},
                           boxprops={"facecolor": "C0", "edgecolor": "white"},
                           whiskerprops={"color": "C0"},
                           capprops={"color": "C0"}
                )
                ax.set_title(f"Gráfico de dispersión de {var_x}")
                ax.set_xticks([4])
                ax.set_xticklabels([var_x])

            
            # Gráfico de Pie
            
            elif tipo == "Gráfico de Pie":
                conteo = data[var_x].value_counts().head(8)
                colores = plt.get_cmap("Blues")(np.linspace(0.2, 0.7, len(conteo)))

                ax.pie(conteo.values,
                       labels=conteo.index,
                       colors=colores,
                       wedgeprops={"linewidth": 1, "edgecolor": "white"})
                ax.set_title(f"Gráfico de Pie: {var_x}")
                ax.axis("equal")

            else:
                ax.text(0.5, 0.5, "Seleccione variables", ha="center", va="center")

        except Exception as e:
            ax.clear()
            ax.text(0.5, 0.5, f"Error: {e}", ha="center", va="center")

        return fig


app = App(app_ui, server)
