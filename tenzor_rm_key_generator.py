from blincodes import vector, matrix
from blincodes.codes.rm import generator
from numpy.random import permutation as npPermutation


#Kronecker Product of 2 matrix
def kron(first, second):
	row_f, row_s = first.nrows, second.nrows
	col_f, col_s = first.ncolumns, second.ncolumns
	result_matrix = []
	for i in range(0, row_f):
		tmp_arr = first[i].support
		for j in range(0, row_s):
			tmp_vec = 0
			tmp_value = second[j].value
			for k in tmp_arr:
				tmp_vec |= tmp_value << ((col_f - k - 1) * col_s)
			result_matrix.append(tmp_vec)
	return matrix.Matrix(result_matrix, col_f * col_s)




def keyGenerator(r1, m1, r2, m2):
#Make a first RM Matrix with n,k,d params
	G1 = generator(r1, m1)
	

#Make a second RM Matrix with n,k,d params
	G2 = generator(r2, m2)


#Make a generating matrix which is tenzor producted by 2 previous RM matrix
#	start = time()
	G = kron(G1, G2)
#	finish = time()
#	print(str(finish - start) +  " G")


#Create public and private keys
#public key => G_pub = M * G * P, where G - generating matrix, M - random Matrix and P - permutation matrix
#private key => a tuple (M^(-1), P^(-1))
#	start = time()
	M = matrix.random(G.nrows, max_rank=True)
#	finish = time()
#	print(str(finish - start) +  " M")
	
#	start = time()
	P = matrix.permutation(npPermutation(G.ncolumns))
#	finish = time()
#	print(str(finish - start) +  " P")

#	start = time()
	G_pub = M * G * P
#	finish = time()
#	print(str(finish - start) +  " G_Pub")

	return G_pub, (M,P) # ret public key + secret_key


