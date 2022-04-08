import requests
from datetime import datetime
def sendWebhook(project, price,website,discord,twitter,type):
    url = 'https://discord.com/api/webhooks/890562915130818623/DC7dnLR0zfZrECrNMAtsMUqvkhJBQOdY64_yHYFFJQk6OImI4-aBOaCiEZEejR9rG40w'
    data = {}
    if website is None:
        website = 'None'
    if discord is None:
        discord = 'None'
    if twitter is None:
        twitter = 'None'
    print(project, price,website,discord,twitter,type)
    desc = f'{project} is dropping today !!'
    type_field = {
        'name' : 'TYPE',
        'value' : type,
        'inline' : True
    }
    price_field = {
        'name' : 'PRICE',
        'value' : f'{price}',
        'inline' : True
    }
    website_field = {
        'name' : 'WEBSITE',
        'value' : website,
        'inline' : True
    }
    discord_field = {
        'name' : 'DISCORD',
        'value' : discord,
        'inline' : True
    }
    twitter_field = {
        'name' : 'TWITTER',
        'value' : f'[@{twitter}](https://twitter.com/{twitter})',
        'inline' : True
    }
    
    
    data["embeds"] = [
        {
            "description" : desc,
            "title" : 'New Collection Drop Details',
            'fields' : [
                type_field , price_field , website_field,discord_field,twitter_field        
            ]
        }
    ]
    result = requests.post(url , json= data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

