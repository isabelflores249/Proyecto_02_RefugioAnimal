
from shiny import App, render, ui
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Users\ESTUDIANTE\Downloads\wter-evkm_version_57907.csv")

df.columns = df.columns.str.lower()
df["animal_type"] = df["animal_type"].fillna("Desconocido")

def convertir_edad(valor):
    if isinstance(valor, str):
        partes = valor.lower().split()
        try:
            numero = float(partes[0])
        except Exception:
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
    lambda x: "Esterilizado" if isinstance(x, str) and ("spayed" in x.lower() or "neutered" in x.lower())
    else "No esterilizado"
)

max_age = int(df["age_years"].dropna().max()) if df["age_years"].notna().any() else 1


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
                    "edad", "Filtrar por edad (años):",
                    min=0, max=max_age, value=(0, max_age)
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
        "descripción",
        ui.markdown("""
        ### Dashboard de Datos
        Este panel muestra:
        - Qué tipo de animales ingresan con mayor frecuencia.
        - La distribución de edades según tipo de animal.
        - Proporción de animales esterilizados vs no esterilizados.
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

        d = d[(d["age_years"].notna()) & (d["age_years"] >= input.edad()[0]) & (d["age_years"] <= input.edad()[1])]

        plt.figure(figsize=(8, 5))
        tipo = input.grafico()

        if tipo == "Tipo de Animal":
            sns.countplot(data=d, x="animal_type", palette="Set2")
            plt.title("Frecuencia de animales ingresados")
            plt.xlabel("Tipo de animal")
            plt.ylabel("Cantidad")

        elif tipo == "Edad por Tipo":
            sns.boxplot(data=d, x="animal_type", y="age_years", palette="Set3")
            plt.title("Distribución de edades por tipo de animal")
            plt.xlabel("Tipo de animal")
            plt.ylabel("Edad (años)")

        elif tipo == "Esterilización":
            sns.countplot(data=d, x="sterilized", hue="animal_type", palette="Set1")
            plt.title("Esterilización por especie")
            plt.xlabel("Esterilización")
            plt.ylabel("Cantidad")

        plt.tight_layout()
        return plt.gcf()

    @output
    @render.text
    def descripcion():
        tipo = input.grafico()
        if tipo == "Tipo de Animal":
            return "Muestra los tipos de animales que ingresan con mayor frecuencia al centro."
        elif tipo == "Edad por Tipo":
            return "Visualiza cómo varía la edad según el tipo de animal."
        elif tipo == "Esterilización":
            return "Compara animales esterilizados y no esterilizados."
        else:
            return "Selecciona un gráfico para ver los resultados."


app = App(app_ui, server)
