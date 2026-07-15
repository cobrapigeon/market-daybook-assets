# Market Daybook — social templates & headline-card renderer

Bland brand-colored background cards with a headline set in **Sora**, for the daily
social engine. Images are served to Buffer via **raw GitHub URLs** (direct 200, no
redirect — this is the fix for the Google Drive 303 problem).

## Layout
```
social/templates/
  render_card.py                 # renderer (CLI + importable)
  fonts/Sora[wght].ttf           # vendored brand font (no download needed at runtime)
  backgrounds/                   # blank reusable backgrounds
    portrait_dark_blank.png
    portrait_light_blank.png
  generated/                     # daily output cards (committed by the engine)
    YYYY-MM-DD_ig.png
```

## Usage
```
python3 render_card.py --headline "A specific plan names the trigger, the invalidation, the size, and the exit — before you enter." \
    --size portrait --style dark --out generated/2026-07-14_ig.png
```

## Raw URL pattern (what goes into Buffer)
```
https://raw.githubusercontent.com/cobrapigeon/market-daybook-assets/main/social/templates/generated/<FILE>.png
```

## Palette
Graphite `#191B20` · Recovery Red `#E34B3E` · Ledger Bone `#F1EDE3`. Sora, weight 700.

Dark card is the primary look; light is an occasional variant. IG default is portrait (1080×1350).
