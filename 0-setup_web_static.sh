#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt -y update
sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "I am HTML" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

config="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

sudo sed -i "/server_name _;/a \ $config" /etc/nginx/sites-available/default

sudo service nginx restart
