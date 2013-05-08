import json


def parser_text(response):
    tweets = []
    for line in response:
        result = json.loads(line.strip())
        if 'text' in result.keys():
            tweets.append(result['text'].encode("utf8"))
    return tweets


def parser_text_state(response):
    txst = []
    for line in response:
        result = json.loads(line.strip())
        if 'place' in result.keys() and (result['place'] is not None):
            if 'country_code' in result['place'].keys() and result['place']['country_code'] == 'US':
                state = result['place']['full_name'].split(", ")[1]
                txst.append({result['place']: state})
    return txst
