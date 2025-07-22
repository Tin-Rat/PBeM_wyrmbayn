#
#
# Read me for Terrain_BS_cyc_3.py
#
# Program to determine the number of fire starters (of average  
# ability) required to raise different terrain types to the 
# ground. This is a neccessary step in the design process.
#
# 'Cells' equate to the number of distinct locations pertain
# to a particular terrain.
# 'Hard' equates to the number of cells that are unburnable
# 'Target No' is slightly artificial being the sum of the
# hard points and 50% of the combustable cells at the 
# initial start conditions. So for 'Fort' terrain the
# 'Target No' is 819 + 1/2(1024 - 819)
# or 819 + 1/2(205) = 819 + 103(rounded) = 922
# Flash Pt. is the difficulty of starting a fire
# 99 = 1% chance; 90 = 10% chance etc.