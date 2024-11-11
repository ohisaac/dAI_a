import fastapi
import app
import app.inference
import app.inference.engines
import loguru


logging = loguru.logger
router = fastapi.APIRouter()



async def ping():
    return {"ping": "pong"}



async def load_model():
    try:
        model = await app.inference.engines.real_load_model()
        return model
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        raise


router.add_api_route(
    "/ping",
    ping,
    methods=["GET"],
    responses={200: {"description": "Pong!"}},
)


router.add_api_route(
    "/load_model",
    load_model,
    methods=["POST"],
    # response_model=schemas.LoadModelResponse,
    responses={
        400: {"description": "Invalid request format or missing fields"},
        200: {"description": "Model loaded successfully"},
    },
)