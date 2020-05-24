import requests
import xmltodict

def lambda_handler(event, context):
    r = requests.get('https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=rmdv2&output=xml')
    dict = xmltodict.parse(r.content)
    data = dict['site']['observed']['datum'][000]['primary']['#text']
    return {
        'statusCode': 200,
        'body': json.dumps(str(data))
    }
