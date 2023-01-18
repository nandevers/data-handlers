FROM python:3.11

# Create a new user
RUN useradd -ms /bin/bash myuser
USER myuser

# Create a new directory
RUN mkdir /home/myuser/app
WORKDIR /home/myuser/app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the source code
COPY . .

# Set the entry point
#ENTRYPOINT ["python"]
#CMD ["main.py"]
