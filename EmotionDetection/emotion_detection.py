import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 400:
        # Return dictionary with None values for all emotions
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    else:
        response.raise_for_status()
           
    response_json = response.json()    
    # Extract emotions from the response JSON
    emotions = response_json['emotionPredictions'][0]['emotion']    
    # Find dominant emotion by max score
    dominant_emotion = max(emotions, key=emotions.get)    
    # Prepare output dictionary
    formatted_output = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }    
    return formatted_output 
