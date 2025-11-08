
from shiny import App, render, ui, reactive
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# --- 2. Cargar y preparar los datos ---
df = pd.read_csv(r"C:\Users\ESTUDIANTE\Downloads\wter-evkm_version_57907.csv")

# Normalizar nombres de columnas y valores básicos
df.columns = df.columns.str.lower()
df["animal_type"] = df["animal_type"].fillna("Desconocido")

# Convertir edad en años (si existe la columna "age_upon_intake")
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

# Crear columna de esterilización
df["sterilized"] = df["sex_upon_intake"].apply(
    lambda x: "Esterilizado" if isinstance(x, str) and ("spayed" in x.lower() or "neutered" in x.lower())
    else "No esterilizado"
)

# Calcular máximo de edad para el slider (manejo cuando no hay datos)
age_series = df["age_years"].dropna()
max_age = int(age_series.max()) if not age_series.empty else 1

# --- 3. Interfaz (UI) ---
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Dashboard",
        ui.layout_sidebar(
            ui.sidebar(
                ui.h3("Filtros 🐾"),
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
        "About",
        ui.markdown("""
        ###  Dashboard de Datos
        Panel interactivo para visualizar:
        - Qué tipo de animales ingresan con mayor frecuencia.
        - La distribución de edades según tipo de animal.
        - Proporción de animales esterilizados vs no esterilizados.
        """)
    ),
    title="Refugio de Animales"
)

# --- 4. Servidor ---
def server(input, output, session):
    @reactive.Calc
    def data_filtrada():
        d = df.copy()
        # Filtrar por tipo de animal
        if input.animal() != "Todos":
            d = d[d["animal_type"] == input.animal()]
        # Filtrar por rango de edad (si hay age_years)
        d = d[(d["age_years"].notna()) & (d["age_years"] >= input.edad()[0]) & (d["age_years"] <= input.edad()[1])]
        return d

    @output
    @render.plot
    def plot():
        d = data_filtrada()
        fig, ax = plt.subplots(figsize=(8, 5))
        tipo = input.grafico()

        if tipo == "Tipo de Animal":
            sns.countplot(data=d, x="animal_type", palette="Set2", ax=ax)
            ax.set_title("Frecuencia de animales ingresados")
            ax.set_xlabel("Tipo de animal")
            ax.set_ylabel("Cantidad")

        elif tipo == "Edad por Tipo":
            sns.boxplot(data=d, x="animal_type", y="age_years", palette="Set3", ax=ax)
            ax.set_title("Distribución de edades por tipo de animal")
            ax.set_xlabel("Tipo de animal")
            ax.set_ylabel("Edad (años)")

        elif tipo == "Esterilización":
            # Usar conteos por esterilización (y opcional hue por animal_type)
            sns.countplot(data=d, x="sterilized", hue="animal_type", palette="Set1", ax=ax)
            ax.set_title("Esterilización: conteo por especie")
            ax.set_xlabel("Esterilización")
            ax.set_ylabel("Cantidad")
            ax.legend(title="Tipo")

        fig.tight_layout()
        return fig

    @output
    @render.text
    def descripcion():
        tipo = input.grafico()
        if tipo == "Tipo de Animal":
            return "Muestra los tipos de animales que ingresan con mayor frecuencia al centro."
        elif tipo == "Edad por Tipo":
            return "Visualiza cómo varía la edad de los animales según su tipo."
        elif tipo == "Esterilización":
            return "Compara la proporción de animales esterilizados y no esterilizados por especie."
        else:
            return "Selecciona un gráfico para ver los resultados."

# --- 5. Crear la app ---
app = App(app_ui, server)


