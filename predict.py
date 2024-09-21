from cog import BasePredictor, Input
import subprocess
import requests
import json

MODEL_NAME = "llama2"
URL = 'http://localhost:11434/api/generate'


class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        subprocess.Popen(["ollama", "serve"])
        # Start server
        print("Starting ollama server...")
        subprocess.Popen(["ollama", "serve"])
        # Download Model and Run
        print("Downloading/Running model...")
        subprocess.check_call(["ollama", "run", MODEL_NAME], close_fds=False)

    def predict(self, prompt: str = Input(description="Input text for the model")) -> str:
        """Run a single prediction on the model"""
        
        data = {
            "model": MODEL_NAME,
            "prompt": prompt
        }
        headers={'Content-Type': 'application/json'}
        response = requests.post(URL, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            return response.json()
        raise "ERROR!!!!"

        
