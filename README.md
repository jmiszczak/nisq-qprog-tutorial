# nisq-qprog-tutorial
Some tests with QAOA, VQE, annealers and other procedures for NISQ quantum computers.


## Managing environements

File `nisq-qprog-tutorial.yml` contains definition of virtual environement for Anacoda. To create new enviroment run

    conda env create -f nisq-qprog-tutorial.yml
  
To updated existing environement run
    
    conda env update -f nisq-qprog-tutorial.yml --prune
 
Option `--prune` results in the remove of the unneeded dependiences.

## Managing Anaconda installation

Some useful commands for managing Anaconda environements.

Cleaning unused packages:

    conda clean --all -y
    
Updating environement:

    conda update -n nisq-qprog-tutorial --all -y
