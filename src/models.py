from typing import List, Dict

from openai import OpenAI


class ModelInterface:
    def chat_completion(self, messages: List[Dict]) -> str:
        pass

    def image_generation(self, prompt: str) -> str:
        pass


class OpenAIModel(ModelInterface):
    def __init__(self, api_key: str, model_engine: str, base_url: str, image_size: str = '512x512'):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model_engine = model_engine
        self.image_size = image_size

    def chat_completion(self, messages) -> str:
        response = self.client.chat.completions.create(
            model=self.model_engine,
            messages=messages
        )
        return response

