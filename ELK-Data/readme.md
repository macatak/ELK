# ELK-data

Learning the ELK basics is not hard but to dive deeper large data sets are required. To that end this repo is to keep track of the steps to do accomplish that. Generally there are 3 steps  
1 - Find and download a good data set  
2 - Create an index template to setup the index in Elasticsearch  
3 - Create a Logstash parser to parse the downloaded dataset into Elasticsearch  

... a little more info on the steps ....  
1A - Need several thousand entires at a minimum.  
1B - Ideally we want geo data (longitude/latitude) so we can use the geo related searches and visualizations.  
1C - Ideally we want a format we can easily parse. CSV and JSON can be good options and are widely available.  
1D - https://www.data.gov/ is a great source. You can search by subject matter or publishing organization.  

2A - Depending on the feed we may have to declare a timestamp field that reflects the actual date of the entry.  
2B - If we are using geo data that will need to be setup.  
2C - Since this is just testing data we can set the shards to 1 and replicas to zero. Not required but makes the index green in a single node setup.  

3A - Depending on experience this is really easy or really hard. All of the conf files will push to Elasticsearch as well as standard out. Easiest way to get started is to copy 5 entries to a smaller file and comment out the Elasticsearch output lines.  
3B - Use dissect where you can (which should probably be most everywhere given the standard data) instead of grok. Grok can be VERY resource intensive where dissect is not.  


Files in this repo  
I will try to include 3 files for each data set:  
1 - A readme with general information and any issues or other comments.  
NOTE - Download link for data file is in the readme.  
2 - A Dev Tools file with the commands to create the template and other relevant commands  
3 - A Logstash conf file. These will need to be edited based on the path to the downloaded data set.  
  
NOTE : Logstash can be run manually from the command line with this syntax:  
<path to Logstash install>/bin/logstash -f <conf file>  
  
For example (Linux install):    
/usr/share/logstash/bin/logstash -f nypd_csv.conf  

Another useful command is to run a syntax check on the the conf file. Adding a '-t' to the end of the command will do that:  
/usr/share/logstash/bin/logstash -f nypd_csv.conf -t


Data sets  
NYPD Motor Vehicle Collisions  
    - around 900K entries  
    
Chicago Crimes - One year prior to present (seems to have more potential for learning than NYPD dataset)  
    - around 200K entries  
