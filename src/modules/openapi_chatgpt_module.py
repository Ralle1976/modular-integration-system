import openai

class OpenAIChatGPTModule:
    def __init__(self, api_key):
        openai.api_key = api_key
    
    def send_message(self, prompt, model="gpt-3.5-turbo"):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"ChatGPT API-Fehler: {str(e)}")
    
    def get_usage_stats(self):
        try:
            response = openai.Organization.get_usage()
            return response
        except Exception as e:
            raise Exception(f"Fehler beim Abrufen der Nutzungsstatistiken: {str(e)}")