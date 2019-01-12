Chicago  Crimes - One year prior to present - This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that have occurred in the City of Chicago over the past year, minus the most recent seven days of data. -

Can be downloaded here - https://catalog.data.gov/dataset/crimes-one-year-prior-to-present-e171f


Files:  
Kibana Dev Tools commands – ChicagoCrime1year_devTools.txt  
Logstash conf – chicago_crime1year.conf  

Notes:   
There appears to be missing geo data. When Logstash is running there are errors about Longitude must be a number.  
There were ocer 200K hits parsed into Elasticsearch so a fairly good sample.  
Use Last 2 Years in the Kibana time picker to get the most out of it.  
