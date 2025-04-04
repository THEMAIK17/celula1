#prueba

preguntas = [
    {
        "pregunta": "¿Cuál de los siguientes personas fue un filosofo?",
        "opciones": ["A. Albert Einstein ", "B. George Washington ", "C. Platon", "D. William Shakespeare"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Cual de las siguientes es una pregunta filosofica fundamental?",
        "opciones": ["A. ¿Cuál es el nombre del presidente actual de Colombia?", "B. ¿Qué es la felicidad?", "C. ¿Cuál es el precio de una libra de arroz?", "D. ¿Qué hora es? "],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Qué es la ética, según la filosofía clásica?", 
        "opciones": ["A. El estudio de la belleza y el arte.", "B. El estudio del conocimiento y la verdad. ", "C.  El estudio del bien y el mal.", "D. El estudio de la existencia y el universo"],
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