# main.py
from fastapi import FastAPI, UploadFile, File
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.docstore.document import Document
import os

app = FastAPI()

CONNECTION_STRING = "postgresql+psycopg2://syash:2004@localhost:5432/resumes"
COLLECTION_NAME = "test"
os.environ["OPENAI_API_KEY"] = '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'

embeddings = OpenAIEmbeddings()
STORE = PGVector(
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
    embedding_function=embeddings,
)

@app.post("/upload_resume/")
async def upload_file(file: UploadFile):
    file_content = file.file.read().decode("utf-8")
    print(file_content)
    if file:
        STORE.add_documents([Document(page_content=file_content)])
        return {"message": "File uploaded and saved successfully"}
    else:
        return {"message": "No file uploaded"}

@app.get("/score_resume/")
async def resumes_with_score(file: UploadFile, ):
    file_content = file.file.read().decode("utf-8")
    docs_with_score = STORE.similarity_search_with_score(file_content)
    for doc, score in docs_with_score:
        print("-" * 80)
        print("Score: ", score)
        print(doc.page_content)
        print("-" * 80)


def start_back():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=30000)

