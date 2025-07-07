import pandas as pd
from producto import Producto
import numpy as np

#pasamos la ruta del archivo
def cargar_datos(ruta_csv):
    #tendra el csv
    df = pd.read_csv(ruta_csv)
    #inicializamos una lista
    lista_productos = []
    #iteramos
    for indice, fila in df.iterrows():
        producto = Producto(fila['ID'], fila['Producto'], fila['Categoria'],
                            fila['Fecha'], fila['Precio'], fila['Unidades Vendidas'])
        #anadimos a la lista
        lista_productos.append(producto)
    #retornamos el dataframe y la lista
    return df, lista_productos

#devuelve las filas segun la categoria puesta
def filtrar_por_categoria(df, categoria):
    return df[df['Categoria'] == categoria]

#devuelve las filas segun la fecha puesta
def filtrar_por_fecha(df, fecha):
    return df[df['Fecha'] == fecha]

def estadisticas_generales(lista_productos):
    #inicializamos una lista
    ventas = []
    #iteramos
    for p in lista_productos:
        ventas.append(p.total_venta())#acumulamos el total
    #retorna un diccionario
    return {
        'total_ventas': sum(ventas),
        'promedio_venta': np.mean(ventas),
        'desviacion_estandar': np.std(ventas)
    }
