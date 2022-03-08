#Use Python 3.10 as a base image
FROM python:3.10
# Copy contents into image
# WORKDIR /dfe_project/flask-app/
# COPY app.py /flask-app/
COPY . .
# ADD application/templates /flask-app/application/templates/
# install pip dependencies from requirements file
# COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r requirements.txt
# Expose correct port
EXPOSE 5000
ENV MYSQL_URI=db_container
ENV MYSQL_ROOT_PASSWORD=$MYSQL_PW
# Create an entrypoint
ENTRYPOINT ["python3", "app.py"]
