# PID-Scanner-via-LFI
## Vulnerability
If you have a LFT vuln you can use this script to scan PIDs and maybe find a vulnerable process to exploit further.

### How does it work:
The script is brute-forcing GET-Requests, trying a defined range of numbers inside the proc directory and filter the result based on the length of the response.
