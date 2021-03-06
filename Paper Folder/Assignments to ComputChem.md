# Assignments to ComputChem

## Q1

### 1. Estimate its HOMO-LUMO energy gap using the particle-in-a-box model.

![image-20201112184743186](/home/bili/.config/Typora/typora-user-images/image-20201112184743186.png)

> Command: b3lyp/6-31g(d) pop=(nbo,savenbos) geom=connectivity

After the implementation of particle in a box  model, I get the molecule orbit as follows.

| NBO index | Molecular units | Energy(Hartree) | Class |
| --------- | --------------- | --------------- | ----- |
| 148       | CR (1) C   40   | -0.024560       | HOMO  |
| 149       | RY*(1) C   1    | 0.05938         | LUMO  |

Consequently, the HOMO-LUMO energy gap is 0.08394 Hartree

### 2. Obtain its stable structure using a proper quantum mechanical method and briefly
describe the structure.

![image-20201112191058644](/home/bili/.config/Typora/typora-user-images/image-20201112191058644.png)

> Command:  opt=calcfc b3lyp/6-31g(d)

In this case, I choose B3LYP and 6-31G(d) as the calculation parameters. And after 13 steps, the total energy converge at around -1557.9 Hartree. Indicating the normal termination of optimization precess. The description of the optimized molecule 

Beta-carotene, with the molecular formula $C_{40}H_{56}$, owns a long chain of conjugated double bounds together with two retinyl groups. The huge conjugated structure equip this molecule of  highly-delocalized  electron groups.

![image-20201112194348066](/home/bili/.config/Typora/typora-user-images/image-20201112194348066.png)

As the picture describes, there are up to 40 electron pairs locate in a same energy level, illustrating the delocalization of the electrons.

The distribution of charge and bonds' length also prove the delocalization of electrons. As is shown in the figure, the charge of the central chain goes through a sort of equalization,  which also happens in the bond length.

| Class               | Typical Bond Length(pm)    | Typical Bond Order |
| ------------------- | -------------------------- | ------------------ |
| $Ethylene$          | (C=C) 133.9                | 2                  |
| $Ethene$            | (C-C) 152.8                | 1                  |
| $ \beta -Carotene $ | (C=C)137.4 <br>(C-C) 144.3 | (C=C)2<br>(C-C)1.5 |

![image-20201112195004674](/home/bili/.config/Typora/typora-user-images/image-20201112195004674.png)

![image-20201112195422729](/home/bili/.config/Typora/typora-user-images/image-20201112195422729.png)

### 3. Based on the structure obtained in step 2, compute its UV-Vis spectra in the gas phase,using the ZINDO method (nstates=10).

![UV-Ris](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q1/UV-Ris.png)

> Command: zindo=(astates=10)

### 4. Re-compute its UV-Vis spectra in ethanol using the same method with the IEFPCM solvation model

![UV-Ris-Eth](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q1/UV-Ris-Eth.png)

> Command:  zindo=(nstates=10) scrf=(iefpcm,solvent=ethanol)

### 5. The experimentally measured maximum UV-vis absorption peak in ethanol is 450 nm. Discuss all the computed and the experimental excitation energy values and comment on

The calculated excitation by ZINDO model get an excitation energy of c.a. 540 nm. Frankly speaking, the gap between the experimental and computed data is not even far. 

Consequently, i would like to have some discussion about the significant gap. As long as solvation model, compute model and molecular itself are considered, I hold the opinion that the *IEFPCM solvation model*  and $\beta-Carotene's $ own properties contribute to the bias. I will elaborate my stand from two aspects ---- the model and the solvent molecular.

First, the IEFPCM solvation model itself plays an important role in generating the bias. An implicit solvent model as it is, it  fails to deal with non-electrostatic components in the given situation, which means the hydrogen bond existing in the system can not be take into consideration. Nevertheless, hydrogen bonds contribute significantly to the  molecular conformation in polarize environment, in this case, the ethanol. The conformation will then have impacts on the conjugate structure, which mainly provides $\pi \rightarrow \pi^\star$ transition, and the UV-Vis spectrum as well. Second, the $\beta-Carotene$ molecule generate UV-Vis absorption by the  $\pi \rightarrow \pi^\star$ transition. But according to the solvent effect upon the UV-Vis spectrum,  polar solvent will leads to a phenomena called "Red shift" on the $\pi \rightarrow \pi^\star$ transition which means the absorption peak will shift to a higher position, from 450 nm to 540 nm.

