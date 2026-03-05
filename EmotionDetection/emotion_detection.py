import requests 
import json

# Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse): 

    # Define a function named emotion_detector that takes a string input (text_to_analyse) 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    # URL of the emotion_detector service 
    myobj = { "raw_document": { "text": text_to_analyse } } 
    # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header)
    #7 If the response status code is 400, make the function return the same dictionary
    # but with values for all keys being "None" 
    if response.status_code == 400:
        extracted_emotions = {
            'anger': 'None',
            'disgust': 'None',
            'fear': 'None',
            'joy': 'None',
            'sadness': 'None',
            'dominant_emotion': 'None'
        }
        return extracted_emotions
    else:
        #3.1 Convert the response text into a dictionary using json library func
        formatted_response = json.loads(response.text)
        #3.2 Extract the required set of emotions (anger, disgust, fear, joy and sadness) along w scores
        prediction = formatted_response["emotionPredictions"][0]
        emotions = prediction["emotion"]
        # Define the required emotions
        required_emotions = ["anger", "disgust", "fear", "joy", "sadness"]
        # Extract only the required emotions with their scores
        extracted_emotions = {emotion: emotions.get(emotion, 0) for emotion in required_emotions}
        #3.3 Find the demoninant emotion and its score
        dominant_emotion = max(extracted_emotions, key=extracted_emotions.get) 
        #3.4 modify dictionary to add 'dominant_emotion': name of dominant emotion
        extracted_emotions['dominant_emotion'] = dominant_emotion

        # Returning a dictionary containing sentiment analysis results 
        return extracted_emotions