from customerio import CustomerIO, Regions
from SubscriptionChoices import subscription_choices
from configparser import ConfigParser

config = ConfigParser()
config.read('config/keys_config.cfg')

SITE_ID = config.get('customerio', 'site_id')
API_KEY = config.get('customerio', 'api_key')
APP_KEY = config.get('customerio', 'app_key')

def get_customer(id):
    import http.client
    import json

    #Make request to Attributes API
    conn = http.client.HTTPSConnection("beta-api.customer.io")
    headers = { 'Authorization': 'Bearer {}'.format(APP_KEY) }
    conn.request("GET", "/v1/api/customers/{}/attributes".format(id), headers=headers)
    res = conn.getresponse()
    data = res.read()

    #Return customer json if found, return false if not found
    try:
        customer = json.loads(data.decode("utf-8"))['customer']
        return customer
    except KeyError as e:
        return False


def update_customer(id, subscriptions):
    cio = CustomerIO(SITE_ID,API_KEY, region=Regions.US)

    #Template update dict
    customer_update = {}
    customer_update['id'] = id

    #set customer to not unsubscribed if currently unsubscribed
    #customer_update['unsubscribed'] = 'false'

    #set customer update values
    for subscription, value in subscriptions.items():
        customer_update[subscription] = value

    return cio.identify(**customer_update)

def create_subscription_center_choices(attributes, unsubscribed):
    subscription_center_choices = {}

    #Get current subscription choices
    current_subscription_chocies = ({key:value for key,value in attributes.items() if key.lower() in subscription_choices.keys()})

    #Set all subscriptions to not subscribed for unsubscribed use case
    if unsubscribed:
        for subscription in subscription_choices.keys():
            subscription_center_choices[subscription] = {'Name': subscription_choices[subscription], 'Value': False}
    else:
        for subscription in subscription_choices.keys():
            #Set subscription to true to represent currently subscribed newsletter
            if subscription in current_subscription_chocies.keys() and current_subscription_chocies[subscription].lower() == 'true':
                subscription_center_choices[subscription] = {'Name': subscription_choices[subscription], 'Value': True}
            #set subscription to false to represent non-subscribed newsletter
            else:
                subscription_center_choices[subscription] = {'Name': subscription_choices[subscription], 'Value': False}
    return subscription_center_choices

