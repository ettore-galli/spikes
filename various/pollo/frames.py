# Sostituisci interamente il vecchio frames.py con questo codice.
# Disegno di profilo per una somiglianza reale. Dimensioni circa 14 righe x 30 caratteri.
# Totale 15 frame, compatibile al 100% con il main originale.

CHICKEN_FRAMES = [
    # --- SEQUENZA 1: Camminata fluida (Frame 1-5) ---
    # Frame 1: Posizione standard, zampa destra avanti
    "\n\n\n\n\n"
    "         _   _ \n"
    "       _(-)-(-)  _ \n"
    "      (  o >    // \n"
    "       \__  ___// \n"
    "         /     \\ \n"
    "        /       | \n"
    "       |   _     | \n"
    "       |  ( )    | \n"
    "        \_______/ \n"
    "          ||  || \n"
    "          ||  || \n"
    "         /__\/__\\ \n",

    # Frame 2: Corpo leggermente in avanti, ali che si muovono
    "\n\n\n\n\n"
    "         _   _ \n"
    "       _(-)-(-)  _ \n"
    "      (  o >    // \n"
    "       \__  ___//  \n"
    "         /     \\__ \n"
    "        /         \\\n"
    "       |   _       |\n"
    "       |  ( )      |\n"
    "        \_______  / \n"
    "          //  || \n"
    "         //   || \n"
    "        /__\ /__\\ \n",

    # Frame 3: Coda che si alza, zampa sinistra avanti
    "\n\n\n\n\n"
    "         _   _     _ \n"
    "       _(-)-(-)   // \n"
    "      (  o >     // \n"
    "       \__  ____// \n"
    "         /     \\ \n"
    "        /       | \n"
    "       |   _     | \n"
    "       |  ( )    | \n"
    "        \_______/ \n"
    "          ||  \\\\ \n"
    "          ||   \\\\ \n"
    "         /__\  /__\\ \n",

    # Frame 4: Passo intermedio
    "\n\n\n\n\n"
    "         _   _ \n"
    "       _(-)-(-)  _ \n"
    "      (  o >    // \n"
    "       \__  ___// \n"
    "         /     \\ \n"
    "        /       | \n"
    "       |   _     | \n"
    "       |  ( )    | \n"
    "        \_______/ \n"
    "          ||  || \n"
    "          ||  || \n"
    "         /__\/__\\ \n",

    # Frame 5: Ali vicine al corpo, collo teso
    "\n\n\n\n\n"
    "           _   _ \n"
    "         _(-)-(-)  _ \n"
    "        (  o >    // \n"
    "         \__  ___// \n"
    "           /     \\ \n"
    "          /       | \n"
    "         |   _     | \n"
    "         |  ( )    | \n"
    "          \_______/ \n"
    "            ||  || \n"
    "            ||  || \n"
    "           /__\/__\\ \n",


    # --- SEQUENZA 2: La Beccata (Frame 6-10) ---
    # Frame 6: Il collo si abbassa verso il terreno
    "\n\n\n\n\n\n"
    "                 _ \n"
    "         _   _  // \n"
    "       _(-)-(-)// \n"
    "      (  o >  // \n"
    "       \____ // \n"
    "       /       \\ \n"
    "      /         | \n"
    "     |   _       | \n"
    "     |  ( )      | \n"
    "      \_________/ \n"
    "         ||  || \n"
    "         ||  || \n"
    "        /__\/__\\ \n",

    # Frame 7: Più giù, il becco sfiora il suolo
    "\n\n\n\n\n\n\n"
    "                   _ \n"
    "                  // \n"
    "          _   _  // \n"
    "        _(-)-(-)// \n"
    "       (  o >  // \n"
    "        \_____//_ \n"
    "        /        \\ \n"
    "       |   _      | \n"
    "       |  ( )     | \n"
    "        \________/ \n"
    "          ||  || \n"
    "          ||  || \n"
    "         /__\/__\\ \n",

    # Frame 8: Becco a terra (mangia)
    "\n\n\n\n\n\n\n\n"
    "                    _ \n"
    "                   // \n"
    "           _   _  // \n"
    "         _(-)-(-)// \n"
    "  ______/  o >  // \n"
    " /             / \n"
    "|    _        | \n"
    "|   ( )       | \n"
    " \___________/ \n"
    "    ||   || \n"
    "    ||   || \n"
    "   /__\ /__\\ \n",

    # Frame 9: Risalita, becco chiuso con chicco ideale
    "\n\n\n\n\n\n"
    "                 _ \n"
    "         _   _  // \n"
    "       _(-)-(-)// \n"
    "      (  o >  // \n"
    "       \____ // \n"
    "       /       \\ \n"
    "      /         | \n"
    "     |   _       | \n"
    "     |  ( )      | \n"
    "      \_________/ \n"
    "         ||  || \n"
    "         ||  || \n"
    "        /__\/__\\ \n",

    # Frame 10: Ritorno in posizione eretta
    "\n\n\n\n\n"
    "         _   _ \n"
    "       _(-)-(-)  _ \n"
    "      (  o >    // \n"
    "       \__  ___// \n"
    "         /     \\ \n"
    "        /       | \n"
    "       |   _     | \n"
    "       |  ( )    | \n"
    "        \_______/ \n"
    "          ||  || \n"
    "          ||  || \n"
    "         /__\/__\\ \n",


    # --- SEQUENZA 3: Il Verso "COCO'" (Frame 11-15) ---
    # Frame 11: Testa alta, becco spalancato ( < diventa = )
    "\n\n\n\n"
    "         _   _ \n"
    "       _(-)-(-)  _ \n"
    "      (  o =    // \n"
    "       \__  ___// \n"
    "         /     \\ \n"
    "        /       | \n"
    "       |   _     | \n"
    "       |  ( )    | \n"
    "        \_______/ \n"
    "          ||  || \n"
    "          ||  || \n"
    "         /__\/__\\ \n",

    # Frame 12: Becco aperto e sussulto della coda
    "\n\n\n\n"
    "         _   _     _ \n"
    "       _(-)-(-)   // \n"
    "      (  o =     // \n"
    "       \__  ____// \n"
    "         /     \\ \n"
    "        /       | \n"
    "       |   _     | \n"
    "       |  ( )    | \n"
    "        \_______/ \n"
    "          ||  || \n"
    "          ||  || \n"
    "         /__\/__\\ \n",

    # Frame 13: Massimo sforzo del verso, ali spiegate
    "\n\n\n\n"
    "         _   _ \n"
    "       _(-)-(-)  _ \n"
    "      (  o =    // \n"
    "       \__  ___//  \n"
    "         /     \\__ \n"
    "        /         \\\n"
    "       |   _       |\n"
    "       |  ( )      |\n"
    "        \_______  / \n"
    "          ||  || \n"
    "          ||  || \n"
    "         /__\/__\\ \n",

    # Frame 14: Il verso finisce, calo di tensione
    "\n\n\n\n"
    "         _   _ \n"
    "       _(-)-(-)  _ \n"
    "      (  o >    // \n"
    "       \__  ___// \n"
    "         /     \\ \n"
    "        /       | \n"
    "       |   _     | \n"
    "       |  ( )    | \n"
    "        \_______/ \n"
    "          ||  || \n"
    "          ||  || \n"
    "         /__\/__\\ \n",

    # Frame 15: Quiete prima del reset del loop
    "\n\n\n\n\n"
    "         _   _ \n"
    "       _(-)-(-)  _ \n"
    "      (  o >    // \n"
    "       \__  ___// \n"
    "         /     \\ \n"
    "        /       | \n"
    "       |   _     | \n"
    "       |  ( )    | \n"
    "        \_______/ \n"
    "          ||  || \n"
    "          ||  || \n"
    "         /__\/__\\ \n"
]


THE_END_SCREEN = """




         _   _ 
       _(-)-(-)  _ 
      (  z z    //     _________________
       \__  ___//     /                 \\
         /     \     <     XXXXXXXX     |
        /       |     \_________________/
       |   _     |
       |  ( )    |
        \_______/ 
          ||  || 
          ||  || 
         /__\/__\\ 

"""

