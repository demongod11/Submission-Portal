Submission Portal:


Description:

This application contains 3 user interfaces. They are:
1) Admin Interface
2) Course Instructor Interface
3) Student Interface

User Authentication:    
IIT Guwahati Outlook authentication has been implemented. i.e, only users with IITG outlook email id will be able to login to our website.

Firstly, an admin would need to authenticate the course instructor's email id through admin's interface. 
Here the admin would need to go to 'Users' section of the admin panel and navigate to course instructor's email id.
Now when he clicks on the course instructor's email id, the admin will get an option to enable the 'is_staff' option of the course instructor's email id to true. By doing this, the email id would be given access as an Instructor.

When an instructor logs in using his email id he will be redirected to his home page where details of all the assignments given by him would be displayed. Here he can
1) View assignment
2) Add assignment
3) Edit assignment
4) View submissions of an assignment
5) Evaluate submissions of an assignment

Also error checks for all the forms has been implemented. For Ex: If an instructor awards an assignment for more marks than the maximum marks of the assignment then a popup alert will be displayed showing the error and the page will be reloaded.

When a student logs in using his email id he will be redirected to his home page where details of all the assignments given to him would be displayed. Here he can
1) View all assignments
2) Submit his submission
3) If the deadine has not been completed yet then there is an option for the student to edit his submission
4) If the deadline has passed then the student would no longer be able to submit his submission
5) View his grades/feedback

Also "Real-Time Notifications" feature has been implemented for this portal using django channels i.e., notifications would be displayed to students or course instructors in "real-time". Notifications implemented in this portal includes the following
1) When an instructor uploads an assignment then the students would get a notification that "so-and-so assignment has been uploaded"
2) When an instructor edits an assignment then the students would get a notification that "so-and-so assignment has been edited"
3) When a student has submitted his submission for an assignment then the instructor would get a notification that "so-and-so student has submitted this assignment"
4) When an instructor grades/evaluates an assignment then the student would get a notification stating "Your submission for so-and-so assignment has been graded"
5) When the deadline of an assignment has been passed a notification would be displayed stating "so-and-so assignment's deadline has passed"



How to run this project:

git clone <this_repository_git_url>                     ---- Clones this repository to your local pc                  
virtualenv some_venv                                    ---- Initializes a virtual environment
some_venv/Scripts/activate                              ---- Activates the initialised virtual environment
pip install -r requirements.txt                         ---- Installs all the libraries/modules required for this project
{ Register your app in Microsoft Azure Portal }         ---- Registering app in azure to fetch microsoft outlook api's for authentication
                                                             Details about how to do this has been recorded and uploaded (Azure App Setup.mkv)
{ Connect your backend to Azure API endpoint }          ---- The backend of the project needs to be connected to the API endpoint that we've got in the previous step
                                                             Details about how to do this has been recorded and uploaded (Backend Azure Connection.mkv)                                                  
python manage.py makemigrations                         ---- Makes migrations to all the models
python manage.py migrate                                ---- Migrates the models to database (dbsqlite in this case)
python manage.py runserver                              ---- Runs the local server


Tech Stack Used:
Frontend:   HTML, CSS, JavaScript, TailwindCSS, Bootstrap
Backend :   Django
Database:   dbsqlite