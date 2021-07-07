# The TechnoFreak Blog
A blogging application developed in Python using Flask framework.
**************************************************************************

How to spin up application specific docker containers on AWS EC2 server?

Paste this in EC2 in user Data while launching the instance:

#! /bin/sh  
yum update -y  
yum install git -y  
amazon-linux-extras install docker  
service docker start  
usermod -a -G docker ec2-user  
chkconfig docker on  
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)"  -o /usr/local/bin/docker-compose  
sudo chmod +x /usr/local/bin/docker-compose  

Once instance is up, execute below commands in home/ec2-user  

git clone https://github.com/roshangardi/Flask_Blog  
docker-compose up --build  

Make sure you're changing the values of email and password in envvars file.  

---
### Blog Application Web Interface:
![BlogApplication](https://github.com/roshangardi/Python-Flask-Blog-Application/blob/main/Images/PythonBlogApplication.PNG?raw=true)
### Support

Reach out to me on:

- LinkedIn at <a href="https://www.linkedin.com/in/roshan-gardi-23090b129/" target="_blank">`Roshan_Gardi`</a>
