# Technický popis kódu
# Rozpoznání barev
Program má dané barevné rozsahy pro jednotlivé barvy na Rubikově kostce, nejprve vezme šest obrázků poskytnutých uživatelem a detekuje jednotlivé barvy na obrázcích. Vypíše nalezené barvy uživateli a zeptá se ho, zda chce barvy opravit. Pokud ne, program pokračuje dál, pokud ano, uživatel musí manuálně zadat každou barvu, program ho procesem provede. 
# Uložení stavu kostky
Dále program vytvoří slovník listů dle stran kostky a jejich barev (U = up, D = down, w = white, y = yellow atd.). Kostka je v tomto stavu vyřešená, takže další funkce toto přepíše barvami, které poskytl uživatel. Další funkce převede uložený stav kostky do řetězce pro lepší ovládání.
# Metody manipulace s kostkou
Následují tři metody poskytují způsob, jak simulovat pohyby, které nejsou pokryty základními rotacemi a inverzemi ploch. Pomocí těchto metod můžete manipulovat s konkrétními řádky, sloupci nebo vrstvami krychle. Byly by potřeba pro komplexnější metody řešení Rubikovy kostky, ale v tomto kódu nejsou potřeba (ovšem nechtěla jsem je smazávat, zabraly hodně času). 
# Samotné řešení kostky
Dále následuje několik částí kódu, které řeší jednotlivé části kostky pomocí LBL metody, každá část samostatně zapisuje pohyby, které jsou potřeba udělat, a nakonec je vypíše. Jednotlivá čísla v těchto postupech znamenají: self.cube[0]: nahoře, self.cube[1]: dole, self.cube[2]: přední strana, self.cube[3]: levá strana, self.cube[4]: zadní strana, self.cube[5]: pravá strana. Takže self.cube[2][1][1] je nálepka ve druhém řádku a druhém sloupci na přední straně Rubikovy kostky (začíná se zde od nuly, proto 1 znamená druhý).
