# Trin 5: Bot

🌐 [English](Step-5-Bot) · **Dansk** · [Bahasa Malaysia](Step-5-Bot-ms)

Milepæl `MIL-005`. Gren og pull request: én for dette trin.

![En headless kørsel af botten med dens score](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/05-bot-headless-run.png)

## Hvad der blev gjort

Botten kører: use casen `play_game`, portene for skærm, tastatur og ur, skrivebordsadapterne (`DesktopScreen` med Pillow, `hit` og `DesktopKeyboard` med pyautogui), headless Chrome-adapteren og kommandolinjen `python -m dino_bot`. Testene bruger falske afhængigheder. En første headless kørsel døde ved en score på 270, så konstanterne blev justeret; de bedste kørsler når nu 2000 og mere, og scoren varierer fra kørsel til kørsel.

## Hvad vi fik ud af det

- At tage kun en lille boks er hurtigt nok; et fuldt skærmbillede ved hvert blik ville være for langsomt til at nå at reagere.
- Spillet bliver hurtigere, så boksen skal række længere frem, efterhånden som tiden går. At udvide den fra 30 til 75 spilpixels var den største forbedring.
- En headless Chrome lader dig se botten spille uden at tage mus og tastatur; pyautogui beholder sin fail-safe (mus i et hjørne stopper botten) ved kørsel på skrivebordet.
