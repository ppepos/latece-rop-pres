## Return-Oriented Programming

Utilisation de séquences d'instructions machine appellés *gadgets*.
Chaque *gadget* se termine par un `return` et existe déjà dans les segments exécutables du code binaire de l'application.
En chaînant ces gadgets, l'attaquant peut exécuter des opérations arbitraires sans injecter de code additionnel.
