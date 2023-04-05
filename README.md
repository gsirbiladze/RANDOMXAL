# RANDOMXAL
Just Random Stuff

**Get GNOME's current theme name**
```
gsettings get org.gnome.desktop.interface gtk-theme
```

**Regex for IP (Starting with zero is included)**
```
^((?![3-9][0-9]{2}|2[6-9][0-9]|25[6-9])[0-9]{1,3}\.){3}(?![3-9][0-9]{2}|2[6-9][0-9]|25[6-9])[0-9]{1,3}$
```

**Password generator in a SHELL**
```
echo -e {1..20}"\r$(cat /dev/random |tr -dc a-z0-9A-Z |head -c 20)\n"
```
