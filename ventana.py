import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    #creamos la ventana
    ventana = tk.Tk()
    ventana.withdraw()#con esto oculta la ventana para que solo muestre el dialog

    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[("Archivos CSV", "*.csv")]
    )
    ventana.destroy()#cerramos la ventana 
    return archivo
