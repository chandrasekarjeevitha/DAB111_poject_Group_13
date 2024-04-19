# 🍔 Swiggy : online food ordering and delivery platform 🍔


##  🍟Group Details

**Group Number:** DAB501Group 13 <br>
**Student Details:** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0856358 - Gopikakrishna <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0856328 - Jeevitha Chandrasekar <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0850007 - Vishnu Mohan <br>

## 🍟About
The website is created using Flask to display the data abour restaurents in Swiggy (an online food ordering and delivery platform). The data is fetched from a SQLite database. The website displays one  restaurent from each  city. 


## 🍟Webpages
**Home Page:** Contains information about Swiggy. Also has navigation links to the 'About' page and 'Data' page. <br>
**About Page:** Diplays information about the attributes in the dataset. <br>
**Data Page:** Diplays one restaurent from each City.


## 🍟Libraries Used
**SQLite:** To create database and table. <br>
**Flask:** To craete web appplication.  <br>

## 🍟Components of the Project
**DatabaseCreation.pynb:** a Jupyter notebook containg code to create the database 'online_delivery.db', the table 'online_orders' and insert data from csv file to the table.  <br>
**online_delivery.db:** SQLite database containing online_orders table.  <br>
**swiggy.csv :** csv file containing data about Swiggy to be imported to the SQLite database.  <br>
**app_template.py:** Flask application containing the route functions for Home, About and Data webpages.  <br>
**templates:** Folder containing html templates for Home, About and Data webpages. <br>

## 🍟Working
1. A database called  'online_delivery.db' and a table 'online_orders' is created in SQLite using DatabaseCreation.pynb script. 
2. The data from csv file swiggy.csv is inserted to the table using the same script. 
app_template.py is the flask application that first imports the necessary libraries such as SQLite, Flask, Pathlib. 
3. Three routes are created in app_template.py:  <br> 
    a. The root route (/) renders the index_links.html template. <br>
    b. The /about route renders the about.html template. <br>
    c. The /data route connects to the SQLite database, retrieves data from the online_orders table, and renders the data_table.html template with the fetched data. <br>

## 🍟Installation Steps
i. Clone the repository using the following command: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; git clone https://github.com/ <br>
ii. Execute the following command to install all the necessary packages: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pip install -r requirements.txt <br>
iii. Run app_template.py and ctrl + click the link generated to access the webpage.  <br>