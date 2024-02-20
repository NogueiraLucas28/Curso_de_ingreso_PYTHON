import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        
        while True:
            numero = prompt ("UTN", "Ingrese un número") 
            if numero == None:
                break
            numero = int(numero)

            if numero > 0:
                suma_positivos += numero
                contador_positivos += 1
            elif numero < 0: 
                suma_negativos += numero
                contador_negativos += 1
            else:
                contador_ceros += 1
        diferencia = contador_positivos - contador_negativos

        mensaje = (f"Suma acumulada de negativos: {suma_negativos}\nSuma acumulada de positivos: {suma_positivos}\n"
                   f"Cantidad de números positivos: {contador_positivos}\nCantidad de números negativos {contador_negativos}\n"
                   f"Cantidad de ceros: {contador_ceros}\nDiferencia entre cantidad de positivos y negativos: {diferencia}")
        alert ("UTN", mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
