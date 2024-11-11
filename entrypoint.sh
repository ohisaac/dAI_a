#!/bin/bash
uvicorn --lifespan on --port 8888 --host 0.0.0.0 app.asgi:app

