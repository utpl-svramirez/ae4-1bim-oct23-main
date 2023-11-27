"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = MatriculaEstudiante.ejemploMongo001
coleccion = db.Matriculados

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre": "Andres", "apellido": "Rojas",
        
"nacionalidad":"ecuatoriana", "Carrera": "Carrera Psicología"}

data_01 = {"nombre": "Luis", "apellido": "Torres",
"nacionalidad":"ecuatoriana", "Carrera": "Carrera: Economía"}

# coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"nombre": "Jose", "apellido": "Jara", "nacionalidad":"ecuatoriana",
"Carrera": 'Psicologia'},
{"nombre": "María", "apellido": "Velez", "nacionalidad":"peruana",
"carrera": "Economía"}
]

coleccion.insert_many(lista)
