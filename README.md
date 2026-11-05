# Fashion Design Plugin

A Hermes Agent plugin providing a fashion design toolkit: design briefs, tech packs, size sheets, bill of materials, fabric yardage calculator, cost sheets, construction guides, color palettes, measurement charts, and collection planning.

## Disclosure

- **Author:** priticolours
- **License:** MIT
- **Requires Hermes:** >=0.1.0
- **Capabilities:** None (no privileged host surfaces requested)
- **External services:** None. All tools run locally with no network access and no API keys.
- **Data:** Shipped static data only (`data/standard_measurements.json`); no runtime file fetching.
- **Core overrides:** None.
- **Hooks:** None.

## Installation

```bash
hermes plugins install /path/to/fashion-design
# or place in ~/.hermes/plugins/fashion-design
hermes plugins enable fashion-design
```

## Tools

- `design_brief` - structured design brief from concept
- `tech_pack` - technical pack for a garment
- `size_sheet` - size chart / grade sheet
- `bom` - bill of materials
- `fabric_calculator` - fabric yardage estimate
- `cost_sheet` - manufacturing cost estimate
- `construction_guide` - step-by-step construction
- `color_palette` - coordinated color palette
- `measurement_chart` - standard body measurements
- `collection_plan` - collection overview

## Bundled Skill

`fashion-design` skill provides fashion design knowledge (construction basics, measurements, fabric properties, grading rules, tech pack standards).