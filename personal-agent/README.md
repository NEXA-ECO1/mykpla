# MYK Personal AI Agent

A powerful, local-first personal AI agent foundation for MYK Platform.

## Core capabilities
- Local LLM through `llama.cpp` OpenAI-compatible server
- Voice input through Whisper-compatible transcription
- Voice output through a configurable TTS endpoint
- Image generation through ComfyUI API
- Tool execution with an explicit allowlist
- Persistent local memory (SQLite)
- Web/API-ready FastAPI backend
- Streaming chat endpoint

## Safety
The agent is intentionally local-first and does not claim unrestricted access. Destructive or privileged operations should be placed behind explicit confirmation and OS-level permissions.

## Quick start
1. Copy `.env.example` to `.env`.
2. Start a llama.cpp server with your chosen GGUF model.
3. Install Python dependencies from `requirements.txt`.
4. Run `python -m app`.

Default API: `http://127.0.0.1:8080`
