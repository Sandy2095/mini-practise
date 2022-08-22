strdata = 'ABCDCDC'

substr = 'CDC'

sl = len(substr)


print([ strdata[i:i+sl] for i in range(0,len(strdata),sl)])
