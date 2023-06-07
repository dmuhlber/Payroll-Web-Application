# Payroll-Web-Application
This is a web application for managing employee payroll data. It utilizes the Bottle web framework and SQLite database for data storage. The application consists of several modules and templates, each serving a specific purpose.
Modules:

Program 6: This module is the main entry point of the application. It sets up the routes and handles HTTP requests.

dept_form: This module defines the template for the department form, allowing users to select a department and retrieve payroll information for employees in that department.

edit_hours: This module defines the template for editing employee hours. Users can enter the employee ID and the number of hours worked to update the data.

get_employee: This module defines the template for displaying employee information for a specific department. It retrieves the data from the database and presents it in a table format.

layout: This module defines the base template for the web pages. It includes the navigation bar and provides a consistent layout for all pages.

login_page: This module defines the template for the login form. Users can enter their username and password to log into the application.

show_department: This module defines the template for displaying the payroll information for a specific department. It retrieves the data from the database and presents it in a table format.

status: This module defines the template for displaying the status of an operation. It is used to indicate whether a database operation (e.g., select, update) was successful or not.

welcome: This module defines the template for the welcome page. It serves as the landing page for the application and prompts users to log in.

This project provides a user-friendly interface for managing and viewing employee payroll data based on departments. It leverages SQLite for data storage and the Bottle web framework for handling HTTP requests and rendering templates.
