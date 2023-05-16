from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from utils.functions import peliculas_mes, peliculas_dia, peliculas_pais, franquicia, productoras, retorno
from utils.recommend import recomendaciones

app = FastAPI()




origins = [
    "https://moviesapp-oxeinkhcia-uc.a.run.app",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Movie Recommendation API"}


#Endpoints

#Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron 
# ese mes (nombre del mes, en str, ejemplo 'enero') historicamente
@app.get("/peliculas/mes/{mes}")
async def peliculas_por_mes(mes):
    return peliculas_mes(mes)


#Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron 
# ese dia (de la semana, en str, ejemplo 'lunes') historicamente
@app.get("/peliculas/dia/{dia}")
async def peliculas_por_dia(dia):
    return peliculas_dia(dia)


#Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
@app.get("/peliculas/franquicia/{nombre_franquicia}")
async def peliculas_franquicia(nombre_franquicia:str):
    return franquicia(nombre_franquicia)


#Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo
@app.get("/peliculas/pais/{pais}")
async def peliculas_por_pais(pais):
    return peliculas_pais(pais)


#Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron
@app.get("/peliculas/productoras/{nombre_productora}")
async def peliculas_por_productora(nombre_productora):
    return productoras(nombre_productora)


#'Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo
@app.get("/peliculas/retorno/{nombre_pelicula}")
async def retorno_peliculas(nombre_pelicula:str):
    return retorno(nombre_pelicula)

#Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores
@app.get("/peliculas/recomendacion/{titulo_pelicula}")
async def recomendacion_peliculas(titulo_pelicula):
    return recomendaciones(titulo_pelicula)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)










