import oauth2 as oauth
import urllib2 as urllib
import json

# See Assignment 1 instructions or README for how to get these credentials

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = "xOnewLAMiaMSySHuCyPFQ"
consumer_secret = "NDHf1tjm9sq7NwRxwqonxJoMi1l0yGsEn1xfRVvrYGg"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token_key = "159536126-P9xgwERWI1Y8sb6obMAcxAwnTZG9c0bF0PwwoARX"
access_token_secret = "UHZX3rIP3gtxjwpzD6BzEqzvskonoLNKcNMd0KhL9A"

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''


def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                                token=oauth_token,
                                                http_method=http_method,
                                                http_url=url,
                                                parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    #headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response


def fetchsamples():
    url = "https://stream.twitter.com/1/statuses/sample.json"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    count = 0
    for line in response:
        print line.strip()
        # result = json.loads(line.strip())
        # if 'text' in result.keys():
        #     print str(result).encode("utf8")
        count += 1
        if count == 500:
            break
if __name__ == '__main__':
    fetchsamples()
