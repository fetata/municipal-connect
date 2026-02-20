# Municipal Connect

Municipal Connect is a simple community platform built with Django.

The idea behind the project is to improve communication inside a local
municipality. Sometimes small problems stay unsolved not because they
are difficult, but because people don't have an easy way to report or
share them.

This platform connects citizens through reports, shared skills, and a
small marketplace.

------------------------------------------------------------------------

## Features

-   Create and manage **Reports** (local issues)
-   Share personal **Skills**
-   Post items in the **Marketplace**
-   Optional condition for marketplace items
-   Search functionality
-   Announcement section
-   Background slideshow (JavaScript)
-   Django messages for user feedback
-   Seed script with Faker for demo data
-   Custom 404 page

------------------------------------------------------------------------

## Apps Structure

-   `common` -- home page, announcements, shared logic\
-   `reports` -- reporting local problems\
-   `skills` -- people sharing skills\
-   `marketplace` -- offer, wanted, giveaway items

------------------------------------------------------------------------

## How to run the project

1.  Clone the repository
2.  Create virtual environment
3.  Install dependencies:


    pip install -r requirements.txt

4.  Apply migrations:


    python manage.py migrate

5.  (Optional) Seed the database with demo data:


    python manage.py seed_data

6.  Run the server:


    python manage.py runserver

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Django
-   PostgreSQL
-   Bootstrap 5
-   JavaScript (for background rotation / small UI interactions)
-   Faker (for demo data)

------------------------------------------------------------------------

## Purpose

This project was built as part of a Django learning journey.\
The goal was to build something realistic, structured, and clean --- not
just a basic CRUD app.
