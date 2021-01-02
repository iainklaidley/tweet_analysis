from twitter_auth import consumer_key, consumer_secret, access_token_key, access_token_secret, NLU_key
import twitter

api = twitter.Api(consumer_key=consumer_key, 
consumer_secret=consumer_secret, 
access_token_key=access_token_key, 
access_token_secret=access_token_secret)

texts = []
def search_twitter(subject):
    results = api.GetSearch(term=subject, count=quantity, return_json=True, lang='en', result_type='popular')
    try:
        for result in results.values():
            for item in result:
                texts.append(item['text'])
    except:
        print('Finished regular Tweets; could not parse metadata.')

search_term = input("What do you want to query Twitter for? ")
quantity = input("And how many Tweets do you want to search over? Maximum is 200. ")
