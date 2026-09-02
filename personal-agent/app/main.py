from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from .config import settings
from .agent import chat
from .services import transcribe, synthesize, generate_image

app = FastAPI(title='MYK Personal AI Agent', version='0.1.0')

class ChatRequest(BaseModel):
    message: str
    history: list[dict] | None = None

@app.get('/health')
async def health():
    return {'ok': True, 'agent': settings.agent_name}

@app.post('/chat')
async def chat_endpoint(request: ChatRequest):
    return {'response': await chat(request.message, request.history)}

@app.post('/voice/transcribe')
async def voice_transcribe(file: UploadFile = File(...)):
    return {'text': await transcribe(await file.read(), file.filename or 'audio.wav')}

@app.post('/voice/synthesize')
async def voice_synthesize(request: ChatRequest):
    from fastapi.responses import Response
    return Response(await synthesize(request.message), media_type='audio/mpeg')

@app.post('/image/generate')
async def image_generate(request: ChatRequest):
    return await generate_image(request.message)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app.main:app', host=settings.host, port=settings.port, reload=False)
