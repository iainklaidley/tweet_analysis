from twitter_scrape_function import search_twitter, texts, search_term
from sentiment_analyzer import tweet_and_sentiment, analyze_tweet_sentiment
from write_results import write_results_to_csv

#invokes the function in the twitter_scrape_function file
search_twitter(search_term)

#takes the results (a list, texts) from search_twitter and runs in through the analyze_tweet_sentiment function
result = analyze_tweet_sentiment(texts)

#takes the dictionary produced by analyze_tweet_sentiment and writes it to CSV
write_results_to_csv(search_term, result)



