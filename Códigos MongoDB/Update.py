from pymongo import MongoClient
from bson.objectid import ObjectId
import time

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Lab2Avanzadas"]
collection = db["Bases_Avanzadas"]

# Actualizar un documento por un _id específico
def actualizar_por_id(id, nuevos_datos):
    print("\nActualizar por _id:")
    start_time = time.perf_counter()
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": nuevos_datos})
    end_time = time.perf_counter()
    print(f"Documentos modificados: {result.modified_count}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

# Actualizar usuarios por region_id
def actualizar_por_region(region_id, nuevos_datos):
    print(f"\nActualizar usuarios por region_id = {region_id}:")
    start_time = time.perf_counter()
    result = collection.update_many({"region_id": str(region_id)}, {"$set": nuevos_datos})
    end_time = time.perf_counter()
    print(f"Documentos modificados: {result.modified_count}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

# Actualizar usuarios nacidos después de 1990
def actualizar_nacidos_despues_1990(nuevos_datos):
    print("\nActualizar usuarios nacidos después de 1990:")
    start_time = time.perf_counter()
    result = collection.update_many({"birth_date": {"$gt": "1990-01-01"}}, {"$set": nuevos_datos})
    end_time = time.perf_counter()
    print(f"Documentos modificados: {result.modified_count}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

# Actualizar todos los documentos
def actualizar_todos_los_documentos(nuevos_datos):
    print("\nActualizar todos los documentos:")
    start_time = time.perf_counter()
    result = collection.update_many({}, {"$set": nuevos_datos})
    end_time = time.perf_counter()
    print(f"Documentos modificados: {result.modified_count}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")


# Datos para modificar, en este caso se modifica el phone
nuevos_datos = {"phone": "(999)999-9999"} 

# Llamada a las funciones para actualizar
actualizar_por_id("6790138142285b128f59282c", nuevos_datos)
actualizar_por_region(1, nuevos_datos)
actualizar_nacidos_despues_1990(nuevos_datos)
actualizar_todos_los_documentos(nuevos_datos)



