import requests
import json
def lambda_handler(event, context):
    version = context.function_version
    ipaddress = requests.get('http://ip.42.pl/raw').text
    suburl = requests.get('http://worldtimeapi.org/api/ip/'+ipaddress+'.json').text
    y = json.loads(suburl)
    y['version'] = version
    print(json.dumps(y))
    
    return {
        'statusCode': 200,
        'body': json.dumps(y)
    }
