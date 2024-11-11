import vllm
import loguru
import time
import fastapi
import uvicorn
import asyncio
import requests

logging = loguru.logger




async def real_load_model():

    # model_instance = None

    app = fastapi.FastAPI()


    @app.post("/generate")
    async def generate_text():
        # if model_instance is None:
        #     return {"message": "Model not loaded"}
        return {"message": "Hello World"}
    
    async def load_model():
        engine_args = vllm.AsyncEngineArgs(
            model='Qwen/Qwen2-VL-2B-Instruct',
        )
    
        logging.info('Loading model')
        logging.info(int(time.time()))
    
        model_instance = vllm.AsyncLLMEngine.from_engine_args(
            engine_args,
        )
    
        logging.info('Model loaded')
        logging.info(int(time.time()))
    
        return model_instance

    async def run_test():
        import time
        print('into test!' + str(int(time.time())))
        await asyncio.sleep(20)
        # time.sleep(20)
        print('out of test!' + str(int(time.time())))
        # return {"message": "Hello test"}


    logging.info("-Child- loading model")
    # asyncio.run(load_model())
    # asyncio.run(run_test())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(run_test())
    # await run_test()
    await load_model()
    logging.info("-Child- running api")
    # await uvicorn.run(app, host="0.0.0.0", port=6910)


async def real_generate_text():
    data = {}
    response = requests.post('http://localhost:6910/generate', json=data)
    if response.status_code == 200:
        print('Success!')
        print('Response:', response.json())
    else:
        print('Failed with status code:', response.status_code)
        print('Error:', response.text)



# results_generator  = model_instance.generate(
#     'who are u ?',
#     sampling_params=vllm.SamplingParams(
#         max_tokens=100,
#         temperature=0.5,
#         top_k=50,
#         top_p=0.95,
#     ),
#     request_id='test',
# )


# import asyncio


# # Assuming model_instance and vllm are already defined above
# async def process_results():
#     try:
#         async for request_output in results_generator:
#             print("Generated output:", request_output.outputs[0].text)
#             print("Request ID:", request_output.request_id)
#     except Exception as e:
#         logging.error(f"Error processing results: {e}")

# async def main():
#     await process_results()
#     timestamp2 = int(time.time())
#     logging.info(timestamp2)
#     logging.info('finished')

# # Run the async code
# if __name__ == "__main__":
#     asyncio.run(main())



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






