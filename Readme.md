# Grab products on Openfoodfacts

This program can grab and save products on a database like "MySQL" for display this to user(s).
Then, the user choose a product in the list and the software show a substitute with a better "nutriscore".

It's create with the language Python.

To follow my project : https://trello.com/b/8Hoz1kbq/openfoodfacts

## How to use ?

Run your local server to have Phpmyadmin.
Replace in files your ID and password to phpmyadmin. 

Then, run the "importation.py" program to save products in database with differents categories (for exemple : bacon, pizza, sauces, desserts, sodas, bonbons, cereals and potatoes, fishes, pastas and fruit juices).

When the database is generated (in your phpmyadmin), run "exe_client.py" and follow steps.


## Requirements

Python 3
A local server Wampserver or equivalent
Install MySQL >= 5.5