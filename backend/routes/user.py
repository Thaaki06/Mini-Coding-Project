from controller.user_controller import UserController
from fastapi import APIRouter, Depends, HTTPException
from auth import get_user
from models import Voter, Candidate


user_routes = APIRouter()
user_controller = UserController()

@user_routes.get('/voters')
def get_all_voters(current_user: dict = Depends(get_user)):
    return user_controller.get_all_voters()

@user_routes.post('/voters')
def create_voter(voter: Voter):
    user_controller.create_voter(voter)
    return voter

@user_routes.get('/voters/{voter_id}')
def get_voter(voter_id: str, current_user: dict = Depends(get_user)):
    voter = user_controller.get_voter(voter_id)
    if voter:
        return voter
    else:
        raise HTTPException(status_code=404, detail="Voter not found")
    
@user_routes.get('/candidates')
def get_all_candidates():
    return user_controller.get_all_candidates()

@user_routes.post('/candidates')
def create_candidate(candidate: Candidate):
    user_controller.create_candidate(candidate)
    return candidate

@user_routes.get('/candidates/{candidate_id}')
def get_candidate(candidate_id: str):
    candidate = user_controller.get_candidate(candidate_id)
    if candidate:
        return candidate
    else:
        raise HTTPException(status_code=404, detail="Candidate not found")
