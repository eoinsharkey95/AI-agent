

import os
from dotenv import load_dotenv
from prompts import *


from google import genai
from google.genai import types
import argparse

from call_function import *

def main():
    print("Hello from ai-agent!")
    
    # Set up new instance of our arg parser
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Import and check API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError ("API key not found")
    
    # Create new instance of Gemini Client
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    if args.verbose:
        print(f'User prompt: {args.user_prompt}\n')

    generate_content(client, messages, args.verbose)



def generate_content(client, messages, verbose):
    
    # Generate a response from the LLM client, record the output
    response = client.models.generate_content( 
        model='gemini-2.5-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            # Provide the input system prompt, limiting function of LLM to specified activities
            system_instruction=system_prompt,
            temperature=0,
            # Provide a list of tools the LLM can use
            tools=[available_functions]
            )
    )
    # Error handling for failed API request
    if not response.usage_metadata:
        raise RuntimeError("No usage metadata present - likely failed API request")
    
    # Collect information on compute used
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    
    if verbose:
        print(f'Prompt tokens: {prompt_tokens}')
        print(f'Response tokens: {response_tokens}')
    
    print("Response:")
    
    # Check if there are function calls in the response
    if not response.function_calls:
        # Only print text if there are NO function calls
        print(response.text)

    else:
        function_results = []   # set up empty list for non-error results

        for function_call in response.function_calls:           
            # Call the requested function
            function_call_result = call_function(function_call, verbose)
            
            # Error handling for failed function call
            if not function_call_result.parts:
                raise Exception('Error: result contains no .parts')
            
            if not function_call_result.parts[0].function_response:
                raise Exception('Error: No FunctionResponse object returned by function')
            
            if not function_call_result.parts[0].function_response.response:
                raise Exception('Error: No FunctionResponse response returned by function')
            
            # Add the result to the list of results
            function_results.append(function_call_result.parts[0])
            
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            





if __name__ == "__main__":
    main()
