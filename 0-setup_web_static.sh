#!/usr/bin/env bash
# Install Nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx
# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Create a fake HTML file
sudo touch /data/web_static/releases/test/index.html
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data
# Update the Nginx configuration using sed
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restart Nginx
sudo service nginx restart

