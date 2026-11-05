"""Tool schemas for the fashion-design plugin."""

DESIGN_BRIEF = {
    "name": "design_brief",
    "description": (
        "Generate a structured fashion design brief from a concept description. "
        "Use when a designer needs to turn a loose concept into a structured brief "
        "covering silhouette, color palette, fabric suggestions, and key details."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "concept": {"type": "string", "description": "Core concept or inspiration for the design"},
            "target_audience": {"type": "string", "description": "Target customer / audience segment"},
            "season": {"type": "string", "description": "Season or collection (e.g., SS25, FW24)"},
            "price_point": {"type": "string", "description": "Price tier (budget, mid, premium, luxury)"},
        },
        "required": ["concept"],
    },
}

TECH_PACK = {
    "name": "tech_pack",
    "description": (
        "Create a technical pack (tech pack) for a garment with flat sketch description, "
        "measurements, construction, materials, grading, and labeling sections."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "garment_type": {"type": "string", "description": "Garment type (e.g., t-shirt, dress, jacket)"},
            "measurements": {"type": "object", "description": "Key measurements by point of measure"},
            "construction_details": {"type": "string", "description": "Construction / stitch details"},
            "fabric": {"type": "string", "description": "Main fabric description"},
            "trims": {"type": "string", "description": "Trims, buttons, zippers, etc."},
        },
        "required": ["garment_type"],
    },
}

SIZE_SHEET = {
    "name": "size_sheet",
    "description": "Generate a size chart / grade sheet with grading increments across a size range.",
    "parameters": {
        "type": "object",
        "properties": {
            "garment_type": {"type": "string", "description": "Garment type"},
            "base_size": {"type": "string", "description": "Base size (e.g., M)"},
            "size_range": {"type": "array", "items": {"type": "string"}, "description": "List of sizes (e.g., [\"XS\",\"S\",\"M\",\"L\",\"XL\"])"},
            "measurement_points": {"type": "array", "items": {"type": "string"}, "description": "Points of measure to include"},
        },
        "required": ["garment_type"],
    },
}

BOM = {
    "name": "bom",
    "description": "Generate a bill of materials for a garment with quantities, units, suppliers, and costs.",
    "parameters": {
        "type": "object",
        "properties": {
            "garment_type": {"type": "string", "description": "Garment type"},
            "fabric": {"type": "string", "description": "Main fabric"},
            "trims": {"type": "string", "description": "Trims and findings"},
            "hardware": {"type": "string", "description": "Hardware (buttons, zippers, snaps)"},
        },
        "required": ["garment_type"],
    },
}

FABRIC_CALCULATOR = {
    "name": "fabric_calculator",
    "description": "Calculate fabric yardage needed for a garment given fabric width, size, and quantity, including waste factor.",
    "parameters": {
        "type": "object",
        "properties": {
            "garment_type": {"type": "string", "description": "Garment type"},
            "fabric_width": {"type": "number", "description": "Fabric width in inches"},
            "size": {"type": "string", "description": "Size"},
            "quantity": {"type": "integer", "description": "Number of garments"},
        },
        "required": ["garment_type"],
    },
}

COST_SHEET = {
    "name": "cost_sheet",
    "description": "Calculate manufacturing cost estimate per unit and total from fabric, labor, and trims costs.",
    "parameters": {
        "type": "object",
        "properties": {
            "garment_type": {"type": "string", "description": "Garment type"},
            "fabric_cost": {"type": "number", "description": "Fabric cost per unit"},
            "labor_cost": {"type": "number", "description": "Labor cost per unit"},
            "trims_cost": {"type": "number", "description": "Trims cost per unit"},
            "quantity": {"type": "integer", "description": "Production quantity"},
        },
        "required": ["garment_type"],
    },
}

CONSTRUCTION_GUIDE = {
    "name": "construction_guide",
    "description": "Generate step-by-step garment construction instructions with tips for a given skill level.",
    "parameters": {
        "type": "object",
        "properties": {
            "garment_type": {"type": "string", "description": "Garment type"},
            "fabric_type": {"type": "string", "description": "Fabric type (woven, knit, etc.)"},
            "skill_level": {"type": "string", "description": "Skill level: beginner, intermediate, advanced"},
        },
        "required": ["garment_type"],
    },
}

COLOR_PALETTE = {
    "name": "color_palette",
    "description": "Suggest coordinated color palettes for a collection with hex codes and Pantone references.",
    "parameters": {
        "type": "object",
        "properties": {
            "season": {"type": "string", "description": "Season (e.g., Spring/Summer 2025)"},
            "trend": {"type": "string", "description": "Trend keyword"},
            "mood": {"type": "string", "description": "Mood / feeling"},
        },
        "required": [],
    },
}

MEASUREMENT_CHART = {
    "name": "measurement_chart",
    "description": "Generate standard body measurements for a given size, gender, and age range.",
    "parameters": {
        "type": "object",
        "properties": {
            "size": {"type": "string", "description": "Size (e.g., M, 8, 32)"},
            "gender": {"type": "string", "description": "Gender: women, men, unisex, kids"},
            "age_range": {"type": "string", "description": "Age range (e.g., adult, teen, child 6-8)"},
        },
        "required": ["size"],
    },
}

COLLECTION_PLAN = {
    "name": "collection_plan",
    "description": "Plan a fashion collection with pieces, color story, and fabric story.",
    "parameters": {
        "type": "object",
        "properties": {
            "season": {"type": "string", "description": "Season"},
            "number_of_pieces": {"type": "integer", "description": "Number of pieces in the collection"},
            "theme": {"type": "string", "description": "Collection theme"},
        },
        "required": [],
    },
}