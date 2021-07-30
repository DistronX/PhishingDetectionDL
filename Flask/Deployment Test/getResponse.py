import requests

API_KEY = "K_rhaG1iU6KkPH07vOYZ-ZaoFZvMIPcYyK0PZj0leV9J"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

payload_scoring = {
    "input_data": [
        {
            "field": [["having_IPhaving_IP_Address", "URLURL_Length",
            "Shortining_Service", "having_At_Symbol", "double_slash_redirecting",
            "Prefix_Suffix", "having_Sub_Domain", "SSLfinal_State",
            "Domain_registeration_length", "Favicon", "port", "HTTPS_token",
            "Request_URL", "URL_of_Anchor", "Links_in_tags", "SFH",
            "Submitting_to_email", "Abnormal_URL", "Redirect", "on_mouseover",
            "RightClick", "popUpWidnow", "Iframe", "age_of_domain", "DNSRecord",
            "web_traffic", "Page_Rank", "Google_Index", "Links_pointing_to_page","Statistical_report"]],
            "values": [[1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 0, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1]]
        }]
}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/fa030a19-86b3-4bfa-b552-191ae9ed1211/predictions?version=2021-07-30', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
json_response = response_scoring.json()
output = json_response['predictions'][0]['values'][0][1][0]

