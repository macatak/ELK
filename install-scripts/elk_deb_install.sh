#!/bin/bash

# ELK + Filebeat download/install/configure script for Debian based systems

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#		MUST BE RUN AS ROOT
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# download/install/configure ELK + filebeat

# get the packages
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.2.deb
wget https://artifacts.elastic.co/downloads/logstash/logstash-6.2.2.deb
wget https://artifacts.elastic.co/downloads/kibana/kibana-6.2.2-amd64.deb
wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.2.2-amd64.deb

# download some basic configuration files
wget https://raw.githubusercontent.com/macatak/ELK-Install-scripts/master/LS_beats.conf
wget https://raw.githubusercontent.com/macatak/ELK-Install-scripts/master/basicFilebeat.yml
wget https://raw.githubusercontent.com/macatak/ELK-Install-scripts/master/bodgeit_access.log

# install the packages
dpkg -i elasticsearch-6.2.2.deb
dpkg -i logstash-6.2.2.deb
dpkg -i kibana-6.2.2-amd64.deb
dpkg -i filebeat-6.2.2-amd64.deb

# backup the YML's
cp /etc/elasticsearch/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml.orig
cp /etc/logstash/logstash.yml /etc/logstash/logstash.yml.orig
cp /etc/kibana/kibana.yml /etc/kibana/kibana.yml.orig
# moving (not copying) this since we're going get a simplified yml
mv /etc/filebeat/filebeat.yml /etc/filebeat/filebeat.yml.orig

# copy the filebeat and logstash basic files
mv LS_beats.conf /etc/logstash/conf.d/beats.conf
mv basicFilebeat.yml /etc/filebeat/filebeat.yml

# create a folder for logs to be parsed
mkdir -p /home/filebeat_logs/test_1
# move a test log over
mv bodgeit_access.log /home/filebeat_logs/test_1/

# setup elasticsearch
path="/etc/elasticsearch/"
filename="elasticsearch.yml"
strClusterNameOrig='#cluster.name: my-application'
strClusterNameNew='cluster.name: local_elk'
strHostOrig='#network.host: 192.168.0.1'
strHostNew='network.host: localhost'
strPortOrig='#http.port: 9200'
strPortNew='http.port: 9200'
sed -i "s|$strClusterNameOrig|$strClusterNameNew|g" $path/$filename
sed -i "s|$strHostOrig|$strHostNew|g" $path/$filename
sed -i "s|$strPortOrig|$strPortNew|g" $path/$filename

# Logstash yml doesn't need any config for basic ops
# connects to Elasticsearch in the conf file

# setup Kibana
path="/etc/kibana/"
filename="kibana.yml"
strPortOrig='#server.port: 5601'
strPortNew='server.port: 5601'
strElasticsearchOrig='#elasticsearch.url: "http://localhost:9200'
strElasticsearchNew='elasticsearch.url: "http://localhost:9200'
sed -i "s|$strPortOrig|$strPortNew|g" $path/$filename
sed -i "s|$strstrElasticsearchOrigOrig|$strstrElasticsearchNew|g" $path/$filename

# skipping filebeat setup since we're going to grab a basic yml file
# setup Filebeat
# really just for dashboard for Kibana
#path="/etc/filebeat/"
#filename="filebeat.yml"
#strPortOrig='  #host: "localhost:5601"'
#strPortNew='  host: "localhost:5601"'
#strPathOrig='    - /var/log/*.log'
#strPathNew='    - /home/*.log'
#sed -i "s|$strPortOrig|$strPortNew|g" $path/$filename
# changing path to a location where there should't be any log files
# Not really needed but this way it won't atart parsing anything we don't want
#sed -i "s|$strPathOrig|$strPathNew|g" $path/$filename


# set the owners
chown -R elasticsearch:elasticsearch /etc/elasticsearch/
chown -R logstash:logstash /etc/logstash/
chown -R kibana:kibana /etc/kibana/

# enable the services
systemctl daemon-reload
systemctl enable elasticsearch.service
systemctl enable logstash.service
systemctl enable kibana.service
systemctl enable filebeat.service


# start the services
systemctl start elasticsearch.service
systemctl start kibana.service
systemctl start filebeat.service
systemctl start logstash.service

# delay for 30 seconds to let the services come up
echo -e '30 second delay for services to start'
sleep 30
echo -e '30 second delay over'

# load the Filebeat templates into Elastisearch
filebeat setup --template -E output.logstash.enabled=false -E 'output.elasticsearch.hosts=["localhost:9200"]'

# load the Filebeat dashboards into Kibana
filebeat setup --dashboards

# stop Filebeat because it's pointless to have it running without
# a valid configuration
# added a config
# systemctl stop filebeat

echo 'Done'
echo 'Elasticsearch - localhost:9200'
echo 'Kibana - localhost:5601'
echo 'Place a file with a .log extension in the /home/filebeat_logs/test_1 folder and it should be parsed'
echo 'if everything worked right the Tomcat access log should be in the logstash* index'
