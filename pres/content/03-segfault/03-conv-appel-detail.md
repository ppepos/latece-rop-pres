### En détail

1. On pousse les arguments sur la pile (dans l'ordre inverse)
2. `call`
  1. On `push` l'adresse de la prochaine instruction (adresse de retour)
  1. On `push` l'adresse de base du cadre d'activation
  2. On change le pointeur d'instruction pour l'adresse spécifiée
  3. On exécute le sous-programme
  4. On `pop` l'adresse de base du cadre sauvegardé dans `ebp`
  4. On `pop` l'adresse de la prochaine instruction dans `eip`
3. On continue l'exécution normalement

