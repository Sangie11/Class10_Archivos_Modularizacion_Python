# Proyecto: Mis compras navideñas.
# Estudiante: Angie Salazar.
# Fecha de Inicio: 13/11/2024
# Fecha de Entrega:13/11/2024
# Descripción: EPresupuesto de lo que voy a gastar esta navidad en compras.
# version: 0:0

#Importar un paquete de modulos
from analisis_datos import *

#Generar una lista de compras aleatoria y escribir esta lista en un archivo
lista_compras = generar_lista_compras()
guardar_lista_compras(lista_compras)
precios = [precio for _, precio in lista_compras]
media = media(precios)
mediana = mediana(precios)
print(f"Media de precios: ¢{media:.2f}")
print(f"Mediana de precios: ¢{mediana:.2f}")

