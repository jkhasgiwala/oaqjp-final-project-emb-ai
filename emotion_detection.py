import requests
import json

def emotion_detector(text_to_analyze: str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {'raw_document': {'text': text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers)
    formatted_response = json.loads(response.text)

    dominant_emotion = ''
    high_score = 0
    new_emotion_dict = {}
    emotions_dict = formatted_response['emotionPredictions'][0]['emotion']
    for emotion, score in emotions_dict.items():
        new_emotion_dict[emotion] = score
        if score > high_score:
            high_score = score
            dominant_emotion = emotion
    new_emotion_dict['dominant_emotion'] = dominant_emotion
    
    return new_emotion_dict