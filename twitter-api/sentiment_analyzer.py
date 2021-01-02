from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from twitter_auth import NLU_key


#watson setup
authenticator = IAMAuthenticator(NLU_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(version='2020-08-01', authenticator=authenticator, service_name='Natural Language Understanding-cl')
natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com')

tweet_and_sentiment = {} 
#watson sentiment analysis
def analyze_tweet_sentiment(texts):
    negative = 0
    neutral = 0
    positive = 0
    for text in texts:
        response = natural_language_understanding.analyze(features=Features(sentiment=SentimentOptions(targets=[text])),text=text).get_result()
        sentiment = response['sentiment']
        target = sentiment['targets']
        new_dict = target[0]
        final = new_dict['label']
        if final == 'negative':
            negative += 1
            tweet_and_sentiment[text] = 'negative'
        elif final == 'positive':
            positive += 1
            tweet_and_sentiment[text] = 'positive'
        else:
            neutral += 1
            tweet_and_sentiment[text] = 'neutral'
    print("Positive tweets: " + str(positive) + ". Neutral tweets: " + str(neutral) + ". Negative tweets: " + str(negative) + ".")
    percent_positivity = positive/len(texts)
    print("The percentage of positive Tweets is: " + str(percent_positivity))
    return tweet_and_sentiment