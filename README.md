# PID-Scanner-via-LFI
## Vulnerability
This little script is pretty simple and easy to recreate but it's usefull if you have a LFI vulnerability. You can use this script to scan PIDs and maybe find a vulnerable process to exploit further.

## How does it work:
The script is brute-forcing GET-Requests, trying a defined range of numbers inside the proc directory and filter the result based on the length of the response.

*Read more about Linux processes [here](https://man7.org/linux/man-pages/man5/proc.5.html)*

## How to use it:
1. Change the URL under **_### CHANGE THIS ###_** to your url. 
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
It's pretty simple to add new stuff or change it up a bit. If you have problem with the script working on another LFI you can change up the code a bit. There are a few reasons why the code maybe isn't working:
1. In the following code add or take away ../
   - Because of how directories work, it could be possible, that the path to "/proc/PID/cmdline" is not always the same. It could be that it's stored a few directory levels above or below so change it up a bit and try it again. 
    ```python
    for i in range(1, 1000):
    tar_url= url + "/../../../../../../proc/"+ str(i) +"/cmdline"
    ```

## Task list Robin
- [x] Upload to Github ⬆️
- [ ] Finish commenting the script
- [ ] Finish the [README](README.md)
- [ ] change the print statement to make it look better
- [ ] maybe make a 2nd version to filter out common processes like systemd or apache
- [ ] Finished :tada:
