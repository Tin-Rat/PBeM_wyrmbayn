
![*wyrmbayn*](./Title.png "wyrmbayn")

***Version 1.01***

***© Kevin Joyce 2025***

---

**Foreword.**

This is a working document as the wyrmbayn project is ongoing it is subject to changes.

Much of the following will initially be a transcript of an earlier unpublished work, and as such may reference features that won’t necessarily be adopted in the finished software.

There may be references to pbm but the project as envisaged now will be strictly pbem.

The mapping system will be different to that referenced in this document, though it will probably be updated later to reflect any adopted, different system.

This foreword will be modified to reflect any subsequent changes, as the project evolves.

---

<span style="background-color: #FFFF00">**Page 1.**</span>

**CONTENTS**
<!---  comments --->
<table style="table-layout: fixed; width: 50%">

  <tablehead>
  <tr>
    <th width="20%">PAGE NUMBER</th>
    <th width="30%">DESCRIPTION</th>
  </tr>
</tablehead>

<tablebody>
  <tr>
    <td><a href="#p2">2</a></td> <td><a href="#intro">Intro.</a></td>
  </tr>
  <tr>
    <td><a href="#p2">2</a></td> <td><a href="#what2">What is PbeM Gaming?</a></td>
  </tr>
  <tr>
    <td><a href="#p2">2</a></td> <td><a href="#game">Game Scenario</a></td>
  </tr>
  <tr>
    <td><a href="#p2">2</a></td> <td><a href="#start">Startup Form</a></td>
  </tr>
  <tr>
    <td><a href="#p2">2</a></td> <td><a href="#hints">Hints</a></td>
  </tr>
  <tr>
    <td><a href="#p3">3</a></td> <td><a href="#char">Character Types</a></td>
  </tr>
  <tr>
    <td><a href="#p3">3 onwards</a></td> <td><a href="#maj">Major Characters</a></td>
  </tr>
  <tr>
    <td><a href="#p7">7</a></td> <td><a href="#minor">Minor Characters</a></td>
  </tr>
  <tr>
    <td><a href="#p8">8 onwards</a></td> <td><a href="#terr">Terrains</a></td>
  </tr>
  <tr>
    <td><a href="#p11">11</a></td> <td><a href="#proc">Processing Sequence</a></td>
  </tr>
   <tr>
    <td><a href="#p12">12</a></td> <td><a href="#map">Map</a></td>
  </tr>
    <tr>
    <td><a href="#p13">13</a></td> <td><a href="#ye">Ye Olde Mappe Legend</a></td>
  </tr>
    <tr>
    <td><a href="#p14">14</a></td> <td><a href="#movement">Movement</a></td>
  </tr>
  <tr>
    <td><a href="#p14">14</a></td> <td><a href="#order">Orders Overview</a></td>
  </tr>
  <tr>
    <td><a href="#p15">15</a></td> <td><a href="#demo">Demolish Order</a></td>
  </tr>
  <tr>
    <td><a href="#p16">16</a></td> <td><a href="#leech">Leech Order</a></td>
  </tr>
  <tr>
    <td><a href="#p16">16</a></td> <td><a href="#move">Move Order</a></td>
  </tr>
  <tr>
    <td><a href="#p17">17</a></td> <td><a href="#raze">Raze Order</a></td>
  </tr>
  <tr>
    <td><a href="#p17">17</a></td> <td><a href="#recruit">Recruit Order</a></td>
  </tr>
  <tr>
    <td><a href="#p18">18</a></td> <td><a href="#stake">Stake Order</a></td>
  </tr>
  <tr>
    <td><a href="#p18">18</a></td> <td><a href="#mcr">Minor Character Recruitment</a></td>
  </tr>
  <tr>
    <td><a href="#p19">19</a></td> <td><a href="#rally">Rallying</a></td>
  </tr>
  <tr>
    <td><a href="#p19">19</a></td> <td><a href="#discor">Discorporation</a></td>
  </tr>
  <tr>
    <td><a href="#p19">19</a></td> <td><a href="#blood">Bloodfeast</a></td>
  </tr>
  <tr>
    <td><a href="#p19">19</a></td> <td><a href="#grim">Grim Reaper</a></td>
  </tr>
  <tr>
    <td><a href="#p20">20</a></td> <td><a href="#cata">Cataleptic Sleep</a></td>
  </tr>
  <tr>
    <td><a href="#p20">20</a></td> <td><a href="#spy">Spying</a></td>
  </tr>
  <tr>
    <td><a href="#p20">20</a></td> <td><a href="#comb">Combat Resolution</a></td>
  </tr>
  <tr>
    <td><a href="#p21">21</a></td> <td><a href="#casu">Casualties</a></td>
  </tr>
  <tr>
    <td><a href="#p21">21</a></td> <td><a href="#ccp">Computer Controlled Positions</a></td>
  </tr>
  <tr>
    <td><a href="#p22">22</a></td> <td><a href="#league">League Tables</a></td>
  </tr>
  <tr>
    <td><a href="#p22">22</a></td> <td><a href="#win">Winning a Game of Wyrmbayn</a></td>
  </tr>
  <tr>
    <td><a href="#p22">22</a></td> <td><a href="#coo">Change of Ownership</a></td>
  </tr>
  <tr>
    <td><a href="#p22">22</a></td> <td><a href="#diplo">Diplomacy</a></td>
  </tr>
  <tr>
    <td><a href="#p23">23</a></td> <td><a href="#appen">Appendix</a></td>
  </tr>
</tablebody>
</table>


<h4 id="p2"><span style="background-color: #FFFF00">Page 2.</span></h4>

<h4 id="intro">Intro.</h4>

Wyrmbane is a 2 to 12 play by e-mail (PbeM) game, in which each player controls a great house. The individuals that make up your house are divided into two different types; Major Characters, and Minor Characters.  There are two ways of winning:- either by having the only surviving Count at the end of a turn, or by owning more than more than half of the remaining forts at the end of the turn.

<h4 id="what2">What is Pbem Gaming?</h4>

One of the objectives of PbeM (Play by email) games is to allow large(ish) numbers of players to be involved in quite complex games. In earlier times the postal service was used [In this guise it was known as PBM (Play by Mail)] and it was viewed as an alternative to tabletop games, with campaigns taking place over several months with weekly or fortnightly turn around.

Whether or not this type of game playing can make a revival has yet to be decided. I am of the view that it is possible (just).


<h4 id="game">Game Scenario</h4>

Wyrmbayn is set on an alternative Earth with a notable absence of oceans. On it vampires can live alongside priests and animated scarecrows.


<h4 id="start">Startup Form.</h4>

With this rulebook you should receive a startup form, or a link to one.  You will be asked if other players may contact you. (You don’t have to agree with this.)  
You will also be asked what ‘turnaround’ time you would prefer.
You will be asked to give your start character a (family) name. The start character is always a Count – and your House will have the same name as him or her.

<h4 id="hints">Hints.</h4>

(Empty at the moment).

<h4 id="p3"><span style="background-color: #FFFF00">Page 3.</span></h4>

<h4 id="char">Character Types.</h4>

There are two classes of Characters, Major and Minor.

<h4 id="maj">Major Characters</h4>

There are twenty five Major Characters, each of which has a health score which is a percentage indicating how fit they are. All major characters will expire if this reaches zero. The exception is the Count character. Counts merely go into a cataleptic sleep when their health score reaches zero. In this state they are vulnerable to staking (which will bring about their demise).

Minor characters are automatically recruited by major characters at the start of the turn processing sequence – however each major characters have their own set of followers that he/she may recruit, details for each type are given below. There could/should be a maximum number of any particular minor character a Major may recruit, a figure of 240 is suggested. 

Major characters can also recruit other majors – the ‘Recruit’ order is used for this.  There are limitations as to which characters can be recruited by a particular major character.

***Alchemist***
Health:-  Max 100%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +3%(plus)
				Resting at Laboratory:-  +50%(plus)
Recruits	Major:- Archaeologist, Botanist, Shaman and Grave Digger.
		Minor:- Demons, Homunculii and Odd Bods.

***Archaeologist***
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Jungle or Desert:-  +20%(plus)
Recruits	Major:- Grave Digger.
		Minor:- Gargoyles, Mummies and Skeletons.

***Botanist***
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Garden, Jungle or Woods:-  +15%(plus)
Recruits	Major:- Farmer and Gardener.
		Minor:- Greenmen, Triffids and Zombies.

***Count***
Health:-  Max 100%		Movement penalty:-   -20%(minus)
	Health Deterioration;	Resting:-  -2%(minus)
				Resting in a Fort:-  -1%(minus)
Recruits	Any Major except another Count.
		Minor:- Vampires, Werewolves and Zombies.

<h4 id="p4"><span style="background-color: #FFFF00">Page 4.</span></h4>

***Couturier***
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in a Mall:-  +25%(plus)
Recruits	Major:- Seamstress.
		Minor:- Manikins, Puppets and Zombies.

***Crow Master***
Health:-  Max 90%		Movement penalty:-   -8%(minus)
	Health Restoration;	Resting:-  +4%(plus)
				Resting in Garden, Plain or Woods:-  +12%(plus)
Recruits	Major:- Farmer, Ploughman and Merchant.
		Minor:- Corn Dollies, Scarecrows and Tar Babies.

***Explorer***
Health:-  Max 100%		Movement penalty:-   -9%(minus)
	Health Restoration;	Resting:-  +4%(plus)
			Resting in Garden, Jungle, Desert or Woods:-  +10%(plus)
Recruits	Major:- Archaeologist.
		Minor:- Triffids, Werewolves and Zombies.

***Farmer***
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Garden:-  +15%(plus)
Recruits	Major:- Crow Master, Gardener and Ploughman.
		Minor:- Greenmen, Scarecrows and Werewolves.

***Gardener***
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Garden:-  +15%(plus)
Recruits	Major:- Grave Digger and Botanists.
		Minor:- Greenmen, Scarecrows and Triffids.

***Grave Digger***
Health:-  Max 50%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church:-  +10%(plus)
Recruits	Major:- Alchemist, Archaeologist, Count, Mason, Monk, Necromancer, Priest, Shaman and Wax Worker.
		Minor:- Demons, Skeletons and Vampires.

***Jester***
Health:-  Max 60%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Fort:-  +15%(plus)
Recruits	Major:- Knave only.
		Minor:- Odd bods, Puppets and Robots.

<h4 id="p5"><span style="background-color: #FFFF00">Page 5.</span></h4>

***Knave***
Health:-  Max 100%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Fort:-  +15%(plus)
Recruits	Major:- Couturier, Jester and Retrobate.
		Minor:- Tar Babies, Tinmen and Werewolves.

***Mason***
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church, Fort or Temple;:-  +10%(plus)
Recruits	Major:- Grave Digger and Sculptor.
		Minor:- Gargoyles, Mummies and Odd Bods.

***Mechanic***
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Scrapyard:-  +15%(plus)
Recruits	Major:- Merchant only.
		Minor:- Androids, Robots and Tar Babies.

***Merchant***
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Scrapyard:-  +15%(plus)
Recruits	Major:- Alchemist, Crow master, Mechanic and Sculptor.
		Minor:- Robots, Tinmen and Triffids.

***Monarch***
Health:-  Max 80%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Fort:-  +15%(plus)
Recruits	Major:- Count, Couturier, Explorer, Gardener, Jester, Knave, Mason 			and Sculptor.
		Minor:- Androids, Odd Bods and Tinmen.

