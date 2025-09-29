
#find all student who scored the maximum marks
score={"Alice" : 0," Bob": 10,"charlie":0,"David":0,"Eve":0}

max_score=max(score.values())
for i in score:
	if(max_score==score[i]):
		print("%s  %d" % (i, score[i]))




