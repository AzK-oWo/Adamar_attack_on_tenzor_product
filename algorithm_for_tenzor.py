from blincodes import vector, matrix
from blincodes.codes import rm
from blincodes.codes.tools import hadamard_product, make_parity_check
from time import time
from tenzor_rm_key_generator import keyGenerator

def algorithm_0(G_pub, q, r, m):
	G_copy = G_pub.copy()
	for i in range(1, q):
		G_copy = hadamard_product(G_pub, G_copy)
		r += r
	G_copy = make_parity_check(G_copy)
	r = m - r - 1
	return G_copy, r


def algorithm_1(G_osum, r, m):
	G_res = G_osum.copy()
	while r != 0 and m % r != 0:
		q = m // r
		r = m - q * r - 1
		G_copy = G_res.copy()
		for i in range(1, q):
			G_res = hadamard_product(G_copy, G_res)
		G_res = make_parity_check(G_res)
	if r == 0:
		return G_res
	G_res = make_parity_check(hadamard_product(G_res, make_parity_check(G_res)))
	return G_res


def algorithm_2(G_0, k):
	columns = G_0.ncolumns
	rows = G_0.nrows
	P = [0 for i in range(columns)]
	for i in range(rows):
		vec = G_0[i].value
		shift = 0
		for j in range(columns):
			if 2 ** j & vec != 0:
				P[i * k + shift] = (columns - j) - 1
				shift += 1
	return matrix.permutation(P)


def attack_on_RM1(G, m):
	pass


def Minder_Shokrollahi_attack(G, r, m):
	pass


def Chizhov_Borodin_attack(G, r, m):
	pass




print("write parametrs of Reed-Mallers codes(r1, m1, r2, m2):")
r1, m1, r2, m2 = input().split(" ")
G1, G2 = rm.generator(r1, m1), rm.generator(r2, m2)
G_pub, (M, P) = keyGenerator(r1, m1, r2, m2)
q1, q2 = m1 // r1, m2 // r2
if m1 % r1 != 0:
	q1 += 1
if m2 % r2 != 0:
	q2 += 1
if q1 != q2:
	q, r, m = 0, 0, 0
	if (q1 > q2):
		q = q2
		r = r2
		m = m2
		k = G2.nrows
	else:
		q = q1
		r = r1
		m = m1
		k = G1.nrows
	G, r_alg = algorithm_0(G_pub, q, r, m)
	G = algorithm_1(G, r_alg, m)
	P0 = algorithm_2(G, k)
else:
	print("error: params are not correct for this algorithm")


		