#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:24:43 2023

@author: leonardo
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

input_file = "/home/leonardo/Documents/Tesis/atenciones.csv"
output_file = "/home/leonardo/Documents/Tesis/atenciones_clean.csv"

df = pd.read_csv(input_file)
df.head()
print(df.columns)
df.replace("?", np.nan, inplace=True)

missing_data = df.isnull()
missing_data.head(5)
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# Función para reemplazar nulos con fechas aleatorias entre 2006 y 2022
def replace_with_random1(value):
    if pd.isna(value) or value == "":
        start_date = datetime(2006, 1, 1)
        end_date = datetime(2022, 12, 31)
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        return random_date.strftime('%Y-%m-%d')
    else:
        return value

# Aplicar la función a la columna "Nacimiento"
df["fecha"] = df["nacimiento"].apply(replace_with_random1)

lista_numeros = []
# Función para reemplazar nulos con fechas aleatorias entre 2006 y 2022
def replace_with_random2(value):
    if pd.isna(value):
        return int(random.choice(lista_numeros))
    else:
        return value
df["edad"] = df["edad"].apply(replace_with_random2)



listado = {
    1: "Azuay",
    2: "Bolivar",
    3: "Cañar",
    4: "Carchi",
    5: "Chimborazo",
    6: "Cotopaxi",
    7: "El Oro",
    8: "Esmeraldas",
    9: "Galapagos",
    10: "Guayas",
    11: "Imbabura",
    12: "Loja",
    13: "Los Rios",
    14: "Manabi",
    15: "Morona Santiago",
    16: "Napo",
    17: "Orellana",
    18: "Pastaza",
    19: "Pichincha",
    20: "Santa Elena",
    21: "Santo Domingo De Los Tsachilas",
    22: "Sucumbios",
    23: "Tungurahua",
    24: "Zamora Chinchipe",
}

# Definir los valores posibles
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# Definir los posibles valores para provincia_id
province_ids = list(range(1, 25))

# Generar pesos aleatorios y normalizar para que sumen 1
weights = np.random.random(len(province_ids))
weights /= weights.sum()

# Función para reemplazar los valores de provincia_id con un valor aleatorio de la lista
def replace_with_random(value):
    return random.choices(province_ids, weights)[0]

# Aplicar la función a la columna provincia_id
df['provincia_id'] = df['provincia_id'].apply(replace_with_random)
df["provincia"] = df["provincia_id"].map(listado)
df.to_csv(output_file, index=False)

# Obtener el número de filas
num_filas = df.shape[0]
print(num_filas)

now = datetime.now()
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')   # Convertir la columna "Nacimiento" a formato de fecha
df['edad'] = (now - df['fecha']).astype('<m8[Y]')

df.head()

valores_unicos = df['edad'].unique()

print(valores_unicos)
