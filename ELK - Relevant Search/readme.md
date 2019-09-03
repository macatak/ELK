# ELK - Relevant-Search
Manning Relevant search book

Started this book and didnt get very far due to issues starting in Chapter 3. Decided to get back to it and figure out the issues like try to make the code work with Python 3 (code in the book is Python 2), add some error checking in the code since when it fails you have no idea that it didn't work right, and figure out the other issues due to some of the dated commands which are for Elasticsearch 2.0 (current version is 7.x)

BETA!!!!  
AS IN BROKEN!!!  

Update 9/3/19 - Came back to this effort for a few different reasons. Figured out a few things that were wrong. Still a work in progess but did make progess. Template is a bust but maybe not needed. At least could duplicate some results in the book.


Issues with TMDB import  
This is just broken due to being done on Elasticsearch 2.0. Version 7.3.1 is latest (as of when I wrote this). Way too many breaking changes to work on 2.0. Book's Jupyter notebook will never work.


Issues with the index template  
fixed by not using a template, may come back to haunt me :)
