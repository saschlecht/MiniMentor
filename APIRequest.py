import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from DBConnection import database_bp

app = Flask(__name__)
API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key="API_KEY")

app.register_blueprint(database_bp, url_prefix="/db_bp")

@app.route('/')
def home():
  return render_template('HomePage.html')

@app.route('/tips/')
def tips():
    return render_template('Tips.html')

@app.route('/howto/')
def howto():
    return render_template('HowTo.html')

@app.route('/history/')
def history():
    return render_template('History.html')

@app.route('/signup/')
def signup():
    return render_template('SignUp.html')

@app.route('/get-completion', methods=['POST'])
def get_completion():
    content = request.json.get('content')
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly and helpful professional assistant. You take paragraphs as inputs and change a few words to make the input sound more professional."},
            {"role": "user", "content": content},
        ]
    )
    revised_text = completion.choices[0].message.content
    # Placeholder for difference logic
    difference = "Difference calculation not implemented."  
    return jsonify({"original": content, "revised": revised_text, "difference": difference})

# This route can be added to test the textDiff functionality once we've implemented it
# It should accept two texts and return their differences
@app.route('/text-diff', methods=['POST'])
def text_diff():
    str1 = request.json.get('str1')
    str2 = request.json.get('str2')
    # Here we need to implement the logic to find and return the differences between str1 and str2
    difference = "Functionality to find differences not implemented."
    return jsonify({"difference": difference})

if __name__ == "__main__":
    app.run(debug=True, port=5100)
    
