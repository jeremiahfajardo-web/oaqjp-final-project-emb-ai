# Import Flask, render_template, request from the flask framework package : DONE
from flask import Flask, render_template, request
# Import the emotion detector function from the package created: DONE
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : DONE
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # DONE
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Define the required emotions
    required_emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    # Extract only the required emotions with their scores
    extracted_emotions = {
        emotion: response.get(emotion, 0)
        for emotion in required_emotions
    }

    # Build the requested formatted string
    emotion_str = ", ".join(
        f"'{emotion}': {score}"
        for emotion, score in extracted_emotions.items()
    )

    # Get dominant emotion
    dominant = response.get("dominant_emotion", "unknown")

    # Final formatted sentence
    final_sentence = (
        f"For the given statement, the system response is {emotion_str}. "
        f"The dominant emotion is {dominant}."
    )

    return final_sentence

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # DONE
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    #DONE
    app.run(host="0.0.0.0", port=5000)
