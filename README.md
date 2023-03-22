ECOHOTEL WEBAPP (USING DJANGO AND BLOCKCHAIN)

🚀 Goal of the project

The goal of the project is to implement a system to track the energy produced and consumed the photovoltaic panels of the Eco Hotel Pomelia, using Django, Redis (a NoSQL database) and the Ethereum Blockchain Testnet Goerli.

REQUESTS:
•	Data entry of produced and consumed energy in JSON format with POST method

•	Record Data on the Blockchain

•	Create a homepage to show this data at the user logged in the system

•	Create a web page only for admins that shows specific analysis

•	A log-in system that show if an administrator user log into the web app with different IP

________________________________________

💻 Features implemented

The features implemented in this project are:

•	Registration and login form for users

•	An homepage, accessible only to logged-in users, showing the table containing the values in question and the hash of the transaction

•	A page, to which only administrators can access, where you can see the total energy consumed and produced

•	A logging system to store the last IP that had access to the platform for a certain administrator user, so as to display a warning message when this is different from the previous one

________________________________________
🔎 How to run this project

Create a Virtual Environment

Clone the repo and install requirements in ecohotel/requirements.txt

Make database migrations

Install and run Redis DB Server

Run python manage.py runserver

Open http://127.0.0.1:8000/ in your browser

________________________________________
✉️

Mail: andreagenovese.management@gmail.com

