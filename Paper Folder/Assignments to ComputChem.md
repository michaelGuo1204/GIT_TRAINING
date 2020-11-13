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

### $R=-H$

![](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q2/H/Tri.svg)

![Sig](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q2/H/Sig.svg)

### $R = -CH_3$

![Sig](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q2/CH3/Sig.svg)![Tri](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q2/CH3/Tri.svg)

### $R = -NH_2 $

![Sig](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q2/NH2/Sig.svg)

### $R = -OH$

![Tri](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q2/OH/Tri.svg)

![Sig](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q2/OH/Sig.svg)

### $ R= -F$

![](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q2/F/Tri.svg)

![Sig](/home/bili/Lernen/Compumental Chemistry/Paper Folder/Q2/F/Sig.svg)

## Q3

### 1. Using the 6-31G(d) basis set, determine the transition state for the dehydration of ethanol to ethylene, and record the B3LYP/6-31G(d) and MP2/6-31G(d) values for the barrier height.

DFT: -155.0313238  -154.9194568

MP2:-154.5171 -154.3949483



## Q4

### 1&2 Guess the structures and optimize the lowest singlet states

After some calculations, I pick up 4 candidates for this question, they are



## Q5

### 1. compute the reaction enthalpy
| Class   | Before      | After       |
| ------- | ----------- | ----------- |
| Pyrr    | -209.573293 | -398.242577 |
| Pyra    | -225.627079 | -414.286986 |
| Imi     | -225.652388 | -414.313914 |
| Tria123 | -241.686778 | -430.331907 |
| Tria124 | -241.710414 | -430.363153 |

### 2. N lone pair energy

|         |       |                   |                                                              |
| ------- | ----- | ----------------- | ------------------------------------------------------------ |
| Pyrr    | 15    | -0.14638          | ![image-20201114000154802](/home/bili/.config/Typora/typora-user-images/image-20201114000154802.png) |
| Pyra    | 14,15 | -0.17512_-0.17501 | ![image-20201114000330492](/home/bili/.config/Typora/typora-user-images/image-20201114000330492.png) |
| Imi     | 14,15 | -0.16573_-0.16575 | ![image-20201113235923611](/home/bili/.config/Typora/typora-user-images/image-20201113235923611.png) |
| Tria123 | 13    | -0.21122          | ![image-20201114000607770](/home/bili/.config/Typora/typora-user-images/image-20201114000607770.png) |
| Tria124 | 15    | -0.18811          | ![image-20201114000743482](/home/bili/.config/Typora/typora-user-images/image-20201114000743482.png) |

