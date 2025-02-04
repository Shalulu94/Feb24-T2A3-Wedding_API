# Term 2 Assignment 2 - Wedding API

## Installation Guidelines

## R0 - Install guide (WSL)
#### Create Virtual Environment
- Open a WSL terminal and create a virtual environment
- `python3 -m venv .venv`
- Activate the virtual environment
- `source .venv/bin/activate`
- Open your IDE
- `code .`
- Install the dependencies
- `pip install -r requirements.txt`
- Install PostgresSQL
- `sudo apt install postgresql postgresql-contrib`

#### Create a PostgreSQL database and admin user
- Open a WSL terminal and open PostgreSQL 
- `sudo -u postgres psql`
- Create a database
- `create database wedding_planner;`
- Create a database admin user with password (example credentials below)
- `create user wedding_dev with password '123456';`
- Grant all privileges to admin user
- `grant all privileges on database wedding_planner to wedding_dev;`
- Grant all permissions on database schemas to admin user
- `grant all on schema public to wedding_dev;`

#### Application Environment files
- Create a new `.flaskenv` file and change the included code in the `.flaskenv_sample` file to suit your needs
- Create a new `.env` file and change the included code in the `.env_sample` file to suit your needs

#### Create tables, seed database and run Flask application
- Open a WSL terminal (exit out of PostgreSQL if still open)
- Create the tables
- `flask db create`
- If you encounter any issues with Flask running type the below command to export the setup function:
- `export FLASK_APP=app:setup`
- Seed the tables with data
- `flask db seed`
- Run the Flask app
- `flask run`
---

## R1: Purpose

Wedding planning in general is already a very daunting task and for majority of us, it is the first and last time we will ever need to do it! There are several vendors out there and an unlimited amount of things that could be added to a wedding and it can very easily and very quickly become overwhelming. 

The purpose of my App is to assist our users with their wedding planning by providing a platform that helps them to keep track of their tasks, budgets and connect with potential suppliers. 

This app will have separate rules and authorisation levels depending on whether you're a user or a supplier. Users will be able to create an account for their own use, browse through potential suppliers and create a checklist to help them organise and progress through their wedding planning. 

Suppliers will have a separate authorisation level and is aimed at giving them the ability to market their services over the app by creating a storefront. User's will be able to view their stores to get an idea of the different services that they provide, different packages and also their pricing. Users will also be able to leave reviews on these store pages to provide insight on their experiences to further assist other users when they are making a decision on which supplier to use. 

This app will servce as a way for users to get access to a range of different vendors for their future wedding. Combined with real user feedback, it ensures that users are getting the best feedback/reviews possible before committing to a prticular supplier/service. This will help to alleviate some of the stress associated with planning a wedding.

## R2: Project Tracking

Within this project, I will be using Trello to plan my tasks and keep track of what I have completed as the project progresses. I will be using 4 separate lists to keep track of the status of my tasks which will include:
- To Do: List of items that I need to beging and have not yet started work on
- In progress: Currently started working on but not yet ready for testing. Ideally I will tackle one item at a time, however there could be multiple pieces in play at any given time
- Testing: Once an task has been completed the functionality will need to be tested. This will not apply to all items, but mainly part of the coding process. Predominantly required using insomnia to test CRUD functionality as well as running SQL statements to ensure dummy data was flowing through to database
- Completed: Tasks that have passed the testing phase and are now ready

Using cards with checklists to track the progress of major tasks within the project will help me manage my time more effectively and keep track of my activities. 

This Trello board will be updated regularly as I complete specific tasks. 

![Trello board](./docs/trello.png)


## R3: Third-party services and dependencies

#### SQL Alchemy

SQLAlchemy is a toolkit for developers, enabling efficient access to relational databases like SQLite, MySQL, and PostgreSQL, and providing an object relational mapper for data querying and handling.

#### Flask

Flask is a Python web micro-framework for developing web applications, based on Werkzeug WSGI and Jinja2 template engine. It allows for requests, response objects, and utility functions.

#### PostgreSQL

