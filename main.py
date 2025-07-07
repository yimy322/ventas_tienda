from utils import cargar_datos, filtrar_por_categoria, filtrar_por_fecha, estadisticas_generales
from resumen import generar_resumen
from ventana import seleccionar_archivo

def main():
    #pasamos la ruta del archivo
    ruta = seleccionar_archivo()
    #devuelve el dataframe y la lista de productos
    df, lista_productos = cargar_datos(ruta)

    #muestra las estadisticas generales
    stats = estadisticas_generales(lista_productos)
    generar_resumen(stats)

    #filtrar por categoria
    categoria = input("Ingresa la categoria para filtrar: ")
    df_categoria = filtrar_por_categoria(df, categoria)
    if df_categoria.empty:
        print(f"No se encontraron ventas de la categoria: {categoria}.")
    else:
        print(f"\nVentas en la categoria '{categoria}':")
        print(df_categoria)

    #filtrar por fecha
    fecha = input("Ingresa la fecha que deseas filtrar (formato YYYY-MM-DD): ")
    df_fecha = filtrar_por_fecha(df, fecha)
    if df_fecha.empty:
        print(f"No se encontraron ventas para la fecha {fecha}.")
    else:
        print(f"\nVentas registradas en la fecha {fecha}:")
        print(df_fecha)

#para que se ejecute el metodo solo cuando se corre este archivo
if __name__ == "__main__":
    main()
