import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("500x550")
    reg.resizable(False, False)
    reg.configure(bg="#722FA1")  # Fondo morado

    # -------------------------
    # TÍTULO
    # -------------------------
    titulo = tk.Label(
        reg,
        text="REGISTRO DE PRODUCTOS",
        font=("Times New Roman", 20, "bold"),
        bg="#722FA1",
        fg="white"
    )
    titulo.pack(pady=20)

    # -------------------------
    # FRAME PRINCIPAL
    # -------------------------
    frame = tk.Frame(reg, bg="#AD70D8", bd=0)
    frame.pack(padx=30, pady=10, fill="both", expand=True)

    # -------------------------
    # ESTILO
    # -------------------------
    estilo_label = {
        "font": ("Times New Roman", 13, "bold"),
        "bg": "#AD70D8",
        "fg": "white"
    }

    estilo_entry = {
        "font": ("Arial", 12),
        "width": 30,
        "bd": 2,
        "relief": "groove"
    }

    # -------------------------
    # ID PRODUCTO
    # -------------------------
    lbl_id = tk.Label(frame, text="ID del Producto", **estilo_label)
    lbl_id.pack(pady=(20, 5))

    txt_id = tk.Entry(frame, **estilo_entry)
    txt_id.pack(pady=5)

    # -------------------------
    # DESCRIPCIÓN
    # -------------------------
    lbl_desc = tk.Label(frame, text="Descripción", **estilo_label)
    lbl_desc.pack(pady=(15, 5))

    txt_desc = tk.Entry(frame, **estilo_entry)
    txt_desc.pack(pady=5)

    # -------------------------
    # PRECIO
    # -------------------------
    lbl_precio = tk.Label(frame, text="Precio", **estilo_label)
    lbl_precio.pack(pady=(15, 5))

    txt_precio = tk.Entry(frame, **estilo_entry)
    txt_precio.pack(pady=5)

    # -------------------------
    # CATEGORÍA
    # -------------------------
    lbl_categoria = tk.Label(frame, text="Categoría", **estilo_label)
    lbl_categoria.pack(pady=(15, 5))

    txt_categoria = tk.Entry(frame, **estilo_entry)
    txt_categoria.pack(pady=5)

    # -------------------------
    # FUNCIÓN GUARDAR
    # -------------------------
    def guardar_producto():
        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # Validar campos vacíos
        if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Por favor complete todos los campos."
            )
            return

        # Validar precio
        try:
            float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )
            return

        # Guardar archivo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{id_prod}|{descripcion}|{precio}|{categoria}\n")

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        # Limpiar campos
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    # -------------------------
    # BOTÓN GUARDAR
    # -------------------------
    btn_guardar = tk.Button(
        frame,
        text="Guardar Producto",
        command=guardar_producto,
        font=("Times New Roman", 13, "bold"),
        bg="#5289FF",
        fg="white",
        activebackground="#274E80",
        activeforeground="white",
        width=22,
        bd=0,
        pady=8,
        cursor="hand2"
    )

    btn_guardar.pack(pady=30)

