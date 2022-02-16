##################################################################################################
#Prototype
#A Meraki API Call to populate and maintain network objects using a JSON dictionary as source
#
#Requirments:
#Python3 and the requests library
#to install requests:
#pip3 install requests
#
#Usage:
#python3 create_obj.py -k <apikey> -o <orgname>
#
#Future:
#Error handling on data iteration
#move record creation to a function
#check if exists and update instead of add
#build in creating and assigning to group objects
###################################################################################################



import requests
import json, sys, getopt


def getorgId(arg_orgname):
    org_response = requests.request("GET", f'{m_baseUrl}/organizations/', headers=m_headers)
    org = org_response.json()
    for row in org:
        if row['name'].lower() == arg_orgname.lower():
            orgid = row['id']
            print("Org" + " " + row['name'] + " " + "found.")
        else:
            print("Exception: This Org does not match:" + ' ' + row['name'] + ' ' + 'Is not the orginization specified!')

    return orgid

#def getpolobj()


def main(argv):
    global arg_apikey
    global m_baseUrl
    global m_headers
    global arg_orgname

    arg_apikey = None
    arg_orgname = None

    try:
        opts, args = getopt.getopt(argv, 'k:o:')
    except getopt.GetoptError:
        sys.exit(0)

    for opt, arg in opts:
        if opt == '-k':
            arg_apikey = arg
        elif opt == '-o':
            arg_orgname = arg

    if arg_apikey is None or arg_orgname is None:
        print('Please specify the required values!')
        sys.exit(0)

    # set needed vlaues from env_vars
    m_headers = {'X-Cisco-Meraki-API-Key': arg_apikey}
    m_baseUrl = 'https://api.meraki.com/api/v1'

    orgid = getorgId(arg_orgname)

    f = open('objects.json', )
    objects = json.load(f)

    #get existing entries if any
    for i in objects['policy_objects']:
        if i['type'] == 'cidr':
            okey = 'cidr'
            ovalue = i['cidr']
        else:
            okey = "fqdn"
            ovalue = i['fqdn']

        payload = {
            "name": i['name'],
            "category": i['category'],
            "type": i['type'],
            okey: ovalue
            }

        print(payload)
        print ('Adding' + ' ' + i['name'])
        create_obj = requests.request("post", f'{m_baseUrl}/organizations/{orgid}/policyObjects', headers=m_headers, data=payload)
        print(create_obj)
        if create_obj.status_code == 201:
            print('Object Added!')
        else:
            print('Something weht wrong adding' + ' ' + i['name'])

    print('Policy Objects added! Have a great day!')

if __name__ == '__main__':
    main(sys.argv[1:])

