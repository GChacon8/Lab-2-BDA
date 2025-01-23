import time
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Lab2Avanzadas"]
collection = db["Bases_Avanzadas"]


start_time = time.perf_counter()
print("Eliminando todos los documentos de la colección:")
result = collection.delete_many({})  # El filtro vacío elimina todos los documentos
end_time = time.perf_counter()

# Mostrar el número de documentos eliminados y el tiempo transcurrido
print(f"Documentos eliminados: {result.deleted_count}")
print(f"Tiempo de eliminación: {end_time - start_time:.4f} segundos")



