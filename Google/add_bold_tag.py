s = "abcxyz123"
dict1 = ["abc","123"]

#Output:
#"<b>abc</b>xyz<b>123</b>"

bold = "<b>"
bold2 = "</b>"


def bold_tag(s):

	l = []
	n = 0
	while n < len(s)+1:
		m = 0
		while m < len(s):
			subString = s[m:n]
			l.append(subString)
			m+= 1
		n+=1

	#find the item in dict

	s2 = ''
	for i in l:
		for j in dict1:
			if i == j:
				result = bold+i+bold2
				s2 = s2+result
	return(s2)


bold_tag(s)

#overlap dic
dict2 = ["aaa","aab","bc"]

l2 = []
for i in dict2:
	n = 0
	while n < len(i)+1:
		m = 0
		while m < len(i):
			subString = s[m:n]
			l2.append(subString)
			m+= 1
		n+=1
l2





















