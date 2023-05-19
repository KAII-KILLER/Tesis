import pandas as pd
import random

# Nombre de archivo de entrada y salida
input_file = '/home/leonardo/Documents/Tesis/pacientes_filtrados.csv'
output_file = '/home/leonardo/Documents/Tesis/pacientes_clean.csv'

# Nombre de la columna que queremos procesar
column_name = 'provincia_id'

# Lista de números asignados aleatoriamente
random_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24]

# Leer archivo CSV
dtypes = {column_name: pd.Int64Dtype()}
df = pd.read_csv(input_file, dtype=dtypes, na_values='')

# Función para reemplazar nulos, espacios en blanco o strings con números aleatorios de la lista
def replace_with_random(value):
    if pd.isna(value) or value == '"':
        return random.choice(random_numbers)
    else:
        return int(value)

# Aplicar la función a la columna especificada
df[column_name] = df[column_name].apply(replace_with_random)

# Guardar el resultado en un nuevo archivo CSV
df.to_csv(output_file, index=False)

print(str(19.0).isdigit())
