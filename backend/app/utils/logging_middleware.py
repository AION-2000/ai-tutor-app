from fastapi import Request, Response
import json

async def log_raw_request_body(request: Request, call_next):
    """
    Middleware to log the raw request body for debugging.
    """
    # Get the raw body
    body = await request.body()
    print("\n--- RAW REQUEST BODY RECEIVED ---")
    print(body)
    print("--- END RAW BODY ---\n")

    # Call the next middleware or endpoint
    response = await call_next(request)
    return response