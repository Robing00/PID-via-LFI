# PID-Scanner-via-LFI
## Vulnerability
This little script is usefull, if you have a LFI vuln. You can use this script to scan PIDs and maybe find a vulnerable process to exploit further.

## How does it work:
The script is brute-forcing GET-Requests, trying a defined range of numbers inside the proc directory and filter the result based on the length of the response.

*Read more about Linux processes [here](https://man7.org/linux/man-pages/man5/proc.5.html)*

## How to use it:
<!-- Put in how-to with code snippet-->
1. Change the URL under *### CHANGE THIS ###* to your url.
```python
# Import requests to use GET and import re for RegEx
import requests
import re

### CHANGE THIS ###
url="http://vulnerable.website.com"
```
2. Use the script with: **python3 PID-Scanner.py** 

## Where could it be usefull:
- There are many ways to find out running tasks/processes if yo have LFI. I find this to be a easy one to use. The annoying stuff is just to search for uncommon processes and it can take a long time. You could just use /proc/sched_debug to list all the runnable tasks and look up the processes there. 

Here is an example of how it could be used in a HackTheBox room:
- There is at least one Box in HTB where this script could be used. On this Box I found out, that there is a wordpress plugin which had a **_LFI vulnerability_**. The plugin was ebook-download and it could be used like this: 
  - I only had to **_change the url_** for it to work. It's pretty simple :>
  - Changed it like this (on line 6) :
    - url="http://IP-ADDRESS/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=" 



## Advanced and additional stuff:
<!-- if not working show how to change url to go out one dir more-->

## Task list Robin
- [x] Upload to Github ⬆️
- [ ] Finish commenting the script
- [ ] Finish the [README](README.md)
- [ ] change the print statement to make it look better
- [ ] Finished :tada:
