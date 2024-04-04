FROM chetan1111/botasaurus:latest

# Set environment variable to prevent buffering of Python output
ENV PYTHONUNBUFFERED=1

# Copy requirements.txt to the image
COPY requirements.txt .

# Install Python dependencies
RUN python -m pip install -r requirements.txt

# Create /app directory in the image
RUN mkdir /app

# Set working directory to /app
WORKDIR /app

# Copy the entire project directory to /app directory in the image
COPY . /app

# Run the install command for your Python program
RUN python main.py install

# Specify the default command to run when the container starts
CMD ["python", "main.py"]
