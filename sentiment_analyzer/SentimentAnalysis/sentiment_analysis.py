# Import necessary libraries
import requests
import json

def sentiment_analyzer(text_to_analyse):

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    if response.status_code == 500:
        label = None
        score = None
    else :
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    return {
        'status_code': response.status_code, 
        'label': label,
        'score' : score
    }

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
