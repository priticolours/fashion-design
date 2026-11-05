"""Tool handlers for the fashion-design plugin."""

import json

# ---------------------------------------------------------------------------
# Shared data
# ---------------------------------------------------------------------------

BODY_MEASUREMENTS = {
    "women": {
        "XS": {"bust": 32, "waist": 25, "hip": 35, "shoulder": 14, "inseam": 30, "height": 64},
        "S": {"bust": 34, "waist": 27, "hip": 37, "shoulder": 14.5, "inseam": 30.5, "height": 65},
        "M": {"bust": 36, "waist": 29, "hip": 39, "shoulder": 15, "inseam": 31, "height": 66},
        "L": {"bust": 38, "waist": 31, "hip": 41, "shoulder": 15.5, "inseam": 31.5, "height": 67},
        "XL": {"bust": 40, "waist": 33, "hip": 43, "shoulder": 16, "inseam": 32, "height": 68},
        "XXL": {"bust": 42, "waist": 35, "hip": 45, "shoulder": 16.5, "inseam": 32.5, "height": 69},
    },
    "men": {
        "XS": {"chest": 34, "waist": 28, "hip": 34, "shoulder": 16, "inseam": 31, "height": 67},
        "S": {"chest": 36, "waist": 30, "hip": 36, "shoulder": 17, "inseam": 31.5, "height": 68},
        "M": {"chest": 38, "waist": 32, "hip": 38, "shoulder": 17.5, "inseam": 32, "height": 69},
        "L": {"chest": 40, "waist": 34, "hip": 40, "shoulder": 18, "inseam": 32.5, "height": 70},
        "XL": {"chest": 42, "waist": 36, "hip": 42, "shoulder": 18.5, "inseam": 33, "height": 71},
        "XXL": {"chest": 44, "waist": 38, "hip": 44, "shoulder": 19, "inseam": 33.5, "height": 72},
    },
}

GRADE_INCREMENTS = {
    "women": {"bust": 2, "waist": 2, "hip": 2, "shoulder": 0.5, "inseam": 0.5},
    "men": {"chest": 2, "waist": 2, "hip": 2, "shoulder": 0.5, "inseam": 0.5},
}

MEASUREMENT_POINTS_BY_GARMENT = {
    "t-shirt": ["chest", "waist", "hip", "shoulder", "sleeve_length", "body_length"],
    "shirt": ["chest", "waist", "hip", "shoulder", "sleeve_length", "body_length", "collar"],
    "dress": ["bust", "waist", "hip", "shoulder", "dress_length", "sleeve_length"],
    "pants": ["waist", "hip", "inseam", "outseam", "thigh", "knee", "hem"],
    "skirt": ["waist", "hip", "skirt_length"],
    "jacket": ["chest", "waist", "hip", "shoulder", "sleeve_length", "body_length"],
    "coat": ["chest", "waist", "hip", "shoulder", "sleeve_length", "body_length"],
}

FABRIC_YARDAGE_BASE = {
    "t-shirt": 1.25,
    "shirt": 1.75,
    "dress": 2.5,
    "pants": 1.5,
    "skirt": 1.25,
    "jacket": 2.0,
    "coat": 3.0,
    "blouse": 1.5,
}

SIZE_FACTOR = {"XS": 0.9, "S": 0.95, "M": 1.0, "L": 1.05, "XL": 1.1, "XXL": 1.15}

COLOR_PALETTES = {
    "spring": [
        {"name": "Soft Petal", "hex": "#F7C5CC", "pantone": "Pantone 13-1520 TPX"},
        {"name": "Sage Mist", "hex": "#A8C3A0", "pantone": "Pantone 15-6316 TPX"},
        {"name": "Butter Cream", "hex": "#F5E6C8", "pantone": "Pantone 12-0719 TPX"},
        {"name": "Sky Blue", "hex": "#A7D8F0", "pantone": "Pantone 14-4318 TPX"},
        {"name": "Warm Coral", "hex": "#F08A7B", "pantone": "Pantone 16-1546 TPX"},
    ],
    "summer": [
        {"name": "Ocean Teal", "hex": "#2A9D8F", "pantone": "Pantone 17-5126 TPX"},
        {"name": "Sunflower", "hex": "#F4A261", "pantone": "Pantone 15-1157 TPX"},
        {"name": "Crisp White", "hex": "#FFFFFF", "pantone": "Pantone 11-0601 TPX"},
        {"name": "Deep Navy", "hex": "#1D3557", "pantone": "Pantone 19-4025 TPX"},
        {"name": "Bright Lime", "hex": "#B5E48C", "pantone": "Pantone 13-0550 TPX"},
    ],
    "fall": [
        {"name": "Rust", "hex": "#B7410E", "pantone": "Pantone 18-1448 TPX"},
        {"name": "Olive", "hex": "#556B2F", "pantone": "Pantone 18-0430 TPX"},
        {"name": "Camel", "hex": "#C19A6B", "pantone": "Pantone 16-1334 TPX"},
        {"name": "Burgundy", "hex": "#800020", "pantone": "Pantone 19-1629 TPX"},
        {"name": "Charcoal", "hex": "#36454F", "pantone": "Pantone 19-4006 TPX"},
    ],
    "winter": [
        {"name": "Icy Blue", "hex": "#DCE6F1", "pantone": "Pantone 12-4005 TPX"},
        {"name": "Emerald", "hex": "#046307", "pantone": "Pantone 18-5634 TPX"},
        {"name": "Plum", "hex": "#673147", "pantone": "Pantone 19-2617 TPX"},
        {"name": "Silver", "hex": "#C0C0C0", "pantone": "Pantone 14-5002 TPX"},
        {"name": "Black", "hex": "#000000", "pantone": "Pantone 19-4008 TPX"},
    ],
}

