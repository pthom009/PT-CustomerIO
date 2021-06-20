from flask import Flask, render_template, request, abort
from flask_bootstrap import Bootstrap
from CustomerIOHelper import get_customer, create_subscription_center_choices, update_customer
from SubscriptionChoices import subscription_choices
app = Flask(__name__)

#Bootstrap Flask Application
Bootstrap(app)

#Subscription Center Manage Page
@app.route('/<user>/subscriptions/manage')
def subscriptions(user):
    customer = get_customer(user)
    if customer:
        customer_attributes = customer['attributes']
        unsubscribed = customer['unsubscribed']
        try:
            email = customer_attributes['email']
        except KeyError as e:
            abort(403)          
        subscription_center_choices = create_subscription_center_choices(customer_attributes, unsubscribed)
        return render_template('manage.html', user=user, email=email, unsubscribed=unsubscribed, customer_subscriptions=subscription_center_choices)
    #If customer not found throw 404 error
    else:
        abort(404)

#Subscription Center Update Page
@app.route('/<user>/subscriptions/update', methods = ['POST', 'GET'])
def update(user):
    #Throw 403 error on GET
    if request.method == 'GET':
        abort(403)
    if request.method == 'POST':
        form_data = request.form
        customer_update = {}
        customer_update_text = {}
        action = request.form['action']
        email = request.form['email']

        customer = get_customer(user)
        customer_attributes = customer['attributes']

        if action == 'Subscribe':
            for subscription, value in form_data.items():
                #Sets subscribed newsletter attribute to true
                if value == 'on':
                    customer_update[subscription] = 'True'
                    customer_update_text[subscription] = subscription_choices[subscription]
            for subscription in subscription_choices.keys():
                #Sets currently subscribed newsletter attributes to false
                if subscription not in customer_update.keys() and subscription in customer_attributes.keys():
                    customer_update[subscription] = 'False'
            if customer['unsubscribed']:
                customer_update['unsubscribed'] ='false'
            update_customer(user, customer_update)
            return render_template('update.html', user=user, customer_update_text=customer_update_text, action=action, email=email)
        elif action == 'Unsubscribe':
            for subscription in subscription_choices.keys():
                #Sets currently subscribed newsletter attributes to false
                if subscription not in customer_update.keys() and subscription in customer_attributes.keys():
                    customer_update[subscription] = 'False'
            customer_update['unsubscribed'] ='true'
            update_customer(user, customer_update)
            #unsubscribe_user(user)
            return render_template('update.html', user=user, action=action, email=email)
if __name__ == '__main__':
    app.run(debug=True)
