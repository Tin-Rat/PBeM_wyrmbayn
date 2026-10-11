
![*wyrmbayn*](./Title.png "wyrmbayn")

***Version 1.0***

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

Botanist
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Garden, Jungle or Woods:-  +15%(plus)
Recruits	Major:- Farmer and Gardener.
		Minor:- Greenmen, Triffids and Zombies.


<h4 id="p4"><span style="background-color: #FFFF00">Page 4.</span></h4>

Count
Health:-  Max 100%		Movement penalty:-   -20%(minus)
	Health Deterioration;	Resting:-  -2%(minus)
				Resting in a Fort:-  -1%(minus)
Recruits	Any Major except another Count.
		Minor:- Vampires, Werewolves and Zombies.

Couturier
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in a Mall:-  +25%(plus)
Recruits	Major:- Seamstress.
		Minor:- Manikins, Puppets and Zombies.

Crow Master
Health:-  Max 90%		Movement penalty:-   -8%(minus)
	Health Restoration;	Resting:-  +4%(plus)
				Resting in Garden, Plain or Woods:-  +12%(plus)
Recruits	Major:- Farmer, Ploughman and Merchant.
		Minor:- Corn Dollies, Scarecrows and Tar Babies.

Explorer
Health:-  Max 100%		Movement penalty:-   -9%(minus)
	Health Restoration;	Resting:-  +4%(plus)
			Resting in Garden, Jungle, Desert or Woods:-  +10%(plus)
Recruits	Major:- Archaeologist.
		Minor:- Triffids, Werewolves and Zombies.

Farmer
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Garden:-  +15%(plus)
Recruits	Major:- Crow Master, Gardener and Ploughman.
		Minor:- Greenmen, Scarecrows and Werewolves.

Gardener
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Garden:-  +15%(plus)
Recruits	Major:- Grave Digger and Botanists.
		Minor:- Greenmen, Scarecrows and Triffids.

Grave Digger
Health:-  Max 50%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church:-  +10%(plus)
Recruits	Major:- Alchemist, Archaeologist, Count, Mason, Monk, Necromancer, Priest, Shaman and Wax Worker.
		Minor:- Demons, Skeletons and Vampires.


<h4 id="p5"><span style="background-color: #FFFF00">Page 5.</span></h4>

Jester
Health:-  Max 60%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Fort:-  +15%(plus)
Recruits	Major:- Knave only.
		Minor:- Odd bods, Puppets and Robots.

Knave
Health:-  Max 100%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Fort:-  +15%(plus)
Recruits	Major:- Couturier, Jester and Retrobate.
		Minor:- Tar Babies, Tinmen and Werewolves.

Mason
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church, Fort or Temple;:-  +10%(plus)
Recruits	Major:- Grave Digger and Sculptor.
		Minor:- Gargoyles, Mummies and Odd Bods.

Mechanic
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Scrapyard:-  +15%(plus)
Recruits	Major:- Merchant only.
		Minor:- Androids, Robots and Tar Babies.

Merchant
Health:-  Max 95%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Scrapyard:-  +15%(plus)
Recruits	Major:- Alchemist, Crow master, Mechanic and Sculptor.
		Minor:- Robots, Tinmen and Triffids.

Monarch
Health:-  Max 80%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Fort:-  +15%(plus)
Recruits	Major:- Count, Couturier, Explorer, Gardener, Jester, Knave, Mason 			and Sculptor.
		Minor:- Androids, Odd Bods and Tinmen.

Monk
Health:-  Max 100%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church, Temple or Fort:-  +10%(plus)
Recruits	Major:- Gardener, Priest and Shaman.
		Minor:- Demons, Gargoyles and Skeletons.


<h4 id="p6"><span style="background-color: #FFFF00">Page 6.</span></h4>

Necromancer
Health:-  Max 50%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church, Temple or Fort:-  +10%(plus)
Recruits	Major:- Alchemist, Grave Digger and Shaman.
		Minor:- Demons, Mummies and Skeletons.

Ploughman
Health:-  Max 100%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Garden, Plain or Woods:-  +10%(plus)
Recruits	Major:- Crow Master only.
		Minor:- Corn Dollies, Scarecrows and Greenmen.

Priest
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church or Temple:-  +10%(plus)
Recruits	Major:- Grave Digger and Monk.
		Minor:- Corn Dollies, Gargoyles and Vampires.

