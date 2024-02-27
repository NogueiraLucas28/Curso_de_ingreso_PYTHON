import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Lucas
apellido:Nogueira
Tutor:Marina/albana
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        acumulador_edades = 0
        acumulador_votos = 0
        contador_candidatos = 0
        primera_vez = True
        continuar = True

        while continuar:
            nombre = prompt("Carga de datos", "Ingrese nombre")
            while nombre == None or nombre == "":  
                nombre = prompt("Carga de datos", "Reingrese nombre")

            edad = prompt("Carga de datos", "Ingrese edad")
            while edad == None or edad == "" or int(edad) < 25:
                edad = prompt("Carga de datos", "Reingrese edad")
            
            votos = prompt("Carga de datos", "Ingrese votos")
            while votos == None or votos == "" or int(votos) < 0:  
                votos = prompt("Carga de datos", "Reingrese votos")

            edad = int(edad)
            votos = int(votos)
            contador_candidatos += 1
            acumulador_edades += edad
            acumulador_votos += votos
            if (primera_vez == True) or (votos > maximos_votos):
                maximos_votos = votos
                candidato_mas_votos = nombre

            if (primera_vez == True) or (votos < minimos_votos):
                minimos_votos = votos
                candidato_menos_votos = nombre
                edad_candidato_menos_votos = edad
                primera_vez = False
            
            continuar = question("UTN","Desea continuar?")
            
            
            
        promedio_edades = acumulador_edades / contador_candidatos


        mensaje = f"candidato mas votado: {candidato_mas_votos}\ncandidato menos votad: {candidato_menos_votos}\nedad del menos votado: {edad_candidato_menos_votos}\npromedio edades: {promedio_edades}\nvotos totales: {acumulador_votos}"
        alert("UTN", mensaje)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
