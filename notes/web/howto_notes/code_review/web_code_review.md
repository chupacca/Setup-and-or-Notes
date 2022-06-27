# CODE REVIEW 

_-----------------------------_
_===== TABLE OF CONTENTS =====_
_-----------------------------_
1. LANGUAGE SPECIFIC TOOLS 
2. TOOLS 
3. KEYWORD SEARCHES 
4. REFERENCES 

## + + + + + + + + + + + + + + + + + + + + + + + + + + +
## `(1) LANGUAGE` SPECIFIC TOOLS 
### _Lang Specific Tools - `Table of Contents`_ 
   1. Android 
   2. Java 
   3. Kotlin 
   4. PHP 
   
###   1 - Android 
SuSi (Java): https://github.com/secure-software-engineering/SuSi
###   2 - Java 
sink tank (java byte code): https://discotek.ca/sinktank.xhtml
###   3 - Kotlin 
###   4 - PHP 
progpilot: https://github.com/designsecurity/progpilot
 
- - - - - - - - - - - - - - - - - - - - - - - -
## + + + + + + + + + + + + + + + + + + + + + + + + + + +
## `(2)` TOOLS

### _TOOLS - `Table of Contents`_ 
   1. SonarQube 
   2. Cobra 
   3. Graudit 
   4. Semgrep 
   5. CodeQL 
   6. OWASP Code Crawler 
   7. Joern
- - - - - - - - - - - - - - - - - - - - - - - -
###   1 - SonarQube
sonarqube: https://www.sonarqube.org/downloads/

###   2 - Cobra
cobra: https://github.com/FeeiCN/Cobra
documentation: https://cobra-docs.readthedocs.io/en/stable/introduction/
video: https://www.youtube.com/watch?v=PAeD330wQnQ

```
git clone https://github.com/FeeiCN/Cobra.git
cd cobra
python3 -m pip install -r requirements.txt  # there will be a problem with a ConcurrentLogHandler
pip install concurrent-log-handler # use this instead

```

-------------------------------------------------------------------------

###   3 - Graudit 
graudit: https://github.com/wireghoul/graudit
+ script and signature sets that allows you to find potential security flaws in source code
```
git clone https://github.com/wireghoul/graudit
sudo ln -s path/to/graudit/graudit ~/bin/graudit
export GRDIR=/path/to/graudit/signatures
// ^ maybe put this in ~/.bash_aliases
```

`graudit -A -i -L <dir>`


-------------------------------------------------------------------------

###   4 - Semgrep 
[semgrep]: https://github.com/returntocorp/semgrep
`python3 -m pip install semgrep`

+ Check for Python == where the left and right hand sides are the same (often a bug)
`semgrep -e '$X == $X' --lang=py path/to/src`

+ Fetch rules automatically by setting the `--config auto` flag.
+ This will fetch rules relevant to your project from Semgrep Registry.
+ The name of your project will be sent to Semgrep Registry as an identifier
+ to make selecting relevant rules fast next time;
+ source code will not be uploaded.
`semgrep --config auto`

+ Run the r2c-ci ruleset (with rules for many languages) on your own code!
`semgrep --config=p/r2c-ci path/to/src`


**===== Queries =====**
`semgrep --config p/minusworld.java-httpservlet-jsp-xss`
`semgrep --config p/minusworld.flask-xss`

`semgrep --config "p/r2c-security-audit"`
`semgrep --config "p/owasp-top-ten"`
`semgrep --config "p/r2c-ci"`
`semgrep --config "p/ci"`


`semgrep --config "p/r2c-best-practices"`

`semgrep --config "p/insecure-transport"`
`semgrep --config "p/headless-browser"`
`semgrep --config "p/secrets"`


`semgrep --config "p/jwt"`
`semgrep --config "p/auto"`
`semgrep --config "p/mobsfscan"`

-------------------------------------------------------------------------

###   5 - CodeQL

CodeQL: https://codeql.github.com/

###   6 - OWASP CODE CRAWLER 

OWASP Code Crawler: https://github.com/vmnguyen/Code-Crawler
Owasp Code Crawler Database: https://gist.github.com/boyter/31f8226abdefaf723c987bdb6d8ea7f3
+ Low Hanging Fruit

`python3 codecrawler.py --config Code-Crawler/config.json -l <language> --path <dir>`
`python3 codecrawler.py --config Code-Crawler/config.json -l java --path /path/to/dir`

-------------------------------------------------------------------------

###   7 - JOERN 

Joern: https://github.com/joernio/joern
Using Joern: https://www.youtube.com/watch?v=qtGRNb_2Khs&list=PLYyY1D3vDdgAPlrbt3kU8qJWThny6W-yG&index=3

+ `joern-scan /dir/to/code`

## + + + + + + + + + + + + + + + + + + + + + + + + + + +
## `(3) KEYWORD` SEARCHERS 
### _KEYWORDS - Table of Contents_
   1. Java
   2. .NET
   3. C++ / Apache
- - - - - - - - - - - - - - - - - - - - - - - - - - -
  Tool (better than grep): `silver_searcher-ag`: 
   * https://github.com/ggreer/the_silver_searcher
  Code Crawling (page 206): 
   * https://owasp.org/www-pdf-archive/OWASP_Code_Review_Guide_v2.pdf

**LOOK AT THE `*.JSON` FILES IN `lang_json/` DIRECTORY**

**JAVA**  
List of Methods: https://thecodemaster.net/methods-considered-sources-sinks-sanitization/
1. `ag @Operation` / `ag Operation`
  + May point to _api entry point_
2. `ag url`
  + May point to _api entry point_
3. `ag request`
  + May point to _api entry point_
4. `ag \.get`
  + May point to _api entry point_ 
 

-------------------------------------------------------------------------



## + + + + + + + + + + + + + + + + + + + + + + + + + + +
## `(4)` REFERENCES 

**Code Review**
[OWASP Code Review]: `OWASP_Code_Review_Guide_v2.pdf`
[Vickie Blog]: https://vickieli.dev/development/code-review-intro/


**Dangerous Functions**
[DOM XSS Sinks]: https://github.com/wisec/domxsswiki/wiki/Sinks


**PAYLOADS**
[Payloads of Al Things]: https://github.com/swisskyrepo/PayloadsAllTheThings

-------------------------------------------------------------------------

## + + + + + + + + + + + + + + + + + + + + + + + + + + +
 -

