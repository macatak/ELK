Grok Filters  

What they do - Parses unstructured event data into structured data.  

How they do it - Parser is based on RegEx patterns and custom RegEx.

Why it is useful - You can build a parser for most any event pattern.

Other Info:  
Although grok is probably the most popular filter a dissect filter is a better option. Dissect is less resource intensive since it does not use RegEx. Advice is to use grok only if dissect will not work. Also dissect and grok can be used together.  

Online grok testers are available:  
http://grokconstructor.appspot.com/do/match

Many prebuilt patterns are available that make parsing easier:
https://github.com/logstash-plugins/logstash-patterns-core/blob/master/patterns/grok-patterns  
https://grokdebug.herokuapp.com/patterns
