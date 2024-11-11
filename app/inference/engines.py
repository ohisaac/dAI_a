import vllm
import loguru

import time


logging = loguru.logger


engine_args = vllm.AsyncEngineArgs(
    model='Qwen/Qwen2-VL-2B-Instruct',
)

logging.info('Loading model')

# timestamp0 = vllm.utils.get_timestamp()
timestamp = int(time.time())


# logging.info(timestamp0)
logging.info(timestamp)


# model_instance = vllm.AsyncLLMEngine(engine_args,log_requests=True,start_engine_loop=False)
model_instance = vllm.AsyncLLMEngine.from_engine_args(engine_args,start_engine_loop=False)

# (engine_args)


logging.info('Model loaded')
timestamp1 = int(time.time())
logging.info(timestamp1)

results_generator  = model_instance.generate(
    'who are u ?',
    sampling_params=vllm.SamplingParams(
        max_tokens=100,
        temperature=0.5,
        top_k=50,
        top_p=0.95,
    ),
    request_id='test',
)


import asyncio
import time
import logging

# Assuming model_instance and vllm are already defined above
async def process_results():
    try:
        async for request_output in results_generator:
            print("Generated output:", request_output.outputs[0].text)
            print("Request ID:", request_output.request_id)
    except Exception as e:
        logging.error(f"Error processing results: {e}")

async def main():
    await process_results()
    timestamp2 = int(time.time())
    logging.info(timestamp2)
    logging.info('finished')

# Run the async code
if __name__ == "__main__":
    asyncio.run(main())



# final_output = None

# async def process_results():
#     global final_output
#     async for request_output in results_generator:
#         final_output = request_output

# import asyncio

# async def main():
#     await process_results()
    
#     timestamp2 = int(time.time())
#     logging.info(timestamp2)
#     logging.info('finished')

# asyncio.run(main())






