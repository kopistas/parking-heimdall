import requests


class DescriptionService:
    def __init__(self, llm_url, llm_authorization_token):
        self.llm_url = llm_url
        self.llm_authorization_token = llm_authorization_token

    def generate_description(self, numberOfFreePlaces: int):
        endpoint = f"{self.llm_url}/get-llm-response"

        headers = {
            'Authorization': f'Bearer {self.llm_authorization_token}',
            'Content-Type': 'application/json'
        }

        # Request body as JSON
        payload = {
            "systemMessage": 'Представь что ты умный ассистент, который помогает пользователю в дороге. Твоя задача ясно и коротко рассказать пользователю о количестве свободных мест на парковке. Говори уважительно, но сделай фразу не очень сухой. Количество мест будет передано далее.',
            "userPrompt": f"Количество свободных мест: {numberOfFreePlaces}"
        }

        response = requests.get(endpoint, headers=headers, json=payload)

        if response.status_code == 200:
            # Parse the JSON response
            print(response)
            data = response.json()
            system_response = data.get('response', 'No response from the system')
            return system_response
        else:
            return f"Количество мест на парковке: {numberOfFreePlaces}"
