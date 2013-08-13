#!/usr/bin/python

# This script will add #: in front of all the lines that contain the strings subsp or var

# Author: tshrinivasan@gmail.com



import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      if opts == []:
	print 'Usage: fix-hash.py  -i <inputfile> -o <outputfile>'
        sys.exit(2)
   except getopt.GetoptError:
      print 'Usage: fix-hash.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'fix-hash.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
#   print 'Input file is "', inputfile
#   print 'Output file is "', outputfile

   input_file = open(inputfile,'r')
   output_file = open(outputfile,'w')

   newline = ''
	
   subsp = 0
   var = 0
   lines = 0
   hashes = 0

   for line in input_file:
	if 'subsp' in line:
		newline = "#:" + line
		subsp = subsp + 1
	elif 'var' in line:
		newline = "#:" + line
		var = var + 1
	else:
		newline = line
		hashes = hashes + 1

        output_file.write(newline)
	lines = lines + 1

   input_file.close()
   output_file.close()   
   
   print "Done. Check the output file " + outputfile

   print "Total lines = " + str(lines)
   print "Total Subsp = " + str(subsp)
   print "Total Var = " + str(var)
   print "Total Hash = " + str(hashes)
  

   print str(hashes), '+', str(subsp),' +' , str(var), "   = " +  str(hashes + var + subsp)


if __name__ == "__main__":
   main(sys.argv[1:])
