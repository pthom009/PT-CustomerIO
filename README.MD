Phillip Thomas's CustomerIO Subscription Center
Overview
This application uses the CustomerIO APIs to create a subscription center tied to CustomerIO attributes. This application will allow CustomerIO clients to send a unique URL to customers to manage their subscription attributes within CustomerIO.
Technical
This application is written in Python utilizing the Flask web framework . The front end of this application uses the Bootstrap framework for graphical elements and JavaScript for front end interactions and form validations used for the buttons. Flask's template functionality with Jinja to create dynamic front-end elements, Templates can be found in the Template folder. 
 
File Structure
CustomerIOWeb.Py
Executing CustomerIOWeb.py will create a Web Server instance of this application. Two routes exist in this module: "Manage" and "Update". The manage route represents the Subscription management page which allows users to select their Newsletter choices. A user’s subscription management page can be found using the following format *webserver*/*user*/subscriptions/manage where webserver is the URL of the webserver and user being the user’s ID attribute in Customer IO. If an invalid user is found a 404 error will be thrown to the user (this can be modified). If a user is found but an email is not recorded for the user a 403 will be thrown. Using the CustomerIOHelper library (see section CustomerIOHelper), the customer’s CustomerIO attributes are retrieved. A successful user pull will lead to a subscription_center_choices dictionary being created which will contain the current user’s attributes of the subscriptions found in the SubscriptionChoices module. The customer’s attributes, email, unsubscription status, and subscription_center_choices are sent to the manage template which will be displayed to the end user.
 
Manage Route Code
An HTML form is presented to the end user with each Subscription Choice and the user’s current Subscription Status. if a user has a Newsletter option selected the submit button will be enabled in the form. If the user is unsubscribed the unsubscribed option will be disabled. Once a user submits their changes these changes via POST get sent to the update route.
 
Manage Subscriptions Page

 
The update route represents the update/submission results page. This page will display a confirmation of changes to the user. If a user tries to retrieve the update page using GET HTTP Method (i.e. not posting a form) a 403 error will be thrown (this can be modified). This route takes input from the from in Manage route and uses the CustomerIOHelper module to compare form results with current attributes. If a new subscription is found a new key:value pair will be added to the customer_attributes dictionary {subscription: ‘True’}, if a subscription was previously subscribed and now no longer subscribed. 
 
Update Route Code
 
Subscriptions Updated Page
 
CustomerIOHelper.py
I have created a general Customer IO helper library (CustomerIOHelper.py) that includes the following functions:
•	Getting a customer’s attributes via ID (get_customer_attributes)
•	Updating a customer’s attributes (update_customer)
•	Creating a Subscription Center Dictionary (create_subscription_center_choices) – A Dictionary of the current user’s subscription status for SubscriptionChoices
 
CustomerIOHeper Code
 
Connecting to Customer IO Workspace
To connect this application to Customer IO workspace update the keys_config_template.cfg in the Config folder for your Customer IO workspace credentials and save as keys_config.cfg.
 
keys_config_template.cfg
Modifying Subscription Choices
To modify this application’s subscription choices edit the Subscription_Chocies.py file. This file contains a dictionary (key: value) with all options for the subscription center. The key will represent a Customer IO attribute and the value will represent a description/title of newsletter that will be shown in the front end.
 
SubscriptionChoices.py Code

