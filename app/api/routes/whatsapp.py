from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.json()

    # TODO: parse incoming message
    # map to agent
    # store in DB

    print("Incoming:", data)

    return {"status": "ok"}