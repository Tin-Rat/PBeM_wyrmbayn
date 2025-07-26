# Read me for Terrain_BS_cyc_3.py 

Program to determine the number of fire starters (of average ability) required to raze different terrain types to the ground. This is a necessary step in the design process.

- **Cells**: Number of distinct locations pertaining to a particular terrain.
- **Hard**: Number of cells that are non burnable.
- **Target No**: Slightly artificial, being the sum of the hard points and 50% of the combustible cells at the initial start conditions.
For 'Fort' terrain:
`Target No = 819 + 1/2(1024 - 819) = 819 + 1/2(205) = 819 + 103 (rounded) = 922`
- **Flash Pt.**: The difficulty of starting a fire.
`99 = 1% chance; 90 = 10% chance`, etc.
