#Se declaran los ingredientes
agua = int(input ("Cuantas tazas de agua?")) #El agua se da en tazas
print("el agua es", agua)
harina = 1 #La harina se da en tazas
print("la harina es", harina)
sal = 1/16/3 #La sal se convierte en cdtas a tazas, hay 3 cdtas por cda y 16 cdas por taza
print("la sal es", sal)
aceite = 1/16 #El aceite se convierte de cdas a tazas

#comienza la preparación de la arepa
bol = agua + harina + sal
budare = bol + aceite

#se imprime el resultado
print("la arepa final es", budare)

input("presione enter para continuar")
