Phillip Thomas's CustomerIO Subscription Center

This application uses the CustomerIO APIs to create a subscription center tied to CustomerIO attributes. 

This application is written in Python utilizing Flask as its web server. Executing CustomerIOWeb.py will create the Web Server Two routes exist in this application "Manage" and "Update". The manage route represents the Subscription Center page, this page allows users to select their Newsletter choices. If an invalid user is found a 404 error will be thrown to the user (this can be modified). The update route represents the update/submission page and will display a confirmation of the users actions. If a user tries to retireve the update page using GET HTTP Method (i.e. not posting a form) a 403 error will be thrown (this can be modified).

I have created a general Customer IO helper library (CustomerIOHelper) that incldues the following functions:
-Getting a users attributes via ID (get_customer_attributes)
-Updating a users attributes (update_customer_subscriptions)
-Unsubscribing a user globally (unsubscribe_user)
-Creating a dictionary to be used by the Front End to represent a users current subscription center "state" (create subscription_center_choices)

The front end of this application uses the bootstrap framework for graphical elements and javascript for front end interactions and form validations used for the buttons. I am utilizing Flask's template fuctionality with Jinja to create dyanmic front-end elements. Templates can be found in the Template folder. Unique fuctionality for the front-end:
-Check/Select All button
-Deactivate Subscribe button when no options are selected
-If Customer is currently unsubscribed all checkmarks on form will be emplty unsubscribe button will be deactivated

Connecting to Customer IO Workspace

To connect this application to Customer IO workspace update the keys_config_template.cfg in the Config folder for your Customer IO workspace credentials and save as keys_config.cfg.

Modifying Subscription Choices

To modify this application to have more subscription options edit the Subscription_Chocies.py file. This file contains a dictionary (key: value) with all options for the subscription center. The key will represent a Customer IO attribute and the value will represent a description/title of newsletter that will be shown in the front end.

