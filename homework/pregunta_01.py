"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    import os
    import numpy as np
    import pandas as pd

    def load_data():
        dataframe = pd.read_csv("./files/input/solicitudes_de_credito.csv", sep=";")
        return dataframe

    def clean_data(dataframe):
        dataframe = dataframe.copy()
        dataframe.dropna(inplace=True)

        dataframe = dataframe.drop(columns=["Unnamed: 0"])
        
        dataframe["sexo"] = dataframe["sexo"].str.lower()        
        dataframe["tipo_de_emprendimiento"] = dataframe["tipo_de_emprendimiento"].str.lower()
        dataframe["tipo_de_emprendimiento"] = dataframe["tipo_de_emprendimiento"].str.strip()
        dataframe["idea_negocio"] = dataframe["idea_negocio"].str.lower()
        dataframe["idea_negocio"] = dataframe["idea_negocio"].str.replace("_", " ")
        dataframe["idea_negocio"] = dataframe["idea_negocio"].str.replace("-", " ")
        dataframe["idea_negocio"] = dataframe["idea_negocio"].str.strip()
        dataframe["barrio"] = dataframe["barrio"].str.lower()
        dataframe["barrio"] = dataframe["barrio"].str.replace("-", " ")
        dataframe["barrio"] = dataframe["barrio"].str.replace("_", " ")
        dataframe["comuna_ciudadano"] = dataframe["comuna_ciudadano"].astype(int)
        dataframe["fecha_de_beneficio"] = pd.to_datetime(dataframe["fecha_de_beneficio"], dayfirst=True, errors='coerce', format='mixed')
        dataframe["monto_del_credito"] = dataframe["monto_del_credito"].str.strip()
        dataframe["monto_del_credito"] = dataframe["monto_del_credito"].str.replace(".00", "")
        dataframe["monto_del_credito"] = dataframe["monto_del_credito"].str.replace(",", "")
        dataframe["monto_del_credito"] = dataframe["monto_del_credito"].str.replace("$ ", "")
        dataframe["línea_credito"] = dataframe["línea_credito"].str.lower()
        dataframe["línea_credito"] = dataframe["línea_credito"].str.replace("_", " ")
        dataframe["línea_credito"] = dataframe["línea_credito"].str.replace("-", " ")

        dataframe.drop_duplicates(inplace=True)

        return dataframe
    
    def save_data(dataframe):
        if not os.path.exists("./files/output"):
            os.makedirs("./files/output")
    
        dataframe.to_csv(
        "./files/output/solicitudes_de_credito.csv",
        sep=";",
    )
    
    def main():
        dataframe = load_data()
        dataframe  = clean_data(dataframe)
        save_data(dataframe)

    return main()

if __name__ == '__main__':
    pregunta_01()
