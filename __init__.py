"""Fashion design plugin registration."""

import logging
from pathlib import Path

from . import schemas, tools

logger = logging.getLogger(__name__)


_TOOLS = [
    ("design_brief", schemas.DESIGN_BRIEF, tools.design_brief),
    ("tech_pack", schemas.TECH_PACK, tools.tech_pack),
    ("size_sheet", schemas.SIZE_SHEET, tools.size_sheet),
    ("bom", schemas.BOM, tools.bom),
    ("fabric_calculator", schemas.FABRIC_CALCULATOR, tools.fabric_calculator),
    ("cost_sheet", schemas.COST_SHEET, tools.cost_sheet),
    ("construction_guide", schemas.CONSTRUCTION_GUIDE, tools.construction_guide),
    ("color_palette", schemas.COLOR_PALETTE, tools.color_palette),
    ("measurement_chart", schemas.MEASUREMENT_CHART, tools.measurement_chart),
    ("collection_plan", schemas.COLLECTION_PLAN, tools.collection_plan),
]


def register(ctx) -> None:
    for name, schema, handler in _TOOLS:
        ctx.register_tool(name=name, toolset="fashion_design", schema=schema, handler=handler)

    # Bundle skill
    skill_path = Path(__file__).parent / "skills" / "fashion-design" / "SKILL.md"
    if skill_path.exists():
        try:
            ctx.register_skill("fashion-design", skill_path, "Fashion design knowledge base")
        except Exception as exc:
            logger.warning("Could not register skill: %s", exc)