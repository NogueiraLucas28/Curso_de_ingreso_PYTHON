import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
# Enunciado: De 5  mascotas que ingresan a una veterinaria  se deben tomar y validar los siguientes datos.

# Nombre
# Tipo (gato ,perro o exotico)
# Peso ( entre 10 y 80)
# Sexo( F o M  )
# Edad(mayor a 0)

# Pedir datos por prompt y mostrar por print, se debe informar:
# Informe A- Cuál fue el sexo menos ingresado (F o M)
# Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
# Informe C- El nombre y tipo de la mascota menos pesada
# Informe D- El nombre del perro más joven
# Informe E- El promedio de peso de todas las mascotas
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_femenino = 0
        contador_masculino = 0
        contador_gato = 0
        contador_perro = 0
        contador_exotico = 0
        acumulador_peso = 0

        for mascotas in range (5):
            nombre = prompt("Datos", "Ingrese el nombre de su mascota")
            while nombre == None or nombre == "":
                nombre = prompt("Datos", "Reingrese nombre de su mascota")

            tipo = prompt ("Datos", "Ingrese tipo de mascota (gato, perro o exotico)")
            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = prompt ("Datos", "Reingrese tipo de mascota (gato, perro o exotico)")
            
            peso = prompt ("Datos", "Ingrese peso de su mascota(kg)")
            while peso == None or peso == "" or (float(peso) < 10 or float(peso) > 80):
                peso = prompt ("Datos", "Reingrese peso de su mascota(kg)")
            peso = float(peso)

            sexo = prompt ("Datos", "Ingrese sexo de su mascota (F o M)")
            while sexo != "F" and sexo != "M":
                sexo = prompt ("Datos", "Reingrese sexo de su mascota (F o M)")

            edad = prompt ("Datos", "Ingrese edad de su mascota") 
            while edad == None or edad == "" or int(edad) < 0:
                edad = prompt ("Datos", "Reigrese edad de su mascota") 

            # Informe A- Cuál fue el sexo menos ingresado (F o M)
            if sexo == "F":
                contador_femenino += 1
            else:
                contador_masculino += 1
            # Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
            match tipo:
                case "gato":
                    contador_gato += 1
                case "perro":
                    # Informe D- El nombre del perro más joven
                    if contador_perro == 0 or edad < edad_minima_perro:
                        edad_minima_perro = edad
                        nombre_edad_minima_perro = nombre
                    contador_perro += 1
                case "exotico":
                    contador_exotico += 1
            # Informe C- El nombre y tipo de la mascota menos pesada
            if mascotas == 0 or peso < peso_minimo:
                peso_minimo = peso
                nombre_peso_minimo = nombre
                tipo_peso_minimo = tipo
            

            # Informe E- El promedio de peso de todas las mascotas
            acumulador_peso += peso

        if contador_femenino > contador_masculino:
            sexo_menos_ingresado = "M"
        else:
            sexo_menos_ingresado = "F"
        
        porcentaje_gato = (contador_gato * 100) / 5
        porcentaje_perro = (contador_perro * 100) / 5
        porcentaje_exotico = (contador_exotico * 100) / 5
        promedio_peso = acumulador_peso / 5

        mensaje = f"Informe A- El sexo menos ingresado fue: {sexo_menos_ingresado}\n"
        mensaje += f"Informe B- Porcentaje de mascotas por tipo:\n\tgatos: {porcentaje_gato}%\n\tperros: {porcentaje_perro}%\n\texoticos: {porcentaje_exotico}%\n"
        mensaje += f"Informe C- El nombre de la mascota menos pesada es: {nombre_peso_minimo} y es su tipo es: {tipo_peso_minimo}\n"        
        mensaje += f"Informe D- El nombre del perro más joven es: {nombre_edad_minima_perro}\n"
        mensaje += f"Informe E- El promedio de peso de todas las mascotas es: {promedio_peso}"

        alert ("Resultados", mensaje)
if __name__ == "__main__":
    app = App()     
    app.geometry("300x300")
    app.mainloop()

'''
# Enunciado: De 5  mascotas que ingresan a una veterinaria  se deben tomar y validar los siguientes datos.

# Nombre
# Tipo (gato ,perro o exotico)
# Peso ( entre 10 y 80)
# Sexo( F o M  )
# Edad(mayor a 0)

# Pedir datos por prompt y mostrar por print, se debe informar:
# Informe A- Cuál fue el sexo menos ingresado (F o M)
# Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
# Informe C- El nombre y tipo de la mascota menos pesada
# Informe D- El nombre del perro más joven
# Informe E- El promedio de peso de todas las mascotas
'''