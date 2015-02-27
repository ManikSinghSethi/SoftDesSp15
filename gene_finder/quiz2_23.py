def HSS(word):
	score = 0
	listed = list(word)
	for i in range(0,len(listed)):
		if listed[i] not in ["A", "K", "O"]:
			score += -1
		elif listed[i] in ["A", "K", "O"]:
			score += 2

	return score

print HSS("AKW")