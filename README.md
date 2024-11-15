Ticketing Tool - Django Project
This is a web-based ticketing tool that allows users to create tickets, assign them to engineers, and manage ticket details, including adding comments and updating ticket statuses.
Table of Contents
•	Features
•	Requirements
•	Installation
•	Usage
•	Deployment
•	Screenshots


Features
•	User Authentication: Only authenticated users can create and tickets.
•	Role-Based Access: Engineers can update ticket statuses and add comments.
•	Ticket Management: Create, view, update, and filter tickets by status.
•	Commenting System: Add comments to tickets.
•	Security: Basic security measures including CSRF protection and input validation.
Requirements
•	Python 3.x
•	Django 3.x or later
•	Virtualenv (recommended for environment isolation)
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/ticketing-tool.git
cd ticket_tool



2. Set Up Virtual Environment
Create and activate a virtual environment to isolate dependencies.
python -m venv env
env\Scripts\activate
3. Install Dependencies
Install required packages from requirements.txt.
bash
Copy code
pip install -r requirements.txt
4. Run Migrations
Run migrations to set up the database tables.
bash
Copy code
python manage.py migrate
5. Create a Superuser
Create an admin user to access the Django admin panel.
bash
Copy code
python manage.py createsuperuser
then by login u can crerate user to create ticket and add comment
6. Start the Development Server
Run the Django development server.
bash
Copy code
python manage.py runserver
The project should now be running at http://127.0.0.1:8000/.
Usage
Ticket Management
•	Create Ticket: Go to http://127.0.0.1:8000/tickets/create_ticket/ to create a new ticket.
•	List Tickets: Go to http://127.0.0.1:8000/tickets/list_ticket/ to view all tickets with optional filtering by status.
•	Ticket Details: Click on a ticket from the list to view its details and associated comments.
Eg.url - http://127.0.0.1:8000/tickets/tickets/1/
•	Update Ticket Status: Engineers can update ticket statuses from the ticket detail page.
•	Add Comment: Users can add comments to tickets from the ticket detail page.
Authentication
•	Only authenticated users can create and view tickets.
•	Engineers have additional permissions to update ticket statuses and add comments.
•	
7.Screenshot
 
 

 