Then i want to have some comments on the ZINDO model.

+ As for the efficiency, ZINDO's semi-empirical type shows higher speed in calculation than those *ab initio* methods such as TDDFT. I calculate in both means and make a compare. 

> TDDFT:  Job cpu time:       0 days 19 hours 33 minutes 11.0 seconds.
>
> ZINDO:  Job cpu time:       0 days  0 hours  4 minutes 20.8 seconds.

+ As for the accuracy, ZINDO's mechanism ----**INDO** method guarantees the accuracy of spectrum calculation. 

> TDDFT : Absorption peak :600 nm
>
> ZINDO:  Absorption peak 540 nm



## Q2

### 

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |



## Q3

### 1. Using the 6-31G(d) basis set, determine the transition state for the dehydration of ethanol to ethylene, and record the B3LYP/6-31G(d) and MP2/6-31G(d) values for the barrier height.

After calculation i have got the possible transition state. Both states have only one  imaginary frequency. And the imaginary frequency suits the procedure of the reaction. Hence we can make sure that these transition states are the exception state. According to such  a formula:
$$
E_{barrier}=E_{trasition}-E_{reactant}
$$
We can get the barrier energy of this reaction.

**DFT Method**:  $293.73 kJ/mol$

**MP2 Method**:  $320.71kJ/mol$

### 2. IRC Path





## Q4

### 1. Guess the structures

Molecule $C_4 H_4$ ,with a degree of unsaturation  $\Omega =4 $, is likely to contain unsaturation bonds within the molecule. The question mentions several frequencies, and I just started some analysis.

+ $215 cm^{-1}$ **s**	Have not found any specific indication, but might refer to conjugate structure
+ $852 cm^{-1}$ **s**	This absorption peak indicates $CH_{2}$ wagging
+ $1608 cm^{-1}$ **s**     This absorption peak indicates $CC$ stretching
+  

### 2&3.  Optimize the lowest singlet states

After some calculations, I pick up 4 candidates for this question. They are listed as follows.

| Structure                                                    | IR Spectrum                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q4/C3C2/Mol.png" style="zoom: 25%;" /> | ![Spec](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q4/C3C2/Spec.png) |
| <img src="/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q4/3C2 Target/Mol.png" alt="Mol" style="zoom: 25%;" /> | ![Spec](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q4/3C2 Target/Spec.png) |
| <img src="/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q4/C3C/Mol.png" alt="Mol" style="zoom:25%;" /> | ![Spec](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q4/C3C/Spec.png) |
| <img src="/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q4/C3C2/Mol.png" alt="Mol" style="zoom:25%;" /> | ![Spec](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q4/C3C2/Spec.png) |

### 4. Discussion upon the structure





## Q5

### 1. Compute the reaction enthalpy
| Class   | Before<br>Hartree | After<br>Hartree | Reaction Enthalpy<br>kJ/mol |
| ------- | ----------------- | ---------------- | --------------------------- |
| Pyrr    | -209.573293       | -398.242577      | -98.3                       |
| Pyra    | -225.627079       | -414.286986      | -74.5                       |
| Imi     | -225.652388       | -414.313914      | -78.3                       |
| Tria123 | -241.686778       | -430.331907      | -35.2                       |
| Tria124 | -241.710414       | -430.363153      | -55.5                       |

### 2. N lone pair energy

| Class   | Bond  Index | Bound Energy<br>(Hartree) | Electron distribution and Energy level                       |
| ------- | ----------- | ------------------------- | ------------------------------------------------------------ |
| Pyrr    | 15          | -384.32069                | ![image-20201114000154802](/home/bili/.config/Typora/typora-user-images/image-20201114000154802.png) |
| Pyra    | 14,15       | -459.77756                | ![image-20201114000330492](/home/bili/.config/Typora/typora-user-images/image-20201114000330492.png) |
| Imi     | 14,15       | -435.124                  | ![image-20201113235923611](/home/bili/.config/Typora/typora-user-images/image-20201113235923611.png) |
| Tria123 | 13          | -554.55811                | ![image-20201114000607770](/home/bili/.config/Typora/typora-user-images/image-20201114000607770.png) |
| Tria124 | 15          | -493.882805               | ![image-20201114000743482](/home/bili/.config/Typora/typora-user-images/image-20201114000743482.png) |

