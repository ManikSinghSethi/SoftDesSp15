"""

@author: Manik Singh Sethi

help recieved from Joey Maalouf
"""


import pickle
import unicodedata
from pattern.web import *
import difflib
import os.path

cantosE = []   #initialize lists for use in later functions
cantosInEn = [] #initialize lists for use in later functions - will store english formatted
translatedcopy = [] #will hold translated copy

input_file_I = open('DC_Orig_Italian','r')  #load up italian version
DC_Original_I = pickle.load(input_file_I)

input_file_E = open('DC_Orig_English','r') #load up english version
DC_Original_E = pickle.load(input_file_E)

abridged_DC_E = DC_Original_E[DC_Original_E.find("is by Giotto.")+20:] #remove excess
abridged_DC_E = abridged_DC_E[:abridged_DC_E.find("INDEX ")]

abridged_DC_I = DC_Original_I[DC_Original_I.find("Al Haines.")+20:] #remove excess, format accented characters for use
abridged_DC_I = abridged_DC_I[:abridged_DC_I.find("PURGATORIO")-20]
abridged_DC_I = unicode(abridged_DC_I, "UTF-8")
abridged_DC_I = unicodedata.normalize('NFD', abridged_DC_I).encode('ascii', 'ignore')

combinecount = 0
fulltext = []

def prelimInfo():
	'''
	This function serves almost as a main function so key processes are run from here. 
	This includes calls to reformatting the english version and translating the Italian version
	'''

	Elist = [abridged_DC_E, abridged_DC_E.find("In middle[160]"),abridged_DC_E.find("It was the close"), abridged_DC_E.find("Through me to"), abridged_DC_E.find(" Resounding thunder broke"), 
	abridged_DC_E.find("From the First Circle"), abridged_DC_E.find("When I regained"), abridged_DC_E.find("Pape Satan"), abridged_DC_E.find("I say, continuing"), abridged_DC_E.find("The hue which cowardice"),
	abridged_DC_E.find("And now advance"), abridged_DC_E.find("We at the margin"), abridged_DC_E.find("The place of our"), abridged_DC_E.find("Ere Nessus landed"), abridged_DC_E.find("Me of my native place"), abridged_DC_E.find("Now lies[454"), abridged_DC_E.find("Now could I hear the water"), 
	abridged_DC_E.find("'Behold the monster"), abridged_DC_E.find(" Of iron colour,"), abridged_DC_E.find("O Simon Magus!"), abridged_DC_E.find("Now of new torment must my"), abridged_DC_E.find("Conversing still from bridge"), abridged_DC_E.find("Horsemen I've seen in"), abridged_DC_E.find("Silent, alone, not now"), abridged_DC_E.find("In season of the"),
	abridged_DC_E.find("The robber,"), abridged_DC_E.find("Rejoice, O Florence"), abridged_DC_E.find("Now, having first"), abridged_DC_E.find("Could any, even"), abridged_DC_E.find("The many folk and wounds"),
	abridged_DC_E.find("Because of Semele"), abridged_DC_E.find("The very tongue that"), abridged_DC_E.find("Had I sonorous rough"), abridged_DC_E.find("His mouth uplifting"), abridged_DC_E.find("Towards where we are")]
	#create the start of each canto and gives the abridged text


	Ilist = [abridged_DC_I, abridged_DC_I.find("Nel mezzo del cammin"),abridged_DC_I.find("Lo giorno"), abridged_DC_I.find("Per me si va ne"), abridged_DC_I.find("Ruppemi lalto sonno"), 
	abridged_DC_I.find("Cosi discesi del cerchio"), abridged_DC_I.find("Al tornar de la"), abridged_DC_I.find("Pape Satan"), abridged_DC_I.find("Io dico, seguitando"), abridged_DC_I.find("Quel color che"),
	abridged_DC_I.find("Ora sen va per un"), abridged_DC_I.find("In su lestremita"), abridged_DC_I.find("Era lo loco"), abridged_DC_I.find("Non era ancor di"), abridged_DC_I.find("Poi che la carita"),
	abridged_DC_I.find("Ora cen porta"), abridged_DC_I.find("Gia era in loco onde"), abridged_DC_I.find("Ecco la fiera con"), abridged_DC_I.find("Luogo"), abridged_DC_I.find("O Simon mago"),
	abridged_DC_I.find("Di nova pena mi"), abridged_DC_I.find("Di nova pena mi conven"), abridged_DC_I.find("Cosi di ponte in"), abridged_DC_I.find("Io vidi gi"), abridged_DC_I.find("Taciti, soli"),
	abridged_DC_I.find("In quella parte del"), abridged_DC_I.find("Al fine de le"), abridged_DC_I.find("Godi, Fiorenza, poi"), abridged_DC_I.find("Gia era dritta in"), abridged_DC_I.find("Chi poria mai pur"), 
	abridged_DC_I.find("La molta gente e"), abridged_DC_I.find("Nel tempo che Iunone"), abridged_DC_I.find("Una medesma lingua"), abridged_DC_I.find("Sio avessi le rime aspre"), abridged_DC_I.find("La bocca sollev"), abridged_DC_I.find("Vexilla regis prodeunt")]
	#create the start of each canto and gives the abridged text

	officialenglishversion = makeListofCantos(Elist)  #creates english version for analysis
	accessiblesentances = makeListofCantos(Ilist)	#allows sentances in cantos to be accessed individually
	if os.path.exists('TranslatedItalian'): #check if a file already exists with the translated italian text
		f = open('TranslatedItalian', 'r') 
		finalItalian = f.read() #if there is, use that file
		f.close()
	else: 											#if not, make go through the process to make a file with the translated text
		translated = translate(accessiblesentances)	#call to translate the sentances individually
		finalItalian = combinestrings(translated) 
		f = open('TranslatedItalian', 'w')
		f.write(finalItalian)
		f.close()

	
	officialenglishversion = combinestrings(officialenglishversion) #have the english version as one long string
	print finalItalian
	print officialenglishversion
	print compare(finalItalian, officialenglishversion)


