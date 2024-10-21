'''
Given a string where each character (A-Z) represents a paint color, determine the minimum number of strokes required to repaint the string into a uniform color. 
For example, for the string "ABBAABZBB", the minimum number of strokes required is 4
'''

''' while the intention was to use a two-pointer technique to determine the minimum strokes needed, the logic implemented only counts character transitions.  '''
# s = "ABBAABZB"

# st = list(s)

# prev = 0
# current = 1
# min_strokes = 1  

# while current < len(st):
#     if st[prev] != st[current]:  
#         min_strokes += 1
#         prev = current  

#     current += 1  

# print(min_strokes)


'''To correctly solve the problem of determining how many characters need to be changed to achieve a uniform string, an approach based on counting character frequencies would be more effective.'''

from collections import Counter

s = "ABBAABZB"
count = Counter(s)
min_number_of_strokes = 0


max_freq = max(count.values())

min_number_of_strokes = len(s) - max_freq

print(min_number_of_strokes)