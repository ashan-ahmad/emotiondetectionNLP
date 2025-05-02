import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=input_json)
    if not text_to_analyze.strip():  # Check for blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    elif response.status_code == 200:
        try:
            emotion_data = json.loads(response.text)
            if emotion_data and 'emotionPredictions' in emotion_data and len(emotion_data['emotionPredictions']) > 0 and 'emotion' in emotion_data['emotionPredictions'][0]:
                emotions = emotion_data['emotionPredictions'][0]['emotion']
                anger_score = emotions.get('anger', 0)
                disgust_score = emotions.get('disgust', 0)
                fear_score = emotions.get('fear', 0)
                joy_score = emotions.get('joy', 0)
                sadness_score = emotions.get('sadness', 0)

                dominant_emotion = max(emotions, key=emotions.get)

                formatted_output = {
                    'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score,
                    'dominant_emotion': dominant_emotion
                }
                return formatted_output
            else:
                return None
        except json.JSONDecodeError as e:
            return None
    else:
        return None