***Monk***
Health:-  Max 100%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church, Temple or Fort:-  +10%(plus)
Recruits	Major:- Gardener, Priest and Shaman.
		Minor:- Demons, Gargoyles and Skeletons.
    
***Necromancer***
Health:-  Max 50%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church, Temple or Fort:-  +10%(plus)
Recruits	Major:- Alchemist, Grave Digger and Shaman.
		Minor:- Demons, Mummies and Skeletons.

<h4 id="p6"><span style="background-color: #FFFF00">Page 6.</span></h4>

***Ploughman***
Health:-  Max 100%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Garden, Plain or Woods:-  +10%(plus)
Recruits	Major:- Crow Master only.
		Minor:- Corn Dollies, Scarecrows and Greenmen.

***Priest***
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church or Temple:-  +10%(plus)
Recruits	Major:- Grave Digger and Monk.
		Minor:- Corn Dollies, Gargoyles and Vampires.

***Retrobate***
Health:-  Max 75%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church or Temple:-  +10%(plus)
Recruits	Major:- Jester Only.
		Minor:- Corn Dollies, Homunculii and Tar Babies.

***Sculptor***
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church or Temple:-  +10%(plus)
Recruits	Major:- Mason and Wax Worker.
		Minor:- Androids, Manikins and Robots.

***Seamstress***
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Mall:-  +20%(plus)
Recruits	Major:- Couturier and Wax Worker.
		Minor:- Manikins, Mummies and Puppets.

***Shaman***
Health:-  Max 100%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church, Garden, Jungle, Plain, Temple or 				Woods:-  +8%(plus)
Recruits	Major:- Monk only.
		Minor:- Homunculii, Puppets and Vampires.

***Wax Worker***
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Mall:-  +20%(plus)
Recruits	Major:- Seamstress only.
		Minor:- Androids, Homunculii and Manikins.


<h4 id="p7"><span style="background-color: #FFFF00">Page 7.</span></h4>

<h4 id="minor">Minor Characters</h4>

There are nineteen different types of Minor Characters, theirs stats are given in the table below:-

| Species | Strength | Hits | Dexterity | Fireproofness | Fire Starter Attrition Rate %|Demolition Attrition Rate Per Thousand|
| :---: | :---: | :---: | :---: | :---: |:---: | :---:|
|Androids|10|10|5|4|1|0|
|Corn Dollies|1|1|6|1|3|25|
|Demons|1|20|5|5|0|0|
|Gargoyles|3|20|6|5|0|0|
|Greenmen|6|3|6|2|5|2|
|Homunculii|3|3|4|3|5|4|
|Manikins|3|3|4|2|3|4|
|Mummies|4|4|4|2|3|3|
|Odd Bods|5|5|5|4|5|1|
|Puppets|2|4|4|2|3|3|
|Robots|8|8|3|4|1|0|
|Scarecrows|2|2|5|2|3|6|
|Skeletons|3|3|5|4|2|4|
|Tar Babies|3|3|6|1|4|4|
|Tinmen|3|7|4|5|5|0|
|Triffids|4|12|2|2|4|0|
|Vampires|12|6|6|3|2|1|
|Werewolves|6|5|7|4|5|1|
|Zombies|5|5|4|3|1|2|


  Note:- 
  1. When determining Fire-Starter abilities equal weighting is given to Strength, Dexterity and Fireproofness.
  2. For Demolition abilities only Strength and Dexterity are considered.


<h4 id="p8"><span style="background-color: #FFFF00">Page 8.</span></h4>

<h4 id="terr">Terrains</h4>
<p>
There are twelve terrain types they are named after the most prominent feature so for example a Church location could reasonable be considered to contain a graveyard a small amount of additional dwellings and the odd yew tree. All terrain locations with the exception of ‘Plain’ are locations where minor characters may be found and (automatically) recruited.</p>
<p>  The ‘Density’ in the table below is an abstract value that gives an indication of the maximum number of the particular type of minor character that may be found there. After a round of recruitment there may temporarily be less characters than the ‘Density’ number (usually down to a bare minimum), replenishment will be approximately one fourth of the ‘Density’ value, falling to approximately one sixth for damaged terrain. Ruins do not appear in the initial map (turn one), but are created using demolish/raze orders. 
</p>

|--------------------------------------|⬅️⬅️⬅️⬅️⬅️ Terrain Damage Percentage & Reinforcements ➡️➡️➡️➡️➡️| 
|:-:|:-|

| Terrain | Minor Character | Density | 0%  | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% | 90% |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| C | Corn Dollies  | 756K  | 189.00K | 182.37K | 175.74K | 169.11K | 162.48K | 155.84K | 149.21K | 142.58K | 135.95K | 129.32K |
| H | Gargoyles | 18K | 4.50K | 4.34K | 4.18K | 4.03K | 3.87K | 3.71K | 3.55K | 3.39K | 3.24K | 3.08K |
| U | Greenmen  | 36K | 9.00K | 8.68K | 8.37K | 8.05K | 7.74K | 7.42K | 7.11K | 6.79K | 6.47K | 6.16K |
| R | Odd Bods  | 36K | 9.00K | 8.68K | 8.37K | 8.05K | 7.74K | 7.42K | 7.11K | 6.79K | 6.47K | 6.16K |
| C | Skeletons | 162K  | 40.50K  | 39.08K  | 37.66K  | 36.24K  | 34.82K  | 33.40K  | 31.97K  | 30.55K  | 29.13K  | 27.71K  |
| H | Triffids  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| ⬇️  | Zombies | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
|   |   |   |   |   |   |   |   |   |   |   |   |   |
| D | Demons  | 27K | 6.75K | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| E | Gargoyles | 9K  | 2.25K | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| S | Homunculii  | 189K  | 47.25K  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| E | Mummies | 108K  | 27.00K  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| R | Odd Bods  | 54K | 13.50K  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| T | Skeletons | 45K | 11.25K  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
|   |   |   |   |   |   |   |   |   |   |   |   |   |
| F | Gargoyles | 18K | 4.50K | 4.34K | 4.18K | 4.03K | 3.87K | 3.71K | 3.55K | 3.39K | 3.24K | 3.08K |
| O | Greenmen  | 63K | 15.75K  | 15.20K  | 14.64K  | 14.09K  | 13.54K  | 12.99K  | 12.43K  | 11.88K  | 11.33K  | 10.78K  |
| R | Odd Bods  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| T | Tinmen  | 81K | 20.25K  | 19.54K  | 18.83K  | 18.12K  | 17.41K  | 16.70K  | 15.99K  | 15.28K  | 14.57K  | 13.86K  |
| ⬇️  | Triffids  | 72K | 18.00K  | 17.37K  | 16.74K  | 16.11K  | 15.47K  | 14.84K  | 14.21K  | 13.58K  | 12.95K  | 12.32K  |
| ⬇️  | Vampires  | 18K | 4.50K | 4.34K | 4.18K | 4.03K | 3.87K | 3.71K | 3.55K | 3.39K | 3.24K | 3.08K |
| ⬇️  | Werewolves  | 36K | 9.00K | 8.68K | 8.37K | 8.05K | 7.74K | 7.42K | 7.11K | 6.79K | 6.47K | 6.16K |
|   |   |   |   |   |   |   |   |   |   |   |   |   |
| G | Corn Dollies  | 504K  | 126.00K | 121.58K | 117.16K | 112.74K | 108.32K | 103.90K | 99.48K  | 95.05K  | 90.63K  | 86.21K  |
| A | Greenmen  | 63K | 15.75K  | 15.20K  | 14.64K  | 14.09K  | 13.54K  | 12.99K  | 12.43K  | 11.88K  | 11.33K  | 10.78K  |
| R | Scarecrows  | 378K  | 94.50K  | 91.19K  | 87.87K  | 84.55K  | 81.24K  | 77.92K  | 74.61K  | 71.29K  | 67.97K  | 64.66K  |
| D | Tar Babies  | 135K  | 33.75K  | 32.57K  | 31.38K  | 30.20K  | 29.01K  | 27.83K  | 26.65K  | 25.46K  | 24.28K  | 23.09K  |
| E | Triffids  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| N | Werewolves  | 9K  | 2.25K | 2.17K | 2.09K | 2.01K | 1.93K | 1.86K | 1.78K | 1.70K | 1.62K | 1.54K |
|   |   |   |   |   |   |   |   |   |   |   |   |   |



<h4 id="p9"><span style="background-color: #FFFF00">Page 9.</span></h4>

|--------------------------------------|⬅️⬅️⬅️⬅️⬅️ Terrain Damage Percentage & Reinforcements ➡️➡️➡️➡️➡️| 
|:-:|:-|

| Terrain | Minor Character | Density | 0%  | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% | 90% |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| J | Demons  | 27K | 6.75K | 6.51K | 6.28K | 6.04K | 5.80K | 5.57K | 5.33K | 5.09K | 4.86K | 4.62K |
| U | Greenmen  | 63K | 15.75K  | 15.20K  | 14.64K  | 14.09K  | 13.54K  | 12.99K  | 12.43K  | 11.88K  | 11.33K  | 10.78K  |
| N | Homunculii  | 189K  | 47.25K  | 45.59K  | 43.93K  | 42.28K  | 40.62K  | 38.96K  | 37.30K  | 35.65K  | 33.99K  | 32.33K  |
| G | Odd Bods  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| L | Robots  | 9K  | 2.25K | 2.17K | 2.09K | 2.01K | 1.93K | 1.86K | 1.78K | 1.70K | 1.62K | 1.54K |
| E | Scarecrows  | 144K  | 36.00K  | 34.74K  | 33.47K  | 32.21K  | 30.95K  | 29.68K  | 28.42K  | 27.16K  | 25.90K  | 24.63K  |
| ⬇️  | Tar Babies  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| ⬇️  | Triffids  | 72K | 18.00K  | 17.37K  | 16.74K  | 16.11K  | 15.47K  | 14.84K  | 14.21K  | 13.58K  | 12.95K  | 12.32K  |
| ⬇️  | Zombies | 72K | 18.00K  | 17.37K  | 16.74K  | 16.11K  | 15.47K  | 14.84K  | 14.21K  | 13.58K  | 12.95K  | 12.32K  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |
| L | Androids  | 9K  | 2.25K | 2.17K | 2.09K | 2.01K | 1.93K | 1.86K | 1.78K | 1.70K | 1.62K | 1.54K |
| A | Homunculii  | 189K  | 47.25K  | 45.59K  | 43.93K  | 42.28K  | 40.62K  | 38.96K  | 37.30K  | 35.65K  | 33.99K  | 32.33K  |
| B | Odd Bods  | 36K | 9.00K | 8.68K | 8.37K | 8.05K | 7.74K | 7.42K | 7.11K | 6.79K | 6.47K | 6.16K |
| S | Puppets | 81K | 20.25K  | 19.54K  | 18.83K  | 18.12K  | 17.41K  | 16.70K  | 15.99K  | 15.28K  | 14.57K  | 13.86K  |
| ⬇️  | Robots  | 36K | 9.00K | 8.68K | 8.37K | 8.05K | 7.74K | 7.42K | 7.11K | 6.79K | 6.47K | 6.16K |
| ⬇️  | Tinmen  | 18K | 4.50K | 4.34K | 4.18K | 4.03K | 3.87K | 3.71K | 3.55K | 3.39K | 3.24K | 3.08K |
| ⬇️  | Triffids  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
|   |   |   |   |   |   |   |   |   |   |   |   |   |
| M | Androids  | 9K  | 2.25K | 2.17K | 2.09K | 2.01K | 1.93K | 1.86K | 1.78K | 1.70K | 1.62K | 1.54K |
| A | Manikins  | 189K  | 47.25K  | 45.59K  | 43.93K  | 42.28K  | 40.62K  | 38.96K  | 37.30K  | 35.65K  | 33.99K  | 32.33K  |
| L | Puppets | 216K  | 54.00K  | 52.11K  | 50.21K  | 48.32K  | 46.42K  | 44.53K  | 42.63K  | 40.74K  | 38.84K  | 36.95K  |
| L | Zombies | 27K | 6.75K | 6.51K | 6.28K | 6.04K | 5.80K | 5.57K | 5.33K | 5.09K | 4.86K | 4.62K |
|   |   |   |   |   |   |   |   |   |   |   |   |   |
| P | See |   |   |   |   |   |   |   |   |   |   |   |
| L | Note 1.|   |   |   |   |   |   |   |   |   |   |   |
| A | ⬇️  |   |   |   |   |   |   |   |   |   |   |   |
| I | ⬇️  |   |   |   |   |   |   |   |   |   |   |   |
| N | ⬇️  |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |
| R | See |   |   |   |   |   |   |   |   |   |   |   |
| U | Note 2. |   |   |   |   |   |   |   |   |   |   |   |
| I | ⬇️  |   |   |   |   |   |   |   |   |   |   |   |
| N | ⬇️  |   |   |   |   |   |   |   |   |   |   |   |
| S | ⬇️  |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |


