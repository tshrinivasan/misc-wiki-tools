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
	print 'Usage: add-single-hash.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
   except getopt.GetoptError:
      print 'Usage: add-single-hash.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'add-single-hash.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
#   print 'Input file is "', inputfile
#   print 'Output file is "', outputfile

   input_file = open(inputfile,'r')
   output_file = open(outputfile,'w')

   for line in input_file:
	newline = "#" + line
        output_file.write(newline)

   input_file.close()
   output_file.close()   
   
   print "Done. Check the output file " + outputfile
if __name__ == "__main__":
   main(sys.argv[1:])
