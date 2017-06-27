#Author: Vinit V.
#Date: 6/12/2017

#!/usr/env/bin python

import requests



#Get the slowest URLs using checkID, ResultID, and APIKey
def check_result_slowest(checkId,resultId,apiKey):
  json_base = {}
  headers = {'Content-Type': 'Application/json'}
  https_data = requests.get('https://api-wpm.apicasystem.com/v3/checks/browser/'+str(checkId)+'/results/'+str(resultId)+'/urldata?format=json&auth_ticket='+apiKey+'&mostrecent=1&detail_level=1', json=json_base, headers=headers).json()
  print ("\n\nCheck: "+str(checkId)+"   :")

  for r in https_data['check_results']:
    for k in r['url_results']:
      print(k['url'] +" | "+str(k['response_time_ms'])+ " ms | "+str(k['http_status_code']))



#Get the recent check result ID using checkID and APIKey
def data_new_check(checkId,apiKey):
  json_base = {}
  headers = {'Content-Type': 'Application/json'}
  https_data = requests.get('https://api-wpm.apicasystem.com/v3/Checks/'+str(checkId)+'/results?mostrecent=1&detail_level=1&auth_ticket='+apiKey, json=json_base, headers=headers).json()
  check_result_slowest(checkId,https_data[0]['identifier'],apiKey)




#Get all check ID using the API key
def get_checks(apiKey):
  json_base = {}
  headers = {'Content-Type': 'Application/json'}
  https_data = requests.get('https://api-wpm.apicasystem.com/v3/Checks/?auth_ticket='+apiKey, json=json_base, headers=headers).json()
  for route in https_data:
          if route['enabled']==True and route['check_type']=="FprXnet":
            data_new_check(route['id'], apiKey)




#Call the function
get_checks("YOUR-API-KEY-GOES-HERE") 