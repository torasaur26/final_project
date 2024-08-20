def emotion_detector(text_to_analyze):
    response = EmotionDetectionFunction(text_to_analyze)
    return response.text

python3.11 -m pip install requests