def compare(Italian, English):
	'''
	compares the two strings too each other and returns a metric between 0 and 1 where 0 is nothing alike and 1 is the exact same text
	function found from http://avrilomics.blogspot.com/2014/01/calculating-similarity-measure-for-two.html
	'''
	score = difflib.SequenceMatcher(None, Italian, English).ratio()
	return score


def combinestrings(listname):
	'''
	combine the list of lists of strings or list of strings into oen long sting for comparision
	'''
	if len(listname[0][0]) > 1: #checks if there is a string or list in the primary list. If the latter case, there will be a full word in the first index
		for cantos in xrange(0, len(listname)):
			listname[cantos] = ' '.join(listname[cantos]) #join together the lists in the list so there is a list of strings overall
		listname = '. '.join(listname)	#join all the strings together to one string. add a period to differentiate sentences
	else:
		listname = ' '.join(listname) 	#join the list of strings in english to be a long string
	return listname

def SendtoList(DC_Original, start):
	'''
	takes in the full Italian text and each start point to remove any special formatting or characters and stores as sentances
	note: canto variable could better be named "sentance"
	'''
	Canto = DC_Original[start:]	#each start is given
	if Canto == DC_Original[184684:]:	#in special case - last case, the word Canto is not used immediately
		end = Canto.find("PURGATORIO")-2
	else:
		end = Canto.find("Inferno  Canto")-2 #otherwise, Inferno  Canto is between canto
	Canto = Canto[:end]
	Canto = " ".join(Canto.split("\r\n")) #remove escapes
	Canto = " ".join(Canto.split()) #add spaces
	Canto = "".join([c for c in list(Canto) if c.isalpha() or c == " " or c == "."]) #remove anything but alphabet, space, and periods
	Canto = Canto.replace(" ", "%20") 	#format for url use
	Canto = Canto.replace(".", "%2E")	#format for url use
	Canto = Canto.split("%2E")	#split into sentances

	cantosE.append(Canto) 	#creat list of sentances
	return cantosE

def formattingEn(DC_Original, start):
	'''
	removes special characters, makes easier comprehension
	'''
	Canto = DC_Original[start:] #defined start
	end = Canto.find("FOOTNOTES") - 2 #at end of each canto
	Canto = Canto[:end]
	Canto = " ".join(Canto.split("\r\n")) #remove escapes
	Canto = " ".join(Canto.split())
	Canto = "".join([c for c in list(Canto) if c.isalpha() or c == " " or c == "."]) #remove anything but alphabet, space, and periods 

	cantosInEn.append(Canto)
	return cantosInEn


def makeListofCantos(listed):
	'''
	determines which function is used depending on language
	'''
	if listed[0] == abridged_DC_I: #if italian version - 
		for i in range(1, len(listed)): #send each canto to SendtoListfunction
			ans = SendtoList(listed[0], listed[i])
	else: #else if english
		for i in range(1, len(listed)): #send each canto to formattingEn function
			ans = formattingEn(listed[0], listed[i])
	return ans



def translate(cantos):
	'''
	Calls to website API to make translations sentance by sentance
	input is full text split into formatted sentances
	note: website cannot take in full canto at a time. must go sentance by sentance
	'''
	translatedcopy = [] #create destination 
	for numbercantos in range(0, len(cantos)): #access each canto
		translatedsentences = [] #temp destination
		for numsentances in range(0, len(cantos[numbercantos])): #access each sentance of each canto
			sentence = cantos[numbercantos][numsentances] #creates url accessable end to link
			standardurl = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=it&tl=en&dt=t&q=" #standard link to translate from it to en
			urltostranslate = standardurl + sentence #creat full URL
			s = URL(urltostranslate).download() #returns form [[["target text, source text"]],target language]
			s = s[4:] #take start of target text
			s = s[:s.find("\"")] #stop at end of target text
			s = unicode(s, "UTF-8") #format url unicode
			s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore') #use standard alphabet for analysis
			translatedsentences.append(s) #add each sentance together
		translatedcopy.append(translatedsentences) #add each canto together
	return translatedcopy



if __name__ == '__main__':
	prelimInfo()
