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

```plaintext
ventas_tienda/
├── data/
│   └── data.csv            # Archivo CSV simulado con los datos
├── main.py                 # Script principal del análisis
├── producto.py             # Clase Producto
└── README.md               # Este archivo
├── resumen.py              # Módulo para mostrar resumen de estadísticas
├── utils.py                # Funciones auxiliares
└── ventana.py              # Archivo que se usa para abrir el cuadro de dialogo para seleccionar el csv
```
---

## 📝 Instrucciones

## 🚀 Pasos para ejecutar el programa
Abrir la terminal o consola en la carpeta donde está el archivo main.py.

### 1. Ejecutar el archivo main.py 
### 2. Seleccionar el archivo CSV cuando aparezca el cuadro de diálogo.
    .Se abrirá una ventana para que selecciones el archivo.
    .✅ Verás el resumen de ventas en la consola, una vez cargado el archivo.
### 3. Filtrar los resultados por categoría y fecha:
    .Se te pedira que ingreses una categoría (por ejemplo: Lacteos).
    .Luego, deberas ingresar una fecha en el siguiente formato: YYYY-MM-DD
    Por ejemplo: 2025-07-01
### 4. El programa mostrara las ventas filtradas según los criterios ingresados.



