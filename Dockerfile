# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
# (Not strictly necessary for Telegram bots, but good practice)
EXPOSE 8080

# Define environment variable
#ENV TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"

COPY translator_bot.py /app
COPY .env /app

# Run app.py when the container launches
CMD ["python", "translator_bot.py"]
