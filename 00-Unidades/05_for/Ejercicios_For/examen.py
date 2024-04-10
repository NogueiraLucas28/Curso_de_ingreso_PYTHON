import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:Lucas
apellido:Nogueira
Tutor:Marina/albana
------
De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos
Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso ( entre 100 y 800)
Tipo de material ( aluminio, hierro , madera)
Costo en $ (mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue tipo de material menos usado ( aluminio, hierro , madera)
Informe B- El porcentaje de contenedores por Categoría (peligroso, comestible, indumentaria)
Informe C- La marca y tipo del contenedor más costoso
Informe D- La marca del contenedor de aluminio con mayor costo
Informe E- El promedio de costo de todos los contenedores

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_aluminio = 0
        contador_hierro = 0
        contador_madera = 0
        contador_peligroso = 0
        contador_comestible = 0
        contador_indumentaria = 0
        acumulador_costo = 0

        for vuelta in range (20):
            marca = prompt("UTN", "Ingrese marca")

            categoria = prompt("UTN", "Ingrese categoria")
            while categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria":
                categoria = prompt ("UTN", "Reingrese categoria (peligroso, comestible o indumentaria)")
            
            peso = prompt("UTN", "Ingrese peso")
            while peso == None or peso.isdigit() == False or int(peso) < 100 or int(peso) > 800:
                peso = prompt("UTN", "Reingrese peso")
            peso = int(peso)

            tipo = prompt ("UTN", "Ingrese tipo")
            while tipo != "aluminio" and tipo != "hierro" and tipo != "madera":
                tipo = prompt ("UTN", "Reingrese tipo (aluminio, hierro o madera)")
            
            costo = prompt ("UTN", "Ingrese costo en $")
            while costo == None or costo.isdigit() == False or int(costo) < 0:
                costo = prompt ("UTN", "Reingrese costo $")
            costo = int(costo)

            match tipo:
                case "aluminio":
                    contador_aluminio += 1
                    if contador_aluminio == 1 or costo > aluminio_maximo_costo:
                        aluminio_maximo_costo = costo
                        marca_aluminio_costoso = marca
                case "hierro":
                    contador_hierro += 1
                case "madera":
                    contador_madera +=1

            match categoria:
                case "peligroso":
                    contador_peligroso += 1
                case "comestible":
                    contador_comestible += 1
                case "indumentaria":
                    contador_indumentaria += 1

            if vuelta == 0 or costo > costo_maximo:
                costo_maximo = costo
                marca_costo_maximo = marca
                tipo_costo_maximo = tipo

            acumulador_costo += costo

        porcentaje_peligroso = (contador_peligroso * 100) / 20
        porcentaje_comestible = (contador_comestible * 100) / 20
        porcentaje_indumentaria = (contador_indumentaria * 100) / 20
        promedio_costo = acumulador_costo / 20

        mensaje = "Resultados:\n"

        if contador_aluminio < contador_hierro and contador_aluminio < contador_madera:
            mensaje += "Informe A- Tipo de material menos usado: Aluminio\n"
        elif contador_hierro < contador_madera:
            mensaje += "Informe A- Tipo de material menos usado: Hierro\n"
        else:
            mensaje += "Informe A- Tipo de material menos usado: Madera\n"

        mensaje += f"Informe B- Porcentaje de contenedores por Categoría: \n\tPeligroso: {porcentaje_peligroso}%\n\tComestible: {porcentaje_comestible}%\n\tIndumentaria: {porcentaje_indumentaria}%\n"
        mensaje += f"Informe C- Marca y tipo del contenedor más costoso: \n\tMarca: {marca_costo_maximo}\n\tTipo: {tipo_costo_maximo}\n"

        if contador_aluminio != 0:
            mensaje += f"Informe D- La marca del contenedor de aluminio con mayor costo es: {marca_aluminio_costoso}\n"
        else:
            mensaje += "Informe D- No se ingresaron contenedores de aluminio\n"

        mensaje += f"Informe E- El promedio de costo de todos los contenedores es: ${promedio_costo}"

        print (mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()