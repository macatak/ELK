Grok Filters  

What they do - Parses unstructured event data into structured data.  

How they do it - Parser is based on RegEx patterns and custom RegEx.

Why it is useful - You can build a parser for most any event pattern.

Other Info:  
Although the most popular a dissect filter is a better option. Disset is less resource intensive since it does not use RegEx.  

Online grok testers are available:  
http://grokconstructor.appspot.com/do/match

Many prebuilt patterns are available that make parsing easier:
https://github.com/logstash-plugins/logstash-patterns-core/blob/master/patterns/grok-patterns  
https://grokdebug.herokuapp.com/patterns
