from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.routing import Router

from src.database import init_database

router = Router()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Контекстный менеджер для управления жизненным циклом приложения FastAPI.

    Инициализирует подключение к базе данных и сохраняет фабрику сессий в состоянии приложения.
    Закрывает подключение к базе данных при завершении приложения.

    Args:
        app (FastAPI): Экземпляр приложения FastAPI.

    Yields:
        None
    """
    # Инициализация фабрики асинхронных сессий и сохранение в состоянии приложения
    app.state.async_session_maker = await init_database()

    try:
        yield
    finally:
        # Здесь можно добавить логику для закрытия ресурсов, если это потребуется
        pass
