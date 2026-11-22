# Trin 3: Design

🌐 [English](Step-3-Design) · **Dansk** · [Bahasa Malaysia](Step-3-Design-ms)

Milepæl `MIL-003`. Gren og pull request: én for dette trin.

![Use case UC-001 og designets lag](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/raw/branch/main/docs/images/03-design-class-diagram.png)

## Hvad der blev gjort

Use casen UC-001 *Spil spillet*, to beslutninger (ADR-0001: Pillow og pyautogui med en valgfri headless Chrome; ADR-0002: en boks af pixels foran dinosaurussen), domænemodellen DM-001 og klassediagrammet DCD-001, hver gennemgået med en `Go`-post.

## Hvad vi fik ud af det

- En bot er en løkke af se, beslutte, handle. Når de tre navngives som en skærm, en regel og et tastatur, kan reglen testes uden nogen skærm.
- En lille boks af pixels er nok: botten behøver ikke genkende en kaktus, kun opdage, at noget mørkt er foran dinosaurussen.
- At skrive beslutningen ned (ADR) fastholder, hvorfor andre idéer, som skabelongenkendelse eller aflæsning af sidens tilstand, blev udeladt.