Retrobate
Health:-  Max 75%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church or Temple:-  +10%(plus)
Recruits	Major:- Jester Only.
		Minor:- Corn Dollies, Homunculii and Tar Babies.

Sculptor
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church or Temple:-  +10%(plus)
Recruits	Major:- Mason and Wax Worker.
		Minor:- Androids, Manikins and Robots.

Seamstress
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Mall:-  +20%(plus)
Recruits	Major:- Couturier and Wax Worker.
		Minor:- Manikins, Mummies and Puppets.

Shaman
Health:-  Max 100%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Church, Garden, Jungle, Plain, Temple or 				Woods:-  +8%(plus)
Recruits	Major:- Monk only.
		Minor:- Homunculii, Puppets and Vampires.


<h4 id="p7"><span style="background-color: #FFFF00">Page 7.</span></h4>

Wax Worker
Health:-  Max 90%		Movement penalty:-   -10%(minus)
	Health Restoration;	Resting:-  +5%(plus)
				Resting in Mall:-  +20%(plus)
Recruits	Major:- Seamstress only.
		Minor:- Androids, Homunculii and Manikins.




<h4 id="minor">Minor Characters</h4>

There are nineteen different types of Minor Characters, theirs stats are given in the table below:-

<table style="table-layout: fixed; width: 55%">
    <tr><th style="width: 18%;">Species</th>
      <th  style="width:8%;">Attack Strength</th>
      <th style="width:8%;">Hits</th>
      <th style="width:8%;">Density</th>
      <th style="width:8%;">Fireproof Rating</th></tr>
    <tr><td>Androids</td>    <td>10</td><td>10</td><td>5</td><td>4</td></tr>
    <tr><td>Corn Dollies</td><td>1</td><td>1</td><td>6</td><td>1</td></tr>
    <tr><td>Demons</td>      <td>1</td><td>20</td><td>5</td><td>5</td></tr>
    <tr><td>Gargoyles</td>   <td>3</td><td>20</td><td>6</td><td>5</td></tr>
    <tr><td>Greenmen</td>    <td>6</td><td>3</td><td>6</td><td>2</td></tr>
    <tr><td>Homunculii</td>  <td>3</td><td>3</td><td>4</td><td>3</td></tr>
    <tr><td>Manikins</td>    <td>3</td><td>3</td><td>4</td><td>2</td></tr>
    <tr><td>Mummies</td>     <td>4</td><td>4</td><td>4</td><td>2</td></tr>
    <tr><td>Odd Bods</td>    <td>5</td><td>5</td><td>5</td><td>4</td></tr>
    <tr><td>Puppets</td>     <td>2</td><td>4</td><td>4</td><td>2</td></tr>
    <tr><td>Robots</td>      <td>8</td><td>8</td><td>3</td><td>4</td></tr>
    <tr><td>Scarecrows</td>  <td>2</td><td>2</td><td>5</td><td>2</td></tr>
    <tr><td>Skeletons</td>   <td>3</td><td>3</td><td>5</td><td>4</td></tr>
    <tr><td>Tar Babies</td>  <td>3</td><td>3</td><td>6</td><td>1</td></tr>
    <tr><td>Tinmen</td>     <td>3</td><td>7</td><td>4</td><td>5</td></tr>
    <tr><td>Triffids</td>    <td>4</td><td>12</td><td>2</td><td>2</td></tr>
    <tr><td>Vampires</td>    <td>12</td><td>6</td><td>6</td><td>3</td></tr>
    <tr><td>Werewolves</td>  <td>6</td><td>5</td><td>7</td><td>4</td></tr>
    <tr><td>Zombies</td>     <td>5</td><td>5</td><td>4</td><td>3</td></tr>
</table>

<h4 id="p8"><span style="background-color: #FFFF00">Page 8.</span></h4>

<h4 id="terr">Terrains</h4>
<p>
There are twelve terrain types they are named after the most prominent feature so for example a Church location could reasonable be considered to contain a graveyard a small amount of dwellings and the odd yew tree. All terrain locations with the exception of ‘Plain’ are locations where minor characters may be found and (automatically) recruited.</p>
<p>  The ‘Density’ in the table below is an abstract value that gives an indication of the maximum number of the particular type of minor character that may be found there. After a round of recruitment there may temporarily be less characters than the ‘Density’ number (usually down to a single character), replenishment will be approximately one fourth of the ‘Density’ value, but never less than one. Ruins do not appear in the initial map (turn one), but are created using demolish/raze orders. 
</p>
<!---
<style>
    table,
    th,
    td {
        border: 1px solid black;
        border-collapse: collapse;
        padding: 2px;
        text-align: center;
    }
