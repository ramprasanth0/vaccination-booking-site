# vaccination-booking-site
Covid Vaccination Booking:
This is a web application for booking Covid vaccination slots. 
The application allows users to search for vaccination centers, view their working hours, and apply for a vaccination slot. The application also includes an admin panel for managing vaccination centers and tracking dosage details.

Technologies Used:
Python 3.8.5
Django 3.2.4
PostgreSQL 13.3
HTML, CSS

User Use Cases:
Login: Users can log in to the application using their username and password.
Sign up: New users can create an account by providing their name, email, and password.
Search for Vaccination centre and working hours: Users can search for vaccination centers by location and view their working hours.
Apply for a vaccination slot (only 10 slots allowed per day): Users can apply for a vaccination slot at their chosen center. Only 10 slots are available per day, so users should book early to avoid disappointment.
Logout: Users can log out of the application when they are finished.

Admin Use Cases:
Login (Separate login for Admin): Admins can log in to the application using their email and password.
Add Vaccination Centres: Admins can add new vaccination centers to the application, including their name, location, and working hours.
Get dosage details (group by centres): Admins can view dosage details for each center, including the number of doses administered and the number of doses remaining.
Remove vaccination centres: Admins can remove vaccination centers from the application.
