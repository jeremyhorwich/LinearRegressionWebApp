Basic web app project I created to help me learn Flask and HTML

The app allows a user to upload a .csv with two dimensional data, at which point the program performs a linear regression (with options for learning rate and iterations) on the data and creates a visualization for it.

All Python scripts necessary to run the program are in the root folder of the project.
All HTML forms are in /templates. 

--
Instructions to run:

1. Download the project
2. In a terminal session, change working directory to the project folder and activate the virtual environment (learningEnv)
3. In terminal, run "flask -app main run"
   
--

Possible future improvements to the application (this is not an exhaustive list)

- Any kind of file sanitation/input handling on the uploaded file
- More user options (separating the test data from the training data - and by what percentage, ability to make predictions, etc.)
- Ability to support more kinds of regression than only linear and detect the best regression type on an uploaded file
- Fixing various minor code inefficiencies (marked out where possible with commented TODOs in the scripts)

  The above should indicate that my goal with this project was not to create particularly robust backend functionality but to understand how to use Flask to pass data back and forth from the web server