</style>
--->

<table style="table-layout: fixed; width: 100%; text-align: center;" >
    <tr><th style="width: 9.2%" rowspan="3"
        >Terrain</th>
      <th  style="width:12.1%" rowspan="3">Minor Character</th>
      <th style="width:9.7%" rowspan="3">Density</th>
      <th style="width:6.9%" colspan = "10">Reinforcements</th>
    </tr>
    <tr>
      <th style="width:6.9%" colspan="10">Percent of Terrain Damage</th>
    </tr>
    <tr><th>0%</th><th>10%</th><th>20%</th><th>30%</th><th>40%</th>
      <th>50%</th><th>60%</th><th>70%</th><th>80%</th><th>90%</th></tr>
    <tr>
      <td rowspan="7">Church</td>
      <td>Corn Dollies</td>
      <td>84</td>
        <td>21</td><td>21</td><td>20</td><td>19</td><td>18</td>
        <td>17</td><td>17</td><td>16</td><td>15</td><td>14</td>  
    </tr>
    <tr><td>Gargoyles</td><td>2</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>  
    </tr>
    <tr><td>Greenmen</td> <td>4</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>  
    </tr>
    <tr><td>Odd bods</td> <td>4</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>  
    </tr>
    <tr><td>Skeletons</td> <td>18</td>
      <td>5</td><td>5</td><td>5</td><td>5</td><td>5</td>
      <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td> 
    </tr>
    <tr><td>Triffids</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Zombies</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr>
    <td rowspan="6">Desert</td><td>Demons</td><td>3</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>  
    </tr>
    <tr><td>Gargoyles</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>  
    </tr>
    <tr><td>Homunculii</td> <td>21</td>
      <td>6</td><td>6</td><td>6</td><td>6</td><td>6</td>
      <td>5</td><td>5</td><td>5</td><td>5</td><td>5</td> 
    </tr>
    <tr><td>Mummies</td> <td>12</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td> 
    </tr>
    <tr><td>Odd Bods</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Skeletons</td> <td>5</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr>
    <td rowspan="7">Fort</td><td>Gargoyles</td><td>2</td>
        <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
        <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
  </tr>
    <tr><td>Greenmen</td><td>7</td>
        <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
        <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>  
    </tr>
    <tr><td>Odd Bods</td> <td>6</td>
        <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
        <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Tinmen</td> <td>9</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td> 
    </tr>
    <tr><td>Triffids</td> <td>8</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Vampires</td> <td>2</td>
        <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
        <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>  
    </tr>
    <tr><td>Werewolves</td> <td>4</td>
        <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
        <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>  
    </tr>
    <tr>
    <td rowspan="6">Garden</td><td>Corn Dollies</td><td>56</td>
      <td>14</td><td>14</td><td>13</td><td>13</td><td>12</td>
      <td>12</td><td>11</td><td>11</td><td>10</td><td>10</td> 
    </tr>
    <tr><td>Greenmen</td><td>7</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Scarecrows</td> <td>42</td>
      <td>11</td><td>11</td><td>11</td><td>10</td><td>10</td>
      <td>9</td><td>9</td><td>9</td><td>8</td><td>8</td> 
    </tr>
    <tr><td>Tar Babies</td> <td>15</td>
      <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
      <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td> 
    </tr>
    <tr><td>Triffids</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Werewolves</td> <td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>  
    </tr>
    
    

</table>



<h4 id="p9"><span style="background-color: #FFFF00">Page 9.</span></h4>


