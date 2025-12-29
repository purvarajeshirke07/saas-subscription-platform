from fastapi import FastAPI

app = FastAPI(title="SaaS Subscription Platform")

@app.get("/health")
def health_check():
    return {"status": "ok good to go purva"}
