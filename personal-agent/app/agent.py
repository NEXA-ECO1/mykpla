import httpx
from .config import settings
from .memory import recent, remember

SYSTEM = '''You are MYK, a private personal AI agent. Plan tasks clearly, use available tools only when appropriate, and be transparent about actions. Never expose secrets. Ask for confirmation before destructive or privileged actions.'''


async def chat(message: str, history: list[dict] | None = None) -> str:
    memories = recent(12)
    context = '\n'.join(f'- {m}' for m in memories)
    messages = [{'role': 'system', 'content': SYSTEM + ('\nRelevant memory:\n' + context if context else '')}]
    if history:
        messages.extend(history[-20:])
    messages.append({'role': 'user', 'content': message})
    payload = {'model': settings.llama_model, 'messages': messages, 'temperature': 0.7, 'stream': False}
    async with httpx.AsyncClient(timeout=180) as client:
        response = await client.post(f'{settings.llama_base_url.rstrip("/")}/chat/completions', json=payload)
        response.raise_for_status()
        text = response.json()['choices'][0]['message']['content']
    remember(f'User: {message}\nAgent: {text}')
    return text