Note:-
  1. (For 'Plain' terrain) - No Minor Characters are to be found at these locations.
  2. (For 'Ruins' terrain) - Minor Characters are randomly assigned influenced by the surrounding terrain types. (See the Appendix.)
  3. Deserts, by their nature cannot be demolished or razed by fire. They are however included above as always 0% damaged.


<h4 id="p10"><span style="background-color: #FFFF00">Page 10.</span></h4>

|--------------------------------------|⬅️⬅️⬅️⬅️⬅️ Terrain Damage Percentage & Reinforcements ➡️➡️➡️➡️➡️| 
|:-:|:-|

| Terrain | Minor Character | Density | 0%  | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% | 90% |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| S | Androids  | 9K  | 2.25K | 2.17K | 2.09K | 2.01K | 1.93K | 1.86K | 1.78K | 1.70K | 1.62K | 1.54K |
| C | Homunculii  | 90K | 22.50K  | 21.71K  | 20.92K  | 20.13K  | 19.34K  | 18.55K  | 17.76K  | 16.97K  | 16.18K  | 15.40K  |
| R | Odd Bods  | 36K | 9.00K | 8.68K | 8.37K | 8.05K | 7.74K | 7.42K | 7.11K | 6.79K | 6.47K | 6.16K |
| A | Puppets | 81K | 20.25K  | 19.54K  | 18.83K  | 18.12K  | 17.41K  | 16.70K  | 15.99K  | 15.28K  | 14.57K  | 13.86K  |
| P | Robots  | 27K | 6.75K | 6.51K | 6.28K | 6.04K | 5.80K | 5.57K | 5.33K | 5.09K | 4.86K | 4.62K |
| Y | Scarecrows  | 144K  | 36.00K  | 34.74K  | 33.47K  | 32.21K  | 30.95K  | 29.68K  | 28.42K  | 27.16K  | 25.90K  | 24.63K  |
| A | Tar Babies  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| R | Tinmen  | 81K | 20.25K  | 19.54K  | 18.83K  | 18.12K  | 17.41K  | 16.70K  | 15.99K  | 15.28K  | 14.57K  | 13.86K  |
| D | Triffids  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| ⬇️  | Werewolves  | 27K | 6.75K | 6.51K | 6.28K | 6.04K | 5.80K | 5.57K | 5.33K | 5.09K | 4.86K | 4.62K |
|   |   |   |   |   |   |   |   |   |   |   |   |   |
| T | Corn Dollies  | 216K  | 54.00K  | 52.11K  | 50.21K  | 48.32K  | 46.42K  | 44.53K  | 42.63K  | 40.74K  | 38.84K  | 36.95K  |
| E | Demons  | 72K | 18.00K  | 17.37K  | 16.74K  | 16.11K  | 15.47K  | 14.84K  | 14.21K  | 13.58K  | 12.95K  | 12.32K  |
| M | Gargoyles | 18K | 4.50K | 4.34K | 4.18K | 4.03K | 3.87K | 3.71K | 3.55K | 3.39K | 3.24K | 3.08K |
| P | Greenmen  | 36K | 9.00K | 8.68K | 8.37K | 8.05K | 7.74K | 7.42K | 7.11K | 6.79K | 6.47K | 6.16K |
| L | Skeletons | 162K  | 40.50K  | 39.08K  | 37.66K  | 36.24K  | 34.82K  | 33.40K  | 31.97K  | 30.55K  | 29.13K  | 27.71K  |
| E | Triffids  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| ⬇️  | Zombies | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
|   |   |   |   |   |   |   |   |   |   |   |   |   |
| W | Androids  | 9K  | 2.25K | 2.17K | 2.09K | 2.01K | 1.93K | 1.86K | 1.78K | 1.70K | 1.62K | 1.54K |
| O | Demons  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| O | Greenmen  | 63K | 15.75K  | 15.20K  | 14.64K  | 14.09K  | 13.54K  | 12.99K  | 12.43K  | 11.88K  | 11.33K  | 10.78K  |
| D | Homunculii  | 90K | 22.50K  | 21.71K  | 20.92K  | 20.13K  | 19.34K  | 18.55K  | 17.76K  | 16.97K  | 16.18K  | 15.40K  |
| S | Puppets | 81K | 20.25K  | 19.54K  | 18.83K  | 18.12K  | 17.41K  | 16.70K  | 15.99K  | 15.28K  | 14.57K  | 13.86K  |
| ⬇️  | Robots  | 9K  | 2.25K | 2.17K | 2.09K | 2.01K | 1.93K | 1.86K | 1.78K | 1.70K | 1.62K | 1.54K |
| ⬇️  | Scarecrows  | 297K  | 74.25K  | 71.65K  | 69.04K  | 66.44K  | 63.83K  | 61.22K  | 58.62K  | 56.01K  | 53.41K  | 50.80K  |
| ⬇️  | Tar Babies  | 108K  | 27.00K  | 26.05K  | 25.11K  | 24.16K  | 23.21K  | 22.26K  | 21.32K  | 20.37K  | 19.42K  | 18.47K  |
| ⬇️  | Triffids  | 54K | 13.50K  | 13.03K  | 12.55K  | 12.08K  | 11.61K  | 11.13K  | 10.66K  | 10.18K  | 9.71K | 9.24K |
| ⬇️  | Werewolves  | 36K | 9.00K | 8.68K | 8.37K | 8.05K | 7.74K | 7.42K | 7.11K | 6.79K | 6.47K | 6.16K |
|   |   |   |   |   |   |   |   |   |   |   |   |   |


<h4 id="p11"><span style="background-color: #FFFF00">Page 11.</span></h4>


<h4 id="proc">Processing Sequence</h4>

  1. **Administration** 	Turn fees (if any) will be deducted, chnges of contact details will be noted, other admin etc.
  2. **Minor Character Recruitment**
  3. **Move Phase**
  4. **Battle Phase**
  5. **Changes of ownership** (of locations)
  6. **Rallying**
  7. **Discorporation**	  Discorporation of Majors who have no Minors.
  8. **Bloodfeast**
  9. **Grim Reaper**   Deaths through pernicious anaemia and other maladies (especially zero health score!)
  10. **Cataleptic Sleep**	(Count from 1 to 10 backwards)
  11. **Demolition**
  12. **Staking**	A la the Hammer House of Horrors
  13. **Leeching**
  14. **Recruiting**  New Major Characters arrive
  15. **Spying**
  16. **Turn reports Generated**  And other housekeeping
       




<h4 id="p12"><span style="background-color: #FFFF00">Page 12.</span></h4>



<h4 id="map">Map.</h4>

TBA






<h4 id="p13"><span style="background-color: #FFFF00">Page 13.</span></h4>




<h4 id="ye">< for ye olde mappe legend ></h4>



<h4 id="p14"><span style="background-color: #FFFF00">Page 14.</span></h4>





<h4 id="movement">Movement.</h4>

Major Characters may move in any of six directions numbered ***1*** to ***6***:- where
- ***1*** is at ***60°*** (approx NE by E), 
- ***2*** is at ***120°*** (approx SE by E), 
- ***3*** is at ***180°*** (S), 
- ***4*** is at ***240°*** (approx SW by W),
- ***5*** is at ***300°*** (approx NW by W) and 
- ***6*** is at ***360°/0°*** (N).

As the Major Characters move, they 'drag along' their retinue of Minor Characters with them.

- This is actually an over simplification; the 'world' as mentioned elsewhere is not flat - so consequently there are 'edge' effects evident when 'wrapping around' from one end of the world-map to the other. This is explained elsewhere.


<h4 id="order">Orders Overview</h4>

You may submit orders for each of your Major Characters. Your Count (if you have one, and who is not in a sleep state) may issue up to six orders per turn. Other Major Characters may have up to three orders submitted. 
The available orders are Demolish, Leech, Move, Raze, Recruit and Stake.
The Stake order may only be submitted on behalf of the Alchemist, Count, Explorer or Priest under your control.

Move orders should work if correctly formatted, so should only be issued once per Major Character per turn. 

Similarly Leech orders should work if correctly formatted, assuming donor and receiver are at the same location. That said a single leech will transfer only 10% health from the donor to the receiver, (or less if the donor starts out with less than 10%). So in the case of a generous donor this order could be issued more than once per turn.

The demolish order is not guaranteed to work as it depends on the Major Character having a ‘critical mass’ of Minor Character underlings under their control. In theory a Major could issue this order more than once per turn, but if if fails on the first attempt it is very, very likely to fail on a second or third attempt in the <u>same</u> turn.

Raze order; very similar to demolish order, but Minor Characters use fire.

The Stake order is not guaranteed to work as the health score of the Major is taken into account – those with poor health score are more likely to fail due to having a critical fumble. For this reason in most cases this order should be issued more than once per character turn where the exacting conditions are already in place.

The Recruit order may be issued more than once per character per turn, this is discussed more thoroughly in the relevant section below.

Note:- Orders are processed in the following order:-
	Move, Demolish, Raze, Stake, Leech then Recruit.


<h4 id="p15"><span style="background-color: #FFFF00">Page 15.</span></h4>

<h4 id="demo">Demolish Order</h4>
<p>
(Available to all Majors)</p><p>
The Major Character will set the Minors he controls to demolish the location he is currently in.  

Note: This order is not guaranteed to work as it requires a critical mass of Minor Characters to work. Also some locations, by their nature are much harder to demolish than others, so the critical mass for them will be a much higher number of Minor Characters.  Some Minor Characters have a higher strength/dexterity combo than others;  so achieving critical mass is a qualitative as well as a quantity conundrum. </p>

