#!/usr/bin/python
import struct
import binascii
import math
import sys
import os

prev_pct = ""
def cb_print( text ):
	global prev_pct
	sys.stdout.write('\x08' * (len(prev_pct)+1))
	#sys.stdout.write(' ' * (len(prev_pct)+1))
	sys.stdout.write('\x08' * (len(prev_pct)+1))
	sys.stdout.write(str(text))
	prev_pct = str(text)
	sys.stdout.flush()

def bmp_read_info_header(raw_data):
	raw_info = raw_data[14:54]
	info_chunk = struct.Struct('< I I I H H I I I I I I')
	decomp_header = info_chunk.unpack(raw_info)
	return decomp_header

def bmp_read_file_header(raw_data):
	raw_header = raw_data[0:14]
	header_chunk = struct.Struct('< H I H H I')
	decomp_header = header_chunk.unpack(raw_header)
	#header_chunk[1] size of color array
	#header_chunk[3] offset
	return decomp_header

def enc_file():
	bmp = open(sys.argv[1],"rb").read()
	bmp_head = bmp_read_file_header(bmp)
	bmp_info = bmp_read_info_header(bmp)

	em_file = open(sys.argv[2],"rb")
	size = os.path.getsize(sys.argv[2])
	print str(size)+" bytes go in"

	cpy_bmp_head = [bmp_head[0], bmp_head[1], bmp_head[2], bmp_head[3], bmp_head[4]]
	cpy_bmp_head[4] += size

	# |----- bmp_header ---|----bmp_info---|--------raw_file_content----------|----bmp_file_data----|

	print "Out file "+str(sys.argv[2])+".bmp"

	enc = open(str(sys.argv[2])+".bmp","wb")
	header_chunk = struct.Struct('< H I H H I')
	#print cpy_bmp_head
	new_header = header_chunk.pack(cpy_bmp_head[0],cpy_bmp_head[1],cpy_bmp_head[2],cpy_bmp_head[3],cpy_bmp_head[4]) 

	enc.write(new_header)
	enc.write(bmp[14:54])

	byte = 0

	print "Template file "+str(sys.argv[1])
	print "Embed file "+str(sys.argv[2])

	while 1:
		try:
			byted = em_file.read(1024)
			if not byted:
				break
			enc.write(byted)
			#print str(byte)+".."
			byte += len(byted)
			cb_print("Processing .. "+str(byte*100//size)+"%")
		except:
			break
	print ""
	print "Writing image data.."
	enc.write(bmp[54::])

def extract_file():

	print "Will extract "+str(sys.argv[2])
	print "from "+str(sys.argv[1])

	bmp = open(sys.argv[1], "rb")
	bmp_head = bmp_read_file_header(bmp.read(54))
	sizef = bmp_head[4]-54
	
	of = str(sys.argv[2])
	off = open(of, "wb")

	bmp.seek(54)
	chunk = 1024
	
	print "Extracting..."
	off.write(bmp.read(sizef))
	
	off.close()
	bmp.close()

print ""
print "BMP-stegano (c) Raja Jamwal <linux1@zoho.com>"
print "This program is just a demonstration of steganography"
print "Use of this program/such programs may be illegal in your country"
print "Use at your own risk"
print ""

if len(sys.argv) < 3:
	print "Invalid parameters\n"
	print "Usage:\n"
	print "\tbmp-stegano <bmp-file> <any-file> [-e]"
	print "bmp-file: bmp file you from which you either want to extract or embed data"
	print "any-file: file which you either want to extract data to or embed into BMP"
	print "-e: specifying -e option will extract data from bmp-file to any-file otherwise"
	print "embed data from any-file to bmp-file"  
	print ""
	print "Important Note:\n\n\tCurrent program is designed to work with only those BMP-images that don't have RGBQUAD or color table embeded in them like 24-bit DIB. The program will not try to VALIDATE the image before embeding.\n\n\tThere is also limit of embeding file of MAX size of 2^32 bytes (4096MB) no matter what CPU (64or32bit) host system supports, this is a direct consequence of BMP file design." 
	print "\nAuthor:\n"
	print "\tRaja Jamwal <linux1@zoho.com>"
	exit(1)

if len(sys.argv) == 3:
	enc_file()
else:
	extract_file()
