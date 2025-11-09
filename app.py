

from shiny import App, render, ui
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Users\ESTUDIANTE\Downloads\wter-evkm_version_57907.csv")


df.columns = df.columns.str.lower()
df["animal_type"] = df["animal_type"].fillna("Desconocido")


def convertir_edad(valor):
    
    if type(valor) == str:
        partes = valor.lower().split()
        try:
            numero = float(partes[0])
        except:
            return None
        unidad = partes[1] if len(partes) > 1 else ""
        if "year" in unidad:
            return numero
        elif "month" in unidad:
            return numero / 12
        elif "week" in unidad:
            return numero / 52
        elif "day" in unidad:
            return numero / 365
    return None

df["age_years"] = df["age_upon_intake"].apply(convertir_edad)


df["sterilized"] = df["sex_upon_intake"].apply(
    lambda x: "Esterilizado" if "spayed" in str(x).lower() or "neutered" in str(x).lower()
    else "No esterilizado"
)


age_series = df["age_years"].dropna()
max_age = int(age_series.max()) if not age_series.empty else 1


app_ui = ui.page_navbar(
    ui.nav_panel(
        "Gráficos",
        ui.layout_sidebar(
            ui.sidebar(
                ui.h3("Filtros"),
                ui.input_select(
                    "animal",
                    "Selecciona tipo de animal:",
                    choices=["Todos"] + sorted(df["animal_type"].dropna().unique().tolist())
                ),
                ui.input_slider(
                    "edad",
                    "Filtrar por edad (años):",
                    min=0,
                    max=max_age,
                    value=(0, max_age)
                ),
                ui.input_select(
                    "grafico",
                    "Selecciona tipo de gráfico:",
                    choices=[
                        "Tipo de Animal",
                        "Edad por Tipo",
                        "Esterilización"
                    ]
                )
            ),
            ui.output_plot("plot"),
            ui.output_text("descripcion")
        )
    ),
    ui.nav_panel(
        "Descripción",
        ui.markdown("""
        ### Dashboard de Datos del Refugio
        Esta aplicación muestra información sobre los animales del refugio:
        - Qué tipo de animales ingresan con mayor frecuencia.
        - La distribución de edades por tipo de animal.
        - La proporción de animales esterilizados y no esterilizados.
        """)
    ),
    title="Refugio de Animales"
)


def server(input, output, session):
    @output
    @render.plot
    def plot():
        
        d = df.copy()
        if input.animal() != "Todos":
            d = d[d["animal_type"] == input.animal()]
        d = d[(d["age_years"].notna()) &
              (d["age_years"] >= input.edad()[0]) &
              (d["age_years"] <= input.edad()[1])]

        tipo = input.grafico()
        fig, ax = plt.subplots(figsize=(7, 5))

        # Gráfico 1: Tipo de Animal (barras)
        if tipo == "Tipo de Animal":
            sns.countplot(data=d, x="animal_type", palette="Set2", ax=ax)
            ax.set_title("Frecuencia de animales ingresados")
            ax.set_xlabel("Tipo de animal")
            ax.set_ylabel("Cantidad")

        # Gráfico 2: Edad por Tipo (boxplot)
        elif tipo == "Edad por Tipo":
            sns.boxplot(data=d, x="animal_type", y="age_years", palette="Set3", ax=ax)
            ax.set_title("Distribución de edades por tipo de animal")
            ax.set_xlabel("Tipo de animal")
            ax.set_ylabel("Edad (años)")

        #Gráfico 3: Esterilización (pastel)
        elif tipo == "Esterilización":
            conteo = d["sterilized"].value_counts()
            colores = ["#66c2a5", "#fc8d62"]
            ax.pie(conteo, labels=conteo.index, autopct='%1.1f%%', colors=colores)
            ax.set_title("Proporción de animales esterilizados")

        plt.tight_layout()
        return fig

    @output
    @render.text
    def descripcion():
        tipo = input.grafico()
        if tipo == "Tipo de Animal":
            return "Muestra los tipos de animales que ingresan con mayor frecuencia al refugio."
        elif tipo == "Edad por Tipo":
            return "Visualiza cómo varía la edad de los animales según su tipo."
        elif tipo == "Esterilización":
            return "Muestra la proporción de animales esterilizados frente a los no esterilizados."
        else:
            return "Selecciona un gráfico para ver los resultados."


app = App(app_ui, server)
