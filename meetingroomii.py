'''
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],....] (s<e), find the minimum number of conference rooms 
required.
Interval class is examplary.
'''

class Interval(object):
	def __init__(self,start,end):
		self.start = start
		self.end = end


def minMeetingRooms(self, intervals):
	start = sorted([i.start for i in intervals])
	end = sorted([i.end for i in intervals])

	res = 0
	count = 0
	startIndex =0
	endIndex = 0

	while startIndex < len(intervals):
		if start[startIndex] < end[endIndex]:
			startIndex += 1
			count += 1
		else:
			endIndex += 1
			count -= 1
		res = max(res,count)
	return res