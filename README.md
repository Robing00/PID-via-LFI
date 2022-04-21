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

## Where could it be usefull:
<!-- Put in guide of. Many ways to use proc directory. (proc/sched_debug) also lists all the runnable tasks with their PID and you can just search everything there. -->
<!--# EXAMPLE FORM HTB BACKDOOR (ebook vulnerability):
# url="http://IP-ADDRESS/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=" -->

## Task list Robin
- [x] Upload to Github ⬆️
- [ ] Finish commenting the script
- [ ] Finish the [README](README.md)
- [ ] Finished :tada:
