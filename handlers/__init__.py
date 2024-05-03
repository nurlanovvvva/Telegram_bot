from aiogram import Router


def setup_routes() -> Router:
    from . import (
    start,
    )
    router = Router()
    router.include_router(start.router)

    return router
