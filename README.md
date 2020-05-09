# MNC Ranking using Realtime data
## Description
The project fetch data from twitter and by doing sentiment analysis it will rank the Multi National Companies.
The algorithm used in this project is Bernoulli Naive Bayes Classifier. You may test other Algorithm too, which are commented in the main `mod_sentiment` file. **BernoulliNB** will give the most accurate result amongst them.

## Dataset Information
More than 10k Positive and Negative review datasets are present in `dataset`.

## Requirements
There are some general library requirements for the project and some which are specific to individual methods. The general requirements are as follows.  
* `numpy`
* `scikit-learn`
* `pandas`
* `nltk`
* `tweepy`

## Usage
### Steps
1. Get [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access) for realtime results
1. Clone this repo on your Computer
1. Input your keys / credentials in `twitter_credentials`
1. Make sure all required python packages are installed on your system before proceeding. If not then, use command ``` pip install "packagename"``` to install package
1. Run command

    ``` python3 main.py ```
    
    or 

    ``` python main.py ```

**Note**: Python 3 is used in this project
## Extras
You can try Different model by uncommenting the lines in the `mod_sentiment` file according to your need. It have 3 algorithm `DecisionTreeClassifier, MultinomialNB and BernoulliNB` but you will get better Results with BernoulliNB.
After Training model save your trained model using [pickle](https://docs.python.org/3/library/pickle.html) to save time when you use model next time.

## Credits
[sentdex](https://www.youtube.com/user/sentdex) for Natural Language Processing Tutorial