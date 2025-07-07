def generar_resumen(estadisticas):
    print("\n=== Resumen de Ventas ===")
    print(f"Total Ventas: S/.{estadisticas['total_ventas']:.2f}")#formato de 2 decimales
    print(f"Promedio por venta: S/.{estadisticas['promedio_venta']:.2f}")
    print(f"Desviación estándar: S/.{estadisticas['desviacion_estandar']:.2f}")
