from flask import Flask, render_template, request, jsonify
import openai

# Set up your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api_request():
    user_message = request.form.get('message')

    # Make a request to OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=100
    )

    # Extract the response message from OpenAI API response
    bot_response = response['choices'][0]['text']

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
