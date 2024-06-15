FROM python:3.9

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port
EXPOSE 5001

# Run the application and create tables
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
