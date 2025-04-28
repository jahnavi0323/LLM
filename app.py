import openai
import time

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def get_llm_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "user", "content": prompt}
            ],
            timeout=15  # Optional: set a timeout for the request
        )
        return response
    except openai.error.AuthenticationError:
        print("Authentication failed. Check your API key.")
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Waiting before retrying...")
        time.sleep(5)  # Wait and you could retry here if you want
    except openai.error.APIConnectionError:
        print("Network error. Please check your internet connection.")
    except openai.error.Timeout:
        print("Request timed out. Try again.")
    except openai.error.OpenAIError as e:
        # Generic catch-all for
