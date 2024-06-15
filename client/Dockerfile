# Use an official Node.js image as the base
FROM node:14

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app for production
RUN npm run build

# Serve the app using a simple HTTP server
RUN npm install -g serve

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["serve", "-s", "build"]
