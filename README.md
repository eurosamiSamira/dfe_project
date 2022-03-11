DFE Cloud Specialism – Final Project
This project required the development of a basic Python application, performing CRUD operations using Flask and MySQL.
The exercise is accessible on VM hosted on Microsoft Azure.
This application is a workout manager that allows the user to create a list of exercises by pre-selecting or choosing the random function. Users can also add, delete, update and create new exercises; and mark exercises as ‘complete’ or ‘incomplete’. 
The Flask application is running on a docker container on port 5000, communicating with a separate MySQL docker container on port 3306. A separate nginx container runs a reverse proxy to the Flask app, effectively making the Flask application accessible on port 80 externally.  A Jenkins pipeline with a webhook has been set up for the CI/CD, automating deployments and testing all the application on each code update. The integration happens via a docker swarm orchestration. 
The use of Microsoft Azure, Docker, GitHub and Jenkins was a requirement from the specification for the final project by the course providers.  
 Please see here how the app works by using the following link:  https://youtu.be/C7tSzjnbVG0


Brief
The brief provided for this project sets the following as its overall objective: "To create a web application that integrates with a database and demonstrates CRUD functionality.
To utilise containers to host and deploy your application. 
To create a CI/CD pipeline that will automatically test, build and deploy the application.”
This should be the culmination of all learning over the last few weeks. The main objective has been to create an application that utilises create, read, update and delete functions.

![image](https://user-images.githubusercontent.com/81493790/157839367-662eca10-78b4-42e8-b1db-c24b08889d3f.png)
