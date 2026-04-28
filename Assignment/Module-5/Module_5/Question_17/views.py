import requests
from django.shortcuts import render
from django.conf import settings

def twitter_feed_view(request):
    username = request.GET.get('username')
    bearer_token = getattr(settings, 'TWITTER_BEARER_TOKEN', 'your_twitter_bearer_token_here')
    
    tweets = []
    error = None
    is_sample = False

    if username:
        if bearer_token == 'your_twitter_bearer_token_here':
            # Sample Data Mode
            is_sample = True
            tweets = [
                {'text': 'Just launched our new product! Check it out at the link below. #launch #tech', 'created_at': '2024-04-21'},
                {'text': 'Web development is evolving faster than ever. Stay curious and keep learning! 🚀', 'created_at': '2024-04-20'},
                {'text': 'Great weekend spent debugging. Sometimes the smallest typo causes the biggest headache! 😂', 'created_at': '2024-04-19'},
                {'text': 'Coffee and code: my two favorite things. ☕️💻', 'created_at': '2024-04-18'},
                {'text': 'Looking forward to the upcoming tech conference. Who else is going?', 'created_at': '2024-04-17'},
            ]
        else:
            # Live API Mode (Twitter v2)
            headers = {"Authorization": f"Bearer {bearer_token}"}
            
            # Step 1: Get User ID from Username
            user_url = f"https://api.twitter.com/2/users/by/username/{username}"
            try:
                user_res = requests.get(user_url, headers=headers)
                user_data = user_res.json()
                
                if user_res.status_code == 200 and 'data' in user_data:
                    user_id = user_data['data']['id']
                    
                    # Step 2: Get Latest 5 Tweets
                    tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets?max_results=5&tweet.fields=created_at"
                    tweet_res = requests.get(tweets_url, headers=headers)
                    tweet_data = tweet_res.json()
                    
                    if tweet_res.status_code == 200 and 'data' in tweet_data:
                        tweets = tweet_data['data']
                    else:
                        error = "Unable to fetch tweets for this user."
                else:
                    error = f"User '{username}' not found or account is private."
            except Exception:
                error = "Connection error. Please check your internet or API settings."

    return render(request, 'Question_17/tweets.html', {
        'search_user': username,
        'tweets': tweets,
        'error': error,
        'is_sample': is_sample
    })
