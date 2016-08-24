'''
MIT License

Copyright (c) 2016 techvoltage

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import webbrowser
import logging
import urllib2
import sys, getopt

def counter(low,high):
	#for count in xrange(450,500):
	for count in xrange(low,high+1):
		try:
			response = urllib2.urlopen('https://ctftime.org/writeup/'+str(count))
			html = response.read()
			t=html.find("Original writeup")
			p=html.rfind("href=\"",0,t)
			q=html.rfind("target=",0,t)
			s=html[p+6:q-2]
			print count,"	",html[p+6:q-2]
			webbrowser.open(s)
		except Exception as e:
			logging.exception("message")
			continue
def help_page():
	print 'writeup_browser.py -l <low_range> -h <high_range>'
	print 'Writeup browser for ctftime.org.',
	print 'Enter the low and high range to read writeups.'
	print 'Say, if you are on https://ctftime.org/writeup/3689 and you want to', 
	print 'read next 4 writeups as well',
	print 'then writeup_browser.py -l 3689 -h 3693'
	sys.exit(2)
def main(argv):
	inputfile = ''
	outputfile = ''
	low=0
	high=0

	try:
		opts, args = getopt.getopt(argv,"l:h:",["low=","high="])
	except getopt.GetoptError:
		help_page()
		sys.exit(2)
	if opts==[]:
		help_page()
	for opt, arg in opts:
		if opt in ("-l", "--low"):
			low = arg
	  	elif opt in ("-h", "--high"):
			high = arg
	if high<0 or low<0:
		sys.exit(2)
	low=int(low)
	high=int(high)
	if high<low:
			sys.exit(2)	
	if (high-low)>10:
		print "This will open more than 10 pages. Continue(Y/N)?"
		x=raw_input("")
		if x=='y' or x=='Y':
			pass
		elif x=='n' or x=='N':
			sys.exit(2)
	counter(low,high)
if __name__ == "__main__":
   main(sys.argv[1:])
