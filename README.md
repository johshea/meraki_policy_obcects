Prototype
A Meraki API Call to export policy objects in a json structure for refrence or to populate other data sources
it will autmatically create the output file if not present or rewrite the file on subsequent runs.

assumes you have activated Policy Objects in your Meraki Dashboard

Contacts:
John Shea (Johshea@cisco.com)

Solution Components:
Python 3.8
requests
pathlib

Solution Overview:
When run we take the provided API key and Orginization name and instantly retrieve the matching ORG ID. This ORG ID is then used pull the Policy Objects from the Meraki API and save them into a JSON formatted file, for review or ingestion into another application. If the obj_export.json file does not exist the script will create it for you. If a currently populated file does exist the data will be replaced by the current retrieval.


Getting Started:
To obtain your orginizations name (we will get the ID for you since sometimes we have multiple orgs!) 
navigate to Orginization -> Settings -> Name

To obtain a valid API key follow the instructions at the following link:
https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API

To Activate Policy Objects in your Orginization:
https://documentation.meraki.com/MX/Firewall_and_Traffic_Shaping/Network_Objects_Configuration_Guide

Usage:
python3 main.py -k apikey -o orginization_name

LICENSE
Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

CODE_OF_CONDUCT
Our code of conduct is available [here](CODE_OF_CONDUCT.md)

DISCLAIMER:
Please note: This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.


  [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/johshea/export_Mpolicy_objects)
  
