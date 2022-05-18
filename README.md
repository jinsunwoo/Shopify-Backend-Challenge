# Shopify Backend Developer Intern Challenge

 

This is an inventory tracking web application for a logistics company with basic CRUD functionalities as following:

- Create inventory items

- Edit inventory items

- Delete inventory items

- View a list of inventory items

 

Chosen additional feature:

- Ability to create warehouses/locations and assign inventory to specific location

 

## Tech Stack

 

**Frontend:** HTML, CSS, Javascript, jQuery

 

**Backend:** Python, Flask, JinJa, Pymongo

 

**Database:** MongoDB

 

## Demo

Click run button on [Replit](https://replit.com/@Jin0977/shopify-fall-2022-backend-challenge) and once it is done, go to [Demo](https://shopify-fall-2022-backend-challenge.jin0977.repl.co) to check the application

 

## Installation

 

**Prerequisites**

 

You need to have Python3 and MongoDB installed on your machine.

 

**Running the inventory web app on your machine**

 

Clone this repository

```shell

git clone https://github.com/jinsunwoo/Shopify-Backend-Challenge.git

```

Create and activate a virtual environment

```shell

pip3 install virtualenv

virtualenv env

source env/bin/activate

```

Install dependencies from requirements.txt

```shell

pip3 install -r requirements.txt

```

Run MongoDB

```shell

brew services start mongoldb-community

```

Run the app on localhost

```shell

python3 app.py

```

 

## Future Features

 

- View a list of warehouse locations.

- Delete warehouse locations. (Should only be deleted when none of the inventories are assigned to the warehouse location about to be deleted).

- More detailed fields in creating new warehouse location. Other than just the location name. 

- Confirm user about deletion before inventory get deleted.

- Sorting inventories according to their warehouse locations or any other categories

- Searching inventory 

 

## Things that can be done better

- The code I have written only have “app.py” file for back-end but separating “app.py” file according to feature and functionality is needed as the application get bigger with more features. It would be better to have separate files for functional part, DB accessing part, and exceptions. For example, it will be better to create a separate directory called “controllers” and under “controllers” separate files according to feature like “inventory.py” and “warehouse.py” and put only functional part in those files.  

- Creating custom exceptions and raise each in all different cases. Not many exceptions are implemented in the code yet but it will be better to create custom exceptions like “DatabaseError”, “NotFoundError” and “BadRequest” and raise each after trying any DB access. 

-  Creating test files using Pytest to test on each functionalities is also needed. 
