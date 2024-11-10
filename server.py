"""Module providing a function emotion detect."""
from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion detection")

@app.route("/")
def render_index_page():
    """Function rendering index.html"""
    return render_template('index.html')


@app.route("/emotionDetector")
def emot_detector():
    """Function analyze emotion"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    all_results = [anger, disgust, fear, joy, sadness, dominant_emotion]

    if anger is None:
        return "Invalid text! Please try again!."
    res1 = "For the given statement, the system response is "
    res2 = f"'anger': { all_results[0]},'disgust': { all_results[1]},"
    res3 = f"'fear': { all_results[2]}, 'joy': { all_results[3]}"
    res4 = f"and 'sadness': { all_results[4]}. The dominant emotion is { all_results[5]}"
    return res1 + res2 + res3 + res4


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