CONSTRUCTION_STEPS = {
    "t-shirt": [
        "Cut fabric pieces: front, back, sleeves, neckband.",
        "Sew shoulder seams (right sides together).",
        "Attach neckband: fold, quarter-mark, stretch to fit neckline, stitch.",
        "Sew sleeves to armholes.",
        "Sew side seams and underarm in one continuous seam.",
        "Hem sleeves and bottom with twin needle or coverstitch.",
        "Press all seams.",
    ],
    "dress": [
        "Cut all pieces and mark notches/darts.",
        "Sew darts on front and back bodice.",
        "Join bodice front and back at shoulders.",
        "Insert zipper (center back or side).",
        "Attach skirt to bodice, matching notches.",
        "Sew side seams.",
        "Finish neckline with facing or bias binding.",
        "Hem skirt.",
        "Press.",
    ],
    "pants": [
        "Cut front and back leg pieces.",
        "Sew front pockets.",
        "Join front and back at side seams.",
        "Sew inseam.",
        "Sew crotch seam.",
        "Attach waistband, insert elastic or button.",
        "Hem legs.",
        "Press.",
    ],
    "jacket": [
        "Cut all pieces including interfacing.",
        "Fuse interfacing to collar, lapel, cuffs.",
        "Sew darts and princess seams.",
        "Join shoulders and side seams.",
        "Set sleeves.",
        "Attach collar and lapel.",
        "Install lining.",
        "Finish hems and buttonholes.",
        "Press.",
    ],
}


def _json(obj):
    return json.dumps(obj, indent=2)


def design_brief(args, **kwargs):
    try:
        concept = args.get("concept", "")
        target = args.get("target_audience", "general")
        season = args.get("season", "all-season")
        price = args.get("price_point", "mid")
        silhouette_map = {
            "budget": "relaxed, commercial silhouettes with broad appeal",
            "mid": "balanced silhouettes mixing classic and trend",
            "premium": "refined, tailored silhouettes with elevated details",
            "luxury": "sculptural, statement silhouettes with couture finishing",
        }
        fabric_map = {
            "spring": ["cotton poplin", "linen", "lightweight jersey"],
            "summer": ["linen", "rayon", "cotton voile"],
            "fall": ["wool blend", "twill", "corduroy"],
            "winter": ["wool", "cashmere blend", "quilted nylon"],
        }
        season_key = season.split()[0].lower() if season else "all-season"
        fabrics = fabric_map.get(season_key, ["cotton", "poly blend", "jersey"])
        brief = {
            "concept": concept,
            "target_audience": target,
            "season": season,
            "price_point": price,
            "silhouette": silhouette_map.get(price, silhouette_map["mid"]),
            "color_palette": [c["name"] + " " + c["hex"] for c in COLOR_PALETTES.get(season_key, COLOR_PALETTES["spring"])[:4]],
            "fabric_suggestions": fabrics,
            "key_details": [
                "signature stitching",
                "branded hardware",
                "functional pockets",
                "adjustable fit elements",
            ],
            "design_notes": f"Build around the concept '{concept}' for {target}; keep {price}-tier finishing.",
        }
        return _json(brief)
    except Exception as e:
        return json.dumps({"error": str(e)})


