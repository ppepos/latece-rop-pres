## Ret2libc

* Trouver du code pour faire ce que l'on veut dans le code exécutable existant.
* On a accès à n'importe quel segment de code exécutable.
* libc!

Objectif:

Retourner dans `__libc_system` avec les bons arguments (`"/bin/sh"`, clairement!)
