### Intro to this readme file 

This project required the development of a basic Python application,
performing CRUD operations using Flask and MySQL.

The exercise is accessible on VM hosted on Microsoft Azure.

This application is a workout manager that allows the user to create a
list of exercises by pre-selecting these or choosing the random
function. Users can also add, delete, update and create new exercises;
and mark exercises as 'complete' or 'incomplete'.

The Flask application is running on a docker container on port 5000,
communicating with a separate MySQL docker container on port 3306. A
separate nginx container runs a reverse proxy to the Flask app,
effectively making the Flask application accessible on port 80
externally.\
A Jenkins pipeline with a webhook has been set up for the CI/CD,
automating deployments and testing all the application on each code
update.\
The integration happens via a docker swarm orchestration.

The use of Microsoft Azure, Docker, GitHub and Jenkins was a requirement
from the specification for the final project by the course providers.

Please see here how the app works by using the following link:\
https://youtu.be/C7tSzjnbVG0![](media/image1.jpeg){width="1.8802307524059492in"
height="1.057630139982502in"}

Blaster Gym

Contents

Brief

[Additional Requirements]{.underline}

[My Approach]{.underline}

-   [Architecture]{.underline}

    -   [Database Structure]{.underline}

    -   [CI Pipeline]{.underline}

-   [[Project
    Tracking]{.underline}](https://github.com/htr-volker/individual-project-example#project-tracking)

-   [[Risk
    Assessment]{.underline}](https://github.com/htr-volker/individual-project-example#risk-assessment)

-   [[Testing]{.underline}](https://github.com/htr-volker/individual-project-example#testing)

-   [[Front-End
    Design]{.underline}](https://github.com/htr-volker/individual-project-example#front-end-design)

-   [[Known
    Issues]{.underline}](https://github.com/htr-volker/individual-project-example#known-issues)

-   [[Future
    Improvements]{.underline}](https://github.com/htr-volker/individual-project-example#future-improvements)

-   [[Authors]{.underline}](https://github.com/htr-volker/individual-project-example#authors)

### 

### Project documentation required by QA

## [Brief]{.underline}

The brief provided for this project sets the following as its overall
objective: \"To create a web application that integrates with a database
and demonstrates CRUD --- utilises create, read, update and delete
functions.

To utilise containers to host and deploy your application.

To create a CI/CD pipeline that will automatically test, build and
deploy the application."

## Additional Requirements

In addition to what has been set out in the brief, I am also required to
include the following:

Jira board

User Stories/points

Git and GitHub to commit all the builds and final coding of the
application

A relational database, consisting of at least two tables that model a
relationship

Clear documentation of the design phase, app architecture and risk
assessment

A python-based functional application performing CRUD operations using
Flask and MySQL.

Test for the application through Pytest, which will include automated
tests for validation of the application

A front-end website, created using Flask

Code integrated into a Version Control System which will be built
through a CI server and deployed to an Azure cloud-based virtual machine

CI/CD via Jenkins

Docker for configuration and orchestration for the use of separate VM's.

### The app 

In order to achieve the above requirements, I have created an app for
*Blaster Gym*, that allows the user to add, create, list and remove
exercises; and also to create a workout set in two ways: by selecting
the exercises from the list, or at random with a press of a button. The
user can also set the exercises as *complete* or *incomplete.*

### Planning stages:

Before getting into development of the application, I have created the
following:

-   project tracking board

-   development board using Scrum

-   MoSCoW analysis

-   risk analysis

-   EDR diagram

The first development Sprint should last one week, and I used story
points to help decide what elements would be developed now, and what
would be left for future development (future sprints).

## Project Tracking

A project tracking board was created with the different stages of the
project displayed for easy tracking, this is also used as support hub
for the overall project.

![image](https://user-images.githubusercontent.com/81493790/157868126-8514780e-a1a5-4f7f-971b-234fbdf49354.png)


The board above is capturing the following:

*Project Requirements* A list of requirements set out in the brief in
order for this to be a successful project.

*Project Resources* List of relevant resources for quick access.

Link to U*ser Stories* using Scrum methodology. Any functionality that
is implemented into the project first begins as a user story. This keeps
the development of every element of the web app focused on the user
experience first. - this tab has a link to the Jira stories added on the
Blaster Gym developers board, which will be used to track the Sprint.

*Planning* The initial stages where a specific element (e.g. a block of
code, a server, etc.) is being considered for implementation.

*In Progress* Once the element has had any code written for it/exists in
any way, it is placed in the \'in progress\' list.

*Testing* Once the element has been created, it moves to the \'testing\'
list, where its functionality is tested.

Sprint planning:

[Epic 1: Create Blaster Gym App]{.underline}\
To have a fully functioning app at the end of the first week, that meet
the CRUD functionality. Improvements will be made from week two.

User stories sprint 1:

BLG-2: As a user, I want to add a new exercise, so I can create exercise
sets\
BLG-3: As a user, I want to view all exercises, so I know what is
currently available\
BLG-4: As a user, I want to change the description of the exercise, so I
can update its contents after creating it\
BLG-5: As a user, I want to delete an exercise, in case is no longer
relevant\
BLG-6: As a user, I want to set an exercise as completed, so I know
which ones I have completed already\
BLG-7: As a user, I want to set an exercise to be incomplete, so I know
what I have to do next\
BLG-8: As a user, I want to create new set of exercises that are chosen
randomly  with a click of a button\
BLG-9: As a user, I want to create a set of exercises by choosing from
the full list so I get to choose the exercises I want to do next\
BLG-15: add MySQL dependancy: As a developer, I want my app to be fully
integrated and functional.\
BLG16: As a developer, I want to have a single entry point to install
all Docker images.\
BLG 17: As a developer, I want to test the code to ensure changes will
not introduce bugs.

Stories were allocated points and added to the backlog for Sprint1:

![image](https://user-images.githubusercontent.com/81493790/157868844-a24c8aaa-991a-44e9-8d7a-29747c7755ac.png)


Jira board progress throughout the Sprint can see below:

![image](https://user-images.githubusercontent.com/81493790/157868677-d1a5ca0f-7717-41fa-b9e1-b131ace8223f.png)


Moscow analysis sprint 1 displayed on the board below:

![image](https://user-images.githubusercontent.com/81493790/157868745-ee79dade-f185-4822-859a-b0e278808420.png)


[Epic 2: Phase 2 development\
]{.underline}To fix any bugs and work on the interface and add users
functionality.

User stories sprint 2:

BLG-11: As a gym owner, I want to see members list so I can see who is
using the gym more often\
BLG-12: as a gym owner, I want to set personalised workouts for
individual members\
BLG-13: as a user, I want a nice interface, including the Master Gym
logo on the website so I know I am using the right application.\
BLG-14: as a user, I want all exercises marked as
[']{dir="rtl"}incomplete[']{dir="rtl"} before starting a new session.

![image](https://user-images.githubusercontent.com/81493790/157869083-070ec62b-2219-4283-a83a-ee32799b4cda.png)


## Risk Assessment

A succinct risk assessment has been carried out prior to the start of
the project. The aim of the risk assessment is to consider possible
challenges/issues and have mitigations in place to reduce the impact of
these risks. As I start building experience as a developer, I expect
that I will be exposed to more risks, and also ways to mitigate these,
so the list will get longer.

![image](https://user-images.githubusercontent.com/81493790/157869133-571646e3-ff3b-4b3c-b1de-7a6591906adc.png)


### Entity Relationship Diagram (EDR)

After deciding what the application would demonstrate, the next step was
to design the Database Layer Relationship. This is very important as it
supports the developers so they can focus on what is needed for the
successful development of the final project. I decided to produce a
many-to-many relationship model. This requires that two tables are
related by a third 'association' or 'relationship' table. One exercise
can be in several workouts, and a workout can have many exercises. This
will also be handy in a future development, where users functionality
will be added. Pictured below is the entity relationship diagram (ERD)
showing the structure of the database. Everything in green has been
implemented into the app, while everything in red is scheduled for
future Sprints.
![image](https://user-images.githubusercontent.com/81493790/157869190-02b2c6f6-9bed-40f2-89af-002bdd71be64.png)


### The flask application

Homepage:

Front-End Design

The front-end of the app is very basic at this stage, as it is built
purely with very simple HTML. Nonetheless, it is largely functional and
stable:

![image](https://user-images.githubusercontent.com/81493790/157869284-06d4d1a5-86c3-4a82-be74-58028f7cb6c1.png)


I have pre-populated the database with some exercises, and a fixed
number of workout sets, so there will always be a few options for the
user to choose from the start.

APP functionality:

CRUD:

Create new exercises (satisfies \'Create\') that stores:

*Exercise Name*

*Number of repetitions*

*Exercise status (set automatically to incomplete when a new exercise is
added.*
![image](https://user-images.githubusercontent.com/81493790/157869376-cd7cfced-76da-41d4-8ec1-706531e32e40.png)


View and update name of exercise and repetition (satisfies \'Read\' and
'Update')

View: all exercises are listed on the Homepage\
![image](https://user-images.githubusercontent.com/81493790/157869515-f911e7fa-d297-4a85-a6fd-5d8037b01aea.png)


Update: (as shown below):\
![image](https://user-images.githubusercontent.com/81493790/157869566-78899e93-6096-4f89-832e-8fa86d40ebed.png)


Read/list all exercises that have been created (satisfies 'Read') - as
demonstrated above on the Homepage

Toggle exercise status - complete/incomplete (satisfies 'Update')\
![image](https://user-images.githubusercontent.com/81493790/157869651-d723257d-6d6a-49b6-a5b7-9d1e688bbb00.png)


Additionally, I would like to allow the user to:

Use the 'random' option to easily create a new workout set\
![image](https://user-images.githubusercontent.com/81493790/157869715-00a2857e-d811-48b6-8994-e506be5d8ee8.png)

![image](https://user-images.githubusercontent.com/81493790/157869781-2be6ae15-0a85-40ce-8e0e-915faed50ad6.png)


10 min random selection: 3 exercises

20 min random selection: 5 exercises

30 min random selection: 7 exercises

40 min random selection: 10 exercises

If preferred, select the exercises to create a new set\
![Image](https://user-images.githubusercontent.com/81493790/157869868-2201ee0e-b0bd-4b99-a834-cf0a198accf8.png)

## CI/CD and infrastructure Pipeline

![image](https://user-images.githubusercontent.com/81493790/157869911-fe86ada1-4721-405b-b1c6-64f7b79addb4.png)


Pictured above is the continuous deployment and integration pipeline
with the associated frameworks and services related to them. The
pipeline automatically starts in Jenkins as soon as the main branch is
changed on GitHub via a webhook to be automatically installed on the
cloud VM. From there, tests are automatically run and reports are
produced.

This process is handled by a series of Jenkins \'pipeline\' jobs with
distinct build stages. The separate pipelines allow for flexibility to
execute the different actions. The design of this type of job means that
if a previous build stage fails, the job will fail altogether and
provide you with detailed information as to where this occurred. The
build stages are:

\'Build\' (would be more accurately named \'Installation\' as Python
doesn\'t require building, in the strictest sense)

\'Test\' (run pytest, produce coverage report)

\'Run\' (deploy application on the host VM)

Once the app is considered stable, it is then deployed to a separate VM
for deployment. This service is run using the Python-based HTTP web
server which is designed around the concept of \'workers\' who split the
CPU resources of the VM equally. When users connect to the server, a
worker is assigned to that connection with their dedicated resources,
allowing the server to run faster for each user.

### Testing

Pytest is used to run unit tests on the app. Jenkins produces console
outputs (pictured below) that will inform the developer how many tests
the code passed and which tests they failed. For my application, the
testing for the CRUD functionality and validation of all files has been
carried out.

By using webhooks on Jenkins, tests are automatically carried out every
time the code is updated/pushed in GitHub.

Screenshots for test coverage reports sow that coverage reached 99%:

![Image](https://user-images.githubusercontent.com/81493790/157869945-9e965f9f-3195-44a2-a88d-ea4902ab5ac9.png)

![Image](https://user-images.githubusercontent.com/81493790/157869976-4fe79c9a-2e2e-47d3-a966-2dd3e63c845b.png)

## Known Issues

There are a few bugs with the current build:

If a user marks an exercise as 'complete', this information is stored.
Once the user creates a new workout list, the exercise marked as
'complete' need to be manually updated to show as incomplete. This is
set to be fixed on the next stage of development.

Currently, there is no form validation. Therefore, a user can create an
'empty' exercise. Form validation is to be implemented in a future
version of the app as per planning.

## Future Improvements

There are a number of improvements I would like to implement (outside of
current bugs):

Add and remove users, so workouts can be tailored

Offer statistics so it is possible to track usability of the app

Chat function, so trainer don't have to be in the Gym

Aesthetic overhaul, to make the front-end both more appealing and more
functional.

Users can customise their accounts with profile pictures, biometric
data, change the colour palette of the website, etc.

Tracking of biometric data and comparison, so user can utilise the app
for tracking fitness.

## Supporting documentation

### Security: 

Password relies on an environment variable. As the password is not
displayed anywhere, it minimises risk of external breach, This is
achieved by using Jenkins credential manager.

![image](https://user-images.githubusercontent.com/81493790/157870032-308bac4a-1ec0-4d5b-9e42-0074706316b5.png)


### Refactoring of the pipeline:

Initially, deployment was manually done connecting Jenkins server onto
the worker machine, as per screenshot below.

Further down, evidence is provided of a streamlined set-up, meeting the
requirement of using docker swarm.

![image](https://user-images.githubusercontent.com/81493790/157870079-bb5339d2-3412-47d7-a70f-9be2e42d08c9.png)

### Advanced deployment strategies evidence/docker swarm with dedicated pipelines for different stages: 
![image](https://user-images.githubusercontent.com/81493790/157870157-cbc35e50-52e2-4877-a192-869927d67442.png)

### Unit test:

![image](https://user-images.githubusercontent.com/81493790/157870193-f3883146-217d-4fbe-925b-a5b181615df8.png)


### Publish docker:

![image](https://user-images.githubusercontent.com/81493790/157870220-3d3cf42d-a3dd-480a-845e-1a07b74ebdb8.png)


### Create services: 

![image](https://user-images.githubusercontent.com/81493790/157870256-5f5353e7-a802-4027-8a63-07c8637e0bc7.png)

### Deployment logs:

During the build and testing of the app and CI/CD pipeline, a number of
logs for the different pipelines have been generated in Jenkins.

Logs are an extremely useful tool as these provide evidence of any
issues, so developers can adapt coding, looking for a successful outcome
on the subsequent builds.

Please see some evidence of logs for the 'publish docker' and 'unit
tests' below:

![image](https://user-images.githubusercontent.com/81493790/157870351-36e7efeb-fb68-49e9-b432-dd612973d9a3.png)
![image](https://user-images.githubusercontent.com/81493790/157870657-19e2061f-253b-4d4d-a9c9-ac57af21920b.png)


### Webhook between Github and Jenkins:

![image](https://user-images.githubusercontent.com/81493790/157870503-2d90c5dc-7a00-4aed-9fdc-e5f65e741599.png)


### Examples of code refactoring: 

![image](https://user-images.githubusercontent.com/81493790/157870414-76247d94-4e86-4e39-96e5-e7e4d1f70845.png)
![image](https://user-images.githubusercontent.com/81493790/157870555-e09254c4-7c2e-47c3-8e39-e440a1d9cd84.png)
![image](https://user-images.githubusercontent.com/81493790/157870567-e8ac6fc6-7eac-4ae8-861e-097501e14d9f.png)

### Author

Samira Pecce, v1 March 2022
