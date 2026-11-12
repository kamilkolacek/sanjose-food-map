# Hella Good Food

An interactive, video-game-style map of 20 classic, low-cost food spots in San Jose and the surrounding area: pho, banh mi, ramen, burgers, taquerias, Filipino, Korean, donuts and sweets.

**Live map:** https://kamilkolacek.github.io/sanjose-food-map/

## Features

- 20 hand-picked spots with chunky 3D-style food pins (burger, taco, donut and more)
- San Jose landmarks, including the SAP Center (Sharks arena)
- Visited checklist, saved in your browser
- Looping original chiptune music that starts when you tap a pin
- YouTube review links for each spot
- Light, colorful cartoon look; no map tiles, with roads and water drawn as vectors

## Spots

| Category | Spots |
|---|---|
| Vietnamese | Pho Ha Noi, Bun Bo Hue An Nam, Duc Huong Sandwiches |
| Japanese | Minato, Kumako Ramen |
| Burgers | Burger Bar, Campus Burgers, Falafel's Drive-In |
| Tacos | La Victoria Taqueria, Super Taqueria, Taqueria Tlaquepaque, Tacos Santiaguito, Tacos Los Tres Reyes |
| Filipino | Gabrielle's Food Market, Max's Restaurant |
| Korean | SGD Tofu House |
| Donuts | Rollo's Donuts, Manley's Donut Shop |
| Sweets | Peters' Bakery, Shuei-Do Manju Shop |

Spots were researched in November 2026. Hours and prices change, so check before you go.

## Project layout

- `index.html`: the built, self-contained page (served by GitHub Pages)
- `src/template.html`: page source
- `src/data.js`: spots, roads, highway shields
- `src/leaflet.css`: Leaflet 1.9.4 styles, inlined into the build
- `src/build.py`: rebuilds `index.html` from the three files above
- `data/`: geocoded spot coordinates and landmarks

To rebuild after editing: `python3 src/build.py`

## Tech notes

- Leaflet 1.9.4 with no tile layer
- Road and water geometry from the U.S. Census TIGERweb REST API
- Spot coordinates geocoded with the Census geocoder and OpenStreetMap Nominatim
- Music is generated live with the Web Audio API

## Sibling project

[Xmas-Adventure](https://github.com/kamilkolacek/Xmas-Adventure): a toddler-friendly Christmas events map for the South Bay.

Built with Claude Code.
