from fastapi import FastAPI

app = FastAPI(
    title="Facility Management SaaS",
    description="API pour gérer la maintenance, les incidents, et le suivi budgétaire",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Bienvenue sur Facility SaaS API 🚀"}

@app.get("/ping")
def ping():
    return {"status": "OK"}
