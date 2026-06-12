# core/vllm_client.py

import requests


class VLLMClient:

    def __init__(
        self,
        base_url="http://localhost:8000/v1/chat/completions",
        # model_name="Qwen/Qwen2-7B-Instruct"
        model_name = "Qwen/Qwen2.5-14B-Instruct"
    ):

        self.base_url = base_url
        self.model_name = model_name

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 2048
    ) -> str:

        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        try:

            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=180
            )

            if response.status_code != 200:
                print("STATUS:", response.status_code)
                print("RESPONSE:", response.text)
                return f"Connection Failed: {response.text}"

            return response.json()[
                "choices"
            ][0]["message"]["content"]

        except Exception as ex:

            return (
                f"Connection Failed: {str(ex)}"
            )