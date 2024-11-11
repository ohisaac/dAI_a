import os
import dotenv

import fastapi

import loguru

from app import endpoints



logging = loguru.logger

dotenv.load_dotenv()
debug = os.getenv("DEBUG", False)


if debug:
    logging.info("STARTING IN DEBUG MODE, THIS BETTER NOT BE PRODUCTION")





app = fastapi.FastAPI(
    title="dAI_a",
    debug=True,
)


async def home():
    return {"message": "Hello World"}




app.add_api_route('/',home)
app.include_router(router=endpoints.router, prefix="/api/v1")
