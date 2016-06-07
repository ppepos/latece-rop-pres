## Ret2libc - suite

* On peut toujours contrôler l'adresse de retour
* Les arguments sont normalement placés sur la pile **avant** l'adresse de retour.

Objectif:

Retourner dans `__libc_system` avec les bons arguments (`"/bin/sh"`, clairement)
