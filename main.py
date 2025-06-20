from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Medha AI", description="AI Mock Interview Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.medhaedutech.in", "https://medhaedutech.in"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)