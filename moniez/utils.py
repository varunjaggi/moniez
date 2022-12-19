import requests
import json

##DEFINED CONSTANT TO HAVE LESS CODE REPEATATION 
MAIN_URL = "https://hackathon.pirimidtech.com/hackathon"
API_KEY =  "4fce8d57b7cc42e71856b3f140"
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'API_KEY': API_KEY
    }

def initiate_consent(phone_number, tracking_id):
    """Phone number | Tracking id"""
    #Initiate Consent
    print(phone_number)
    url = MAIN_URL+"/init/redirection"

    payload = json.dumps({
    "vuaId": str(phone_number)+"@dashboard-aa-uat",
    "templateType": "ONETIME",
    "trackingId": tracking_id,
    "redirectionUrl": "https://baseurl.com"
    })
    headers = HEADERS

    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)
    print(result['trackingId'])
    fetch_consent_status(result['trackingId'],result['referenceId'])
    fetch_data(result['trackingId'],result['referenceId'])
    return response.text


def fetch_consent_status(tracking_id, reference_id):
    """Used to fetch status of the consent here"""
    url = MAIN_URL+"/consent/status?referenceId="+str(reference_id)+"&trackingId="+str(tracking_id)
    payload = ""
    headers = HEADERS

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return response.text


def fetch_data(tracking_id, reference_id):
    """To fetch data"""
    """Used to fetch status of the consent here"""
    url = MAIN_URL+"/consent/data/fetch?referenceId="+str(reference_id)+"&trackingId="+str(tracking_id)
    payload = ""
    headers = HEADERS

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return response.text
def fetch_analytics_data(tracking_id, reference_id):
    """To fetch data"""
    """Used to fetch status of the consent here"""
    url = MAIN_URL+"/consent/analytics/fetch?referenceId="+str(reference_id)+"&trackingId="+str(tracking_id)
    payload = ""
    headers = HEADERS

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return response.text


def fetch_fips():
    """To fetch data"""
    """Used to fetch status of the consent here"""
    url = MAIN_URL+"/fip"
    payload = ""
    headers = HEADERS

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return response.text