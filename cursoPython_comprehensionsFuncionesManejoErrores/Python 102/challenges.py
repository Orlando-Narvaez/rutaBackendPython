"""numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [number for number in numbers if number % 2 == 0]

print('v2 =>', even_numbers_v2)"""

def message_creator(text):
   # Escribe tu solución 👇

   respuestas = {
    'computadora' : "Con mi computadora puedo programar usando Python", 
   'celular' : "En mi celular puedo aprender usando la app de Platzi",
    'cable' : "¡Hay un cable en mi bota!"
    }

   if text in respuestas.keys(): 
      return respuestas[text]
   else: 
      return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)