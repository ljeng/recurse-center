source('import.r')
source('functions.r')
qCog = c(178, 255, 256, 267, 303, 337, 409, 477, 511, 1201, 7040, 8672, 12625, 14835, 16153, 18154, 18698, 21086, 43639, 57844)
for (q in qCog) {
	print(toString(questionData[grep(q, questionData[,1]), 2]))
	print(qTable(userData, q))
}
aCog = c(2, 1, 3, 1, 1, 3, 4, 2, 2, 2, 1, 4, 1, 2, 4, 1, 3, 3, 4, 3)
for (i in c(2:1460, 1540:2621)) {
	qi = substring(colnames(userData)[i], 2)
	phiDf = matrix(nrow = 0, ncol = nrow(qTable(userData, qi)))
	for (j in 1:length(qCog)) {
		phiDf = rbind(phiDf, corMatrix(userData, qi, qCog[j])[,aCog[j]])
	}
	count = colSums(phiDf > 0)
	phiSumDf = matrix(nrow = 1, ncol = ncol(phiDf))
	colnames(phiSumDf) = rownames(qt)
	for (k in c(grep(TRUE, count == length(qCog)), grep(TRUE, count == 0))) {
		phiSumDf[1, k] = colSums(phiDf)[k]
	}
	if (!is.na(phiSumDf) > 0) {
		print(toString(questionData[grep(paste0('q', qi, '$'), questionData[,1]), 2]))
		print(phiSumDf)
	}
}
