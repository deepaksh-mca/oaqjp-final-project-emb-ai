from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector 

app = Flask(__name__)

@app.route('/')
def index():
    # Render the index.html 
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotionDetector():
    if request.method == 'POST':
        data = request.get_json() or request.form
        text_to_analyze = data.get('text', '')
    else:  # GET request
        text_to_analyze = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyze)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)