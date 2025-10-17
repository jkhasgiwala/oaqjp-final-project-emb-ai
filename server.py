from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return "Invalid Text! Please try again!"

    # Return a formatted string with the sentiment label and score
    ret_val = "For the given statement, the system response is"
    dominant_enotion = ""
    for emotion, score in response.items():
        if emotion != 'dominant_emotion':
            ret_val += " '" + emotion + "': " + str(score) + ","
        else:
            dominant_emotion = score
    # get rid of last comma
    ret_val = ret_val[:-1]
    ret_val += ". The dominant emotion is " + dominant_emotion + "."
    return ret_val

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
