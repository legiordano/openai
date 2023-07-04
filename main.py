import openai

openai.api_key = 'tu_clave_de_api'

def obtener_respuesta(consulta):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=consulta,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    respuesta = response.choices[0].text.strip()
    
    return respuesta

consulta_usuario = input("Escribe tu consulta: ")
respuesta_modelo = obtener_respuesta(consulta_usuario)
print(respuesta_modelo)
