#! /bin/bash
sudo systemctl stop apache2
sudo systemctl start nginx
sudo systemctl start skills-incubator
