#this pogram will help you find available wifi networks
import subprocess

nw=subprocess.check_output(['netsh','wlan','show','network'])
decode_nw=nw.decode('ascii')
print(decode_nw)