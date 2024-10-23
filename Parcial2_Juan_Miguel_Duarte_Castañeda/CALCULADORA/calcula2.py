import tkinter as tk
from tkinter import messagebox

def verificar_division(num):
    if num == 0:
        raise ZeroDivisionError("División por cero no permitida.")

def realizar_operacion(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = ""

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            verificar_division(num2)  # Verificar división por cero
            resultado = num1 / num2
        elif operacion == "potencia":
            verificar_division(num2)  # Verificar división por cero para potencia
            resultado = num1 ** num2

        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear los widgets
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

# Botones de operaciones
boton_suma = tk.Button(ventana, text="Sumar", command=lambda: realizar_operacion("suma"))
boton_suma.pack()

boton_resta = tk.Button(ventana, text="Restar", command=lambda: realizar_operacion("resta"))
boton_resta.pack()

boton_multiplicacion = tk.Button(ventana, text="Multiplicar", command=lambda: realizar_operacion("multiplicacion"))
boton_multiplicacion.pack()

boton_division = tk.Button(ventana, text="Dividir", command=lambda: realizar_operacion("division"))
boton_division.pack()

boton_potencia = tk.Button(ventana, text="Potencia", command=lambda: realizar_operacion("potencia"))
boton_potencia.pack()

# Label para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
