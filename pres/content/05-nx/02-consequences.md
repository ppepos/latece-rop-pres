## Conséquences sur notre exploit

* Si le pointeur d'instruction pointe sur un secteur qui n'est pas exécutable: *Segfault*!
* La pile, et donc notre *input* n'est plus exécutable.
* Exploit absolument plus fonctionnel. `=/`
