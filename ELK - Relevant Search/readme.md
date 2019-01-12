# ELK---Relevant-Search
Manning Relevant search book

BETA!!!!  
AS IN BROKEN!!!  

Started this book and didnt get very far due to issues starting in Chapter 3. Decided to get back to it and figure out the issues like try to make the code work with Python 3 (code in the book is Python 2), add some error checking in the code since when it fails you have no idea that it didn't work right, and figure out the other issues due to some of the dated commands which are for Elasticsearch 2.0

Issues with TMDB import  
Never could get the Jupyter notebook import to work. The book approach with a bulk import never worked. Posted on the forum for the book and never got a response. Decided to try Logstash but had issues with Logstash parsing the 14MB file (not sure why) so broke the file up and it seemed to work using Logstash (book uses Python code to bulk import). See the tmdb_json.conf file for how this worked)


Issues with the index template  
Index template provided is not longer supported (uses a string type which is now text type) so redid the Index template. Ssee DevTools.txt for the command
