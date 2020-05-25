import requests
import xmltodict
import json

def current_stage():
    r = requests.get('https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=rmdv2&output=xml')
    dict = xmltodict.parse(r.content)   
    current_height = dict['site']['observed']['datum'][000]['primary']['#text']
    future_height = dict['site']['forecast']['datum'][000]['primary']['#text']
    is_rising = (float(current_height) <= float(future_height))
    if is_rising:
        trend = "and rising"
    else:
        trend = "and falling"
        
    speak_output = "The James River is currently " + current_height + " feet " + trend +  " at the Westham gauge."    
    return speak_output
