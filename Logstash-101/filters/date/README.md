Date filters - Just a start, need more format examples

What they do - Take a log date in most any format and transform it into the timestamp

How they do it - Creates a patern that matches the timestamp in the log  
  see https://www.elastic.co/guide/en/logstash/current/plugins-filters-date.html  
  
Why it is useful - The default timestamp in Elasticsearch is when Logstash processed the event. A more useful timestamp is the timestamp in the log. By default the date filter will replace the @timestamp field

About the conf file - Just a snippet, no input or output. It removes the original timestamp field since it is now redundant
