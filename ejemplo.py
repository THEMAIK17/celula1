
	
preguntas = [
    {
        "pregunta.1": "¿Cuál de los siguientes personas fue un filosofo?",
        "opciones": ["A- Albert Einstein ", "B- George Washington ", "C-Platon", "D- William Shakespeare"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta.2": "¿Cual de las siguientes es una pregunta filosofica fundamental?",
        "opciones": ["A- ¿Cuál es el nombre del presidente actual de Colombia?", "B- ¿Qué es la felicidad?", "C- ¿Cuál es el precio de una libra de arroz?", "D- ¿Qué hora es? "],
        "respuesta_correcta": "B"
    },
    {
        "pregunta.3": "¿Qué es la ética, según la filosofía clásica?", 
        "opciones": ["A- El estudio de la belleza y el arte.", "B- El estudio del conocimiento y la verdad. ", "C-  El estudio del bien y el mal.", "D-El estudio de la existencia y el universo"],
        "respuesta_correcta": "C"
    }
]

contador = 0
print ("="*25)
print ("     ENCUESTA RIWI     ")
print ("="*25)

# Mostrar las preguntas y opciones
for pregunta in preguntas:
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)
    
    # Asegurarse de que el usuario ingrese una opción válida
    while True:

        respuesta_usuario = input("Elige una opción (A, B, C o D): ").upper()
            
        # Verificamos si la respuesta es válida (número entre 1 y 4)
        if respuesta_usuario not in ["A", "B", "C", "D"]:
            print("Opción inválida. Por favor, elige una opcion entre A y D.")
        else:
            break  # Salir del bucle si la respuesta es válida

    
    # Comprobar si la respuesta es correcta
    if respuesta_usuario == pregunta["respuesta_correcta"]:
        contador += 1


    
print(f"Su promedio fue: {contador} respuesta(s) correcta(s) de 3 preguntas") 