<table style="table-layout: fixed; width: 100%; text-align: center;">
    <tr><th style="width: 9.2%" rowspan="3"
        >Terrain</th>
      <th  style="width:12.1%" rowspan="3">Minor Character</th>
      <th style="width:9.7%" rowspan="3">Density</th>
      <th style="width:6.9%" colspan = "10">Reinforcements</th>
    </tr>
    <tr>
      <th style="width:6.9%" colspan="10">Percent of Terrain Damage</th>
    </tr>
    <tr><th>0%</th><th>10%</th><th>20%</th><th>30%</th><th>40%</th>
      <th>50%</th><th>60%</th><th>70%</th><th>80%</th><th>90%</th></tr>
    <tr>
      <td rowspan="9"  style ="width: 1px;padding: 2px;">Jungle</td>
      <td>Demons</td><td>3</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
    </tr>
    <tr><td>Greenmen</td><td>7</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr>
    <tr><td>Homunculii</td> <td>21</td>
      <td>6</td><td>6</td><td>6</td><td>6</td><td>6</td>
      <td>5</td><td>5</td><td>5</td><td>5</td><td>5</td> 
    </tr>
    <tr><td>Odd Bods</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr><td>Robots</td> <td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>  
    </tr>
    <tr><td>Scarecrows</td> <td>16</td>
      <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
      <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr><td>Tar Babies</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr><td>Triffids</td> <td>8</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
    </tr>
    <tr><td>Zombies</td> <td>8</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>  
    </tr>
    <tr>
    <td rowspan="7"  style ="width: 1px;padding: 2px;">Labs</td><td>Androids</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>   
    </tr>
    <tr><td>Homunculii</td><td>21</td>
      <td>6</td><td>6</td><td>6</td><td>6</td><td>6</td>
      <td>5</td><td>5</td><td>5</td><td>5</td><td>5</td> 
    </tr>
    <tr><td>Odd Bods</td> <td>4</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>   
    </tr>
    <tr><td>Puppets</td> <td>9</td>
        <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
        <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>   
    </tr>
    <tr><td>Robots</td> <td>4</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>   
    </tr>
    <tr><td>Tinmen</td> <td>2</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>   
    </tr>
    <tr><td>Triffids</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr>
    <td rowspan="4" style ="width: 1px;padding: 2px;">Mall</td><td>Androids</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
    <tr><td>Manikins</td><td>21</td>
      <td>6</td><td>6</td><td>6</td><td>6</td><td>6</td>
      <td>5</td><td>5</td><td>5</td><td>5</td><td>5</td> 
    </tr>
    <tr><td>Puppets</td> <td>24</td>
        <td>6</td><td>6</td><td>6</td><td>6</td><td>6</td>
      <td>5</td><td>5</td><td>5</td><td>5</td><td>5</td> 
    </tr>
    <tr><td>Zombies</td> <td>3</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
    <tr>
    <td style ="width: 1px;padding: 2px;">Plain</td>
    <td colspan="12"style = "word-wrap: break-word; padding-right: 50px">No minor characters are to be found at these locations</td>
    <!---<td>&nbsp</td>--->
    </tr>
    <tr>
    <td style ="width: 1px;padding: 2px;">Ruins</td>
    <td colspan="12" style = "word-wrap: break-word; padding-right: 50px">Initially none. Minor characters to be randomly assigned 1/10 from each contiguous region. 1/10 from region at direction one, a further 1/10 from region at direction two, and so on so up to 60% occupation of randomized minor characters.</td>
    <!---<td>&nbsp</td>--->
    </tr>
    <tr>
    <td rowspan="10" style ="word-wrap: break-word;width: 1px;padding: 2px;">Scrap yard</td><td>Androids</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>    
    </tr>
    <tr><td>Homunculii</td><td>10</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>   
    </tr>
    <tr><td>Odd Bods</td> <td>4</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
    <tr><td>Puppets</td> <td>9</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
    </tr>
    <tr><td>Robots</td> <td>3</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
    <tr><td>Scarecrows</td> <td>16</td>
      <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
      <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
    </tr>
     <tr><td>Tar Babies</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
     </tr>
    <tr><td>Tinmen</td> <td>9</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
    </tr>
    <tr><td>Triffids</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Werewolves</td> <td>3</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
</table>    


<h4 id="p10"><span style="background-color: #FFFF00">Page 10.</span></h4>


