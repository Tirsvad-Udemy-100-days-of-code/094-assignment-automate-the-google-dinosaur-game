# Trin 4: Syn

🌐 [English](Step-4-Vision) · **Dansk** · [Bahasa Malaysia](Step-4-Vision-ms)

Milepæl `MIL-004`. Gren og pull request: én for dette trin.

![Detektionsboksen tegnet på et rigtigt spilbillede og testene](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/04-vision-detection-box.png)

## Hvad der blev gjort

Den del af botten, der ser: værdiobjekterne `Box` og `Frame`, `find_game_area` (jordlinjen giver position og skala), `GameArea.detection_box` og `is_collision` (er der en forhindring i pixlerne?). Enhedstests bruger billeder lavet i testen, så der ikke skal bruges en skærm.

## Hvad vi fik ud af det

- Et skærmbillede i gråtoner er kun en liste af tal; jordlinjen er rækken med flest mørke pixels, og dens bredde fortæller skærmens skala.
- Når den mest almindelige grå værdi tages som baggrund, virker én regel i dagtilstand (mørkt på hvidt) og nattilstand (lyst på sort).
- Fordi reglerne arbejder på rene bytes, kan testene tegne en kaktus på tre linjer og afprøve botten uden at åbne spillet.
