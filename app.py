from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import replicate
import os

# Set Replicate API Key (Replace with your own key)
os.environ["REPLICATE_API_TOKEN"] = "r8_03soQ9WiMeBarSQGJU6oiXt9sRYnwgo3L6PCu"

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/chat")
async def chat(prompt: dict):
    try:
        # Get response from Replicate API
        response_stream = replicate.run(
            "meta/llama-2-7b-chat",
            input={"prompt": prompt["message"], "max_length": 200}
        )

        # Convert response to a single string
        response_text = "".join(response_stream).strip()

        # Ensure the response is properly formatted
        clean_response = response_text.replace(" ,", ",").replace(" .", ".").replace("\n", " ")

        return {"response": clean_response}

    except Exception as e:
        return {"error": str(e)}