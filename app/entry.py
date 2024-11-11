# engines.py
import fastapi
import logging
import asyncio
import time
import vllm
from fastapi import FastAPI
from contextlib import asynccontextmanager

# Global model instance
model_instance = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model on startup
    global model_instance
    model_instance = await load_model()
    yield
    # Cleanup on shutdown
    if model_instance:
        await model_instance.abort()

app = FastAPI(lifespan=lifespan)

async def load_model():
    try:
        engine_args = vllm.AsyncEngineArgs(
            model='Qwen/Qwen2-VL-2B-Instruct',
            rope_scaling={
                "factor": 1.0,
                'type': 'linear',
                'rope_type': 'none',
            },
        )
        
        logging.info('Loading model')
        logging.info(int(time.time()))
        
        model = await vllm.AsyncLLMEngine.from_engine_args(
            engine_args,
            start_engine_loop=True
        )
        
        logging.info('Model loaded')
        logging.info(int(time.time()))
        
        return model
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        raise

@app.post("/generate")
async def generate_text():
    if not model_instance:
        return {"error": "Model not loaded"}
    try:
        # Add your generation logic here
        return {"message": "Hello World"}
    except Exception as e:
        logging.error(f"Error generating text: {e}")
        return {"error": str(e)}

@app.get("/status")
async def get_status():
    return {"status": "running", "model_loaded": model_instance is not None}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)