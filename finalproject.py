#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  finalproject.py
#  
#  Copyright 2016 scott <scott@LAPTOP-RBRQM0DR>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os, random

#dictionaries of subjects with classes and courses with flashcards
subjectDict = {}
flashcards = {}
def main():
	'''Main function to run program'''
	#ongoing program
	response = input("Would you like to (a)dd, (r)ead, or (t)est flashcards? (('q') to quit)")
	while response != 'q':
		if response == 'a':
			addFlashcards()
		elif response == 'r':
			readFlashcards()
		elif response == 't':
			testFlashcards()
		response = input("Would you like to (a)dd, (r)ead, or (t)est flashcards? (('q') to quit)")
	return 0
    
   
def addFlashcards():
	'''Function to add subject, courses, or flashcards'''
	sub = input("Use (e)xisting subject or (a)dd new subject")
	if sub == 'e':
		print("Subjects")
		#list the subjects
		for i in subjectDict.keys():
			print(i)
		subject = input("Please choose a subject")
		print("Courses within " + subject)
		#list courses
		for i in subjectDict[subject]:
			print(i)
		cou = input("Use (e)xisting course or (a)dd new course?")
		if cou == 'e':
			course = input("Please choose a course within this subject")
			count = int(input("How many flashcards would you like to add?"))
			j = 0
			while j < count:
				word = input("Please choose a key word for your flashcard.")
				definition = input("Please choose a definition for your flashcard.")
				card = (word, definition)
				flashcards[course].append(card)
				j = j + 1
		#add a course 
		elif cou == 'a':
			newCourse = input("What course would you like to add?")
			#check for duplicate
			if newCourse not in subjectDict[subject]:
				subjectDict[subject] == subjectDict[subject].append(newCourse)
				flashcards[newCourse] = []
				#let user add many flashcards at once instead of always re-running the program
				count = int(input("How many flashcards would you like to add to this new course?"))
				j = 0
				while j < count:
					word = input("Please choose a key word for your flashcard.")
					definition = input("Please choose a definition for your flashcard.")
					card = (word, definition)
					flashcards[newCourse].append(card)
					j = j + 1
	#add subject
	if sub == 'a':
		newSubject = input("What is your new subject?")
		subjectDict[newSubject] = []
		courseAmount = int(input("How many courses would you like to add?"))
		j = 0
		while j < courseAmount:
			newCourse = input("Name of course: ")
			subjectDict[newSubject].append(newCourse)
			flashcards[newCourse] = []
			j = j + 1
		for i in subjectDict[newSubject]:
			print(i)
		course = input("Please choose a course within this new subject")
		count = int(input("How many flashcards would you like to add?"))
		j = 0
		while j < count:
			word = input("Please choose a key word for your flashcard.")
			definition = input("Please choose a definition for your flashcard.")
			card = (word, definition)
			flashcards[course].append(card)
			j = j + 1
			
		
	return None
		
def readFlashcards():
	'''Read all subject, courses, and flashcards within each'''
	for i in subjectDict.keys():
		print("Subject: ", i)
		for j in subjectDict[i]:
			print("Course: ", j)
			for k in flashcards[j]:
				print("Word: " + k[0] + "\n" + "Definition: " + k[1])
	return None
	
def testFlashcards():
	'''test the user on their flashcard knowledge'''
	print("Subjects")
	for i in subjectDict.keys():
		print(i)
	subject = input("Please choose a subject")
	print("Courses within this subject")
	for j in subjectDict[subject]:
		print(j)
	course = input("Please choose a course")
	defs = []
	pair = {}
	score = 0
	questions = len(flashcards[course])
	for card in flashcards[course]:
		defs.append(card[1])
		pair[card[1]] = card[0]
	#shuffle cards
	random.shuffle(defs)
	for l in defs:
		#less error prone for user to guess word than definition
		print("Definition: ", l)
		options = [pair[l]]
		possibleOptions = []
		for val in pair.values():
			possibleOptions.append(val)
		random.shuffle(possibleOptions)
		#only allow 4 options, assuming there is at least 4 flashcards
		while len(options) < 4:
			opt = possibleOptions.pop(0)
			if opt != pair[l]: #no duplicates of answer
				options.append(opt)
		random.shuffle(options)
		print(options[0] + "\n" + options[1] + "\n" + options[2] + "\n" + options[3])
		answer = input("What word above matches the definition?")
		if answer == pair[l]:
			print("Correct! Great Job")
			score = score + 1
		else:
			print("Sorry, you were incorrect. The right answer was " + pair[l])
			
	grade = score / questions
	print("The amount you got correct was %i" % score)
	print("That's a successful rate of %f" % grade)
			
		
main()

		
		
	
	
		
			
	
	
	
		
	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
