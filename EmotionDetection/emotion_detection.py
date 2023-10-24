import requests
import json

def emotion_detector (text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)


    if response.status_code == 200:
        # Extract emotion data
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']

        # Find the dominant emotion
        dominant_emotion = max(emotion_data, key=emotion_data.get)       
        anger_score = emotion_data['anger']
        disgust_score = emotion_data['disgust']
        fear_score = emotion_data['fear']
        joy_score = emotion_data['joy']
        sadness_score = emotion_data['sadness']

    elif response.status_code == 500:
        dominant_emotion = None 
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None 
    

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }