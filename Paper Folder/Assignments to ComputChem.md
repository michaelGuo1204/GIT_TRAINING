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

Beta-carotene, with the molecular formula C40H56, owns a long chain of conjugated double bounds together with two retinyl groups. The huge conjugated structure equip this molecule of  highly-delocalized  electron groups.

![image-20201112194348066](/home/bili/.config/Typora/typora-user-images/image-20201112194348066.png)

As the picture describes, there are up to 40 electron pairs locate in a same energy level, illustrating the delocalization of the electrons.

The distribution of charge and bonds' length also prove the delocalization of electrons. As is shown in the figure, the charge of the central chain goes through a sort of equalization,  which also happens in the bond length.

| Class               | Typical Bond Length(pm)    | Typical Bond Order |
| ------------------- | -------------------------- | ------------------ |
| Ethylene            | (C=C) 133.9                | 2                  |
| Ethene              | (C-C) 152.8                | 1                  |
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
the models used.





## Q2

### $R=-H$

$ \beta $