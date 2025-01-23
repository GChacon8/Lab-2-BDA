import csv
import time
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Lab2Avanzadas"]
collection = db["Bases_Avanzadas"]

# Leer el archivo CSV
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)  # Usa los encabezados del CSV como claves
    documentos = [row for row in reader]

# Medir el tiempo de inserción
start_time = time.time() 
collection.insert_many(documentos)  #Inserta todos los documentos
end_time = time.time()

# Mostrar el tiempo transcurrido
print(f"Tiempo de inserción: {end_time - start_time:.2f} segundos")



