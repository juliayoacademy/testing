from fastapi import FastAPI
import os
import socket

app = FastAPI(title="Server Test API")



@app.get("/")
def root():
    return {
        "message": "FastAPI is alive 🖤",
        "status": "ok",
        "server": socket.gethostname()
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "api": "working"
    }