<table style="table-layout: fixed; width: 100%; text-align: center;">
    <tr><th style="width: 9.2%" rowspan="3"
        >Terrain</th>
      <th  style="width:12.1%" rowspan="3">Minor Character</th>
      <th style="width:9.7%" rowspan="3">Density</th>
      <th style="width:6.9%" colspan = "10">Reinforcements</th>
    </tr>
    <tr>
      <th style="width:6.9%" colspan="10">Percent of Terrain Damage</th>
    </tr>
    <tr><th>0%</th><th>10%</th><th>20%</th><th>30%</th><th>40%</th>
      <th>50%</th><th>60%</th><th>70%</th><th>80%</th><th>90%</th></tr>
    <tr>
      <td rowspan="7">Temple</td><td>Corn Dollies</td><td>24</td>
      <td>6</td><td>6</td><td>6</td><td>6</td><td>6</td>
      <td>5</td><td>5</td><td>5</td><td>5</td><td>5</td> 
    </tr>
    <tr> <td>Demons</td><td>8</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Gargoyles</td> <td>2</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
    <tr><td>Greenmen</td> <td>4</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
    <tr><td>Skeletons</td> <td>18</td>
      <td>5</td><td>5</td><td>5</td><td>5</td><td>5</td>
      <td>4</td><td>4</td><td>4</td><td>4</td><td>4</td>
    </tr>
    <tr><td>Triffids</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Zombies</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr>
    <td rowspan="10">Woods</td><td>Androids</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
    <tr><td>Demons</td><td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Greenmen</td> <td>7</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Homunculii</td> <td>10</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
    </tr>
    <tr><td>Puppets</td> <td>9</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
    </tr>
    <tr><td>Robots</td> <td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
    <tr><td>Scarecrows</td><td>33</td>
      <td>9</td><td>9</td><td>9</td><td>9</td><td>8</td>
      <td>8</td><td>8</td><td>7</td><td>7</td><td>7</td> 
    </tr>
    <tr><td>Tar Babies</td> <td>12</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
      <td>3</td><td>3</td><td>3</td><td>3</td><td>3</td>
    </tr>
    <tr><td>Triffids</td> <td>6</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td>
      <td>2</td><td>2</td><td>2</td><td>2</td><td>2</td> 
    </tr>
    <tr><td>Werewolves</td> <td>4</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td>
      <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td> 
    </tr>
    <tr>
</table>


<h4 id="p11"><span style="background-color: #FFFF00">Page 11.</span></h4>


- <h4 id="proc">Processing Sequence</h4>

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

Major Characters may move in any of six directions numbered 1 to 6:- where
- ***1*** is at 60° (approx NE by E), 
- ***2*** is at 120° (approx SE by E), 
- ***3*** is at 180° (S), 
- ***4*** is at 240° (approx SW by W),
- ***5*** is at 300° (approx NW by W) and 
- ***6*** is at 360°/0° (N).

Their retinue of Minor Characters will move with them.


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
adjoining locations. The Saturation level for a particular Minor Type is a maximum population level (or cut-off point) that the particular type can grow to. For example, if a migration of say two Greenmen to the ruined location brings the population to more than five, say to a total of six or seven, then the excess will be immediately discounted and the population will be reduced back down its 'Saturation Level' of five.

'Saturation' levels for 'Ruins' terrains are similar to 'Density' levels for other terrain types. The different terminology is used because the 'Density' level is also related to the initial 'turn one' population for terrains other than 'Ruins' or 'Plains'.

#### Saturation levels for <mark>'Ruins'</mark> terrain types are given in the table below:

|Minor Type    |Saturation Level|Minor Type    |Saturation Level|Minor Type    |Saturation Level|
|:------------:|:--------------:|:------------:|:--------------:|:------------:|:--------------:|
| Androids     | 1              | Mummies      | 8              | Tar Babies   | 9              | 
| Corn Dollies | 51             | Odd Bods     | 4              | Tinmen       | 6              | 
| Demons       | 5              | Puppets      | 15             | Triffids     | 5              | 
| Gargoyles    | 2              | Robots       | 3              | Vampires     | 2              | 
| Greenmen     | 5              | Scarecrows   | 26             | Werewolves   | 3              | 
| Homunculli   | 13             | Skeletons    | 11             | Zombies      | 5              |  
| Manikins     | 13             |              |                |              |                |


### 2. Reinforcement of 'Ruins' Terrain Type

