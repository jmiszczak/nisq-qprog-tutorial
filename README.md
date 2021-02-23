# nisq-qprog-tutorial
Some tests with QAOA, VQE, annealers and other procedures for NISQ quantum computers


## Conda environement management

File `nisq-qprog-tutorial.yml` contains definition of virtual environement for Anacoda. To create new enviroment run

    conda env create -f nisq-qprog-tutorial.yml
  
To updated existing environement run
    
    conda env update -f nisq-qprog-tutorial.yml --prune
 
Option `--prune` results in the remove of the unneeded dependiences.   
