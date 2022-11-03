# ADS-509_Final_Project_Team1
Analytical text mining

### Short description of your project and objectives:
We are to use Twitter API “Tweepy'' to scrape tweets off the official page of some popular cryptocurrencies and build a supervised machine learning model to classify for corresponding labels (crypto type); Then we are to build a topic model using various text mining techniques to evaluate on how well the topics identified for our tweets lined up with the labels (cryptos types). The designated end goal for deployment is to use “flask” to upload our model(s) to the website (local host) as an end product to predict crypto types based on keyword(s) from user input.
### Name of your selected dataset: Approximately 1000 tweets (with retweets) per cryptocurrency, for a total of five cryptocurrencies.
### Description of your selected dataset (data source, number of variables, size of dataset, etc.):
We are pulling approximately 1000 tweets per cryptocurrency for a total of five crypto types from twitter API. Using “client.get_users_tweets” to perform a maximum of 15 pulls with 100 tweets per pull. Since some cryptocurrencies have less tweets than others, we ended up getting:
For Bitcoin: 1498 tweets.
For Ethereum: 1497 tweets.
For Cardano, 1496 tweets.
For Dogecoin: 957 tweets.
For Shiba Inu: 770 tweets, for a total of 6218 tweets with two columns: “crypto_type” for crypto types and “tweets” for each tweet we pulled for each crypto.
