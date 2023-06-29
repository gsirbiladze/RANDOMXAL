# RANDOMXAL
Just Random Stuff

**Regex for IP (Starting with zero is included)**
```
^((?![3-9][0-9]{2}|2[6-9][0-9]|25[6-9])[0-9]{1,3}\.){3}(?![3-9][0-9]{2}|2[6-9][0-9]|25[6-9])[0-9]{1,3}$
```

**Password generator in a SHELL**
```
echo -e {1..20}"\r$(tr -dc a-z0-9A-Z < /dev/random | head -c 20)\n"
```

---
## 'sed' command examples
---
---


**Print additional 3 lines after pattern matchs**
```
cat somefile.txt | sed  -n '/pattern/ {N;N;N;p}'
```


**Print N-th colored output after patter match**
```
cat somefile.txt | sed -e  '/pattern/ { s/^/\x1b[32m/; N;N;N; s/$/\x1b[0m/}'
```


**Match text from pattern1 to patter2**
```
cat somefile.txt | sed  -n '/pattern1/,/pattern2/p'
```


**Cut out text in between pattern1 and patter2**
```
cat somefile.txt | sed  -e 's/.*pattern1\(.*\)pattern2.*/\1/'
```


**Color the text from pattern1 to pattern2**
```
cat somefile.txt | sed -e '/pattern1/,/pattern2/ { s/^/\x1b[32m/; s/$/\x1b[0m/}'
```


**_To match brackets use HEX `\x27="'"`_**


**For loop replacement in line
here "t" is the operator for loop**
```
echo ",,;;,,,,;;;," | sed ':loop; s/,,/,/; t loop'
```


**To pass the variable in 'sed', double quotes are required around SED script
OR put the variable inside the single  quotes**

1. ```cat somefile.txt | sed -e "s/pattern/$ANY_VARIABLE/g"```
2. ```cat somefile.txt | sed -e 's/pattern/'$ANY_VARIABLE'/g'```


---
## 'bash' examples
---
---


- **_'name'_ will be the variable. `name="my.own.domain.org"` (in this case "." is only delimiter "."  can be any character)**

 
- `echo  ${name%.*}`
  - _result_ : **my.own.domain**

- `echo  ${name%%.*}`
  - _result_ : **my**

- `echo  ${name#*.}`
  - _result_ : **own.domain.org**

- `echo  ${name##*.}`
  - _result_ : **org**

- `echo  ${#name}`
  - _result_ : **_number_ length of the string**

- `echo  ${name^^}`
  - _result_ : **All Upper case**
- `echo  ${name,,}`
  - _result_ : **All Lower case**

- `echo  ${name::3}`
  - _result_ : **Displays  first 3 characters**
- `echo  ${name:3}`
  - _result_ : **Displays  all except first 3 characters**
- `echo  ${name:3:5}`
  - _result_ : **Skips 3 first characters and displays following 5**

- `echo  ${name/st1/st2}`
  - _result_ : **Replace first match 'st1' with 'st2' in 'name'**
- `echo  ${name//st1/st2}`
  - _result_ : **Replace all  match 'st1' with 'st2' in 'name'**

**Get GNOME's current theme name**
```
gsettings get org.gnome.desktop.interface gtk-theme
```
