import json
import requests 


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": 
    "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json= my_obj)
    raw_response = response.text
    formatted_response = json.loads(raw_response)
    
    if response.status_code == 400:
        emotion = {}
        emotion['sadness'] = None
        emotion['joy'] = None
        emotion['fear'] = None
        emotion['disgust'] = None
        emotion['anger'] = None
        emotion['dominant_emotion'] = None 
        return emotion

    emotion = formatted_response['emotionPredictions'][0]['emotion']

    

    max_key = max(emotion, key=emotion.get)
    emotion['dominant_emotion'] = max_key
    
    return emotion