Example:-
<span style="background-color: #00FFFF">Explorer Demolish</span>
<p>
Explorer character to set Minor Characters in his retinue to work demolishing at their current location. (Takes place after movement phase, so possibly different to where they were at the start of turn). 
</p>
Note

1. Won’t work if there are not enough Minor Characters in the Major Characters retinue.
2. Deserts and Plains cannot be demolished.
3. This order will fail is Major Character has perished in the ‘Discorporation’ or ‘Grim Reaper’ phases. Also if the Character is a Count who has fallen asleep, then the order will fail.
4. Any Major Character may issue this order.
5. Several locations such as for example, a Church cannot be demolished in one hit, but will be downgraded to a less imposing structure, a Temple. Table below gives this and other examples.
       
<table style="table-layout: fixed; width: 50%">

<tr>
  <td style="width: 25%" colspan= "2" ><h4>Demolition</h4></td>
</tr>
<tr>
  <td ><h4>Before</h4></td><td><h4>After</h4></td>
</tr>


  <tr><td>Church</td><td>Temple</td></tr>
  <tr><td>* Desert</td><td>Desert</td></tr>
  <tr><td>Fort</td><td>Temple</td></tr>

  <tr><td>Garden</td><td>Desert</td></tr>
  <tr><td>Jungle</td><td>Woods</td></tr>
  <tr><td>Labs</td><td>Scrapyard</td></tr>

  <tr><td>Mall</td><td>Scrapyard</td></tr>
  <tr><td>* Plain</td><td>Plain</td></tr>
  <tr><td>Scrapyard</td><td>Plain</td></tr>

  <tr><td>Woods</td><td>Garden</td></tr>
  <tr><td>Temple</td><td>Scrapyard</td></tr>
  

</table>

			Key: * – No change after demolition



<h4 id="p16"><span style="background-color: #FFFF00">Page 16.</span></h4>

<h4 id="leech">Leech Order</h4>
<p>
(Available to all Majors except Count)</p><p>
The Major Character(MC) will open his veins to revive a sleeping Count, his health will deteriorate by 10% and the count will receive an equivalent boost.</p><p>  
If the MC has less than 10% then the Count will receive a lesser amount and the MC will perish.  </p><p>
The Count at the location will revive but not before all leech orders from all Majors have been processed.  </p><p>
Note, the Major Characters will have the opportunity to move away before the following turns Bloodfeast phase. (As this happens after the movement phase).  
</p><p>
Example:-
<span style="background-color: #00FFFF">Ploughman Leech Count Vlaad</span>
</p><p>
Ploughman character to leech his veins to revive the Count character of house Vlaad.
</p>
<p>
Note

1. Two or more characters may perform leeching to ensure the count is stronger.
2. An individual character may be ordered to perform leeching more than once. So the example order above, could have been issued up to three times (the max number of orders allowed, assuming the Ploughman didn’t have to move there in the same turn.)
3. If the house is omitted from the leech order it is assumed to reference the Count belonging to the MC’s house.
4. Counts are not permitted to a donor to/reviver of another Count. 
</p>

<h4 id="move">Move Order</h4>
(Available to all Majors)
The Major Character(MC) move to an adjoining location.
Two examples are shown below they are equivalent and either form is acceptable.

Examples:-
- <span style="background-color: #00FFFF">Shaman move 1</span> The Shaman will move in direction 1, at a bearing of 60°to the next location.
- <span style="background-color: #00FFFF">Shaman move EC</span> The Shaman will move to location EC.
<p>
The second example is equivalent to the first if the Shaman’s start location is ED.
</p><p>
The format for the first example takes a number between <span style="background-color: #00FFFF">  1 </span> and <span style="background-color: #00FFFF">  6 </span> (inclusive) as its final parameter this corresponds to the six directions available.
Whilst the format for the second form takes any one of the 42 location designations as shown in the Map section on page 12. Examples include
<span style="background-color: #00FFFF"> AA, DC, AE, CG, EC </span> and <span style="background-color: #00FFFF"> GF </span>, etc.
</p>

<h4 id="p17"><span style="background-color: #FFFF00"> Page 17. </span></h4>



<h4 id="raze">Raze Order</h4>
(Available to all Majors)
Similar to Demolish Order discussed above.


<h4 id="recruit">Recruit Order</h4>

<h4 id="p18"><span style="background-color: #FFFF00">Page 18.</span></h4>

<h4 id="stake">Stake Order</h4>


<h4 id="mcr">Minor Character Recruitment</h4>

<h4 id="p19"><span style="background-color: #FFFF00">Page 19.</span></h4>

<h4 id="rally">Rallying</h4>


<h4 id="discor">Discorporation</h4>


<h4 id="blood">BloodFeast</h4>


<h4 id="grim">Grim Reaper</h4>

<h4 id="p20"><span style="background-color: #FFFF00">Page 20.</span></h4>

<h4 id="cata">Cataleptic Sleep</h4>


<h4 id="spy">Spying</h4>


<h4 id="comb">Combat Resolution</h4>

<h4 id="p21"><span style="background-color: #FFFF00">Page 21.</span></h4>

<h4 id="casu">Casualties</h4>


<h4 id="ccp">Computer Controlled Positions</h4>

<h4 id="p22"><span style="background-color: #FFFF00">Page 22.</span></h4>

<h4 id="league">League Tables</h4>


<h4 id="win">Winning a Game of Wyrmbayn</h4>


<h4 id="coo">Change of Ownership</h4>


<h4 id="diplo">Diplomacy</h4>


<h4 id="p23"><span style="background-color: #FFFF00">Page 23.</span></h4>

<h4 id="appen"></h4>

## Appendix.

### 1. Saturation Level of 'Ruins' Terrain Type 

'Ruins' terrain types are re-populated by random migrations of Minor Characters from
adjoining locations. The Saturation level for a particular Minor Type is a maximum population level (or cut-off point) that the particular type can grow to. For example, if a migration of say 18K Greenmen to the ruined location brings the population to more than 32.4K, say to a total 36K, then the excess will be immediately discounted and the population will be reduced back down its 'Saturation Level' of 32.4K.

'Saturation' levels for 'Ruins' terrains are similar to 'Density' levels for other terrain types. The different terminology is used because the 'Density' level is also related to the initial 'turn one' population for terrains other than 'Ruins' or 'Plains'.

#### Saturation levels for <mark>'Ruins'</mark> terrain types are given in the table below:

|Minor Type    |Saturation Level|Minor Type    |Saturation Level|Minor Type    |Saturation Level|
|:------------:|:--------------:|:------------:|:--------------:|:------------:|:--------------:|
| Androids     | 3.6K           | Mummies      | 10.8K          | Tar Babies   | 35.1K          | 
| Corn Dollies | 147.6K         | Odd Bods     | 27K            | Tinmen       | 18K            | 
| Demons       | 18K            | Puppets      | 45.9K          | Triffids     | 46.8K          | 
| Gargoyles    | 6.3K           | Robots       | 8.1K           | Vampires     | 1.8K           | 
| Greenmen     | 32.4K          | Scarecrows   | 96.3K          | Werewolves   | 10.8K          | 
| Homunculli   | 74.7K          | Skeletons    | 36.9K          | Zombies      | 20.7K          |  
| Manikins     | 18.9K          |              |                |              |                |


### 2. Reinforcement of 'Ruins' Terrain Type

Reinforcement of the 'Ruins' terrain type is by migration from the surrounding adjoining terrain types, which may total five or six. Note that no migration from a 'Plains' terrain type is possible because those types are devoid of native Minor Characters.
Random factors are used using simulated die rolls from D6, D8, D10, D12 and D20s. 

Note, these migrations have no effect on the population level of the donor locations - this may annoy the purests but its not worth the extra book keeping and complications.
Migration is possible from the following adjacent locations:- Church, Desert, Fort, Garden, Jungle, Labs, Mall, other Ruins, Scrapyards, Temples and Woods.

#### Tables for the different terrain types are given below:-

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “CHURCH” TERRAIN 
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D8    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : CHURCH 

 | DIE ROLL (D8)  |  Type           |  Number  | DIE ROLL (D8)  |  Type           |  Number  |  
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|
 |   1             |  Corn Dollies   |   84K    |   5             |  Odd Bods       |   8K     | 
 |   2             |  Corn Dollies   |   84K    |   6             |  Skeletons      |   36K    |  
 |   3             |  Gargoyles      |   4K     |   7             |  Triffids       |   12K    |   
 |   4             |  Greenmen       |   8K     |   8             |  Zombies        |   12K    | 
 
---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “DESERT” TERRAIN
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D8    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : DESERT  

 | DIE ROLL (D8)  |  Type           |  Number  | DIE ROLL (D8)  |  Type           |  Number  |  
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:| 
 |  1              |Demons           |    6K    |  5              |Homunculli       |    14K     |
 |  2              |Gargoyles        |    2K    |  6              |Mummies          |    24K     | 
 |  3              |Homunculli       |    14K   |  7              |Odd Bods         |    12K     |
 |  4              |Homunculli       |    14K   |  8              |Skeletons        |    10K     |

---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “FORT” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D8    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : FORT  

 | DIE ROLL (D8)  |  Type      |  Number  | DIE ROLL (D8)  |  Type      |  Number  | 
 |:---------------:|:----------:|:--------:|:---------------:|:----------:|:--------:|  
 |  1              |Gargoyles   |    4K     |  5             |Tinmen      |    9K    |
 |  2              |Greenmen    |    14K    |  6             |Triffids    |    16K   |
 |  3              |Odd Bods    |    12K    |  7             |Vampires    |    4K    |
 |  4              |Tinmen      |    9K     |  8             |Werewolves  |    8K    |
 

---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “GARDEN” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D8    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : GARDEN 

 | DIE ROLL (D8)  |  Type           |  Number  | DIE ROLL (D8)  |  Type           |  Number  |   
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|   
 | 1   | Corn Dollies   | 56K | 5   | Scarecrows     | 42K |
 | 2   | Corn Dollies   | 56K | 6   | Tar Babies     | 30K |
 | 3   | Greenmen       | 14K | 7   | Triffids       | 12K | 
 | 4   | Scarecrows     | 42K | 8   | Werewolves     | 2K  | 

--- 

##### RANDOM MIGRATION TO THE”RUINS” TERRAIN FROM AN ADJOINING “JUNGLE” TERRAIN   
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D10    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM: JUNGLE 

 | DIE ROLL (D10)  |  Type           |  Number  | DIE ROLL (D10)  |  Type           |  Number  |   
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|   
 | 1   | Demons         | 8K  | 6   | Robots         | 3K |
 | 2   | Greenmen       | 18K | 7   | Scarecrows     | 40K |
 | 3   | Homunculli     | 26K | 8   | Tar Babies     | 15K | 
 | 4   | Homunculli     | 26K | 9   | Triffids       | 24K | 
 | 5   | Odd Bods       | 15K | 10  | Zombies        | 24K |

---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “LABS” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D8    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : LABS   

 | DIE ROLL (D8)  |  Type           |  Number  | DIE ROLL (D8)  |  Type           |  Number  |   
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|   
 | 1   | Androids         | 2K  | 5   | Puppets      | 18K |
 | 2   | Homunculli       | 21K | 6   | Robots       | 8K  |
 | 3   | Homunculli       | 21K | 7   | Tinmen       | 4K  | 
 | 4   | Odd Bods         | 8K  | 8   | Triffids     | 12K | 
 
