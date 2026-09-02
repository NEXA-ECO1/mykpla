import uuid
import httpx
from .config import settings


async def transcribe(audio: bytes, filename: str) -> str:
    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(f'{settings.whisper_url.rstrip("/")}/transcribe', files={'file': (filename, audio)})
        response.raise_for_status()
        return response.json().get('text', '')


async def synthesize(text: str) -> bytes:
    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(f'{settings.tts_url.rstrip("/")}/tts', json={'text': text})
        response.raise_for_status()
        return response.content


async def generate_image(prompt: str) -> dict:
    # ComfyUI integration point. Keep the workflow server-side so models/workflows can be swapped without changing the agent API.
    workflow_id = str(uuid.uuid4())
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(f'{settings.comfyui_url.rstrip("/")}/system_stats')
        response.raise_for_status()
    return {'workflow_id': workflow_id, 'prompt': prompt, 'status': 'ComfyUI reachable; configure a workflow for generation.'}
