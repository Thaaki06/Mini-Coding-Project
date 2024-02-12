from models import Vote
from controller.vote_controller import VoteController
from fastapi import APIRouter, Depends, HTTPException
from auth import get_user
from typing import List

vote_routes = APIRouter()

vote_controller = VoteController()

@vote_routes.get('/votes', response_model=List[Vote])
async def get_all_votes(current_user: dict = Depends(get_user)):
    return vote_controller.get_all_votes()

@vote_routes.post('/votes', response_model=Vote)
async def create_vote(vote: Vote, current_user: dict = Depends(get_user)):
    vote_controller.create_vote(vote)
    return vote

@vote_routes.get('/votes/{vote_id}', response_model=Vote)
async def get_vote(vote_id: str, current_user: dict = Depends(get_user)):
    vote = vote_controller.get_vote(vote_id)
    if vote:
        return vote
    else:
        raise HTTPException(status_code=404, detail="Vote not found")
    