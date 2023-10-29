from vacancy_resume_backend.main import app


def start_back():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=30000)
