# Study (Simulation) to find out how many firestarters are needed to destroy 
# different types of terrain.
# For this study the 9 combustable terrains are considered
# They are Fort, Church, Temple, Labs, Mall, Scrapyard, Garden,
# Woods and Jungle


from os import system
import random
global count_out #= 0
global burnt_out #= 0
count_out =0
burnt_out =0
cells = 0
hard = 0
target = 0
flash = 0
# pigeonholes == for storing sample out-comes by number-of-firestarting-attempts by 'up to' number i.e first column was for the quickest
# whilst last column (rightmost in table) for the slowest. First row (starting 26220) for forts (less combustable) than last row (starting 12)
# for jungle -- considered easiest terrain to set alight.
pigeonholes = [[26220,27368,28515,29663,30810,31958,33105,34253,35400,36548,37695,38843,39990,41138,42285,43433,44580,45728,46875,46875],
			   [ 1041, 1120, 1199, 1278, 1357, 1436, 1515, 1594, 1673, 1752, 1831, 1910, 1989, 2068, 2147, 2226 ,2305, 2384, 2463, 2463],
			   [  652,  712,  771,  831,  891,  950, 1010, 1070, 1129, 1189, 1249, 1309, 1368, 1428, 1488, 1547, 1607, 1667, 1726, 1726],
			   [  194,  211,  228,  244,  261,  278,  295,  312,  328,  345,  362,  379,  395,  412,  429,  446,  463,  479,  496,  496],
			   [   94,  114,  134,  154,  175,  195,  215,  235,  255,  275,  296,  316,  336,  356,  376,  396,  417,  437,  457,  457],
			   [   34,   46,   57,   69,   81,   93,  104,  116,  128,  140,  151,  163,  175,  187,  198,  210,  222,  234,  245,  245],
			   [   44,   51,   58,   65,   72,   79,   86,   93,  100,  107,  114,  121,  128,  135,  142,  149,  156,  163,  170,  170],
			   [   20,   25,   30,   35,   40,   45,   50,   55,   60,   65,   70,   75,   80,   85,   90,   95,  100,  105,  110,  110],
			   [   12,   16,   21,   25,   29,   34,   38,   43,   47,   51,   56,   60,   64,   69,   73,   78,   82,   86,   91,   91]
			  ]
histoMidPts = [[ 25646.5,26794.5,27942,29089.5,30237,31384.5,32532,33679.5,34827,35974.5,37122,38269.5,39417,40564.5,41712,42859.5,44007,45154.5,46302,47449.5],
			   [  1002,1081,1160,1239,1318,1397,1476,1555,1634,1713,1792,1871,1950,2029,2108,2187,2266,2345,2424,2503],
			   [  623,682.5,742,802,862,921,980.5,1041,1100,1160,1220,1280,1339,1399,1459,1518,1578,1638,1697,1757],
			   [  186,203,220,237,235,270,287,304,320.5,337,354,371,387.5,404,421,438,455,471.5,488,505],
			   [ 84.5,104.5,125,145,165,186,205.5,225.5,245.5,265.5,286,306.5,326.5,347,366.5,387,407,427.5,447.5,467.5],
			   [ 28.5,40.5,52,63.5,75.5,87.5,  99,110.5,122.5,134.5,146,157.5,169.5,182,193,  205,216.5,228.5,240,251.5],
			   [  41,48,55,62,69,      76,83,90,97,104,    111,118,125,132,139, 146,153,160,167,174],
			   [  18,23,28,33,38,      43,48,53,58,63,      68,73,78,83,88,      93,98,103,108,113],
			   [10.5,14.5,19,23.5,27.5,32,36.5,41,45.5,49.5,54,58.5,62.5,67,71.5,76,80.5,84.5,89,93.5]
			  ]
fort_coop = []
church_coop = []
temple_coop = []
labs_coop = []
mall_coop = []
scrap_coop = []
garden_coop = []
wood_coop = []
jungle_coop = []
for i in range(20):
	fort_coop.append(0)
	church_coop.append(0)
	temple_coop.append(0)
	labs_coop.append(0)
	mall_coop.append(0)
	scrap_coop.append(0)
	garden_coop.append(0)
	wood_coop.append(0)
	jungle_coop.append(0)

#print(f'Fort_coop: {fort_coop}')
#print(f'Church_coop: {church_coop}')
coop = [fort_coop,church_coop,temple_coop,labs_coop,mall_coop,scrap_coop,garden_coop,wood_coop,jungle_coop]
print(f'Coop: {coop}')

