"""numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [number for number in numbers if number % 2 == 0]

print('v2 =>', even_numbers_v2)

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

def message_creator(text):
    # Escribe tu solución 👇
    if text == "computadora":
        return "Con mi computadora puedo programar usando Python"
    elif text ==" celular":
        return "En mi celular puedo aprender usando la app de Platzi"
    elif text == "cable":
        return "¡Hay un cable en mi bota!"
    else:
        return "Artículo no encontrado"

text = "computadora"
response = message_creator(text)
print(response)

def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda number: number * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)"""

def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda numLetters: len(numLetters) >= 4, words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)