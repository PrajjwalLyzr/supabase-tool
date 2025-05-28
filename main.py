from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db_utils import insert_ticket

app = FastAPI()

class TicketRequest(BaseModel):
    ticket: str

# @app.get("/")
# def health_check():
#     return {"status": "ok", "message": "API is up and running"}


@app.post("/add-ticket")
def add_ticket(request: TicketRequest):
    try:
        result = insert_ticket(request.ticket)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