---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “MALL” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D6   
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : MALL  

 | DIE ROLL (D6)  |  Type           |  Number  | DIE ROLL (D6)  |  Type           |  Number  |   
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|   
 | 1   | Androids         | 2K  | 4   | Puppets       | 18K |
 | 2   | Manikins         | 16K | 5   | Puppets       | 18K |
 | 3   | Manikins         | 16K | 6   | Zombies       | 5K | 
 
---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “RUINS” TERRAIN   
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D20    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : RUINS   

 | DIE ROLL (D20)  |  Type      |  Number  | DIE ROLL (D20)  |  Type      |  Number  | 
 |:---------------:|:----------:|:--------:|:---------------:|:----------:|:--------:|  
 |  1              |Androids    |    2K    |  11             |Puppets     |    26K   |
 |  2              |Corn Dollies|    41K   |  12             |Robots      |    5K    |
 |  3              |Corn Dollies|    41K   |  13             |Scarecrows  |    54K   |
 |  4              |Demons      |    10K   |  14             |Skeletons   |    21K   |
 |  5              |Gargoyles   |    4K    |  15             |Tar Babies  |    20K   |
 |  6              |Greenmen    |    18K   |  16             |Tinmen      |    10K   |
 |  7              |Homunculli  |    42K   |  17             |Triffids    |    26K   |
 |  8              |Manikins    |    11K   |  18             |Vampires    |    1K    |
 |  9              |Mummies     |    6K    |  19             |Werewolves  |    6K    |
 |  10             |Odd Bods    |    15K   |  20             |Zombies     |    12K   |

---

##### RANDOM MIGRATION TO THE”RUINS” TERRAIN FROM AN ADJOINING “SCRAPYARD” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D10    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM: SCRAPYARD

 | DIE ROLL (D10)  |  Type      |  Number  | DIE ROLL (D10)  |  Type      |  Number  | 
 |:---------------:|:----------:|:--------:|:---------------:|:----------:|:--------:|  
 |  1              |Androids    |    3K    |  6             |Scarecrows  |    40K   |
 |  2              |Homunculli  |    25K   |  7             |Tar Babies  |    15K   |
 |  3              |Odd Bods    |    10K   |  8             |Tinmen      |    23K   |
 |  4              |Puppets     |    23K   |  9             |Triffids    |    15K   |
 |  5              |Robots      |    8K    |  10            |Werewolves  |    8K    |
 
---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “TEMPLE” TERRAIN.   
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D12    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : TEMPLE   

| DIE ROLL (D12)  |  Type      |  Number  | DIE ROLL (D12)  |  Type      |  Number  | 
 |:---------------:|:----------:|:--------:|:---------------:|:----------:|:--------:|  
 |  1              |Corn Dollies|    24K   |  7              |Skeletons   |    18K   |
 |  2              |Corn Dollies|    24K   |  8              |Skeletons   |    18K   |
 |  3              |Corn Dollies|    24K   |  9              |Skeletons   |    18K   |
 |  4              |Demons      |    24K   |  10             |Triffids    |    18K   |
 |  5              |Gargoyles   |    6K    |  11             |Zombies     |    9K    |
 |  6              |Greenmen    |    12K   |  12             |Zombies     |    9K    |

---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “WOODS” TERRAIN.   
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D12    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : WOODS   

| DIE ROLL (D12)  |  Type      |  Number  | DIE ROLL (D12)  |  Type      |  Number  | 
 |:---------------:|:----------:|:--------:|:---------------:|:----------:|:--------:|  
 |  1              |Androids    |    3K   |  7              |Scarecrows   |    33K   |
 |  2              |Demons      |    18K  |  8              |Scarecrows   |    33K   |
 |  3              |Greenmen    |    21K  |  9              |Scarecrows   |    33K   |
 |  4              |Homunculii  |    30K  |  10             |Tar Babies   |    36K   |
 |  5              |Puppets     |    27K  |  11             |Triffids     |    18K   |
 |  6              |Robots      |    3K   |  12             |Werewolves   |    12K   |

---




### 3. Firestarters' and Demolishers' Reports for various terrains. 

### Church                   
                    
- ### Firestarters’ Report ###  

| Minor Character | Required Number per Fire Crew | Individual Survivability  | Individual Chance of Perishing  | 'Save’ Roll – Min Die Roll 1-100 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 6 | 99 %  | 1 % | 2 |
| Corn Dollies  | 203 | 97 %  | 3 % | 4 |
| Demons  | 51  | 100 % | 0 % | Not Required  |
| Gargoyles | 14  | 100 % | 0 % | Not Required  |
| Greenmen  | 34  | 95 %  | 5 % | 6 |
| Homunculli  | 68  | 95 %  | 5 % | 6 |
| Manikins  | 51  | 97 %  | 3 % | 4 |
| Mummies | 37  | 97 %  | 3 % | 4 |
| Odd Bods  | 25  | 95 %  | 5 % | 6 |
| Puppets | 81  | 97 %  | 3 % | 4 |
| Robots  | 13  | 99 %  | 1 % | 2 |
| Scarecrows  | 116 | 97 %  | 3 % | 4 |
| Skeletons | 41  | 98 %  | 2 % | 3 |
| Tar Babies  | 135 | 96 %  | 4 % | 5 |
| Tin Men | 35  | 95 %  | 5 % | 6 |
| Triffids  | 162 | 96 %  | 4 % | 5 |
| Vampires  | 14  | 98 %  | 2 % | 3 |
| Werewolves  | 15  | 95 %  | 5 % | 6 |
| Zombies | 20  | 99 %  | 1 % | 2 |

- Number of crews for a guaranteed total burn = **44** (from an undamaged state).

| CHURCH: {Raze} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 2 |           
| 2 | 2 |           
| 3 | 2 |           
| 4 | 2 |           
| 5 | 4 |           
| 6 | 15  |           
                    
Percentage destruction is given by rolling a modified D6 as specified for each Fire Crew, adding the results and rounding down to the nearest 5%.                   
                    
