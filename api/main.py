from fastapi import FastAPI



app = FastAPI()


@app.post("/clientes/")
async def create_item(cliente:Cliente):
    return cliente