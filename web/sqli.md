### Table of Contents 
1. Finding SQLi Vulnerabilities


---------------------------------------------------------------
---------------------------------------------------------------


# 1. Finding SQLi Vulnerabilities

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

**Black Box Testing**
+ Mapp application

+ Fuzz the application
 - Submit _SQL-specific charcters_ such as `'` & `"` and
   look for _error/anomalies_
   
+ Submit _boolean_ conditions such as `OR 1=1` and `OR 1=2`,
  and look for _differences in the applications's responses_
  
+ Submit payloads to trigger _time delays_

+ Submit `OAST payloads` to trigger _out-of-band network interaction_
  when executed within a `SQL Query`, and monitor interactions

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

**White Box Testing**
+ Enable _Web Server Logging_
+ Enable _Database Logging_
+ Mapp application
 - Visible functionality in the application
 - _Regex search_ on all instances in _code that talk to DB_
+ Code Review
 - Follow code path for all input vectors

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 2. Exploiting Union-Based SQLi

[2 rules]: When COMBINING the results of 2 queries by using UNION
  1. # and the order of the columns must be the same in all queries
  2. Data types must be compatible
  
**Exploitation**

+ Figure out the `# of columns` that query is making
 - Use the `ORDER BY` clause
 - Example: `select title, cost from product where id =1 order by 1`
  * `order by 1--`
  * `order by 2--`
  * `order by 3--`
  
 - Use the `NULL VALUES`
  * Examples: `select title, cost from product where id =1 UNION SELECT NULL--`

+ Figure out the `data types` of columns (`mainy interested in strings`)
 - Can use _INT_ to get _ASCII representation of string_

+ Use the `UNION` operator to _output info from the DB_

