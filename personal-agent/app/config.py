from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    host: str = os.getenv('HOST', '127.0.0.1')
    port: int = int(os.getenv('PORT', '8080'))
    llama_base_url: str = os.getenv('LLAMA_BASE_URL', 'http://127.0.0.1:8081/v1')
    llama_model: str = os.getenv('LLAMA_MODEL', 'local-model')
    whisper_url: str = os.getenv('WHISPER_URL', 'http://127.0.0.1:9000')
    tts_url: str = os.getenv('TTS_URL', 'http://127.0.0.1:5002')
    comfyui_url: str = os.getenv('COMFYUI_URL', 'http://127.0.0.1:8188')
    database_path: str = os.getenv('DATABASE_PATH', './data/memory.db')
    agent_name: str = os.getenv('AGENT_NAME', 'MYK')

settings = Settings()
