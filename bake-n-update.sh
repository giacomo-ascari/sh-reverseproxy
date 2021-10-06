#!/bin/bash
python3 builder.py
cp conf/* /etc/nginx/sites-available/
rm /var/www/html/*
cp www/* /var/www/html/
systemctl restart nginx