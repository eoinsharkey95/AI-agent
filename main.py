
# Import and check API key
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError ("API key not found")


# Create new instance of Gemini Client
from google import genai
client = genai.Client(api_key=api_key)



def main():
    print("Hello from ai-agent!")
    response = client.models.generate_content( 
        model = 'gemini-2.5-flash',
        contents= "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

    if response.usage_metadata == None:
        raise RuntimeError("No usage metadata present - likely failed API request")
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(f'Prompt tokens: {prompt_tokens}')
    print(f'Response tokens: {response_tokens}')

    print(response.text)



if __name__ == "__main__":
    main()
