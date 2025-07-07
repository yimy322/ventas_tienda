# 📊 Análisis de Datos de Ventas en una Tienda

Este proyecto consiste en un programa en Python diseñado para analizar un conjunto de datos de ventas en una tienda. Utiliza bibliotecas como `pandas` y `numpy`, así como programación orientada a objetos, para ofrecer estadísticas relevantes y filtrado de información.

---

## 🛒 Descripción

El programa trabaja con un archivo CSV que contiene los registros de las ventas. Cada registro representa una venta de producto con la siguiente estructura:

- `ID`: Identificador único del producto
- `Producto`: Nombre del producto
- `Categoría`: Categoría del producto (Ej: Lácteos, Aseo, etc.)
- `Fecha`: Fecha de venta
- `Precio`: Precio por unidad
- `Unidades Vendidas`: Cantidad de unidades vendidas

---

## ⚙️ Funcionalidades

✅ Cargar los datos desde un archivo CSV simulado  
✅ Filtrar las ventas por **fecha** o **categoría de producto**  
✅ Calcular estadísticas como:
- Total de ventas
- Promedio de ventas
- Desviación estándar  
✅ Generar resúmenes por categoría o producto  
✅ Uso de Programación Orientada a Objetos mediante una clase `Producto`

---

## 📁 Estructura del Proyecto

ventas_tienda/
├── data/
│ └── ventas.csv # Archivo CSV simulado con los datos
├── main.py # Script principal del análisis
├── producto.py # Clase Producto
├── funciones.py # Funciones auxiliares
└── README.md # Este archivo


