# RealState Complaint Management Odoo APP

## Features

- **Website View Form**: Users can fill out a form without any authorization via the link: [http://localhost:8015/complaints/form](http://localhost:8015/complaints/form).

- **User Groups**: Groups of representatives and supervisors are created, and users can be assigned to either group in the users section of Odoo settings.

- **Pipeline Creation**: A pipeline for managing complaints has been created.

- **Dockerfile Solution**: The repository includes a Dockerfile solution allowing the creation of a customized image based on Odoo 15 image, including the custom addon realstate_complaint.

- **Action Plan Button**: This button prints out a document inside the view in the flow of the pipeline. Note: Further implementation is needed to match exact requirements.

## Yet to Develop

- **Email Notifications**: At certain steps, it's required to send an email to specific users. While the feature is partially implemented, there were errors encountered. Due to time constraints, further work on this feature is pending.

- **Development of Test Cases**: Test cases for the application need to be developed.

- **Dashboard Development**: Given more time, a dashboard would be developed to enhance the application's functionality.

## Pipeline Flow


1- a new complaint record is created by an external user without any authorization through the following link:
http://localhost:8015/complaints/form
<img width="650" alt="1" src="https://github.com/masoudsalehii/Complaint-Management-Odoo/assets/86241995/c2757172-5f29-48b1-9490-963b12010a57">

2- The record is added to the list of the complaints in a tree view with the state of New. The representative and supervisor can see the list of the complaints.



3- In the state New, the representative and supervisor can open the complaint record, and they both can click on Classify button, Drop button, And Solved Button:

   Solved: with clicking on solved button, the state changes to solved:
   
	 - In the state Solved, the representative and supervisor both can click on Close buthon. 
  
	 - Loggically when the state changes to Closed, the tenent should be notified by an email. Due to the lack of time the email part is not implemented.
  
   Drop: If they click on Drop, the state changes to Closed
   
   Classify: if they click on classify button, the state changes to In Review:

   - In the state in Review the supervisor should click on Reviewed button, after the reviewing the issue.
     
   - In "In Review" state, the representative will not have the option to click on the Reviewed button.

<img width="935" alt="review" src="https://github.com/masoudsalehii/Complaint-Management-Odoo/assets/86241995/d1c6b918-ee09-4957-9504-c89dac36b3ea">



   - After clicking on Reviewed button, the state changes to  progress

   - In progress state, the manager can click on Print Action Plan button, and the representative cannot see this button.

<img width="937" alt="progress" src="https://github.com/masoudsalehii/Complaint-Management-Odoo/assets/86241995/9f25cdb4-55d4-4b2d-b7c4-e3f483ba3f5c">

   - After solving the issue, the supervisor or representatvie can click on both Solved or Drop buttons

3- After clicking on Solved button the state changes to solved


4- Finally the supervisor or representative can click on the the close button to close the issue


