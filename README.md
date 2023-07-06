# Payroll Web Application

The Payroll Web Application is a web-based program designed to manage employee payroll data for WXYZ Corp. It provides various functionalities, such as viewing employee data by department, editing employee hours worked, and displaying the status of operations. The application utilizes the Bottle framework and SQLite database to handle HTTP requests and store the payroll information.

## Files

The program folder contains the following files:

1. **dept_form.tpl**: A template file that displays a form to select a department and retrieve the corresponding payroll information.

2. **edit_hours.tpl**: A template file that displays a form to enter an employee ID and the number of hours worked by the employee.

3. **get_employee.tpl**: A template file that displays the payroll information for a specific department, including employee ID, name, wage, hours worked, and weekly pay.

4. **layout.tpl**: A template file defining the layout structure of the web pages, including common elements such as the navigation bar and styling.

5. **login_page.tpl**: A template file that displays a login page (not fully implemented in the given program).

6. **show_department.tpl**: A template file similar to get_employee.tpl, displaying the payroll information for a specific department.

7. **status.tpl**: A template file that displays the status of an operation, indicating whether it was successful or not.

8. **welcome.tpl**: A template file that displays a welcome message and prompts the user to log in (not fully implemented in the given program).

9. **program6.py**: The main Python file containing the program logic. It utilizes the Bottle framework to define routes and handle HTTP requests. The file establishes a connection to the SQLite database and performs operations based on the requested routes.

10. **payroll.db**: An SQLite database file that stores the employee and payroll data used by the program. The database structure and content are hosted on GitHub [here](link-to-your-database-file-on-github).

## Usage

To run the Payroll Web Application, follow these steps:

1. Ensure that the required dependencies, such as the Bottle framework, are installed.
2. Place all the program files, including the database file (`payroll.db`), in the same folder or directory.
3. Execute the `program6.py` file using a Python interpreter.
4. The program will start a web server on `localhost` at port `8080`.
5. Open a web browser and navigate to `http://localhost:8080/` to access the application.
6. Use the available routes to interact with the application:
   - `/`: Displays the welcome page.
   - `/getDepartment`: Allows selection of a department to view payroll information.
   - `/editHours`: Allows editing of employee hours worked.

## Notes

- Make sure to obtain the `payroll.db` database file from the provided GitHub link and place it in the same directory as the program files.
- Extend the program as necessary based on the provided files and additional requirements not included in the given program.
- Regularly update and maintain the program to ensure compatibility with the latest dependencies and security patches.
- Keep the database file secure and ensure appropriate access controls are in place when hosting it on GitHub or any other platform.
