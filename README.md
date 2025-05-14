# Llama Chatbot with FastAPI

A simple chatbot interface using the LLaMA 2-7B model through Replicate's API, with a FastAPI backend and HTML/CSS/JavaScript frontend.

## Features

- Chat interface with LLaMA 2-7B model
- Responsive design for different screen sizes
- Real-time message display
- Simple and clean UI

## Technologies Used

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: LLaMA 2-7B via Replicate API
- **Middleware**: CORS for cross-origin requests

## Setup Instructions

### Prerequisites

- Python 3.7+
- Replicate API token
- FastAPI and Uvicorn installed

### Installation

1. Clone the repository: 
    git clone https://github.com/Greed003/ollama-chatbot.git
2. Install required Python packages: 
    pip install fastapi uvicorn replicate python-dotenv

## Running the Application

1. Start the FastAPI server:
    uvicorn main:app --reload
2. Open the HTML file in your browser or serve it through a local server
