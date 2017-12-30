import numpy as np
import re
import sys

filename = sys.argv[1]
titlename = sys.argv[2]



with open(filename+".txt") as f:
    content = f.read().splitlines()
contentarray = np.asarray(content)
splitcontent = np.array_split(contentarray, [148,259,385,516,640,750,899,1041,1200, 1327,1478,1648,1802,2029,2214,2483,2673,2875,3214,3385,3563,3732,4089,4264,4510,4705,5104,5241,5672])
reitlen = len(splitcontent)
for x in range(0, reitlen):
	juzno = x + 1
	with open(filename+"{}.multids".format(juzno), "w") as files:
		files.write("{}".format(splitcontent[x]))

for x in range(1, 31):
	with open(filename+"{}.multids".format(x), "r") as fh:
		subject = fh.read()
		fh.close()
		subject = re.sub("(\d+)\|(\d+)\|",r"\n\1/\2: ", subject)
		subject = re.sub("\n(?!\d).*|^\[.*\n","", subject)
		subject = re.sub("/(\d{2}:)",r"/0\1", subject)
		subject = re.sub("\n(\d{2}/)",r"\n0\1", subject)
		subject = re.sub("^(\d{2}/)",r"0\1", subject)
		subject = re.sub("/(\d{1}:)",r"/00\1", subject)
		subject = re.sub("\n(\d{1}/)",r"\n00\1", subject)
		subject = re.sub("^(\d{1}/)",r"00\1", subject)
		subject = re.sub("''","",subject)
		subject = re.sub("'\s*\n|'\s*$","\n",subject)

		

# write the file
		f_out = open(filename+"{}.multids".format(x), "w")
		f_out.write("title: " + titlename + "/\n")
		f_out.write("created:  20171108214748719\n")
		f_out.write("creator:  R\n")
		f_out.write("content:  Translation\n\n")
		f_out.write(subject)
		f_out.close()






