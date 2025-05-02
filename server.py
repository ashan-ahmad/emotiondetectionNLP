"""This module implements a Flask web application for emotion detection."""
from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)  # pylint: disable=invalid-name

@app.route('/emotion_detector', methods=['POST'])  # pylint: disable=undefined-variable
def emotion_detector_route():
    """
    Receives text input via POST request, analyzes the emotion using the
    emotion_detector function, and returns the results as a JSON response.
    Handles blank input by returning an error message.
    """
    if request.method == 'POST':  # pylint: disable=undefined-variable
        text_to_analyze = request.form['text']  # pylint: disable=undefined-variable
        result = emotion_detector(text_to_analyze)  # pylint: disable=undefined-variable
        if result and result['dominant_emotion'] is not None:
            output_string = (
                f"For the given statement, the system response is 'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
                f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )
            return jsonify(output=output_string, emotion_result=result)  # pylint: disable=undefined-variable
        return jsonify(output="Invalid text! Please try again!", emotion_result=None), 400  # pylint: disable=undefined-variable
    return jsonify(output="Invalid request method!", emotion_result=None), 405  # Explicit return for non-POST

@app.route('/')
def index():
    """Renders the index.html page."""
    return render_template('index.html')  # pylint: disable=undefined-variable

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # pylint: disable=undefined-variable
    