from flask import Flask, render_template, request, jsonify
import openai
import requests

# Set your API keys
openai.api_key = 'YOUR_OPENAI_API_KEY'
deepai_api_key = 'YOUR_DEEPAI_API_KEY'

# Initialize Flask app
app = Flask(__name__)

# Function to generate character description using OpenAI GPT-3
def generate_character_description(personality, appearance):
    prompt = f"Create a detailed description of a new anime character with the following traits:\n- Personality: {personality}\n- Appearance: {appearance}\nThe description should include the character's name, background, and any unique characteristics."
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # or use 'gpt-4' if you have access
        prompt=prompt,
        max_tokens=150
    )
    
    # Extract the generated description
    return response.choices[0].text.strip()

# Function to generate anime-style character image using DeepAI
def generate_anime_image(description):
    url = "https://api.deepai.org/api/text2img"
    headers = {'api-key': deepai_api_key}
    data = {'text': description}

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()['output_url']  # URL of the generated image
    else:
        return "Error generating image"

# Render HTML page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Handle character creation via POST request
@app.route('/create_character', methods=['POST'])
def create_character():
    # Get data from the user (e.g., traits like personality, appearance)
    personality = request.form.get('personality')
    appearance = request.form.get('appearance')

    # Step 1: Generate character description using GPT-3
    character_description = generate_character_description(personality, appearance)

    # Step 2: Generate anime character image using DeepAI
    character_image_url = generate_anime_image(character_description)

    # Return a JSON response with description and image URL
    return jsonify({
        'description': character_description,
        'image_url': character_image_url
    })

if __name__ == '__main__':
    app.run(debug=True)
