import google.generativeai as genai
import base64
from PIL import Image
import io

# Configure your API key
# Replace "YOUR_API_KEY" with your actual Google Gemini API Key
# It's recommended to load your API key from environment variables for security.
# For example: import os; genai.configure(api_key=os.environ["GEMINI_API_KEY"])
genai.configure(api_key="YOUR_API_KEY") # <<< IMPORTANT: Replace with your API Key

def generate_image(prompt: str, output_filename: str = "old_dog_image.png"):
    """
    Generates an image using the Imagen model and saves it to a file.

    Args:
        prompt (str): The descriptive text for the image to be generated.
        output_filename (str): The name of the file to save the generated image.
    """
    try:
        # Select the image generation model (imagen-3.0-generate-002)
        # Note: 'predict' method is used with this specific model for image generation
        model = genai.GenerativeModel('imagen-3.0-generate-002')

        print(f"Generating image for prompt: '{prompt}'...")

        # Make the API call for image generation
        # The 'generate_content' method is used, with prompt as content
        # and generation_config for model parameters like sampleCount.
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.9, # Adjust temperature for creativity (0.0 to 1.0)
                candidate_count=1, # Number of images to generate
            )
        )

        # Check if the response contains images and extract the first one
        if response.candidates:
            # The image data is in base64 format within the 'media' object
            # Access the first part's image data
            image_data_base64 = response.candidates[0].content.parts[0].blob.data

            # Decode the base64 string to bytes
            image_bytes = base64.b64decode(image_data_base64)

            # Open the image using Pillow and save it
            image = Image.open(io.BytesIO(image_bytes))
            image.save(output_filename)
            print(f"Image successfully saved as '{output_filename}'")
        else:
            print("No image candidates found in the response.")
            if response.prompt_feedback:
                print(f"Prompt feedback: {response.prompt_feedback.block_reason}")
                print(f"Safety ratings: {response.prompt_feedback.safety_ratings}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Define the prompt for the old dog image
image_prompt = "An old, wise-looking dog, perhaps a golden retriever or labrador, with grey fur around its muzzle and eyes, in a warm and peaceful setting. It should convey a sense of calm and gentle wisdom."

# Call the function to generate and save the image
if __name__ == "_main_":
    generate_image(image_prompt)