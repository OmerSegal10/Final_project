# Use the official MySQL image from the Docker Hub
FROM db-app:latest

# Copy the database schema file into the container
COPY Sports_db.sql /docker-entrypoint-initdb.d/

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=omer2002
ENV MYSQL_DATABASE=Sports_db

# Expose the MySQL port
EXPOSE 3306
