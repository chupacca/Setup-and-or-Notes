### Decode base64 and split by char
`echo 'somebase64==' | base64 -d | tr ";" "\n"`
+ This decodes bas64 then splits it based on  
  `;` or `\n`
