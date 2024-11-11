import vllm
import loguru
import time
logging = loguru.logger
engine_args = vllm.AsyncEngineArgs(
    model='Qwen/Qwen2-VL-2B-Instruct',
    rope_scaling={"factor": 1.0},
)
logging.info('Loading model')
# timestamp0 = vllm.utils.get_timestamp()
timestamp = int(time.time())
# logging.info(timestamp0)
logging.info(timestamp)
# model_instance = vllm.AsyncLLMEngine(engine_args,log_requests=True,start_engine_loop=False)
model_instance = vllm.AsyncLLMEngine.from_engine_args(engine_args,start_engine_loop=True)
# (engine_args)
logging.info('Model loaded')
timestamp1 = int(time.time())
logging.info(timestamp1)