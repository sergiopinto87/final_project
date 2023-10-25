"""Module providing a function flask and Emotion detection."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Function sending text to analyzer."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    result_message = "For the given statement, the system response is: \n"
    result_message += f"'anger': {anger}, \n"
    result_message += f"'disgust': {disgust}, \n"
    result_message += f"'fear': {fear}, \n"
    result_message += f"'joy': {joy}, \n"
    result_message += f"'sadness': {sadness}. \n"
    result_message += f"The dominant emotion is {dominant_emotion}."
    return result_message

@app.route("/")
def render_index_page():
    """Function rendering index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

##End-of-file (EOF)