Reinforcement of the 'Ruins' terrain type is by migration from the surrounding adjoining terrain types, which may total five or six. Note that no migration from a 'Plains' terrain type is possible because those types are devoid of native Minor Characters.
Random factors are used using simulated die rolls from D11, D12, D13,D14, D15, D18 and D27s. (Some of these may not exist in the physical world, but can be simulated with software).
Note, these migrations have no effect on the population level of the donor locations - this may annoy the purests but its not worth the extra book keeping and complications.
Migration is possible from the following adjacent locations:- Church, Desert, Fort, Garden, Jungle, Labs, Mall, other Ruins and Scrapyards.

#### Tables for the different terrain types are given below:-

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “CHURCH” TERRAIN 
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D11    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : CHURCH 

 | DIE ROLL (D11)  |  Type           |  Number  | DIE ROLL (D11)  |  Type           |  Number  |  
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|
 |   1             |  Corn Dollies   |   4      |   7             |  Greenmen       |   1      | 
 |   2             |  Corn Dollies   |   4      |   8             |  Odd Bods       |   1      |  
 |   3             |  Corn Dollies   |   5      |   9             |  Skeletons      |   6      |   
 |   4             |  Corn Dollies   |   5      |  10             |  Triffids       |   2      | 
 |   5             |  Corn Dollies   |   5      |  11             |  Zombies        |   2      |
 |   6             |  Gargoyles      |   1      |                 |                 |          |
 
---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “DESERT” TERRAIN
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D13    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : DESERT  

 | DIE ROLL (D13)  |  Type           |  Number  | DIE ROLL (D13)  |  Type           |  Number  |  
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:| 
 |  1              |Demons           |    1     |  8              |Mummies          |    1     |
 |  2              |Gargoyles        |    1     |  9              |Mummies          |    1     | 
 |  3              |Homunculli       |    1     |  10             |Odd Bods         |    1     |
 |  4              |Homunculli       |    1     |  11             |Odd Bods         |    1     |
 |  5              |Homunculli       |    2     |  12             |Skeletons        |    1     |
 |  6              |Homunculli       |    2     |  13             |Skeletons        |    1     |
 |  7              |Mummies          |    1     |                 |                 |          |

---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “FORT” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D18    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : FORT  

 | DIE ROLL (D18)  |  Type      |  Number  | DIE ROLL (D18)  |  Type      |  Number  | 
 |:---------------:|:----------:|:--------:|:---------------:|:----------:|:--------:|  
 |  1              |Gargoyles   |    1     |  10             |Tinmen      |    1     |
 |  2              |Greenmen    |    1     |  11             |Tinmen      |    1     |
 |  3              |Greenmen    |    1     |  12             |Tinmen      |    1     |
 |  4              |Greenmen    |    1     |  13             |Triffids    |    1     |
 |  5              |Odd Bods    |    1     |  14             |Triffids    |    1     |
 |  6              |Odd Bods    |    1     |  15             |Triffids    |    1     |
 |  7              |Odd Bods    |    1     |  16             |Vampires    |    1     |
 |  8              |Odd Bods    |    1     |  17             |Werewolves  |    1     |
 |  9              |Tinmen      |    1     |  18             |Werewolves  |    1     |

---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “GARDEN” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D11    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : GARDEN 

 | DIE ROLL (D11)  |  Type           |  Number  | DIE ROLL (D11)  |  Type           |  Number  |   
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|   
 | 1   | Corn Dollies   | 4 | 7   | Scarecrows     | 4 |
 | 2   | Corn Dollies   | 4 | 8   | Scarecrows     | 4 |
 | 3   | Corn Dollies   | 4 | 9   | Tar Babies     | 4 | 
 | 4   | Corn Dollies   | 4 | 10  | Triffids       | 2 | 
 | 5   | Greenmen       | 2 | 11  | Werewolves     | 1 |
 | 6   | Scarecrows     | 3 |     |                |   |
 
--- 

##### RANDOM MIGRATION TO THE”RUINS” TERRAIN FROM AN ADJOINING “JUNGLE” TERRAIN   
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D11    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM: JUNGLE 

 | DIE ROLL (D11)  |  Type           |  Number  | DIE ROLL (D11)  |  Type           |  Number  |   
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|   
 | 1   | Demons         | 1 | 7   | Scarecrows     | 2 |
 | 2   | Greenmen       | 2 | 8   | Scarecrows     | 2 |
 | 3   | Homunculli     | 3 | 9   | Tar Babies     | 2 | 
 | 4   | Homunculli     | 3 | 10  | Triffids       | 2 | 
 | 5   | Odd Bods       | 2 | 11  | Zombies        | 2 |
 | 6   | Robots         | 1 |     |                |   |

