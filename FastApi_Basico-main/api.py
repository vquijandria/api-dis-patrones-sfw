from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#! Crear una ruta Hola Mundo
@app.get("/")
def hola_mundo():
    return {"mensaje": "Hola Mundo"}

# TODO: Run the server
# ? Comando base: uvicorn {nombre_archivo}:{nombre_variable_app}
# uvicorn api:app
# ? Comando con reload: uvicorn {nombre_archivo}:{nombre_variable_app} --reload
# uvicorn api:app --reload
# ? Comando con puerto: uvicorn {nombre_archivo}:{nombre_variable_app} --port {puerto}
# uvicorn api:app --port 8000


# TODO: Objetos de prueba
# ? Base de datos de prueba
db_datos = [
    {"id": 1, "nombre": "Luis", "edad": 20},
    {"id": 2, "nombre": "Juan", "edad": 30},
    {"id": 3, "nombre": "Maria", "edad": 40},
    {"id": 4, "nombre": "Diana", "edad": 50},
    {"id": 5, "nombre": "Daniela", "edad": 60},
    {"id": 6, "nombre": "Pedro", "edad": 70},
]


# ? Modelo de prueba para crear datos (POST)
class Dato(BaseModel):
    id: int
    nombre: str
    edad: int


# ? Modelo de prueba para actualizar datos (PUT)
class DatoActualizar(BaseModel):
    nombre: str
    edad: int


# ? Modelo de prueba para actualizar datos (PATCH)
class DatoActualizarParcial(BaseModel):
    nombre: str = None
    edad: int = None


# TODO: Tipos de rutas CRUD

# ? GET: Obtener datos
@app.get("/obtenerDatos")
def obtener_datos():
    return db_datos

@app.get("/obtenerDato/{id}")
def obtener_datos(id: int):
    try:
        dato = db_datos[id-1]
        return dato
    except:
        return {"mensaje": "No existe el dato"}


# ? POST: Crear datos
@app.post("/crearDato")
def crear_dato(dato: Dato):
    try:
        db_datos.append(dato.dict())
        return {"mensaje": "Dato creado correctamente"}
    except:
        return {"mensaje": "Error al crear el dato"}


# ? PUT: Actualizar datos
@app.put("/actualizarDato/{id}")
def actualizar_dato(id: int, dato: DatoActualizar):
    try:
        db_datos[id-1]["nombre"] = dato.nombre
        db_datos[id-1]["edad"] = dato.edad
        return {"mensaje": "Dato actualizado correctamente"}
    except:
        return {"mensaje": "Error al actualizar el dato"}

# ? PATCH: Actualizar datos de forma parcial
@app.patch("/actualizarDatoParcial/{id}")
def actualizar_dato_parcial(id: int, dato: DatoActualizarParcial):
    try:
        db_datos[id-1]["nombre"] = dato.nombre
        db_datos[id-1]["edad"] = dato.edad
        return {"mensaje": "Dato actualizado correctamente"}
    except:
        return {"mensaje": "Error al actualizar el dato"}
# ? DELETE: Eliminar datos

@app.delete("/eliminarDato/{id}")
def eliminar_dato(id: int):
    try:
        db_datos.pop(id-1)
        return {"mensaje": "Dato eliminado correctamente"}
    except:
        return {"mensaje": "Error al eliminar el dato"}

# TODO: Ruta de la documentación
# ? http://localhost:8000/docs
