# kuralabs_deployment_2
Testing stage of the CI/CD pipeline deployment 2
Chanesh Mahadeo
Kura Labs
9/26/2022

Deployment 2


Intro:
	Welcome to deployment 2 where we go further than the last deployment and actually automate another part of our deployment. In our last deployment we set up our jenkins environment then manually zipped our application and uploaded it to elastic beanstalk. In this deployment we will be automating this process and actually have Jenkins handle our deployment step after a few configurations.

Issues:
	Obviously multiple issues are bound to arise in a process such as this. My first issue in following the original documentation was that it lacked specific guidelines to various issues. I fixed these within my own steps but examples of this would include installing the dependencies. Unzip is not a dependency that comes with an aws ec2 so you must apt install this. Also the jenkins user must first be added to the sudoers group. The jenkins user must also have its bin added to the path in order to run the eb command. This is all solved within my userdata script when creating the ec2. My script will do all of this and have the environment set up properly before you even load into the ec2. The workspace folder was also not in the location that it was assumed to be in the original documentation.

Changes:
	Some changes I made to the original documentation was the order of the steps in which things were executed. First, my userdata script covers a lot of background setup steps which just take up time and dont need to be manually done by the engineer. Next I removed the github access token step because it is not needed as this is a public repository. I also removed the need to include the shell everytime you su into the jenkins user because jenkins automatically assigns the bash shell to the jenkins user. I confirmed this by running cat /etc/passwd upon initial startup of my ec2 to verify that it had a shell assigned to it. I corrected the location of the workspace folder. Another change I made to this deployment was I added a test to check if the json storing the “go” variable was working correctly. In the future I will be adding a Cypress test, adding more to the html of the site, and adding more phases to the jenkins including a linter.
