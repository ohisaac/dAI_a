import fastapi


router = fastapi.APIRouter()



async def ping():
    return {"ping": "pong"}



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