def abrir_registro_ventas():
    ven = tk.Toplevel()
    ven.title("Registro de Ventas")
    ven.geometry("500x550")
    ven.resizable(False, False)
    ven.configure(bg="#722FA1")  # Fondo morado

    # -------------------------
    # TÍTULO
    # -------------------------
    titulo = tk.Label(
        ven,
        text="REGISTRO DE VENTAS",
        font=("Times New Roman", 20, "bold"),
        bg="#722FA1",
        fg="white"
    )
    titulo.pack(pady=20)

    # -------------------------
    # FRAME PRINCIPAL
    # -------------------------
    frame = tk.Frame(
        ven,
        bg="#AD70D8",
        bd=0
    )
    frame.pack(
        padx=30,
        pady=10,
        fill="both",
        expand=True
    )

    # -------------------------
    # ESTILOS
    # -------------------------
    estilo_label = {
        "font": ("Times New Roman", 13, "bold"),
        "bg": "#AD70D8",
        "fg": "white"
    }

    estilo_entry = {
        "font": ("Arial", 12),
        "width": 30,
        "bd": 2,
        "relief": "groove"
    }

    # ------------------------------------
    # Cargar productos
    # ------------------------------------
    productos = {}

    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivof = os.path.join(BASE_DIR, "productos.txt")

        with open(archivof, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split("|")

                if len(partes) == 4:
                    idp, desc, precio, cat = partes
                    productos[desc] = float(precio)

    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "No se encontró productos.txt"
        )
        ven.destroy()
        return

    lista_productos = list(productos.keys())

    # -------------------------
    # PRODUCTO
    # -------------------------
    lbl_prod = tk.Label(
        frame,
        text="Producto",
        **estilo_label
    )
    lbl_prod.pack(pady=(20,5))

    cb_producto = ttk.Combobox(
        frame,
        values=lista_productos,
        font=("Arial",12),
        width=28,
        state="readonly"
    )
    cb_producto.pack(pady=5)

    # -------------------------
    # PRECIO
    # -------------------------
    lbl_precio = tk.Label(
        frame,
        text="Precio",
        **estilo_label
    )
    lbl_precio.pack(pady=(15,5))

    txt_precio = tk.Entry(
        frame,
        **estilo_entry,
        state="readonly"
    )
    txt_precio.pack()

    # -------------------------
    # CANTIDAD
    # -------------------------
    lbl_cantidad = tk.Label(
        frame,
        text="Cantidad",
        **estilo_label
    )
    lbl_cantidad.pack(pady=(15,5))

    cantidad_var = tk.StringVar()

    txt_cantidad = tk.Entry(
        frame,
        **estilo_entry,
        textvariable=cantidad_var
    )
    txt_cantidad.pack()

    # -------------------------
    # TOTAL
    # -------------------------
    lbl_total = tk.Label(
        frame,
        text="Total",
        **estilo_label
    )
    lbl_total.pack(pady=(15,5))

    txt_total = tk.Entry(
        frame,
        **estilo_entry,
        state="readonly"
    )
    txt_total.pack()

    # -------------------------
    # FUNCIONES
    # -------------------------
    def actualizar_precio(event):

        prod = cb_producto.get()

        if prod in productos:

            txt_precio.config(state="normal")
            txt_precio.delete(0, tk.END)
            txt_precio.insert(0, productos[prod])
            txt_precio.config(state="readonly")

            calcular_total()

    def calcular_total(*args):

        try:
            cant = int(txt_cantidad.get())
            precio = float(txt_precio.get())

            total = cant * precio

            txt_total.config(state="normal")
            txt_total.delete(0, tk.END)
            txt_total.insert(0, total)
            txt_total.config(state="readonly")

        except:
            txt_total.config(state="normal")
            txt_total.delete(0, tk.END)
            txt_total.config(state="readonly")

    cantidad_var.trace_add(
        "write",
        calcular_total
    )

    def registrar_venta():

        prod = cb_producto.get()
        precio = txt_precio.get()
        cant = txt_cantidad.get()
        total = txt_total.get()

        if prod == "" or precio == "" or cant == "" or total == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Complete todos los campos"
            )
            return

        archivov = os.path.join(
            BASE_DIR,
            "ventas.txt"
        )

        with open(archivov,"a",encoding="utf-8") as archivo:
            archivo.write(
                f"{prod}|{precio}|{cant}|{total}\n"
            )

        messagebox.showinfo(
            "Venta registrada",
            "La venta se registró correctamente."
        )

        cb_producto.set("")

        txt_precio.config(state="normal")
        txt_precio.delete(0,tk.END)
        txt_precio.config(state="readonly")

        txt_cantidad.delete(0,tk.END)

        txt_total.config(state="normal")
        txt_total.delete(0,tk.END)
        txt_total.config(state="readonly")

    # -------------------------
    # EVENTOS
    # -------------------------
    cb_producto.bind(
        "<<ComboboxSelected>>",
        actualizar_precio
    )

    # -------------------------
    # BOTÓN
    # -------------------------
    btn_guardar = tk.Button(
        frame,
        text="Registrar Venta",
        command=registrar_venta,
        font=("Times New Roman",13,"bold"),
        bg="#5289FF",
        fg="white",
        activebackground="#274E80",
        activeforeground="white",
        width=22,
        bd=0,
        pady=8,
        cursor="hand2"
    )

    btn_guardar.pack(pady=30)

def abrir_reportes():
   messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
   messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\n Proyecto Escolar\n Versión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - DJ Software")
ventana.geometry("500x600")
ventana.resizable(False, False)

# Fondo morado
ventana.configure(bg="#722FA1")  # Morado

# -------------------------
# LOGO
# -------------------------
try:
   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   imagen = Image.open(os.path.join(BASE_DIR,"logo.png"))
   imagen = imagen.resize((250, 250))
   img_logo = ImageTk.PhotoImage(imagen)

   lbl_logo = tk.Label(ventana, image=img_logo, bg="#AD70D8")
   lbl_logo.pack(pady=20)
except:
   lbl_sin_logo = tk.Label(
       ventana,
       text="(Aquí va el logo del sistema)",
       font=("Arial", 12),
       bg="#6A0DAD",
       fg="white"
   )
   lbl_sin_logo.pack(pady=40)

# -------------------------
# ESTILO DE BOTONES
# -------------------------
btn_style = {
    "font": ("Times New Roman", 12),
    "bg": "#5289FF",   # Morado claro
    "fg": "white",
    "activebackground": "#274E80",
    "activeforeground": "white",
    "width": 25,
    "bd": 0
}

# -------------------------
# BOTONES PRINCIPALES
# -------------------------
btn_reg_prod = tk.Button(ventana, text="Registro de Productos", command=abrir_registro_productos, **btn_style)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(ventana, text="Registro de Ventas", command=abrir_registro_ventas, **btn_style)
btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(ventana, text="Reportes", command=abrir_reportes, **btn_style)
btn_reportes.pack(pady=10)

btn_acerca = tk.Button(ventana, text="Acerca de", command=abrir_acerca_de, **btn_style)
btn_acerca.pack(pady=10)

# -------------------------
# INICIO DE LA APP
# -------------------------
ventana.mainloop()