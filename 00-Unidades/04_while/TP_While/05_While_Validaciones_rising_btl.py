import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.txt_tipo = customtkinter.CTkEntry(master=self)
        self.txt_tipo.grid(row=2, column=1, padx=20, pady=10)
        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):  
        while True:
            apellido = prompt ("Carga de datos", "Apellido")
            if apellido.isalpha() == False or apellido == "":
                alert ("ERROR", "INGRESE SU APELLIDO SIN NUMEROS O CARACTERES ESPECIALES")
            else:
                break

        while True:
            edad_str = prompt ("Carga de datos", "Cargue su edad (solo numeros entre 18 y 90)")
            if edad_str.isdigit() == False:
                alert ("ERROR", "INGRESE SOLO NUMEROS")
                continue
                
            edad = int(edad_str) 
            if (edad < 18 or edad > 90):
                alert ("ERROR", "INGRESE NUMEROS DEL 18 AL 90")
                continue
            else:
                break

        while True:
            estado = prompt ("Carga de datos", "Estado civil")
            if estado == None:
                estado = int(estado)
            elif estado != "soltero" and estado != "casado" and estado != "divorciado" and estado != "viudo": 
                alert ("ERROR", "VALORES ACEPTADOS: soltero, casado, divorciado, viudo")
            else:
                break

        while True:
            legajo_str = prompt ("Carga de datos", "Número de legajo")
            if legajo_str.isdigit() == False:
                alert ("ERROR", "INGRESE SOLO NUMEROS")
                continue
            legajo = int(legajo_str)
            if (legajo < 1000 or legajo > 9999):
                alert ("ERROR", "INGRESE SOLO 4 CIFRAS, SIN CEROS A LA IZQUIERDA")
                continue
            else:
                break

        print ("Hola", apellido, edad, estado, legajo)
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
