import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "iCtivea7asU56CctwkXYeq6mr",
    "consumer_secret"     : "Dbgwxr2oogfjqjY8N2qRa1hrrfqQVO5tJa092ietA8bULnFLz3",
    "access_token"        : "966152761661382656-JAMFEevUQzu4Xtocc2D4bPbVsVSEnAw",
    "access_token_secret" : "okilIX6MuVSurf62Tnj06DqkdTAM0m7w5p7S4yYmLPbi8" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
