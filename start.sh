#!/usr/bin/env bash

echo "Starting backend..."
uvicorn backend.api:app --host 0.0.0.0 --port $PORT &

sleep 5

echo "Starting frontend..."
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0