![EvsN](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q5/EvsN.png)

### 3. Discuss the geometry change of $CO_2$ and its reactivity with azole anions

The geometry of $CO_2$ consists of two parts: the   $\angle OCO$ angle and $d_{C-O}$. In my opinion, the $\angle OCO$ will have supervise impact on the 

After the calculation, I have got some data of $CO_2$ geometry and  its reactivity.

| Class   | $d_{C-N}$ | $\angle OCO$ | $d_{C-O}$ | Reaction Enthalpy |
| ------- | --------- | ------------ | --------- | ----------------- |
| Pyrr    | 1.53      | 134          | 1.23603   | -98.3             |
| Pyra    | 1.57      | 136          | 1.23550   | -74.5             |
| Imi     | 1.6       | 135          | 1.23295   | -78.3             |
| Tria123 | 1.67      | 140          | 1.21512   | -35.2             |
| Tria124 | 1.56      | 136          | 1.22928   | -55.5             |

Here i choose $\angle OCO$  ,  $d_{C-O}$ to represent the geometry change of the $CO_2$ molecule, and choose the bond length between carbon and nitrogen atom and reaction enthalpy as the measurements of the reactivity. And I get such graphs.

| Reaction enthalpy                                            | C-N bond                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![image-20201114224344983](/home/bili/.config/Typora/typora-user-images/image-20201114224344983.png) | ![image-20201114224647465](/home/bili/.config/Typora/typora-user-images/image-20201114224647465.png) |
| ![image-20201114225825638](/home/bili/.config/Typora/typora-user-images/image-20201114225825638.png) | ![image-20201114225927009](/home/bili/.config/Typora/typora-user-images/image-20201114225927009.png) |

From these graphs we can make further assumption, the more the $\angle OCO$ bends , the higher the reactivity will be. The more the $d_{C-O}$ stretch, the higher the reactivity will be. It 's a funny phenomena that deserve some discussion. 

I want to discuss this question by Frontier molecular orbital theory. Take pyrr into consideration, the frontier of the reaction are

| $CO_2$                                                       | Pyrr                                                         | Pyrr-$CO_2$                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![Carbon Dioxide](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q5/Example/Carbon Dioxide.png) | ![Pyrr_optfrep](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q5/Example/Pyrr_optfrep.png) | ![Pyrr_CD_Reaction](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q5/Example/Pyrr_CD_Reaction.png) |

To generate more stable bond, which is $\sigma_{N-C}$ bond in the Pyrr-$CO_2$, the $CO_2$ molecule should bend to a proper angle to get its $\pi_{C-O}^{\star}$ orbit maximum overlap with the N-lone pair orbit. And this kind of bend depends on the N lone pair's energy. The higher the N lone pair's energy, the easier it would bend the $CO_2$molecule to reach stable state. The larger degree carbon dioxide bends, the more stable molecular will form. After the binding of the C-N atoms, newly constructed molecular conjugate structure will then shorten the $CO_2$ bond length by conjugative effects. Hence i can have more faith on my assumption that the $\angle OCO$ is the main components of the carbon dioxide's reactivity with azole anions, the length of C-O is just a consequence of forming a molecule ,which is also a consequence of $\angle OCO$ bends;

But when cast our sight into both molecules, we will find another problem. A same $\angle OCO$ might have a reaction enthalpy gap, for instance Pyrr and Tria124. Then i find that the more N atoms existing on the ring, the higher the reaction enthalpy will be. And the effect of the N number is far meticulous that the effect from angle bends in carbon dioxide. I would like to make a assumption that the bigger electronegativity leads to a dispose of electron density in the ring, which will then deactivate the reaction But there are just few molecules and data so i can not illustrate my assumption. I will try to make some further discussion after reaching more data.

