from shiny import App, ui, render, reactive
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#ruta csv
CSV_PATH = r"C:/Users/Usuario/OneDrive - Universidad de Costa Rica/Bach Estadistica/IV Ciclo/XS0130 Programacion para estadistica II/Materia/proyecto 2/Austin_Animal_Center_Intakes.csv"

if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"CSV no encontrado en: {CSV_PATH}")

# Carga del dataset
df = pd.read_csv(CSV_PATH, low_memory=False)
# Normalizar nombres de columnas
df.columns = [c.strip() for c in df.columns]

# Informaciones útiles
print("Pandas version:", pd.__version__)
print("Columnas disponibles:", df.columns.tolist()[:50])
print("Filas:", len(df))
