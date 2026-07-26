# Hex Road Builder

A hex-grid track-laying game built in `pygame`. Connect a power source to
every city through a road network, while a river, lakes, hills, and a
small industrial economy (forest/sawmill, mine/forge, vineyard) push back
against just blanketing the map.

## Running it

```
pip install pygame
python hex_road_builder.py
```

An instructions screen shows on launch - press **SPACE** to start.

## Goal

Power every city (they turn yellow once built on, glow once powered) by
connecting a road network back to your gold **power-source** tile. The
power source starts face-up in hand slot 4 - place it whenever you like,
it doesn't have to be your first move.

## Controls

| Input | Action |
|---|---|
| `1`-`5` / click a hand slot | select that tile |
| `6` | deselect |
| `R` | rotate the selected tile |
| Click a board hex | place the selected tile there |
| `D` / Overdraw button | draw a spare tile into hand |
| Undo button | remove the last placed tile |
| Trash button | discard the selected tile for a random replacement |
| Shop | sacrifice the selected tile + pay, get an exact shape |
| `N` / Reroll button | regenerate the whole map |

## Hand economy

- Baseline hand size is 3 - placing a tile auto-refills back up to 3 for
  free, but never refills you *above* 3.
- Overdraw adds one tile beyond that: free if you're below 3, costs more
  the fuller your hand already is, and is blocked once you're holding 5.
- The Shop lets you sacrifice a hand tile plus a listed price to get a
  specific shape instead of a random draw - useful when the deck keeps
  handing you the wrong piece.

## Scoring

- Placing a tile costs score (more on a river tile, even more on a hill).
- Plain tiles score nothing on their own, powered or not - only cities,
  vineyards, and matched industry pairs actually pay off.
- Cities and vineyards score live, the moment they're powered.
- Once **every** city is powered, a one-time tally fires:
  - `min(powered forests, powered sawmills) x 10`
  - `min(powered mines, powered forges) x 10`
  - every road-arm that reaches the map's edge is a bonus (a clean exit)
  - every road-arm that dangles into a tile that doesn't connect back is
    a penalty (a genuinely unfinished route)
- Score can go negative. That's fine - it's meant to happen if you
  overbuild.

## Map features

- **River**: flows down the map from a random top-row tile. Building a
  track on it costs extra.
- **Lakes**: up to 4, clustered near the river. Nothing can be built on
  them.
- **Hills**: 4, confined to the top half of the map (away from the very
  edges). Building on one costs the most of any terrain.
- **Forest / Sawmill**: 2 each, forests biased left, sawmills right.
- **Mine / Forge**: mines seeded next to hills, forges seeded near
  cities (skipping around a bit so they don't cluster).
- **Vineyard**: 2, placed near river tiles scanning bottom-up.

## Modding

Every number that shapes the map or the economy is collected in one
block near the top of the file, under `TUNABLE CONSTANTS` - feature
counts (`NUM_HILLS`, `NUM_MINES`, ...), placement costs, live scoring
values, the one-time pairing/border bonuses, and hand-economy costs.
Change a number there (or press Reroll / restart) to feel the effect -
no need to go hunting through the generation or scoring functions.

## Known rough edges / ideas not built yet

- No sound. A small "Songs" catalogue + a play/pause/skip music player
  was floated as a bold future idea - `pygame.mixer` would handle it,
  just didn't fit this pass.
- No persistence - closing the window loses the game; Reroll is the only
  "reset."
- A Java port has been discussed as a way to put this in front of more
  people online - nothing ported yet, this file is pure Python/pygame.
