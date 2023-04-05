"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime

def clean_data():

    dataframe = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    dataframe.drop_duplicates(inplace = True)
    dataframe.dropna(axis=0, inplace=True)
    
    for column in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']: 
        dataframe[column] = dataframe[column].apply(lambda x: x.lower())
    for character in ['_', '-']:
        for column in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
            dataframe[column] = dataframe[column].apply(lambda x: x.replace(character, ' '))

    dataframe['monto_del_credito'] = dataframe['monto_del_credito'].apply(lambda x: re.sub("\$[\s*]", "", x))
    dataframe['monto_del_credito'] = dataframe['monto_del_credito'].apply(lambda x: re.sub(",", "", x))
    dataframe['monto_del_credito'] = dataframe['monto_del_credito'].apply(lambda x: re.sub("\.00", "", x))
    dataframe['monto_del_credito'] = dataframe['monto_del_credito'].apply(int)
    dataframe['comuna_ciudadano'] = dataframe['comuna_ciudadano'].apply(float)
    dataframe['fecha_de_beneficio'] = dataframe['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))

    dataframe.dropna(axis=0,inplace=True)
    dataframe.drop_duplicates(inplace = True)

    return dataframe