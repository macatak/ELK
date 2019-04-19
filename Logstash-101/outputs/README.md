Output Plugins  

out_stdout.conf - send to standard (console) output, most useful for learning and developing  

out_stdout_dots.conf - send to standard (console) output but with dots as an indicator of processing

out_es_basic.conf - Standard Elasticsearch output, OK for learning and developing not really useful in the real world  

out_es_index.conf - Send to a specific index in Elasticsearch, the more you learn the more useful this will become  

out_es_variable.conf - Destination index is determied by logic. 
NOTE - This file assumes the variable (field name or metadata) exists
