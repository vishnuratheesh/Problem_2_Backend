###Problem 2 - (Backend)


####Problem:

	Customers often have complaints which call the customer service representatives and talk to. The CSR then logs the information by choosing the available areas to which the issue is related to, into the system. This record is called as a ticket. A ticket has the below details:

		1. Customer Information - DONE

		2. Comments - DONE

		3. Created By

		4. Assigned To - DONE

		5. Status (New,Open – once it is assigned to someone,Closed) - DONE

	You are free to create the list of areas. Create all the required data through backend scripts or any other means

	This application should have a UI with/without authentication to 

		1. Log the ticket. - DONE

		2. Add Comments to a ticket - DONE

		3. Change the status - DONE

		4. Assign to - DONE

		5. Once closed this ticket should not be editable - DONE

		6. View the tickets - DONE

		7. Has to work with REST Services in the backend. - DONE

	Feel free to implement any improvement you see fit for this application.
	
####Solution

Overview:

- Database : PostgreSQL, the schema + dummy data inserts in '/sql/pgSchema.sql'. 

- Tables for: csr, status, problem types, tickets, customers.

- Backend API: FLask + Gunicorn

- Hosted on Heroku: [https://prob2backend.herokuapp.com](https://prob2backend.herokuapp.com), For e.g. A [GET] call to	[https://prob2backend.herokuapp.com/v1/tickets](https://prob2backend.herokuapp.com/v1/tickets), lists all tickets logged.
 
- Front-End Repo: [https://github.com/vishnuratheesh/Problem_2_Frontend](https://github.com/vishnuratheesh/Problem_2_Frontend)