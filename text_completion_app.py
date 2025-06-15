import os
from huggingface_hub import InferenceClient # Import the InferenceClient

# Initialize the Hugging Face Inference Client
# It will automatically look for the HF_TOKEN environment variable
# You can specify a default model here, or pass it to get_completion
# For text generation, `model` is important.
# I'm using "HuggingFaceH4/zephyr-7b-beta" as an example.
client = InferenceClient() # Will use HF_TOKEN from environment

def get_completion_hf(prompt_text, model="HuggingFaceH4/zephyr-7b-beta", temperature=0.5, max_new_tokens=10, top_p=0.9, do_sample=True):
    """
    Sends a prompt to the Hugging Face Inference API model and returns the completion.
    """
    if not prompt_text.strip():
        return "Error: Input prompt cannot be empty."

    try:
        # The .text_generation() method is used for causal language models
        # Parameters might vary slightly between models, but these are common
        response = client.text_generation(
            prompt_text,
            model=model,
            max_new_tokens=max_new_tokens, # Renamed from max_tokens for clarity with HF
            do_sample=do_sample,         # Set to True for creative generation
            temperature=temperature,
            top_p=top_p,
            # You might need to adjust other parameters like `stop_sequences`
            # or `repetition_penalty` depending on the model and desired output
        )
        return response
    except Exception as e:
        # Hugging Face errors might look different from OpenAI errors
        return f"An error occurred with Hugging Face: {e}"

if __name__ == "__main__":
    print("AI-Powered Text Completion App (using Hugging Face Inference API)")
    print("Type 'quit' or 'exit' to end the session.")

    # You can specify the model to use here, or let the function default
    # chosen_model = "mistralai/Mistral-7B-Instruct-v0.2" # Example alternative
    # print(f"Using model: {chosen_model}")

    while True:
        user_input = input("\nEnter your prompt: ")
        if user_input.lower() in ['quit', 'exit']:
            break

        # Call the Hugging Face specific completion function
        # You can pass model, temperature etc. explicitly here if you want to allow user input for them
        response = get_completion_hf(user_input)
        print("\nAI Response:")
        print(response)