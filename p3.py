from pickle import*
import os

fn = "dia.pkl"
if os.path.exists(fn):
	f = open(fn,"rb")
	model = load(f)
	f.close()
	

	fs = float(input("Enter fasting sugar "))
	fu = float(input("Enter 1 for No and 2 for yes "))


	if fu == 1:
		d =[[fs,0]]
	else:
		d= [[fs,1]]
	result = model.predict(d)
	print(result[0])
else:
	print(fn,"does not exists")