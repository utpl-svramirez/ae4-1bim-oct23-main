"""
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import MatriculaEstudiante

# se obtiene la colección general (base de datos)

db = MatriculaEstudiante.ejemploMongo001
coleccion = db.autores

print("Muestra todas las matrículas")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)

# se usa método delete_many con parámetros, a partir de la colección
# para eliminar un documento de la colección
print("Proceso para borrar un documento de una colección")
coleccion.delete_many({'numero_publicaciones':80})

print("Matrículas")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)
