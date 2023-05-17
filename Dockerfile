# Base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose the port that the app will run on
EXPOSE 8501

# Set the entry point to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
