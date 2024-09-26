from fastapi import FastAPI
import numpy as np
from starlette.responses import PlainTextResponse

dataset = np.empty((5053,9), dtype=object)
with open("data_2.csv","r") as data:
    c = -1
    for line in data:
        line_split = line.split(",")
        if len(line_split) == 9:
            c = c + 1
            dataset[c] = line_split

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    return f"Welcome to my Protein Dipole Database!\nPlease use the following endpoints.\n/protein will return a list of valid pdb ids included in this database.\n/radius/pdb will return the protein radius.\n/dipole/pdb will return the protein dipole moment."



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Welcome to my Protein Dipole Database!\nPlease use the following endpoints.\n\/protein will return a list of valid pdb ids included in this database.\n\/radius\/pdb will return the protein radius.\n\/dipole\/pdb will return the protein dipole moment."}

@app.get("/goodbye/{name}")
async def say_goodbye(name: str):
    return {"message": f"Goodbye {name}"}

@app.get("/protein/{name}")
async def get_idx(name: str):
    rme = int(np.where(dataset[:,0] == name)[0][0])
    return {"Protein IDX": f"{rme}"}

@app.get("/protein")
async def get_all():
    strreturn = ""
    for i in dataset[:,0]:
        strreturn = strreturn + ", " + str(i)
    return {"Protein Names": f"{strreturn}"}

@app.get("/radius/{name}")
async def get_idx(name: str):
    idx = np.where(dataset[:, 0] == name)[0][0]
    rme = float(dataset[idx, 1])
    return {"Protein Radius": f"{rme} nm"}

@app.get("/dipole/{name}")
async def get_idx(name: str):
    idx = np.where(dataset[:, 0] == name)[0][0]
    rme = float(dataset[idx, 2])
    return {"Protein Dipole": f"{rme} Debye"}