#prueba

preguntas = [
    {
        "pregunta": "\n¿Cuál de los siguientes personas fue un filosofo?",
        "opciones": ["\nA. Albert Einstein ", "B. George Washington ", "C. Platon", "D. William Shakespeare\n"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "\n¿Cual de las siguientes es una pregunta filosofica fundamental?",
        "opciones": ["\nA. ¿Cuál es el nombre del presidente actual de Colombia?", "B. ¿Qué es la felicidad?", "C. ¿Cuál es el precio de una libra de arroz?", "D. ¿Qué hora es? \n"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "\n¿Qué es la ética, según la filosofía clásica?", 
        "opciones": ["\nA. El estudio de la belleza y el arte.", "B. El estudio del conocimiento y la verdad. ", "C. El estudio del bien y el mal.", "D. El estudio de la existencia y el universo\n"],
        "respuesta_correcta": "C"
    }
]
contador = 0
print ("="*64)
print ("                       QUIZ DE FILOSOFIA    ")
print ("="*64)

# Mostrar las preguntas y opciones
for pregunta in preguntas:
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)