# base image  
FROM python:3.8
LABEL maintainer="yusufadell.dev@gmail.com"  
# setup environment variable  
ENV DockerHOME=/home/fluxy/mysite  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]