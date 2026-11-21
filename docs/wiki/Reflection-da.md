# Refleksionsjournal

🌐 [English](Reflection) · **Dansk** · [Bahasa Malaysia](Reflection-ms)

Opgave til dag 94: Automatisér Googles dinosaurspil. Wikien har denne journal på engelsk, dansk og bahasa malaysia.

## Hvordan jeg greb projektet an

Jeg læste opgaven først og målte derefter spillet, før jeg skrev kode. Jeg åbnede det i en headless Chrome, tog skærmbilleder og fandt ud af, hvor jordlinjen er, hvor mange skærmpixels de 600 spilpixels fylder (956 i mit vindue, skala 1,6), og hvilken grå farve dinosaurussen og kaktusserne er tegnet med. Derefter planlagde jeg seks milepæle, hver med sin egen gren og pull request, designede botten som tre små dele (en skærm, en regel og et tastatur), byggede og testede den del, der ser, og koblede først derefter tastaturet på og finjusterede botten mod det rigtige spil.

## Hvad der var nemt

- At finde spillet: jordlinjen er rækken med flest mørke pixels, og dens længde giver skalaen. Én løkke over rækkerne klarer det.
- At arbejde med pixels: et skærmbillede i gråtoner er kun en liste af bytes, så beskæring, optælling og sammenligning kræver intet billedbibliotek.
- At teste den del, der ser: testene tegner en kaktus på tre linjer, og 55 af dem kører på under 0,2 sekunder uden en skærm.

## Hvad der var svært

- Timing. Den samme bot fik 233 i én kørsel og 2310 i en anden. Et skærmbillede tager titusinder af millisekunder, så kaktussen ses nogle billeder for sent, og ved høj fart er nogle billeder mange pixels. Min første zone på 30 spilpixels døde efter få hundrede point. En zone, der rækker 75 spilpixels frem, hjalp mest, men rækker den for langt, hopper dinosaurussen for tidligt og lander på kaktussen.
- Spillet strækkes først til fuld bredde efter det første tastetryk, så søgningen efter jordlinjen før start mislykkedes. Botten trykker nu mellemrum, venter et sekund og søger derefter.
- I browseren rullede mellemrumstasten siden og flyttede spillet væk fra det sted, botten havde fundet. At skjule sidens rulning løste det.
- At undgå skrivebordet i test. Alle live-kontroller kører i en headless Chrome, så Pillow- og pyautogui-adapterne testes med stand-ins og bruges kun for alvor af den, der kører botten.

## Hvad jeg ville gøre anderledes næste gang

- Måle spillets fart ud fra to blik på den samme forhindring i stedet for at gætte den ud fra tiden siden start.
- Bruge pil ned til at falde hurtigere efter et hop, dukke sig under høje fugle og klare to kaktusser tæt på hinanden; de dødsfald, jeg så på, var alle sådanne tilfælde.
- Gemme et billede af det sidste billede i hver kørsel og køre mange spil i træk, så en ændret konstant bedømmes på ti kørsler og ikke på én.
- Prøve skrivebordsadapterne én gang i en engangs Windows Sandbox for at have set dem virke fra ende til anden.

## Største læring

En bot er en løkke af se, beslutte og handle, og det svære er tiden, ikke koden. At holde reglen som en ren funktion af bytes gjorde den let at teste, og tynde adaptere gjorde dem lette at skifte: headless Chrome spiller med samme regel som skrivebordet. Over otte kørsler med den endelige kode var scorerne 233, 432, 547, 625, 704, 1109, 1301 og 2310, så en enkelt god kørsel beviser lidt, og en tabel over kørsler fortæller sandheden.