def tech_pack(args, **kwargs):
    try:
        gtype = args.get("garment_type", "")
        measurements = args.get("measurements") or {}
        construction = args.get("construction_details", "")
        fabric = args.get("fabric", "")
        trims = args.get("trims", "")
        points = MEASUREMENT_POINTS_BY_GARMENT.get(gtype.lower(), ["chest", "waist", "hip", "length"])
        meas_table = {}
        for p in points:
            meas_table[p] = measurements.get(p, "TBD")
        pack = {
            "garment_type": gtype,
            "flat_sketch_description": f"Front and back flat sketch of {gtype} with labeled points of measure.",
            "measurements": meas_table,
            "construction": construction or "Standard construction; see construction_guide.",
            "materials": {
                "main_fabric": fabric or "TBD",
                "trims": trims or "TBD",
                "thread": "matching, 100% polyester",
                "interfacing": "as required",
            },
            "grading": "Grade from base size using standard increments; see size_sheet.",
            "labeling": {
                "care_label": "Machine wash cold, tumble dry low",
                "size_label": "Printed size",
                "brand_label": "Woven main label",
                "country_of_origin": "TBD",
            },
            "points_of_measure": points,
        }
        return _json(pack)
    except Exception as e:
        return json.dumps({"error": str(e)})


def size_sheet(args, **kwargs):
    try:
        gtype = args.get("garment_type", "")
        base = args.get("base_size", "M")
        sizes = args.get("size_range") or ["XS", "S", "M", "L", "XL", "XXL"]
        points = args.get("measurement_points") or MEASUREMENT_POINTS_BY_GARMENT.get(gtype.lower(), ["chest", "waist", "hip", "length"])
        # base body measurements for the garment's relevant gender default women
        gender = "women"
        base_meas = BODY_MEASUREMENTS[gender].get(base, BODY_MEASUREMENTS[gender]["M"])
        # build chart
        size_index = {s: i for i, s in enumerate(sizes)}
        base_idx = size_index.get(base, len(sizes) // 2)
        chart = {}
        for s in sizes:
            delta = size_index[s] - base_idx
            row = {}
            for p in points:
                bv = base_meas.get(p, base_meas.get("chest", 36))
                # garment ease: add 2-4 inches; keep simple
                ease = 4 if p in ("chest", "bust", "hip") else 0
                inc = GRADE_INCREMENTS[gender].get(p, 1) if p in GRADE_INCREMENTS[gender] else 1
                val = (bv + ease) + (delta * inc)
                row[p] = round(val, 1)
            chart[s] = row
        result = {
            "garment_type": gtype,
            "base_size": base,
            "size_range": sizes,
            "measurement_points": points,
            "grade_increments": GRADE_INCREMENTS[gender],
            "size_chart": chart,
            "units": "inches",
            "notes": "Garment measurements include ease. Adjust per fabric and fit.",
        }
        return _json(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def bom(args, **kwargs):
    try:
        gtype = args.get("garment_type", "")
        fabric = args.get("fabric", "main fabric")
        trims = args.get("trims", "standard trims")
        hardware = args.get("hardware", "standard hardware")
        items = [
            {"item": "Main fabric", "description": fabric, "quantity": 2.5, "unit": "yards", "supplier": "Fabric Co", "cost": 8.0},
            {"item": "Lining", "description": "poly lining", "quantity": 1.0, "unit": "yards", "supplier": "Fabric Co", "cost": 3.0},
            {"item": "Thread", "description": "polyester thread", "quantity": 1, "unit": "spool", "supplier": "Trim Supp", "cost": 1.5},
            {"item": "Trims", "description": trims, "quantity": 1, "unit": "set", "supplier": "Trim Supp", "cost": 2.0},
            {"item": "Hardware", "description": hardware, "quantity": 1, "unit": "set", "supplier": "Hardware Inc", "cost": 1.5},
            {"item": "Labels", "description": "brand/size/care", "quantity": 3, "unit": "pcs", "supplier": "Label Co", "cost": 0.5},
            {"item": "Packaging", "description": "polybag + hangtag", "quantity": 1, "unit": "set", "supplier": "Pack Co", "cost": 0.75},
        ]
        total = round(sum(i["cost"] for i in items), 2)
        result = {
            "garment_type": gtype,
            "bill_of_materials": items,
            "total_material_cost_per_unit": total,
            "currency": "USD",
        }
        return _json(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def fabric_calculator(args, **kwargs):
    try:
        gtype = args.get("garment_type", "")
        width = args.get("fabric_width", 45)
        size = args.get("size", "M")
        qty = args.get("quantity", 1) or 1
        base = FABRIC_YARDAGE_BASE.get(gtype.lower(), 1.5)
        size_f = SIZE_FACTOR.get(str(size).upper(), 1.0)
        # adjust for width: 60in is more efficient
        width_factor = 45.0 / float(width) if width else 1.0
        per_garment = base * size_f * width_factor
        waste = 0.12
        per_with_waste = per_garment * (1 + waste)
        total = per_with_waste * qty
        result = {
            "garment_type": gtype,
            "fabric_width_inches": width,
            "size": size,
            "quantity": qty,
            "yardage_per_garment": round(per_with_waste, 3),
            "total_yardage": round(total, 3),
            "waste_factor": waste,
            "units": "yards",
            "notes": "Includes 12% waste. Verify with marker/lay plan for production.",
        }
        return _json(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def cost_sheet(args, **kwargs):
    try:
        gtype = args.get("garment_type", "")
        fc = float(args.get("fabric_cost", 0) or 0)
        lc = float(args.get("labor_cost", 0) or 0)
        tc = float(args.get("trims_cost", 0) or 0)
        qty = int(args.get("quantity", 1) or 1)
        per_unit = fc + lc + tc
        overhead = per_unit * 0.10
        total_cost_per_unit = per_unit + overhead
        total = total_cost_per_unit * qty
        suggested_retail = total_cost_per_unit * 2.5
        result = {
            "garment_type": gtype,
            "cost_breakdown_per_unit": {
                "fabric": fc,
                "labor": lc,
                "trims": tc,
                "overhead_10pct": round(overhead, 2),
                "total_cost_per_unit": round(total_cost_per_unit, 2),
            },
            "quantity": qty,
            "total_production_cost": round(total, 2),
            "suggested_retail_price": round(suggested_retail, 2),
            "currency": "USD",
        }
        return _json(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def construction_guide(args, **kwargs):
    try:
        gtype = args.get("garment_type", "")
        fabric = args.get("fabric_type", "woven")
        skill = args.get("skill_level", "intermediate")
        steps = CONSTRUCTION_STEPS.get(gtype.lower(), [
            "Cut all pattern pieces.",
            "Prepare and finish raw edges.",
            "Assemble main seams.",
            "Attach closures and trims.",
            "Finish hems.",
            "Press garment.",
        ])
        tips = {
            "beginner": "Use a longer stitch length for basting; press as you go.",
            "intermediate": "Use appropriate needle and presser foot for fabric.",
            "advanced": "Consider couture finishes and hand-stitching details.",
        }
        result = {
            "garment_type": gtype,
            "fabric_type": fabric,
            "skill_level": skill,
            "steps": [{"step": i + 1, "instruction": s} for i, s in enumerate(steps)],
            "tips": tips.get(skill, tips["intermediate"]),
            "estimated_time_hours": max(2, len(steps)),
        }
        return _json(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def color_palette(args, **kwargs):
    try:
        season = (args.get("season") or "spring").lower()
        trend = args.get("trend", "")
        mood = args.get("mood", "")
        key = "spring"
        for k in ("spring", "summer", "fall", "winter"):
            if k in season:
                key = k
                break
        palette = COLOR_PALETTES.get(key, COLOR_PALETTES["spring"])
        result = {
            "season": season,
            "trend": trend,
            "mood": mood,
            "palette": palette,
            "usage_notes": "Use 1-2 hero colors, 2 supporting, 1 neutral for balance.",
        }
        return _json(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def measurement_chart(args, **kwargs):
    try:
        size = str(args.get("size", "M"))
        gender = (args.get("gender") or "women").lower()
        age = args.get("age_range", "adult")
        g = "men" if gender.startswith("m") else "women"
        if gender.startswith("u"):
            g = "women"
        table = BODY_MEASUREMENTS.get(g, BODY_MEASUREMENTS["women"])
        meas = table.get(size.upper(), None)
        if meas is None:
            # approximate from M
            base = table.get("M", table[list(table.keys())[2]])
            meas = {k: round(v + 1 * (ord(size[0]) % 5 - 2), 1) for k, v in base.items()}
        result = {
            "size": size,
            "gender": gender,
            "age_range": age,
            "body_measurements": meas,
            "units": "inches",
            "notes": "Standard body measurements; adjust for target fit and brand standards.",
        }
        return _json(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def collection_plan(args, **kwargs):
    try:
        season = args.get("season", "Spring/Summer")
        n = int(args.get("number_of_pieces", 6) or 6)
        theme = args.get("theme", "core collection")
        pieces = []
        types = ["t-shirt", "shirt", "pants", "dress", "jacket", "skirt", "coat", "blouse"]
        for i in range(n):
            pieces.append({
                "piece": i + 1,
                "name": f"Piece {i + 1}",
                "garment_type": types[i % len(types)],
                "color": "hero" if i < 2 else "supporting",
            })
        result = {
            "season": season,
            "theme": theme,
            "number_of_pieces": n,
            "collection_overview": pieces,
            "color_story": "2 hero colors, 2 supporting, 1 neutral",
            "fabric_story": "Mix of natural fibers and performance blends",
            "notes": "Balance tops and bottoms; include at least one outerwear.",
        }
        return _json(result)
    except Exception as e:
        return json.dumps({"error": str(e)})