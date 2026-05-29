"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    ruta_archivo = 'files/input/solicitudes_de_credito.csv'
    df = pd.read_csv(ruta_archivo, sep=';')

    # Limpiar el DataFrame
    df.drop(['Unnamed: 0'], axis=1, inplace=True)  
    df.dropna(inplace=True)  # Eliminar filas con valores nulos.
    df.drop_duplicates(inplace=True)  # Eliminar filas duplicadas.

    # Corregir la columna 'fecha_de_beneficio'
    df[['día', 'mes', 'año']] = df['fecha_de_beneficio'].str.split('/', expand=True)  # Dividir 'fecha_de_beneficio' en tres columnas.
    df.loc[df['año'].str.len() < 4, ['día', 'año']] = df.loc[df['año'].str.len() < 4, ['año', 'día']].values  # Reordenar si el año tiene menos de 4 dígitos.
    df['fecha_de_beneficio'] = df['año'] + '-' + df['mes'] + '-' + df['día']  # Reconstruir la fecha en formato 'YYYY-MM-DD'.
    df.drop(['día', 'mes', 'año'], axis=1, inplace=True)  # Eliminar las columnas auxiliares.

     # Limpiar las columnas de texto
    columnas_objeto = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito']  # Columnas de texto que necesitan limpieza.
    df[columnas_objeto] = df[columnas_objeto].apply(lambda x: x.str.lower().replace(['-', '_'], ' ', regex=True).str.strip())  # Convertir a minúsculas, reemplazar caracteres y quitar espacios extra.
    df['barrio'] = df['barrio'].str.lower().replace(['-', '_'], ' ', regex=True)  # Limpiar la columna 'barrio'.

    # Limpiar la columna 'monto_del_credito'
    df['monto_del_credito'] = df['monto_del_credito'].str.replace("[$, ]", "", regex=True).str.strip()  # Eliminar caracteres no numéricos.
    df['monto_del_credito'] = pd.to_numeric(df['monto_del_credito'], errors='coerce')  # Convertir a tipo numérico, manejando errores como NaN.
    df['monto_del_credito'] = df['monto_del_credito'].fillna(0).astype(int)  # Rellenar NaN con 0 y convertir a entero.
    df['monto_del_credito'] = df['monto_del_credito'].astype(str).str.replace('.00', '')  # Convertir nuevamente a texto y eliminar '.00'.

    # Eliminar duplicados después de las transformaciones.
    df.drop_duplicates(inplace=True)

    # Crear el directorio de salida si no existe
    directorio_salida = 'files/output'  # Directorio donde se guardará el archivo limpio.
    os.makedirs(directorio_salida, exist_ok=True)  # Crear la carpeta si no existe.

    # Guardar los datos limpios en un nuevo archivo CSV
    ruta_salida = f'{directorio_salida}/solicitudes_de_credito.csv'
    df.to_csv(ruta_salida, sep=';', index=False)  # Guardar el DataFrame limpio en formato CSV.

    return df.head()