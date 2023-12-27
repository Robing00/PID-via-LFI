# PID-Scanner-via-LFI
## Vulnerability
This script, though simple and easy to replicate, is highly effective for exploiting Local File Inclusion (LFI) vulnerabilities. It allows for scanning Process IDs (PIDs) to identify potentially vulnerable processes for further exploitation.

## How does it work:
The script employs a brute-force approach with GET requests, attempting a predefined range of numbers within the 'proc' directory. It then filters the results based on the response length.

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

## Practical Applications:
- This script is an efficient tool for identifying active tasks/processes in the presence of an LFI vulnerability. The primary challenge is isolating uncommon processes, which can be time-consuming. An alternative is using /proc/sched_debug to list all runnable tasks, either via scripting or manual inspection in tools like Burp Suite.

Example in a HackTheBox Challenge:

In at least one HackTheBox (HTB) challenge, this script has proven useful. I discovered a WordPress plugin with an LFI vulnerability, namely 'ebook-download'. The only modification required was the URL:
Update the URL on line 6 to:
url = "http://IP-ADDRESS/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl="



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