---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “LABS” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D15    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : LABS   

 | DIE ROLL (D15)  |  Type           |  Number  | DIE ROLL (D15)  |  Type           |  Number  |   
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|   
 | 1   | Androids         | 1 | 9   | Puppets      | 1 |
 | 2   | Homunculli       | 2 | 10  | Puppets      | 1 |
 | 3   | Homunculli       | 2 | 11  | Robots       | 1 | 
 | 4   | Homunculli       | 2 | 12  | Tinmen       | 1 | 
 | 5   | Odd Bods         | 1 | 13  | Tinmen       | 1 |
 | 6   | Odd Bods         | 1 | 14  | Triffids     | 1 |
 | 7   | Odd Bods         | 1 | 15  | Triffids     | 1 |
 | 8   | Puppets          | 1 |     |              |   |

---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “MALL” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D14    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : MALL  

 | DIE ROLL (D14)  |  Type           |  Number  | DIE ROLL (D14)  |  Type           |  Number  |   
 |:---------------:|:---------------:|:--------:|:---------------:|:---------------:|:--------:|   
 | 1   | Androids         | 1 | 8   | Puppets       | 1 |
 | 2   | Manikins         | 1 | 9   | Puppets       | 1 |
 | 3   | Manikins         | 1 | 10  | Puppets       | 1 | 
 | 4   | Manikins         | 1 | 11  | Puppets       | 1 | 
 | 5   | Manikins         | 1 | 12  | Puppets       | 2 |
 | 6   | Manikins         | 2 | 13  | Puppets       | 2 |
 | 7   | Manikins         | 2 | 14  | Zombies       | 1 |

---

##### RANDOM MIGRATION TO THE “RUINS” TERRAIN FROM AN ADJOINING “RUINS” TERRAIN   
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D27    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM : RUINS   

 | DIE ROLL (D27)  |  Type      |  Number  | DIE ROLL (D27)  |  Type      |  Number  | 
 |:---------------:|:----------:|:--------:|:---------------:|:----------:|:--------:|  
 |  1              |Androids    |    1     |  15             |Robots      |    1     |
 |  2              |Corn Dollies|    2     |  16             |Scarecrows  |    1     |
 |  3              |Corn Dollies|    3     |  17             |Scarecrows  |    2     |
 |  4              |Demons      |    1     |  18             |Skeletons   |    1     |
 |  5              |Gargoyles   |    1     |  19             |Skeletons   |    1     |
 |  6              |Greenmen    |    2     |  20             |Tar Babies  |    1     |
 |  7              |Homunculli  |    1     |  21             |Tar Babies  |    1     |
 |  8              |Homunculli  |    2     |  22             |Tinmen      |    1     |
 |  9              |Manikins    |    1     |  23             |Triffids    |    1     |
 |  10             |Mummies     |    1     |  24             |Triffids    |    1     |
 |  11             |Odd Bods    |    1     |  25             |Vampires    |    1     |
 |  12             |Odd Bods    |    1     |  26             |Werewolves  |    1     |
 |  13             |Puppets     |    1     |  27             |Zombies     |    1     |
 |  14             |Puppets     |    1     |                 |            |          |

---

##### RANDOM MIGRATION TO THE”RUINS” TERRAIN FROM AN ADJOINING “SCRAPYARD” TERRAIN    
    
##### NOTE: THEORETICAL DICE REQUIRED = SINGLE D12    
    
##### MIGRANTS TO “RUINS” TERRAIN FROM: SCRAPYARD

 | DIE ROLL (D12)  |  Type      |  Number  | DIE ROLL (D12)  |  Type      |  Number  | 
 |:---------------:|:----------:|:--------:|:---------------:|:----------:|:--------:|  
 |  1              |Androids    |    1     |  7              |Scarecrows  |    2     |
 |  2              |Homunculli  |    3     |  8              |Tar Babies  |    2     |
 |  3              |Odd Bods    |    1     |  9              |Tinmen      |    1     |
 |  4              |Puppets     |    3     |  10             |Tinmen      |    2     |
 |  5              |Robots      |    1     |  11             |Triffids    |    2     |
 |  6              |Scarecrows  |    2     |  12             |Werewolves  |    1     |

---

---






