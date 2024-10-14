from fastapi import APIRouter

router_travels = APIRouter(
    prefix="/travels",
    tags=["Travels"]
)


@router_travels.get('/')
async def travels_status():
    return {
        "status": "Ok"
    }
