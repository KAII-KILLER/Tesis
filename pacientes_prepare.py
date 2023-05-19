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

input_file = "/home/leonardo/Documents/Tesis/pacientes_clean2.csv"
output_file = "/home/leonardo/Documents/Tesis/pacientes_clean2.csv"

# Lista de números asignados aleatoriamente
lista_numeros = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17
]

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


# Función para reemplazar nulos, espacios en blanco o strings con números aleatorios de la lista
def replace_with_random(value):
    if pd.isna(value) or value == "":
        return random.choice(lista_numeros)
    else:
        return int(value)


# Aplicar la función a la columna especificada
print(df[2])
df["provincia_id"] = df["provincia_id"].apply(replace_with_random)

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


valores_unicos = df['edad'].unique()
print(valores_unicos)


# Factores
factores = {
    'a': 2.5 / 1000,
    'b': 1.5 / 1000,
    'c': 1 / 1000,
    'd': 0.75 / 100,
    'e': 4 / 100000,
    'f': 7.5 / 100,
    'g': 1.5 / 100,
    'h': 6.5 / 100 
}

# Sumar todos los factores
total = sum(factores.values())

# Calcular el porcentaje que representa cada factor del total
porcentajes = {grupo: factor / total for grupo, factor in factores.items()}

# Número de pacientes
pacientes = 8911

# Distribuir a los pacientes entre los grupos
distribucion = {grupo: round(pacientes * porcentaje) for grupo, porcentaje in porcentajes.items()}

print(distribucion)

# Crear una lista con los factores repetidos el número de veces correspondiente
factores_pacientes = [factor for factor, count in distribucion.items() for _ in range(count)]

# Asegurarte de que la lista tenga la longitud correcta (puede que no sea exacta debido al redondeo)
factores_pacientes = factores_pacientes[:len(df)]
print(len(factores_pacientes))
# Mezclar la lista
random.shuffle(factores_pacientes)

# Añadir la lista al DataFrame como una nueva columna
df['diagnostico'] = factores_pacientes

# Convertir la columna "fecha" a tipo datetime
df['fecha2'] = pd.to_datetime(df['registro'])
# Obtener el listado de años
anios = np.sort(df['fecha2'].dt.year.unique())
print(anios)
conteo_atenciones = df['fecha2'].dt.year.value_counts()
print(conteo_atenciones)


# Convertir la columna de registro a datetime
df['registro'] = pd.to_datetime(df['registro'], errors='coerce')

# Crear una función para generar una fecha aleatoria entre el 1/1/2013 y el 1/5/2023
def generar_fecha():
    inicio = datetime(2013, 1, 1)
    fin = datetime(2023, 5, 1)
    return inicio + (fin - inicio) * random.random()

# Reemplazar las fechas anteriores a 2013 y los espacios en blanco (NaN) con fechas aleatorias entre 1/1/2013 y 1/5/2023
df.loc[df['registro'].isna() | (df['registro'] < '2013-01-01'), 'registro'] = df.loc[df['registro'].isna() | (df['registro'] < '2013-01-01'), 'registro'].apply(lambda x: generar_fecha())


df['acido_folico'] = [1 if random.random() <= 0.4 else 0 for _ in range(len(df))]
df['toxoplasmosis'] = [1 if random.random() <= 0.2 else 0 for _ in range(len(df))]
df['rubeola_citomegalovirus'] = [1 if random.random() <= 0.7 else 0 for _ in range(len(df))]
df['herpes_simple'] = [1 if random.random() <= 0.5 else 0 for _ in range(len(df))]
df['VIH'] = [1 if random.random() <= 0.2 else 0 for _ in range(len(df))]
df['sangrado'] = [1 if random.random() <= 0.5 else 0 for _ in range(len(df))]
df['amenaza_parto_prematuro'] = [1 if random.random() <= 0.7 else 0 for _ in range(len(df))]
df['vomito_embarazo'] = [1 if random.random() >= 0.2 else 0 for _ in range(len(df))]
df['medicacion_embarazo'] = [1 if random.random() <= 0.5 else 0 for _ in range(len(df))]
df['infecciones'] = [1 if random.random() <= 0.6 else 0 for _ in range(len(df))]
df['hipertension_arterial'] = [1 if random.random() <= 0.65 else 0 for _ in range(len(df))]
df['diabetes_gestacional'] = [1 if random.random() <= 0.4 else 0 for _ in range(len(df))]
df['preeclampsia'] = [1 if random.random() >= 0.2 else 0 for _ in range(len(df))]
df['requiere_reanimacion'] = [1 if random.random() <= 0.8 else 0 for _ in range(len(df))]
df['ictericia'] = [1 if random.random() <= 0.5 else 0 for _ in range(len(df))]
df['hipoglicemia'] = [1 if random.random() <= 0.5 else 0 for _ in range(len(df))]
df['oxigenoterapia'] = [1 if random.random() <= 0.5 else 0 for _ in range(len(df))]
df['hospitalizacion'] = [1 if random.random() <= 0.5 else 0 for _ in range(len(df))]
df['apgar1'] = [random.randint(1, 10) for _ in range(len(df))]
df['apgar5'] = [random.randint(1, 10) for _ in range(len(df))]
df['vomito_embarazo'] = [1 if random.random() >= 0.2 else 0 for _ in range(len(df))]

print(df['apgar1'].value_counts())

df.columns
