# demosite
Demo Site built using Python and the Django framework with the Wagtail CMS. Basic blog/article section and comments.

# Usage
This repo includes a small sqlite3 database with sample data. You can view the quick demo <a href="http://46.101.90.234/" target="_blank">here</a>, and edit pages/create new ones <a href="http://46.101.90.234/admin" target="_blank">here</a> using **ds_admin** as a username and _demoadmin_ as the password.

# Emails
The Gmail SMTP server is used to send out any emails coming from the *Contact Us* form. This form is configurable via its' relevant page in the admin, as it uses ```wagtailforms``` which can be used as a dynamic form builder.

#Site-wide settings
The social icons in the footer are configurable in the <a href="http://46.101.90.234/admin/">admin</a> by clicking on the ```Settings -> Social Media Settings``` menu item. This allows for the email address, github account and linkedIn profile URL to be changed.