#print(f'Third element in temple_coop: {coop[2][2]}')
#coop[2][2] = 0
#print(f'Third element in temple_coop: {coop[2][2]}')



structure = []
print("Pigeon Holes")
print(pigeonholes)
print("histoMidPts")
print(histoMidPts)

def burnloop(cells,hard,target,flash,structure,count_out,burnt_out):
	#print(f'Jay/py_choice: {jay}')
	#print("TEST")
	#print(f'{structure}')
	#print(f'passed: {cells} {hard} {target} {flash} ')
	def refresh():
		nonlocal cells
		nonlocal hard
		nonlocal structure
		for x in range(cells):
			if x < hard:
				structure[x] = 'B'  # -- mark as Burnt already (or ** unBurnable !! **)
			else:
				structure[x] = 'U'  # -- mark as Unburnt (i.e. can be ignited)

	count = 0
	burnt = hard
	iter = 0
	breakiter = 100000
	while burnt <= target:
		#print("In while loop ")
		if iter > breakiter:
			print("Breaking")
			break
		iter += 1
		#print(f'iter: {iter}')
		count = count + 1
		#print(f'count: {count}')
		count_out = count
		testCellNumber = random.randrange(0,cells)
		#print(f'at {testCellNumber} it is {structure[testCellNumber]}')
		if structure[testCellNumber] == 'U':
				#print('Trying to start a fire')
				if random.randrange(1,101) >= flash:
					#print(f"Success - started a fire at {count}")
					structure[testCellNumber] = 'B'
					burnt = burnt + 1
					burnt_out = burnt
	j = str(terr_count+1)
	#terrainStr = terrain_dict.get(j)
	#print(f"RESULT {terrainStr} Burnt: {burnt_out} at Count: {count_out}")
	refresh()
	#structure = []				
	return(count_out)

# end burnloop


# Number to description dictionary
terrain_dict = {'1':'Fort',
				'2':'Church',
				'3':'Temple',
				'4':'Labs',
				'5':'Mall',
				'6':'Scrapyard',
				'7':'Garden',
				'8':'Woods',
				'9':'Jungle',
				}
terry_dict={ 0:('1024','819','922','99'),  	#Fort
			 1:('256','179','218','90'),	#Church
			 2:('256','153','205','85'),	#Temple
			 3:('121','48','85','75'),	#Labs
			 4:('64','32','48','80'),	#Mall
			 5:('36','14','26','75'),	#Scrapyard
			 6:('36','7','22','70'), 	#Garden
			 7:('25','5','15','65'),	#Woods
			 8:('16','3','10','60'), 	#Jungle
			 }


# system("clear")
toothpick = " "*8
toothpickend = "---"
toothpick_inc = "---|"
toothpick2= " "*8
toothpick3= " "*8
toothpick2_inc = "-------|"
toothpick3_inc = "---|----"
for q in range(20):
	toothpick += toothpick_inc
toothpick += toothpickend
for r in range(10):
	toothpick2 += toothpick2_inc
	toothpick3 += toothpick3_inc
toothpick2 += toothpickend
toothpick3 += toothpickend
print(toothpick)
print(toothpick2)
print(toothpick3)

bar = []			#for histogram
underline = ("_"*94)
a_space = ' '*5
b_space = ' '*5
c_space = ' '*5
d_space = ' '*7
a_upper = ' '*5
b_upper = ' '*4
c_upper = ' '*3
d_upper = ' '*2
start_upper = ' '*5
print(a_space)
print(f"{start_upper}Terrain{a_upper}Cells{b_upper}Hard{c_upper}Target No.{d_upper}Flash Pt.")
for i in range(9):
	my_tuple = terry_dict.get(i)
	j = str(i+1)
	terrainStr = terrain_dict.get(j)
	print(f"{terrainStr.rjust(12)}{a_space}{my_tuple[0].rjust(4)}{b_space}{my_tuple[1].rjust(4)}{c_space}{my_tuple[2].rjust(4)}{d_space}{my_tuple[3].rjust(4)}")
	# Cell Hard Target Flash	
print('#'*80)
print(' 		Number of fire starters required for different terrains ')
print('#'*80)
#print("Terrains: 1 == Fort;   2 == Church; 3 == Temple")
#print("          4 == Labs;   5 == Mall;   6 == Scrapyard")
#print("          7 == Garden; 8 == Woods;  9 == Jungle")

