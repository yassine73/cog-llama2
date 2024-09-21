from cog import BasePredictor, Input
from langchain_ollama import ChatOllama
import subprocess
import requests
import json
import time

MODEL_NAME = "llama2"
URL = 'http://localhost:11434/api/generate'

class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        print("Launch ollama server...")
        subprocess.Popen(["ollama", "serve"])
        time.sleep(2)
        print("Start", MODEL_NAME + "...")
        subprocess.check_output(["ollama", "run", MODEL_NAME])

    def predict(self, prompt: str = Input(description="Input text for the model")) -> str:
        """Run a single prediction on the model"""
        data = {
            "model": MODEL_NAME,
            "prompt": prompt
        }
        headers={'Content-Type': 'application/json'}
        response = requests.post(URL, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            return str(response.json())
        raise "ERROR!!!!"        

        
