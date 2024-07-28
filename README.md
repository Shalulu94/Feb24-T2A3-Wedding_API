# Term 2 Assignment 2 - Wedding API

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
- Testing: Once an task has been completed the functionality will need to be tested. This will not apply to all items, but mainly part of the coding process
- Completed: Tasks that have passed the testing phase and are now ready

Using cards with checklists to track the progress of major tasks within the project will help me manage my time more effectively and keep track of my activities. 

This Trello board will be updated regularly as I complete specific tasks. 




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