PostgreSQL, an open-source database management system, was utilized in this project to create the wedding_planner database, which supports SQL and JSON querying.

#### marshmallow

Marshmallow is a Flask integration layer that supports object serialisation/deserialisation, SQLAlchemy integration, and data validation functions. It is used in a project to validate data configuration, including categories, password length, and non-blank values.

#### Psycopg2

Psycopg2 is a widely-used Python database adapter that enables developers to perform a wide range of SQL operations against PostgreSQL databases.

#### Bcrypt

Bcrypt is a cryptographic hash function used in this project for one-way password hashing, comparing input passwords with stored passwords for registration and login routes.

#### JWT Extended

JWT Extended is a package that adds support for using JSON Web Tokens to Flask for protecting routes. I have utilised this in my project to issue out tokens when users login which have a timer before relog is required. Also for making changes and updates to certain databases, users will need to have an active token.

## R4: Explain the benefits and drawbacks of this app’s underlying database system.

I have chosen to utilise PostgreSQL as my database system behind this API. PostgreSQL is a popular open-source database with robust features like Python-based functions, cascading functions, support for long data types, full-text search, and large data handling. It also has authentication, access control, and privilege management systems, crucial for projects with multiple users and different levels of authorisation. As PostgreSQL is open source, it also comes with a very strong community backing who continue to improve and develop the functionality.

Some of the drawbacks of PostgreSQL include:

- PostgreSQL is suitable for various workloads but may not be optimal for high-transaction environments or large-scale data warehousing solutions compared to specialized databases.
- PostgreSQL's robustness and extensive features make it a more efficient database than other options, resulting in a higher consumption of disk space for certain data types.
- PostgreSQL's extensive feature set can be overwhelming for beginners or those who don't require advanced functionalities.

## R5: Features, purpose and functionality of an ORM

An ORM tool is a library or framework that enables interaction between a relational database and an object-oriented programming language, allowing developers to use native constructs instead of SQL.

Some of the key functionalities include:

- Object-Relational Mapping: The tool maps database tables to classes and rows to objects, allowing developers to work with database records like regular objects in their code.
- Create, Read, Update and Delete (CRUD): The system offers CRUD operations, simplifying database interactions without the need for SQL writing.
- Querying: The database querying feature enables the use of programming language syntax or a domain-specific language (DSL), enhancing the comprehensibility and maintainability of queries.
- Relationships: The system aids in defining and managing relationships between entities, incorporating foreign key relationships in the database.

Some of the benefits include:

- Improve productivity: The tool enhances developer productivity by reducing boilerplate code for database interactions and simplifies complex queries, allowing developers to concentrate on business logic.
- Maintainability: The integration of database logic within models improves code maintainability, organization, and simplifies schema changes through migrations.
- Data integrity: The system ensures data integrity by implementing validation and constraints at the application level, preventing errors from reaching the database.
- Code resuability: The system encourages code reusability by enabling the reuse of models and data access logic across various application parts.

## R6: Entity Relationship Diagram (ERD):

Below is the ERD for my Wedding planning API

![Wedding ERD](./docs/Wedding%20ERD.jpg)

My API will have two separate levels for account creation - "Users" and "Suppliers".

**Suppliers**

Suppliers will have a one-to-many relationship with stores, as a single supplier can engage in serveral different goods/services. Keeping suppliers under a separate login, ensures that we can implement som restrictions to only allow suppliers to create stores. We do not want Users to be able to create their own stores as it needs to be associated with a proper business. 

**Users**

Primary function for users are to be able to browse through the database and filter through specific stores/suppliers relevant to their needs. Users will also be able to leave ratings for specific stores based on their own experiences. This will have a one-to-many relationship with Ratings.

**Ratings**

Ratings has a many-to-one relationship with Users and well as stores. This is because multiple users can leave multiple reviews for multiple stores which means a Rating join table was required to be able to represent this relationship and hold the data. 

**Stores**

This is where all of the different services will be held. Users will be able to browse the stores and look at their descriptions/ratings before making a choice to engage the supplier directly. All of the information will be presented as there are foreign keys for ratings and suppliers included in the stores model. 

