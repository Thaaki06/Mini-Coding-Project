from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import election_controller, user_controller, vote_controller


app = FastAPI()



# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4100",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
    
   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.include_router(election_controller.election_controller)
app.include_router(user_controller.user_controller)
app.include_router(vote_controller.vote_controller)


if __name__ == "__main__":
    uvicorn.run(app)