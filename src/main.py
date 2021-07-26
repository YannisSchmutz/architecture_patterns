from api.api import api_router
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(api_router)


def init_db() -> None:
    register_tortoise(
        app,
        config={
            "connections": {
                # Using a DB_URL string
                "default": "postgres://postgres:postgres@hostel_db:5432/dev",
            },
            "apps": {
                "hostel": {
                    "models": [
                        "models.room",
                        "models.bed",
                    ],
                    "default_connection": "default",
                },
            },
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )


@app.on_event("startup")
async def startup_event():
    init_db()


@app.on_event("shutdown")
async def shutdown_event():
    pass
