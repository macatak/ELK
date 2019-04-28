Translate Filters

What they do - Can do a search and replace on the field or add an additional field based on a field value.

How they do it - Matches an existing field value to perfomr the addition/replacement function.

Why it is useful - Adding new fields based on an existing field value can be very useful. It can provide data enrichment and/or a means to implement addional logic in the filter by adding a key:value. For example, you can add a field to perform a classification of the data

About the conf file - Parses the h2g2.log in sample logs, adds a home planet and occupation field, and outputs to the console

Other Info: It is a good practice to include the fallback value even if you don't plan on using it in your logic. It can easily show what values are not being matched by your translate filter dictionary.
