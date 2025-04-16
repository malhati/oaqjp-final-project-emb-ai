"""
this is python file for flask app 
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)


@app.route('/emotionDetector')
def emotion_detectors():
    """
    emotion_detectors is view function return a text formatting about emation
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if not response.get('dominant_emotion'):
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is \
    'anger': {response.get('anger')}, \
    'disgust': {response.get('disgust')}, \
    'fear': {response.get('fear')}, \
    'joy': {response.get('joy')} \
    and 'sadness': {response.get('sadness')}. \
    The dominant emotion is <b>{response.get('dominant_emotion')}</b>."

@app.route('/')
@app.route('/index')
def index():
    """
    index is view function for render main page. 
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
