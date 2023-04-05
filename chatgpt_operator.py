from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import openai


class ChatGPTOperator(BaseOperator):
    @apply_defaults
    def __init__(self, api_key, prompt, *args, max_tokens=1024, temperature=0.5, engine="text-davinci-002", **kwargs):
        super().__init__(*args, **kwargs)
        self.api_key = api_key
        self.prompt = prompt
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.engine = engine

    def execute(self, context):
        # Set up the OpenAI API client
        openai.api_key = self.api_key

        # Generate a response using the ChatGPT API
        response = openai.Completion.create(
            engine=self.engine,
            prompt=self.prompt,
            max_tokens=self.max_tokens,
            n=1,
            stop=None,
            temperature=self.temperature,
        )

        # Log the response and return it
        self.log.info(f"Generated response: {response.choices[0].text}")
        return response.choices[0].text