Afterwards each Fire Crew member must roll a D100 to check for accidental death (due to heat, smoke and fire), (Demons and Gargoyles exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 203 Corn Dollies to make just one fire crew. (Expect about 6 of which will perish to fire damage).


- ### Demolishers’ Report ###                   
                    
| Minor Character | Required Number per Demolish Crew | Survival Rate per Thousand  | Individual Chance of Perishing (per 1000) | 'Save’ Roll – Min Dice Roll 1 – 1000 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 600 | 1000  | 0 | Not Required  |
| Corn Dollies  |  5.01K  | 975 | 25‰ | 26  |
| Demons  |  6.01K  | 1000  | 0 | Not Required  |
| Gargoyles |  1.67K  | 1000  | 0 | Not Required  |
| Greenmen  |  1.67K  | 998 | 2‰  | 3 |
| Homunculli  |  5.01K  | 996 | 4‰  | 5 |
| Manikins  |  2.5K   | 996 | 4‰  | 5 |
| Mummies |  1.88K  | 997 | 3‰  | 4 |
| Odd Bods  |  2.4K   | 999 | 1‰  | 2 |
| Puppets |  3.76K  | 997 | 3‰  | 4 |
| Robots  |  1.25K  | 1000  | 0 | Not Required  |
| Scarecrows  |  6.01K  | 994 | 6‰  | 7 |
| Skeletons |  4.01K  | 996 | 4‰  | 5 |
| Tar Babies  |  3.34K  | 996 | 4‰  | 5 |
| Tin Men |  4.29K  | 1000  | 0 | Not Required  |
| Triffids  |  7.51K  | 1000  | 0 | Not Required  |
| Vampires  |  1K   | 999 | 1‰  | 2 |
| Werewolves  |  1.43K  | 999 | 1‰  | 2 |
| Zombies |  1.5K   | 998 | 2‰  | 3 |

- Number of crews for a guaranteed total demolition = **30** (from an undamaged state).

| CHURCH: {DEMOLISH} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  | 
| 1 | 1.49  | 
| 2 | 2.89  | 
| 3 | 4.3 |
| 4 | 5.7 |
| 5 | 7.11  |
| 6 | 8.51  |

Percentage destruction is given by rolling a modified D6 as specified for each Demolish Crew, adding the results and rounding down to the nearest 5%.

Afterwards each Demolish Crew member must roll a D1000 to check for accidental death (due to slips, trips and falls), (Androids, Demons, Gargoyles, Robots, Tin men and Triffids exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 6.01K Scarecrows to make just one demolish crew. (Expect about 36 of which will perish to accidents).

---

### Desert 

- ### Firestarters' Report ###

  - Deserts can't be set alight.

- ### Demolishers' Report ###

  - Deserts can't be demolished.
---

### Fort 
                  
- ### Firestarters' Report ###

| Minor Character | Required Number per Fire Crew | Individual Survivability  | Individual Chance of Perishing  | 'Save’ Roll – Min Die Roll 1-100 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 122 | 99 %  | 1 % | 2 |
| Corn Dollies  | 4091  | 97 %  | 3 % | 4 |
| Demons  | 1023  | 100 % | 0 % | Not Required  |
| Gargoyles | 273 | 100 % | 0 % | Not Required  |
| Greenmen  | 683 | 95 %  | 5 % | 6 |
| Homunculli  | 1364  | 95 %  | 5 % | 6 |
| Manikins  | 1023  | 97 %  | 3 % | 4 |
| Mummies | 744 | 97 %  | 3 % | 4 |
| Odd Bods  | 497 | 95 %  | 5 % | 6 |
| Puppets | 1639  | 97 %  | 3 % | 4 |
| Robots  | 256 | 99 %  | 1 % | 2 |
| Scarecrows  | 2341  | 97 %  | 3 % | 4 |
| Skeletons | 820 | 98 %  | 2 % | 3 |
| Tar Babies  | 2721  | 96 %  | 4 % | 5 |
| Tin Men | 702 | 95 %  | 5 % | 6 |
| Triffids  | 3268  | 96 %  | 4 % | 5 |
| Vampires  | 273 | 98 %  | 2 % | 3 |
| Werewolves  | 293 | 95 %  | 5 % | 6 |
| Zombies | 410 | 99 %  | 1 % | 2 |
                    
- Number of crews for a guaranteed total burn = **49** (from an undamaged state).

| FORT: {Raze} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 2 |           
| 2 | 2 |           
| 3 | 2 |           
| 4 | 2 |           
| 5 | 2.2 |           
| 6 | 16.8  |           
                    
Percentage destruction is given by rolling a modified D6 as specified for each Fire Crew, adding the results and rounding down to the nearest 5%.                   
                    
Afterwards each Fire Crew member must roll a D100 to check for accidental death (due to heat, smoke and fire), (Demons and Gargoyles exempt).                   
                    
Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 410 Zombies to make just one fire crew. (Expect about 4 of which will perish to fire damage).                   

- ### Demolishers’ Report ###                   
                    
| Minor Character | Required Number per Demolish Crew | Survival Rate per Thousand  | Individual Chance of Perishing (per 1000) | 'Save’ Roll – Min Dice Roll 1 – 1000 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 740 | 1000  | 0 | Not Required  |
| Corn Dollies  |  6.14K  | 975 | 25‰ | 26  |
| Demons  |  7.37K  | 1000  | 0 | Not Required  |
| Gargoyles |  2.05K  | 1000  | 0 | Not Required  |
| Greenmen  |  2.05K  | 998 | 2‰  | 3 |
| Homunculli  |  6.14K  | 996 | 4‰  | 5 |
| Manikins  |  3.07K  | 996 | 4‰  | 5 |
| Mummies |  2.3K   | 997 | 3‰  | 4 |
| Odd Bods  |  2.95K  | 999 | 1‰  | 2 |
| Puppets |  4.61K  | 997 | 3‰  | 4 |
| Robots  |  1.54K  | 1000  | 0 | Not Required  |
| Scarecrows  |  7.37K  | 994 | 6‰  | 7 |
| Skeletons |  4.91K  | 996 | 4‰  | 5 |
| Tar Babies  |  4.1K   | 996 | 4‰  | 5 |
| Tin Men |  5.27K  | 1000  | 0 | Not Required  |
| Triffids  |  9.22K  | 1000  | 0 | Not Required  |
| Vampires  |  1.23K  | 999 | 1‰  | 2 |
| Werewolves  |  1.76K  | 999 | 1‰  | 2 |
| Zombies |  1.84K  | 998 | 2‰  | 3 |

- Number of crew for a guaranteed total demolition = ** 32 ** (from an undamaged state.)

| FORT: {DEMOLISH} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 0.85  |           
| 2 | 2.51  |           
| 3 | 4.17  |           
| 4 | 5.83  |           
| 5 | 7.49  |           
| 6 | 9.15  |

Percentage destruction is given by rolling a modified D6 as specified for each Demolish Crew, adding the results and rounding down to the nearest 5%.                   

Afterwards each Demolish Crew member must roll a D1000 to check for accidental death (due to slips, trips and falls), (Androids, Demons, Gargoyles, Robots, Tin men and Triffids exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 2.05K Greenmen to make just one demolish crew. (Expect about 4 of which will perish to accidents).                    

---

### Garden                    
                    
- ### Firestarters’ Report ###                    
| Minor Character | Required Number per Fire Crew | Individual Survivability  | Individual Chance of Perishing  | 'Save’ Roll – Min Die Roll 1-100 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 1 | 99 %  | 1 % | 2 |
| Corn Dollies  | 41  | 97 %  | 3 % | 4 |
| Demons  | 10  | 100 % | 0 % | Not Required  |
| Gargoyles | 3 | 100 % | 0 % | Not Required  |
| Greenmen  | 7 | 95 %  | 5 % | 6 |
| Homunculli  | 14  | 95 %  | 5 % | 6 |
| Manikins  | 10  | 97 %  | 3 % | 4 |
| Mummies | 7 | 97 %  | 3 % | 4 |
| Odd Bods  | 5 | 95 %  | 5 % | 6 |
| Puppets | 16  | 97 %  | 3 % | 4 |
| Robots  | 3 | 99 %  | 1 % | 2 |
| Scarecrows  | 23  | 97 %  | 3 % | 4 |
| Skeletons | 8 | 98 %  | 2 % | 3 |
| Tar Babies  | 27  | 96 %  | 4 % | 5 |
| Tin Men | 7 | 95 %  | 5 % | 6 |
| Triffids  | 33  | 96 %  | 4 % | 5 |
| Vampires  | 3 | 98 %  | 2 % | 3 |
| Werewolves  | 3 | 95 %  | 5 % | 6 |
| Zombies | 4 | 99 %  | 1 % | 2 |

- Number of crews for a guaranteed total burn = **35** (from an undamaged state).

| GARDEN: {Raze} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 2 |           
| 2 | 2 |           
| 3 | 2 |           
| 4 | 4.2 |           
| 5 | 8.4 |           
| 6 | 8.4 |           
                    
Percentage destruction is given by rolling a modified D6 as specified for each Fire Crew, adding the results and rounding down to the nearest 5%.                   
                    
Afterwards each Fire Crew member must roll a D100 to check for accidental death (due to heat, smoke and fire), (Demons and Gargoyles exempt).                   
                    
Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 41 Corn Dollies to make just one fire crew. (Expect about 1 of which to perish to fire damage i.e. approximately 3%).

- ### Demolishers’ Report ###                   
                    
| Minor Character | Required Number per Demolish Crew | Survival Rate per Thousand  | Individual Chance of Perishing (per 1000) | 'Save’ Roll – Min Dice Roll 1 – 1000 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 120 | 1000  | 0 | Not Required  |
| Corn Dollies  | 970 | 975 | 25‰ | 26  |
| Demons  |  1.17K  | 1000  | 0 | Not Required  |
| Gargoyles | 330 | 1000  | 0 | Not Required  |
| Greenmen  | 330 | 998 | 2‰  | 3 |
| Homunculli  | 970 | 996 | 4‰  | 5 |
| Manikins  | 490 | 996 | 4‰  | 5 |
| Mummies | 370 | 997 | 3‰  | 4 |
| Odd Bods  | 470 | 999 | 1‰  | 2 |
| Puppets | 730 | 997 | 3‰  | 4 |
| Robots  | 240 | 1000  | 0 | Not Required  |
| Scarecrows  |  1.17K  | 994 | 6‰  | 7 |
| Skeletons | 780 | 996 | 4‰  | 5 |
| Tar Babies  | 650 | 996 | 4‰  | 5 |
| Tin Men | 840 | 1000  | 0 | Not Required  |
| Triffids  |  1.46K  | 1000  | 0 | Not Required  |
| Vampires  | 200 | 999 | 1‰  | 2 |
| Werewolves  | 280 | 999 | 1‰  | 2 |
| Zombies | 290 | 998 | 2‰  | 3 |

- Number of crews for a guaranteed total demolition = **29** (from an undamaged state).

| GARDEN: {DEMOLISH} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 1.76  |           
| 2 | 3.06  |           
| 3 | 4.35  |           
| 4 | 5.65  |           
| 5 | 6.94  |           
| 6 | 8.24  |

Percentage destruction is given by rolling a modified D6 as specified for each Demolish Crew, adding the results and rounding down to the nearest 5%.                   

Afterwards each Demolish Crew member must roll a D1000 to check for accidental death (due to slips, trips and falls), (Androids, Demons, Gargoyles, Robots, Tin men and Triffids exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 970 Corn Dollies to make just one demolish crew. (Expect about 24 of which will perish to accidents).

---

### Jungle                    
                    
- ### Firestarters’ Report ###

| Minor Character | Required Number per Fire Crew | Individual Survivability  | Individual Chance of Perishing  | 'Save’ Roll – Min Die Roll 1-100 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 1 | 99 %  | 1 % | 2 |
| Corn Dollies  | 33  | 97 %  | 3 % | 4 |
| Demons  | 8 | 100 % | 0 % | Not Required  |
| Gargoyles | 2 | 100 % | 0 % | Not Required  |
| Greenmen  | 6 | 95 %  | 5 % | 6 |
| Homunculli  | 11  | 95 %  | 5 % | 6 |
| Manikins  | 8 | 97 %  | 3 % | 4 |
| Mummies | 6 | 97 %  | 3 % | 4 |
| Odd Bods  | 4 | 95 %  | 5 % | 6 |
| Puppets | 13  | 97 %  | 3 % | 4 |
| Robots  | 2 | 99 %  | 1 % | 2 |
| Scarecrows  | 19  | 97 %  | 3 % | 4 |
| Skeletons | 7 | 98 %  | 2 % | 3 |
| Tar Babies  | 22  | 96 %  | 4 % | 5 |
| Tin Men | 6 | 95 %  | 5 % | 6 |
| Triffids  | 27  | 96 %  | 4 % | 5 |
| Vampires  | 2 | 98 %  | 2 % | 3 |
| Werewolves  | 2 | 95 %  | 5 % | 6 |
| Zombies | 3 | 99 %  | 1 % | 2 |

- Number of crews for a guaranteed total burn = **32** (from an undamaged state).

| JUNGLE: {Raze} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 2 |           
| 2 | 2 |           
| 3 | 4 |           
| 4 | 6 |           
| 5 | 6 |           
| 6 | 7 |           
                    
Percentage destruction is given by rolling a modified D6 as specified for each Fire Crew, adding the results and rounding down to the nearest 5%.                   
                    
Afterwards each Fire Crew member must roll a D100 to check for accidental death (due to heat, smoke and fire), (Demons and Gargoyles exempt).                   
                    
Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 33 Corn Dollies to make just one fire crew. (Expect about 1 of which to perish to fire damage i.e. approximately 3%)

- ### Demolishers’ Report ###                   
                    
| Minor Character | Required Number per Demolish Crew | Survival Rate per Thousand  | Individual Chance of Perishing (per 1000) | 'Save’ Roll – Min Dice Roll 1 – 1000 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 510 | 1000  | 0 | Not Required  |
| Corn Dollies  |  4.27K  | 975 | 25‰ | 26  |
| Demons  |  5.12K  | 1000  | 0 | Not Required  |
| Gargoyles |  1.42K  | 1000  | 0 | Not Required  |
| Greenmen  |  1.42K  | 998 | 2‰  | 3 |
| Homunculli  |  4.27K  | 996 | 4‰  | 5 |
| Manikins  |  2.14K  | 996 | 4‰  | 5 |
| Mummies |  1.6K   | 997 | 3‰  | 4 |
| Odd Bods  |  2.05K  | 999 | 1‰  | 2 |
| Puppets |  3.2K   | 997 | 3‰  | 4 |
| Robots  |  1.07K  | 1000  | 0 | Not Required  |
| Scarecrows  |  5.12K  | 994 | 6‰  | 7 |
| Skeletons |  3.42K  | 996 | 4‰  | 5 |
| Tar Babies  |  2.85K  | 996 | 4‰  | 5 |
| Tin Men |  3.66K  | 1000  | 0 | Not Required  |
| Triffids  |  6.4K   | 1000  | 0 | Not Required  |
| Vampires  | 850 | 999 | 1‰  | 2 |
| Werewolves  |  1.22K  | 999 | 1‰  | 2 |
| Zombies |  1.28K  | 998 | 2‰  | 3 |

- Number of crews for a guaranteed total demolition = **30** (from an undamaged state).

| JUNGLE: {DEMOLISH} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  | 
| 1 | 1.44  | 
| 2 | 2.86  | 
| 3 | 4.29  | 
| 4 | 5.71  | 
| 5 | 7.14  | 
| 6 | 8.56  |

Percentage destruction is given by rolling a modified D6 as specified for each Demolish Crew, adding the results and rounding down to the nearest 5%.

Afterwards each Demolish Crew member must roll a D1000 to check for accidental death (due to slips, trips and falls), (Androids, Demons, Gargoyles, Robots, Tin men and Triffids exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 1.6K Mummies to make just one demolish crew. (Expect about 5 of which will perish to accidents).

---

### Labs                    

- ### Firestarters’ Report ###

| Minor Character | Required Number per Fire Crew | Individual Survivability  | Individual Chance of Perishing  | 'Save’ Roll – Min Die Roll 1-100 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 4 | 99 %  | 1 % | 2 |
| Corn Dollies  | 136 | 97 %  | 3 % | 4 |
| Demons  | 34  | 100 % | 0 % | Not Required  |
| Gargoyles | 9 | 100 % | 0 % | Not Required  |
| Greenmen  | 23  | 95 %  | 5 % | 6 |
| Homunculli  | 45  | 95 %  | 5 % | 6 |
| Manikins  | 34  | 97 %  | 3 % | 4 |
| Mummies | 25  | 97 %  | 3 % | 4 |
| Odd Bods  | 17  | 95 %  | 5 % | 6 |
| Puppets | 55  | 97 %  | 3 % | 4 |
| Robots  | 9 | 99 %  | 1 % | 2 |
| Scarecrows  | 78  | 97 %  | 3 % | 4 |
| Skeletons | 27  | 98 %  | 2 % | 3 |
| Tar Babies  | 91  | 96 %  | 4 % | 5 |
| Tin Men | 23  | 95 %  | 5 % | 6 |
| Triffids  | 109 | 96 %  | 4 % | 5 |
| Vampires  | 9 | 98 %  | 2 % | 3 |
| Werewolves  | 10  | 95 %  | 5 % | 6 |
| Zombies | 14  | 99 %  | 1 % | 2 |

- Number of crews for a guaranteed total burn = **34** (from an undamaged state).

| LABS: {Raze} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 2 |           
| 2 | 2 |           
| 3 | 2 |           
| 4 | 6.4 |           
| 5 | 7 |           
| 6 | 7.6 |           
                    
Percentage destruction is given by rolling a modified D6 as specified for each Fire Crew, adding the results and rounding down to the nearest 5%.                   
                    
Afterwards each Fire Crew member must roll a D100 to check for accidental death (due to heat, smoke and fire), (Demons and Gargoyles exempt).                   
                    
Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 136 Corn Dollies to make just one fire crew. (Expect about 4 of which will perish to fire damage i.e. approximately 3%).

- ### Demolishers’ Report ###                   
                    
| Minor Character | Required Number per Demolish Crew | Survival Rate per Thousand  | Individual Chance of Perishing (per 1000) | 'Save’ Roll – Min Dice Roll 1 – 1000 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 190 | 1000  | 0 | Not Required  |
| Corn Dollies  |  1.61K  | 975 | 25‰ | 26  |
| Demons  |  1.93K  | 1000  | 0 | Not Required  |
| Gargoyles | 540 | 1000  | 0 | Not Required  |
| Greenmen  | 540 | 998 | 2‰  | 3 |
| Homunculli  |  1.61K  | 996 | 4‰  | 5 |
| Manikins  | 800 | 996 | 4‰  | 5 |
| Mummies | 600 | 997 | 3‰  | 4 |
| Odd Bods  | 770 | 999 | 1‰  | 2 |
| Puppets |  1.21K  | 997 | 3‰  | 4 |
| Robots  | 400 | 1000  | 0 | Not Required  |
| Scarecrows  |  1.93K  | 994 | 6‰  | 7 |
| Skeletons |  1.29K  | 996 | 4‰  | 5 |
| Tar Babies  |  1.07K  | 996 | 4‰  | 5 |
| Tin Men |  1.38K  | 1000  | 0 | Not Required  |
| Triffids  |  2.41K  | 1000  | 0 | Not Required  |
| Vampires  | 320 | 999 | 1‰  | 2 |
| Werewolves  | 460 | 999 | 1‰  | 2 |
| Zombies | 480 | 998 | 2‰  | 3 |

- Number of crews for a guaranteed total demolition = **32** (from an undamaged state).

| LABS: {DEMOLISH} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 0.84  |           
| 2 | 2.5 |           
| 3 | 4.17  |           
| 4 | 5.83  |           
| 5 | 7.5 |           
| 6 | 9.16  |           

Percentage destruction is given by rolling a modified D6 as specified for each Demolish Crew, adding the results and rounding down to the nearest 5%.                   

Afterwards each Demolish Crew member must roll a D1000 to check for accidental death (due to slips, trips and falls), (Androids, Demons, Gargoyles, Robots, Tin men and Triffids exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 600 Mummies to make just one demolish crew. (Expect about 2 of which will perish to accidents).

---

### Mall                    
                    
- ### Firestarters’ Report ###    

| Minor Character | Required Number per Fire Crew | Individual Survivability  | Individual Chance of Perishing  | 'Save’ Roll – Min Die Roll 1-100 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 1 | 99 %  | 1 % | 2 |
| Corn Dollies  | 41  | 97 %  | 3 % | 4 |
| Demons  | 10  | 100 % | 0 % | Not Required  |
| Gargoyles | 3 | 100 % | 0 % | Not Required  |
| Greenmen  | 7 | 95 %  | 5 % | 6 |
| Homunculli  | 14  | 95 %  | 5 % | 6 |
| Manikins  | 10  | 97 %  | 3 % | 4 |
| Mummies | 7 | 97 %  | 3 % | 4 |
| Odd Bods  | 5 | 95 %  | 5 % | 6 |
| Puppets | 16  | 97 %  | 3 % | 4 |
| Robots  | 3 | 99 %  | 1 % | 2 |
| Scarecrows  | 23  | 97 %  | 3 % | 4 |
| Skeletons | 8 | 98 %  | 2 % | 3 |
| Tar Babies  | 27  | 96 %  | 4 % | 5 |
| Tin Men | 7 | 95 %  | 5 % | 6 |
| Triffids  | 32  | 96 %  | 4 % | 5 |
| Vampires  | 3 | 98 %  | 2 % | 3 |
| Werewolves  | 3 | 95 %  | 5 % | 6 |
| Zombies | 4 | 99 %  | 1 % | 2 |

- Number of crews for a guaranteed total burn = **44** (from an undamaged state).

| MALL: {Raze} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 2 |           
| 2 | 2 |           
| 3 | 2 |           
| 4 | 2 |           
| 5 | 3.7 |           
| 6 | 15.3  |           
                    
Percentage destruction is given by rolling a modified D6 as specified for each Fire Crew, adding the results and rounding down to the nearest 5%.                   
                    
Afterwards each Fire Crew member must roll a D100 to check for accidental death (due to heat, smoke and fire), (Demons and Gargoyles exempt).                   
                    
Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 41 Corn Dollies to make just one fire crew. (Expect about 1 of which to perish to fire damage i.e. approximately 3%).

- ### Demolishers’ Report ###                   
                    
| Minor Character | Required Number per Demolish Crew | Survival Rate per Thousand  | Individual Chance of Perishing (per 1000) | 'Save’ Roll – Min Dice Roll 1 – 1000 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 330 | 1000  | 0 | Not Required  |
| Corn Dollies  |  2.78K  | 975 | 25‰ | 26  |
| Demons  |  3.34K  | 1000  | 0 | Not Required  |
| Gargoyles | 930 | 1000  | 0 | Not Required  |
| Greenmen  | 930 | 998 | 2‰  | 3 |
| Homunculli  |  2.78K  | 996 | 4‰  | 5 |
| Manikins  |  1.39K  | 996 | 4‰  | 5 |
| Mummies |  1.04K  | 997 | 3‰  | 4 |
| Odd Bods  |  1.33K  | 999 | 1‰  | 2 |
| Puppets |  2.09K  | 997 | 3‰  | 4 |
| Robots  | 700 | 1000  | 0 | Not Required  |
| Scarecrows  |  3.34K  | 994 | 6‰  | 7 |
| Skeletons |  2.22K  | 996 | 4‰  | 5 |
| Tar Babies  |  1.85K  | 996 | 4‰  | 5 |
| Tin Men |  2.38K  | 1000  | 0 | Not Required  |
| Triffids  |  4.17K  | 1000  | 0 | Not Required  |
| Vampires  | 560 | 999 | 1‰  | 2 |
| Werewolves  | 790 | 999 | 1‰  | 2 |
| Zombies | 830 | 998 | 2‰  | 3 |

- Number of crews for a guaranteed total demolition = **32** (from an undamaged state).

| MALL: {DEMOLISH} D6_Dice_Roll | Modified Number (percent of damage to location) |
| :----------:  | :----------:  | 
| 1 | 0.97  | 
| 2 | 2.58  | 
| 3 | 4.19  | 
| 4 | 5.81  | 
| 5 | 7.42  | 
| 6 | 9.03  | 

Percentage destruction is given by rolling a modified D6 as specified for each Demolish Crew, adding the results and rounding down to the nearest 5%.                   

Afterwards each Demolish Crew member must roll a D1000 to check for accidental death (due to slips, trips and falls), (Androids, Demons, Gargoyles, Robots, Tin men and Triffids exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 2.78K Corn Dollies to make just one demolish crew. (Expect about 70 of which will perish to accidents).                   

---

### Plain 

- ### Firestarters' Report ###

  - Plains can't be set alight.

- ### Demolishers' Report ###

  - Plains can't be demolished.

---

### Ruins 

- ### Firestarters' Report ###

  - Ruins are already destroyed.

- ### Demolishers' Report ###

  - Ruins are already destroyed.

---

### Scrapyard                   
                    
- ### Firestarters’ Report ###                    
                    
| Minor Character | Required Number per Fire Crew | Individual Survivability  | Individual Chance of Perishing  | 'Save’ Roll – Min Die Roll 1-100 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 1 | 99 %  | 1 % | 2 |
| Corn Dollies  | 41  | 97 %  | 3 % | 4 |
| Demons  | 10  | 100 % | 0 % | Not Required  |
| Gargoyles | 3 | 100 % | 0 % | Not Required  |
| Greenmen  | 7 | 95 %  | 5 % | 6 |
| Homunculli  | 14  | 95 %  | 5 % | 6 |
| Manikins  | 10  | 97 %  | 3 % | 4 |
| Mummies | 7 | 97 %  | 3 % | 4 |
| Odd Bods  | 5 | 95 %  | 5 % | 6 |
| Puppets | 16  | 97 %  | 3 % | 4 |
| Robots  | 3 | 99 %  | 1 % | 2 |
| Scarecrows  | 23  | 97 %  | 3 % | 4 |
| Skeletons | 8 | 98 %  | 2 % | 3 |
| Tar Babies  | 27  | 96 %  | 4 % | 5 |
| Tin Men | 7 | 95 %  | 5 % | 6 |
| Triffids  | 33  | 96 %  | 4 % | 5 |
| Vampires  | 3 | 98 %  | 2 % | 3 |
| Werewolves  | 3 | 95 %  | 5 % | 6 |
| Zombies | 4 | 99 %  | 1 % | 2 |

- Number of crews for a guaranteed total burn = **35** (from an undamaged state).                   
                    
| SCRAPYARD: {Raze} D6_Dice_Roll  | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 2 |           
| 2 | 2 |           
| 3 | 2 |           
| 4 | 3.5 |           
| 5 | 7 |           
| 6 | 10.5  |           
                    
Percentage destruction is given by rolling a modified D6 as specified for each Fire Crew, adding the results and rounding down to the nearest 5%.                   
                    
Afterwards each Fire Crew member must roll a D100 to check for accidental death (due to heat, smoke and fire), (Demons and Gargoyles exempt).                   
                    
Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 41 Corn Dollies to make just one fire crew. (Expect about 1 of which to perish to fire damage i.e. approximately 3%).

- ### Demolishers’ Report ###                   
                    
| Minor Character | Required Number per Demolish Crew | Survival Rate per Thousand  | Individual Chance of Perishing (per 1000) | 'Save’ Roll – Min Dice Roll 1 – 1000 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 320 | 1000  | 0 | Not Required  |
| Corn Dollies  |  2.63K  | 975 | 25‰ | 26  |
| Demons  |  3.16K  | 1000  | 0 | Not Required  |
| Gargoyles | 880 | 1000  | 0 | Not Required  |
| Greenmen  | 880 | 998 | 2‰  | 3 |
| Homunculli  |  2.63K  | 996 | 4‰  | 5 |
| Manikins  |  1.32K  | 996 | 4‰  | 5 |
| Mummies | 990 | 997 | 3‰  | 4 |
| Odd Bods  |  1.26K  | 999 | 1‰  | 2 |
| Puppets |  1.98K  | 997 | 3‰  | 4 |
| Robots  | 660 | 1000  | 0 | Not Required  |
| Scarecrows  |  3.16K  | 994 | 6‰  | 7 |
| Skeletons |  2.11K  | 996 | 4‰  | 5 |
| Tar Babies  |  1.76K  | 996 | 4‰  | 5 |
| Tin Men |  2.26K  | 1000  | 0 | Not Required  |
| Triffids  |  3.95K  | 1000  | 0 | Not Required  |
| Vampires  | 530 | 999 | 1‰  | 2 |
| Werewolves  | 750 | 999 | 1‰  | 2 |
| Zombies | 790 | 998 | 2‰  | 3 |

- Number of crews for a guaranteed total demolition = **31** (from an undamaged state).

| SCRAPYARD: {DEMOLISH} D6_Dice_Roll  | Modified Number (percent of damage to location) |
| :----------:  | :----------:  | 
| 1 | 1.25  | 
| 2 | 2.75  | 
| 3 | 4.25  | 
| 4 | 5.75  | 
| 5 | 7.25  | 
| 6 | 8.75  | 

Percentage destruction is given by rolling a modified D6 as specified for each Demolish Crew, adding the results and rounding down to the nearest 5%.

Afterwards each Demolish Crew member must roll a D1000 to check for accidental death (due to slips, trips and falls), (Androids, Demons, Gargoyles, Robots, Tin men and Triffids exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 2.63K Corn Dollies to make just one demolish crew. (Expect about 66 of which will perish to accidents).

---

### Temple                    
                    
- ### Firestarters’ Report ###                    
                    
| Minor Character | Required Number per Fire Crew | Individual Survivability  | Individual Chance of Perishing  | 'Save’ Roll – Min Die Roll 1-100 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 7 | 99 %  | 1 % | 2 |
| Corn Dollies  | 223 | 97 %  | 3 % | 4 |
| Demons  | 56  | 100 % | 0 % | Not Required  |
| Gargoyles | 15  | 100 % | 0 % | Not Required  |
| Greenmen  | 37  | 95 %  | 5 % | 6 |
| Homunculli  | 74  | 95 %  | 5 % | 6 |
| Manikins  | 56  | 97 %  | 3 % | 4 |
| Mummies | 41  | 97 %  | 3 % | 4 |
| Odd Bods  | 27  | 95 %  | 5 % | 6 |
| Puppets | 89  | 97 %  | 3 % | 4 |
| Robots  | 14  | 99 %  | 1 % | 2 |
| Scarecrows  | 128 | 97 %  | 3 % | 4 |
| Skeletons | 45  | 98 %  | 2 % | 3 |
| Tar Babies  | 148 | 96 %  | 4 % | 5 |
| Tin Men | 38  | 95 %  | 5 % | 6 |
| Triffids  | 178 | 96 %  | 4 % | 5 |
| Vampires  | 15  | 98 %  | 2 % | 3 |
| Werewolves  | 16  | 95 %  | 5 % | 6 |
| Zombies | 22  | 99 %  | 1 % | 2 |

- Number of crews for a guaranteed total burn = **40** (from an undamaged state).

| TEMPLE: {Raze} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 2 |           
| 2 | 2 |           
| 3 | 2 |           
| 4 | 2 |           
| 5 | 6.5 |           
| 6 | 12.5  |

Percentage destruction is given by rolling a modified D6 as specified for each Fire Crew, adding the results and rounding down to the nearest 5%.                   
                    
Afterwards each Fire Crew member must roll a D100 to check for accidental death (due to heat, smoke and fire), (Demons and Gargoyles exempt).                   
                    
Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 223 Corn Dollies to make just one fire crew. (Expect about 7 of which to perish to fire damage i.e. approximately 3%)

- ### Demolishers’ Report ###                   
                    
| Minor Character | Required Number per Demolish Crew | Survival Rate per Thousand  | Individual Chance of Perishing (per 1000) | 'Save’ Roll – Min Dice Roll 1 – 1000 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 540 | 1000  | 0 | Not Required  |
| Corn Dollies  |  4.48K  | 975 | 25‰ | 26  |
| Demons  |  5.38K  | 1000  | 0 | Not Required  |
| Gargoyles |  1.49K  | 1000  | 0 | Not Required  |
| Greenmen  |  1.49K  | 998 | 2‰  | 3 |
| Homunculli  |  4.48K  | 996 | 4‰  | 5 |
| Manikins  |  2.24K  | 996 | 4‰  | 5 |
| Mummies |  1.68K  | 997 | 3‰  | 4 |
| Odd Bods  |  2.15K  | 999 | 1‰  | 2 |
| Puppets |  3.36K  | 997 | 3‰  | 4 |
| Robots  |  1.12K  | 1000  | 0 | Not Required  |
| Scarecrows  |  5.38K  | 994 | 6‰  | 7 |
| Skeletons |  3.58K  | 996 | 4‰  | 5 |
| Tar Babies  |  2.99K  | 996 | 4‰  | 5 |
| Tin Men |  3.84K  | 1000  | 0 | Not Required  |
| Triffids  |  6.72K  | 1000  | 0 | Not Required  |
| Vampires  | 900 | 999 | 1‰  | 2 |
| Werewolves  |  1.28K  | 999 | 1‰  | 2 |
| Zombies |  1.34K  | 998 | 2‰  | 3 |

- Number of crews for a guaranteed total demolition = **30** (from an undamaged state).

| TEMPLE: {DEMOLISH} D6_Dice_Roll | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 1.48  |           
| 2 | 2.89  |           
| 3 | 4.3 |           
| 4 | 5.7 |           
| 5 | 7.11  |           
| 6 | 8.52  | 

Percentage destruction is given by rolling a modified D6 as specified for each Demolish Crew, adding the results and rounding down to the nearest 5%.                   
 
Afterwards each Demolish Crew member must roll a D1000 to check for accidental death (due to slips, trips and falls), (Androids, Demons, Gargoyles, Robots, Tin men and Triffids exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 4.48K Corn Dollies to make just one demolish crew. (Expect about 112 of which will perish to accidents).                    

---

### Woods                   
                    
- ### Firestarters’ Report ###                    
| Minor Character | Required Number per Fire Crew | Individual Survivability  | Individual Chance of Perishing  | 'Save’ Roll – Min Die Roll 1-100 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 1 | 99 %  | 1 % | 2 |
| Corn Dollies  | 37  | 97 %  | 3 % | 4 |
| Demons  | 9 | 100 % | 0 % | Not Required  |
| Gargoyles | 2 | 100 % | 0 % | Not Required  |
| Greenmen  | 6 | 95 %  | 5 % | 6 |
| Homunculli  | 12  | 95 %  | 5 % | 6 |
| Manikins  | 9 | 97 %  | 3 % | 4 |
| Mummies | 7 | 97 %  | 3 % | 4 |
| Odd Bods  | 4 | 95 %  | 5 % | 6 |
| Puppets | 15  | 97 %  | 3 % | 4 |
| Robots  | 2 | 99 %  | 1 % | 2 |
| Scarecrows  | 21  | 97 %  | 3 % | 4 |
| Skeletons | 7 | 98 %  | 2 % | 3 |
| Tar Babies  | 25  | 96 %  | 4 % | 5 |
| Tin Men | 6 | 95 %  | 5 % | 6 |
| Triffids  | 29  | 96 %  | 4 % | 5 |
| Vampires  | 2 | 98 %  | 2 % | 3 |
| Werewolves  | 3 | 95 %  | 5 % | 6 |
| Zombies | 4 | 99 %  | 1 % | 2 |

- Number of crews for a guaranteed total burn = **29** (from an undamaged state).

| WOODS: {Raze} D6_Dice_Roll  | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 2 |           
| 2 | 3.5 |           
| 3 | 3.5 |           
| 4 | 6 |           
| 5 | 6 |           
| 6 | 6 |

Percentage destruction is given by rolling a modified D6 as specified for each Fire Crew, adding the results and rounding down to the nearest 5%.

Afterwards each Fire Crew member must roll a D100 to check for accidental death (due to heat, smoke and fire), (Demons and Gargoyles exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 25 Tar Babies to make just one fire crew. (Expect about 1 of which to perish to fire damage i.e. approximately 4%)

- ### Demolishers’ Report ###                   
                    
| Minor Character | Required Number per Demolish Crew | Survival Rate per Thousand  | Individual Chance of Perishing (per 1000) | 'Save’ Roll – Min Dice Roll 1 – 1000 Scale  |
| :----------:  | :----------:  | :----------:  | :----------:  | :----------:  |
| Androids  | 240 | 1000  | 0 | Not Required  |
| Corn Dollies  |  2K   | 975 | 25‰ | 26  |
| Demons  |  2.4K   | 1000  | 0 | Not Required  |
| Gargoyles | 670 | 1000  | 0 | Not Required  |
| Greenmen  | 670 | 998 | 2‰  | 3 |
| Homunculli  |  2K   | 996 | 4‰  | 5 |
| Manikins  |  1K   | 996 | 4‰  | 5 |
| Mummies | 750 | 997 | 3‰  | 4 |
| Odd Bods  | 960 | 999 | 1‰  | 2 |
| Puppets |  1.5K   | 997 | 3‰  | 4 |
| Robots  | 500 | 1000  | 0 | Not Required  |
| Scarecrows  |  2.4K   | 994 | 6‰  | 7 |
| Skeletons |  1.6K   | 996 | 4‰  | 5 |
| Tar Babies  |  1.34K  | 996 | 4‰  | 5 |
| Tin Men |  1.72K  | 1000  | 0 | Not Required  |
| Triffids  |  3K   | 1000  | 0 | Not Required  |
| Vampires  | 400 | 999 | 1‰  | 2 |
| Werewolves  | 570 | 999 | 1‰  | 2 |
| Zombies | 600 | 998 | 2‰  | 3 |

- Number of crews for a guaranteed total demolition = **30** (from an undamaged state).

| WOODS: {DEMOLISH} D6_Dice_Roll  | Modified Number (percent of damage to location) |           
| :----------:  | :----------:  |           
| 1 | 1.56  |           
| 2 | 2.94  |           
| 3 | 4.31  |           
| 4 | 5.69  |           
| 5 | 7.06  |           
| 6 | 8.44  |

Percentage destruction is given by rolling a modified D6 as specified for each Demolish Crew, adding the results and rounding down to the nearest 5%.

Afterwards each Demolish Crew member must roll a D1000 to check for accidental death (due to slips, trips and falls), (Androids, Demons, Gargoyles, Robots, Tin men and Triffids exempt).

Crews must be made up of the same species type, the numbers required are given in the table above. e.g. 2K Corn Dollies to make just one demolish crew. (Expect about 50 of which will perish to accidents).

---

