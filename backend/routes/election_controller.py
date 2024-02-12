from models import ElectionModel
from controller.election_controller import ElectionController
from fastapi import APIRouter, Depends, HTTPException
from auth import get_user
from typing import List

election_routes = APIRouter()

election_controller = ElectionController()

@election_routes.get('/elections', response_model=List[ElectionModel])
async def get_all_elections(current_user: dict = Depends(get_user)):
    return election_controller.get_all_elections()

@election_routes.post('/elections', response_model=ElectionModel)
async def create_election(election: ElectionModel, current_user: dict = Depends(get_user)):
    election_controller.create_election(election)
    return election

@election_routes.get('/elections/{election_id}', response_model=ElectionModel)
async def get_election(election_id: str, current_user: dict = Depends(get_user)):
    election = election_controller.get_election(election_id)
    if election:
        return election
    else:
        raise HTTPException(status_code=404, detail="ElectionModel not found")
    
    