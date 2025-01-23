from pymongo import MongoClient
from bson.objectid import ObjectId
import time

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Lab2Avanzadas"]
collection = db["Bases_Avanzadas"]

# Consulta por un id específico
def por_id(id):
    print("Consulta por _id:")
    start_time = time.perf_counter()
    documento = collection.find_one({"_id": ObjectId(id)})
    end_time = time.perf_counter()
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

# Consulta los usuarios de una región específica
def por_region(region_id):
    print("\nConsulta por region_id = ", region_id)
    start_time = time.perf_counter()
    usuarios_region = collection.find({"region_id": str(region_id)})
    # Forzar la iteración para medir tiempo de carga de los resultados
    count = 0
    for usuario in usuarios_region:
        count += 1  # Solo contar los documentos
    end_time = time.perf_counter()
    print(f"Se procesaron {count} documentos")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
    
# Consulta los usuarios nacidos después de 1990
def nacidos_despues_1990():
    print("\nUsuarios nacidos después de 1990:")
    start_time = time.perf_counter()
    usuarios_nacidos = collection.find({"birth_date": {"$gt": "1990-01-01"}})
    # Forzar la iteración para medir tiempo de carga de los resultados
    count = 0
    for usuario in usuarios_nacidos:
        count += 1
    end_time = time.perf_counter()
    print(f"Se procesaron {count} documentos")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

# Cantidad de usuarios por cada región
def cant_users_region():
    print("\nConteo de usuarios por region_id:")
    start_time = time.perf_counter()
    pipeline = [
        {"$group": {"_id": "$region_id", "conteo": {"$sum": 1}}}
    ]
    resultados = collection.aggregate(pipeline)
    count = 0
    for resultado in resultados:
        count += 1
    end_time = time.perf_counter()
    print(f"Se procesaron {count} resultados")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
    
# Consulta por todos los usuarios
def sel_all():
    print("Consulta de todos los registros:")
    start_time = time.perf_counter()
    documentos = collection.find()
    count = 0
    for documento in documentos:
        count += 1  # Forzar iteración para medir el tiempo de carga
    end_time = time.perf_counter()
    print(f"Se procesaron {count} documentos")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

por_id("6790138142285b128f59282c")
por_region(1)
nacidos_despues_1990()
cant_users_region()
sel_all()



