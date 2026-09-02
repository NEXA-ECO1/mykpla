import os
import sqlite3
from .config import settings


def _connect():
    directory = os.path.dirname(settings.database_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    db = sqlite3.connect(settings.database_path)
    db.execute('CREATE TABLE IF NOT EXISTS memories (id INTEGER PRIMARY KEY, content TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)')
    return db


def remember(content: str) -> None:
    with _connect() as db:
        db.execute('INSERT INTO memories(content) VALUES (?)', (content,))


def recent(limit: int = 20) -> list[str]:
    with _connect() as db:
        rows = db.execute('SELECT content FROM memories ORDER BY id DESC LIMIT ?', (limit,)).fetchall()
    return [r[0] for r in reversed(rows)]
