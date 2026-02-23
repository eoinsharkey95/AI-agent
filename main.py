
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

# Set up new instance of our arg parser
import argparse
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

def main():
    print("Hello from ai-agent!")
    response = client.models.generate_content( 
        model = 'gemini-2.5-flash',
        contents= args.user_prompt
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
