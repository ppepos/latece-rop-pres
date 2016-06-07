### En détail

1.  `push` les arguments sur la pile (dans l'ordre inverse)
2. `call`
  1.  `push` l'adresse de la prochaine instruction (adresse de retour)
  2.  change le pointeur d'instruction pour l'adresse spécifiée
  3.  exécute le sous-programme
  4.  `pop` l'adresse de la prochaine instruction dans `eip`
3.  continue l'exécution normalement

