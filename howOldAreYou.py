#!/usr/bin/python
#GeorgeKirm
import time

"""
int daysI,monthsI,yearsI,timeInDaysI,disektaYearsI,i
# timeInDaysI=sunolo hmerwn, disektaYearsI=ari8mos disektwn etwn apo tin arxi mexri ta gene8lia */
int hms,mis,xrs,disektaYearsTodayI,timeInDaysTodayI
# hms-mis-xrs=7-11-2013, disektaYearsTodayI=disekta eti apo tin arxi mexri simera,d*/
int migt,xrgt;
# telikoi mines kai xronia
"""

def limitOfDaysInMonths(year, month):
	if year%400== 0 or year%4== 0 and year%100!= 0:
		if month== 2:
			print 'loula'
			return 29
	return {
		1: 31, #jenuary
		2: 28, #february
		3: 31, #March
		4: 30, #April
		5: 31, #may
		6: 30, #june
		7: 31, #jule
		8: 31, #aug
		9: 30, #sept
		10: 31, #okt
		11: 30, #noveb
		12: 31, #dece
	}[month]

def getNumberFromUser(limit, year, month):
	helper1I=0
	if month!= -1:
		limit= limitOfDaysInMonths(year, month)
	while helper1I==0:
		print 'Give number: ',
		s= (raw_input())
		try:
			s= int(s)
			if s>0 and s<=limit:
				helper1I=1
				return s
			else:
				print 'need positive number smaller than',limit
		except ValueError:
			print 'Need number'

print 'What year was you borned? ',
yearsI= getNumberFromUser(2014, -1, -1)
print 'What month? ',
monthsI= getNumberFromUser(12, yearsI, -1)
print 'What day it was? ',
daysI= getNumberFromUser(30, yearsI, monthsI)

current_time = time.localtime()
s= time.strftime('%Y-%m-%d', current_time)
s = s.split("-")
yearTodayI= int(s[0])
monthTodayI= int(s[1])
dayTodayI= int(s[2])

leapYearsI= 0
leapYearsTodayI= 0
for i in range(0, yearTodayI):
	if i%400==0 or i%4==0 and i%100!=0:
		leapYearsTodayI= leapYearsTodayI+1
		if i<=yearsI:
			leapYearsI= leapYearsI+1

timeInDaysI= (yearsI-leapYearsI)*365+leapYearsI*366+daysI
timeInDaysTodayI= (yearTodayI-leapYearsTodayI)*365+leapYearsTodayI*366+dayTodayI #time in days without days from last year
for i in range(1, monthsI):
	timeInDaysI= timeInDaysI+ limitOfDaysInMonths(yearsI, i)
for i in range(1, monthTodayI):
	timeInDaysTodayI= timeInDaysTodayI+ limitOfDaysInMonths(yearTodayI, i)
print '~~~'
print 'You lived for',timeInDaysTodayI-timeInDaysI,'days'
print leapYearsTodayI-leapYearsI,'leap years where included'
if dayTodayI-daysI<0:
	dayTodayI= dayTodayI+limitOfDaysInMonths(yearTodayI, monthTodayI)
	monthTodayI= monthTodayI-1
if monthTodayI-monthsI<0:
	monthTodayI= monthTodayI+12
	yearTodayI= yearTodayI-1
print 'That is',yearTodayI-yearsI,'years',monthTodayI-monthsI,'months and',dayTodayI-daysI,'days'








