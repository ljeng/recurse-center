qCol <- function (dataframe, q) {
	dataframe[,grep(paste0('q', q, '$'), colnames(dataframe))]
}
qTable <- function (dataframe, q = NULL) {
	if (length(q) == 1) {
		tb = table(qCol(dataframe, q))
		tb[2:length(tb)]
	}
	else if (length(q) == 2) {
		tb = table(qCol(dataframe, q[1]), qCol(dataframe, q[2]))
		tb[2:nrow(tb), 2:ncol(tb)]
	}
	else {
		table(dataframe)
	}
}
phi <- function (dataframe, i, j) {
	ij = dataframe[i, j]
	rows = 1:nrow(dataframe)
	a = rows[rows != i]
	cols = 1:ncol(dataframe)
	b = cols[cols != j]
	d1 = sqrt(sum(dataframe[i,])*sum(dataframe[,j]))
	d2 = sqrt(sum(dataframe[a,])*sum(dataframe[,b]))
	(ij*(sum(dataframe) - sum(dataframe[i,]) - sum(dataframe[,j]) + ij) - sum(dataframe[i, b])*sum(dataframe[a, j]))/d1/d2
}
corMatrix <- function (dataframe, q1, q2) {
	qt = qTable(dataframe, c(q1, q2))
	qtCopy = qt
	for (i in 1:nrow(qt)) {
		for (j in 1:ncol(qt)) {
			qtCopy[i, j] = phi(qTable(userData, c(q1, q2)), i, j)
		}
	}
	qtCopy
}
