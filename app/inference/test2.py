import vllm
from vllm import AsyncLLMEngine, SamplingParams
import asyncio
import time
# import logging
import loguru


logging = loguru.logger

# Initialize the engine
async def init_engine():
    engine_args = vllm.AsyncEngineArgs(
        model='Qwen/Qwen2-VL-2B-Instruct',
    )
    # engine = AsyncLLMEngine.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")
    engine = vllm.AsyncLLMEngine.from_engine_args(engine_args, start_engine_loop=True)

    return engine

async def process_results(engine):
    try:
        sampling_params = SamplingParams(
            max_tokens=100,
            temperature=0.5,
            top_k=50,
            top_p=0.95
        )
        
        # results = await engine.generate(
        #     "who are u ?", 
        #     sampling_params,
        #     request_id='test',
        # )
        
        # for result in results:
        #     print("Generated output:", result.outputs[0].text)
        #     print("Request ID:", result.request_id)

        async for result in engine.generate(
            "who are u ?", 
            sampling_params,
            request_id='test',
        ):
            print("Generated output:", result.outputs[0].text)
            print("Request ID:", result.request_id)
            
    except Exception as e:
        logging.error(f"Error processing results: {e}")

async def main():
    engine = await init_engine()
    try:
        await process_results(engine)
        timestamp2 = int(time.time())
        logging.info(timestamp2)
        logging.info('finished')
    finally:
        logging.info('Aborting request')
        await engine.abort(request_id='test')
        # await engine.shutdown()

if __name__ == "__main__":
    asyncio.run(main())

    