<img width="250" height="250" alt="LF" src="https://github.com/user-attachments/assets/4eb13ca4-ea9d-4de5-bdf0-46e615902c3e" />

Open-source digital lithography software for UV exposure systems and educational semiconductor manufacturing.

# LithoForge Process
### Fritzing SVG → resin-LCD UV mask → exposed board

This covers the pipeline of turning a PCB layer from Fritzing into a mask
that a resin printer's LCD can display for a timed UV exposure.

---

## 1. Export the artwork from Fritzing
- Open your board in Fritzing's **PCB view**.
- **File → Export → [layer you need] → SVG** (copper/etch layer, silkscreen, or
  soldermask — whichever layer you're exposing).
- Note which side of the board this layer represents (top/bottom copper) — you'll
  need this for the mirror decision in step 3.

## 2. Prep the physical board
- Clean the copper-clad board (isopropyl alcohol, no fingerprints/oxidation).
- If it isn't pre-sensitized, apply photoresist and let it cure per your
  resist's instructions.
- Keep the resist's protective film on until you're ready to expose — don't
  expose it to light early.

## 3. Convert the SVG in LithoForge
- Load the SVG.
- Pick your printer's LCD preset (or enter custom resolution + physical screen
  size) — this is what determines the pixel scale.
- Set the artwork's real-world size in mm (auto-detected from the SVG when
  possible, override if it looks wrong).
- **Mirror**: turn on if you're exposing through the back of the board or the
  layer is otherwise reversed from how it'll sit on the LCD — check against
  which copper side faces the light.
- **Invert**: on/off depending on whether your resist is positive or negative
  — you want the traces you're *keeping* to end up as the correct color for
  your resist type (white = UV passes through).
- Leave **pure black/white** on — no gray edges, cleaner exposure boundary.
- Set exposure time and layer height (rough starting point; you'll fine-tune
  in UVtools or by test exposure).
- Export as **.sl1**.

## 4. Bring it into UVtools
- **File → Open** the `.sl1` file — it should load directly as a 1-layer file.
- Double-check exposure time and any printer-specific light settings.
- **File → Save As**, and pick your exact printer model so it writes the
  correct native format (`.ctb`, `.pwmx`, `.goo`, etc.) for your machine's
  firmware.

## 5. Expose the board
- Copy the file to USB, load it on the printer.
- Resin vat empty/clean — you're using the LCD as a UV light source, not
  printing resin.
- Peel the resist's protective film right before exposing.
- Place the board directly against the screen, resist side facing the light.
- Run the "print" — it will just display the mask and count down the
  exposure time.
(It may be desirable to create a fixtured 3d print or other method in order to index the board in a repeatable way.)

## 6. Develop
- Rinse the board and remove the undeveloped portions of photoresist.

## 7. Etch
- Etch in ferric chloride / cupric chloride (or your preferred etchant) until
  bare copper is removed from the open areas.
- Rinse, then strip the remaining resist.

## 8. Finish
- Inspect traces, clean up, drill holes, tin if desired.

---

**Dial-in note:** exposure time is the variable most worth test-strip
tuning — same file, a few different times on scrap board, and go with
whichever gives the cleanest trace edges before committing your real board.



## License

LithoForge is licensed under the MIT License. See the LICENSE file for details.

Copyright © 2026 Benjamin Lloyd and Contributors.