## R7: Implemented models and their relationships

**User Model**

- The user model represents a single user in this project. As a user, you typically want the ability to browse through all of the stores/suppliers and also leave reviews on stores that you have used for other users to view. The user model has a one-to-many relationship with ratings as user can leave multiple ratings for several different stores. 
- The user is identified with a unique ID which is also used as an identifier in the the Ratings table as a foreign key. 
- The user model has it's own authentication controller for both registration and login functionality. Database will search prior to registering to ensure there are no duplicate users and if so will handle these errors gracefully. 

**Suppliers Model**

- The suppliers model is for companies to create an account under a different authority level which allows them to create stores. These stores are designed for them to display their services to users
- Suppliers has a one-to-many relationship with stores as a single supplier can create multiple stores to showcase their different services offerings. 
- The supplier model has it's own authentication controller for both registration and login functionality. Database will search prior to registering to ensure there are no duplicate users and if so will handle these errors gracefully. 

**Stores Model**

- The stores model represents different goods/services provided by suppliers which will be on offer to users to browse and review. 
- The stores model holds a many-to-one relationship with suppliers and a one-to-many relationship with ratings. There can be multiple ratings for a specific store, but a specific rating can only be designated to a single store

**Ratings Model**

- The ratings model acts as a join table between users and stores. This was necessary as because multiple users could leave multiple reviews for multiple stores, users and stores would end up having a many-to-many relationship. 
- The Ratings table manages this many-to-many relationship by utilising the foreign ID keys for both user_id and store_id within the model.
- Ratings table allows users to leave reviews for stores for other users to see

## R8: API Endpoints

1. Register User

New user can be registered to the database. Access token wll be granted up login

- Endpoint: /auth/register
- HTTP verb: POST
- Attributes:
    - first name
    - surname
    - email
    - password
    - contact
- Expected response:
    - 201 Created
    - Return registration details

![User_registration](./docs/user_register.png)

2. User Login

New user can be login to the database. Access token wll be granted up login

- Endpoint: /auth/login
- HTTP verb: POST
- Attributes:
    - email
    - password
- Expected response:
    - 200 OK
    - Return access token

![User_login](./docs/user_login.png)

3. Supplier Registration

New supplier can register to the database. Access token wll be granted up login

- Endpoint: /auth_supp/register
- HTTP verb: POST
- Attributes:
    - company name
    - company email
    - description
    - password
- Expected response:
    - 201 CREATED
    - Return registration details

![supplier_registration](./docs/supplier_register.png)

4. Supplier Login

New supplier can login to the database. Access token wll be granted up login

- Endpoint: /auth_supp/login
- HTTP verb: POST
- Attributes:
    - company email
    - password
- Expected response:
    - 200 OK
    - Return Access token

![supplier_login](./docs/supplier_login.png)

5. Retrieve all stores

User can search all stores in database

- Endpoint: /stores
- HTTP verb: GET
- Expected response:
    - 200 OK
    - Return all stores in database

![All stores](./docs/get_stores.png)

6. Retrieve specific store

User can retrieve a specific store

- Endpoint: /stores/<int>
- HTTP verb: GET
- Expected response:
    - 200 OK
    - Return all stores in database

![One store](./docs/get_stores_indiv.png)

7. Create new store

suppliers can create a new store

- Endpoint: /stores
- HTTP verb: POST
- Attributes:
    - store_name
    - description
- Expected response:
    - 200 OK
    - Create new store, return store and supplier details

![New store](./docs/create_store.png)

8. Delete an existing store

Suppliers can delete existing store. Error handling if store does not exist

- Endpoint: /stores/<int>
- HTTP verb: DELETE
- Expected response:
    - 200 OK
    - Store deleted successfully

![Delete store](./docs/delete_store.png)

9. Update existing store

Suppliers can make changes to their existing store description

- Endpoint: /stores/<int>
- HTTP verb: PUT
- Expected response:
    - 200 OK
    - Store deleted successfully

![Update store](./docs/update_store.png)