NowterrainStr = ""
woods_out = "mid pts:"
garden_out = "mid pts:"
jungle_out_2 = "pts:    "
jungle_out_1 = "mid "
terr_out_1 = ["","","","","","","",""]
terr_out_2 = ["","","","","","","",""]
for h in range(7):
	terr_out_2[h] = "pts:    "
	terr_out_1[h] = "mid "
	for j in range(10):
		terr_out_1[h] += str(histoMidPts[h][j*2]).rjust(8)
		terr_out_2[h] += str(histoMidPts[h][j*2+1]).rjust(8)


for m in range(20):
	woods_out +=  str(histoMidPts[7][m]).rjust(4)
	garden_out += str(histoMidPts[6][m]).rjust(4)
for g in range (10):
	jungle_out_1 += str(histoMidPts[8][g*2]).rjust(8)
	jungle_out_2 += str(histoMidPts[8][g*2+1]).rjust(8)

terr_count = -1   # define here
while terr_count < 8:  ################################# WHILE LOOP
	terr_count = terr_count + 1 # 0 to 8

	##choice = input(f'Choose a number between 1 and 9 ')	
	choice = str(terr_count + 1)
	#print(f"Building Database for: {terrain_dict.get(choice)}")	

	# as python indexes from zero
	py_choice = int(choice) - 1
	# print(f"Adjusted for python to: {py_choice}")

	# For given choice find the variables cells, hard, target, flash
	Our_Tuple = terry_dict.get(py_choice)
	# print(f'Our Tuple {Our_Tuple}')
	cells = int(Our_Tuple[0])
	hard  = int(Our_Tuple[1])
	target= int(Our_Tuple[2])
	flash = int(Our_Tuple[3])

	#structure = []
	for x in range(cells):
		structure.append('U')   #mark as unburnt
	for x in range(hard):
		structure[x] = 'B'		# mark as burnt (technically 'some' unburnable, this is a cope)

	int_average = 0     # better to have a whole number than a float perhaps
	Our_Range = 1000	# set to 1000 in final version
	''' Number of test runs per terrain; 200 is a fair compromise
	                    	decrease if sim. runs to slow; increase for more accuracy '''
	high = 0            # expect to be over written on first pass
	low = 1000000       # expect to be over written on first pass
	average = 0.00      # just defined here
	runningTotal = 0     # increased each loop
	#print(f'Populating {terrain_dict.get(str(terr_count + 1))} database')
	for x in range(Our_Range):
		lastCount = 9999
		lastCount = burnloop(cells,hard,target,flash,structure,burnt_out,count_out)
		#print(f'Found lastCount: {lastCount}')
		# add 'lastcount' to its pigeonhole
		if lastCount <= pigeonholes[terr_count][0]:
			coop[terr_count][0] += 1 
		elif lastCount <= pigeonholes[terr_count][1]:
			coop[terr_count][1] += 1
		elif lastCount <= pigeonholes[terr_count][2]:
			coop[terr_count][2] += 1
		elif lastCount <= pigeonholes[terr_count][3]:
			coop[terr_count][3] += 1
		elif lastCount <= pigeonholes[terr_count][4]:
			coop[terr_count][4] += 1
		elif lastCount <= pigeonholes[terr_count][5]:
			coop[terr_count][5] += 1
		elif lastCount <= pigeonholes[terr_count][6]:
			coop[terr_count][6] += 1
		elif lastCount <= pigeonholes[terr_count][7]:
			coop[terr_count][7] += 1
		elif lastCount <= pigeonholes[terr_count][8]:
			coop[terr_count][8] += 1
		elif lastCount <= pigeonholes[terr_count][9]:
			coop[terr_count][9] += 1
		elif lastCount <= pigeonholes[terr_count][10]:
			coop[terr_count][10] += 1
		elif lastCount <= pigeonholes[terr_count][11]:
			coop[terr_count][11] += 1
		elif lastCount <= pigeonholes[terr_count][12]:
			coop[terr_count][12] += 1
		elif lastCount <= pigeonholes[terr_count][13]:
			coop[terr_count][13] += 1
		elif lastCount <= pigeonholes[terr_count][14]:
			coop[terr_count][14] += 1
		elif lastCount <= pigeonholes[terr_count][15]:
			coop[terr_count][15] += 1
		elif lastCount <= pigeonholes[terr_count][16]:
			coop[terr_count][16] += 1
		elif lastCount <= pigeonholes[terr_count][17]:
			coop[terr_count][17] += 1
		elif lastCount <= pigeonholes[terr_count][18]:
			coop[terr_count][18] += 1
		else:
			coop[terr_count][19] += 1
		if lastCount > high:
			high = lastCount
			#print(f'new high: {high}')
		if lastCount < low:
			low = lastCount
			#print(f'new low: {low}')
		runningTotal += lastCount
	average = runningTotal/Our_Range

	#print("found average")
	j = str(terr_count+1)
	NowterrainStr = terrain_dict.get(j)
	int_average = int(average + 0.5)
	minus_range = int(int_average - low)
	plus_range = int(high - int_average)
	#print(f"RESULT {NowterrainStr} Low: {low} High: {high} Avg: {average}")
	print(f'Analysed: {NowterrainStr.rjust(10).upper()} Average: {str(int_average).rjust(5)} Range:(Minus: {str(minus_range).rjust(5)} Plus: {str(plus_range).rjust(5)})')
	print(f'Histogram: Lowest bar: {histoMidPts[terr_count][0]} Highest bar: {histoMidPts[terr_count][19]}')
	outputline = ""
	outputline_1 = "Frq%"
	outputline_2 = "Frq. %  "
	mode = "simple"
	meh =""
	tempString = ""
	g = 0
	tempCount = 0
	while g < 20:
		if len(str(coop[terr_count][g])) > 3:  # set to 3 in final version (greater than 123 lengthwise)
			mode = "complex"
			#mystr = str((coop[terr_count][g]*100)/Our_Range)[:7]
			print(f' Complexed by: {str((coop[terr_count][g]*100)/Our_Range)[:7]}')
			g = 20
		else:
			tempString = str((coop[terr_count][g]*100)/Our_Range)
			tempCount = len(tempString)
			if tempCount > 5:
				mode = "complex"
				print(f' Complexed by: {str((coop[terr_count][g]*100)/Our_Range)[:7]}')
				g = 20
			elif tempString[-2:] != ".0": # not a whole number float so can't reduced by 2 to 1,2 or 3 in lengthwise size
				if tempCount > 3: # to leave 1.2, 3.4, 4.2 etc and whole number floats
					mode = "complex"
					print(f' Complexed by: {str((coop[terr_count][g]*100)/Our_Range)[:7]}')
					g = 20
		g += 1
	print(f'detected mode: {mode}')
	if mode == "simple":
		for k in range(20):
			#bar[terr_count] = str(coop[terr_count][k]).rjust(3)
			#outputline = concatenate(outputline,str(coop[terr_count][k]).rjust(3))
			outputline += str(coop[terr_count][k]).rjust(4)
		print("_"*94)   #
		print(f'Frq. %  {outputline}')
	elif mode == "complex":
		for k2 in range(20):
			dispfloat = ""
			tempfloat = (coop[terr_count][k2] * 100)/ Our_Range # Percent 99.9999; 9.999; 0.999
			strlen = len(str(tempfloat))
			if strlen < 8:
				if str(tempfloat)[-2:] == ".0":
					# print(f'{str(tempfloat)}')
					dispfloat = str(tempfloat)[0:-2]
					# print(f'short string thus: {dispfloat}')
				else: #leave tempfloat as is
					dispfloat = str(tempfloat)
					# print(f'SHORT string thus: {dispfloat}')
			else:
				k2x = str(tempfloat).index(".")
				if k2x == 0:
					dispfloat = str(tempfloat)
				elif k2x == 1:
					dispfloat = '%.5f'%tempfloat
				elif k2x == 2:
					dispfloat = '%.4f'%tempfloat
				elif k2x == 3:
					dispfloat = '%.3f'%tempfloat
				else:
					dispfloat = str(tempfloat)

				# print(f'string length {strlen} point at: {k2x} thus: {dispfloat}')  # was {str(dispfloat)}
			if k2%2 == 0: # k2 = 0,2,4,6,8
				outputline_1 += dispfloat.rjust(8)  ## later (x  * 100)/ Our_Range
			else:
				outputline_2 += dispfloat.rjust(8)  #was str(coop[terr_count][k2]).rjust(8)
		print("_"*94)
		print(outputline_1)
		print(toothpick3)
		print(outputline_2)
		print(toothpick2)

	if terr_count == 7:
		print(toothpick)
		print(woods_out)  # row of mid-points to add context to outputline above for woods terrain
	elif terr_count == 6:
		print(toothpick)
		print(garden_out) # row of mid-points to add context to outputline above for garden terrain
	elif terr_count == 8:
		print(toothpick)
		print(jungle_out_1)
		print(jungle_out_2)
	else:
		print(toothpick)
		print(terr_out_1[terr_count])
		print(terr_out_2[terr_count])


		# row of mid-points to add context to outputline above for garden terrain
		#requires two or more lines to display mid points

	print(underline)
	print(underline)
	
	#print("*"*100)
	structure.clear()
print(f'[ No of cycles: {Our_Range} ]')	
print("*"*94)


