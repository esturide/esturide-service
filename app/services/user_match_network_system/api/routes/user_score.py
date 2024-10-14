from fastapi import APIRouter

router_user_score = APIRouter(
    prefix="/userscore",
    tags=["User score"]
)


@router_user_score.get('/')
async def user_score_status():
    return {
        "status": "Ok"
    }
