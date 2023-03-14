from fastapi import FastAPI, HTTPException
from app.document import Document


documents: list[Document] = [
    Document(0, 'First doc', 'Content'),
    Document(1, 'Second doc', 'Long, long, long, long, long, long, long, long, long, long, long, long, long text')
]

app = FastAPI()


@app.get("/v1/docs")
async def get_docs():
    return documents

@app.get("/v1/docs/{id}")
async def get_docs_by_id(id: int):
    result = [item for item in documents if item.id == id]
    if len(result) > 0:
        return result[0]
    
    raise HTTPException(status_code=404, detail="Document not found")