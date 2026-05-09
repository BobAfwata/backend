import httpx
from app.core.config import settings

async def send_whatsapp_message(to: str, text: str):
    url = f"https://graph.facebook.com/v18.0/{settings.whatsapp_phone_id}/messages"

    headers = {
        "Authorization": f"Bearer {settings.whatsapp_token}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
        return response.json()
