tfile=open("/sys/bus/w1/devices/28-000000d7970b/w1_slave")
ttext=tfile.read()
tfile.close()
temp=ttext.split("\n")[1].split(" ")[9]
temperature=float(temp[2:])/1000
print temperature
