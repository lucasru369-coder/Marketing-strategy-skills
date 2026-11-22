# Marketing Strategy Skills

A collection of practical, modular skills for marketing research, strategy, planning, and execution.

## Skills

| Skill | Purpose |
|---|---|
| [Marketing Research](./marketing-research/SKILL.md) | Market, audience, category, trend, and localization research. |
| [Competitor Analysis](./competitor-analysis/SKILL.md) | Competitive landscape, positioning, benchmarking, and strategic implications. |
| [Brand Strategy](./brand-strategy/SKILL.md) | Brand positioning, value proposition, messaging, and brand experience. |
| [Marketing Localization](./marketing-localization/SKILL.md) | Adapt global marketing strategy and communication to local markets. |
| [Marketing Planning](./marketing-planning/SKILL.md) | Annual and quarterly priorities, budgets, calendars, resources, and performance governance. |
| [Campaign Strategy](./campaign-strategy/SKILL.md) | Individual campaign objectives, audience insight, concepts, channels, and measurement. |

## Getting started

Read the [Skill usage guide](./docs/skill-usage-guide.md) for the directory, suggested workflows, and a reusable invocation format.

## Templates by workflow

- **Research:** [Research brief](./marketing-research/templates/research-brief.md), [source evaluation log](./marketing-research/templates/source-evaluation-log.md)
- **Competitive analysis:** [Competitor matrix](./competitor-analysis/templates/competitor-matrix.md)
- **Brand:** [Positioning platform](./brand-strategy/templates/positioning-platform.md)
- **Localization:** [Market adaptation checklist](./marketing-localization/templates/market-adaptation-checklist.md)
- **Campaigns:** [Campaign brief](./campaign-strategy/templates/campaign-brief.md), [channel plan](./campaign-strategy/templates/channel-plan.md), [post-campaign review](./campaign-strategy/templates/post-campaign-review.md)
- **Planning:** [Planning templates index](./marketing-planning/templates/README.md), including annual plans, quarterly reviews, budget, prioritization, KPIs, RACI, risk, and decision logs.
- **Cross-functional:** [Marketing brief intake](./docs/brief-intake-template.md), [measurement plan](./docs/measurement-plan-template.md), [decision log](./docs/decision-log-template.md)

## Quality and maintenance

- [Skill quality checklist](./docs/skill-quality-checklist.md)
- [Maintenance policy](./docs/maintenance-policy.md)
- [Contribution guide](./docs/contribution-guide.md)
- [Shared glossary](./docs/glossary.md)

## Planning examples and utility

See the [fictional annual plan](./marketing-planning/examples/fictional-annual-plan.md), [fictional budget scenarios](./marketing-planning/examples/fictional-budget-scenarios.md), and [fictional cross-market plan](./marketing-planning/examples/fictional-cross-market-plan.md) for illustrative applications.

The [budget allocator](./tools/README.md) is a small Python command-line utility for proportional budget allocation. Run its tests with:

```bash
python -m unittest discover -s tests -v
```

A GitHub Actions workflow runs the Python test suite when relevant files change.

## Principles

- Use reliable, current sources and cite them when research is required.
- Separate verified facts, estimates, assumptions, and recommendations.
- Make planning assumptions and trade-offs explicit.
- Never invent market data, budgets, performance results, or resource capacity.
- Turn analysis into clear, actionable decisions.
- Adapt the depth of the framework to the task and available information.
- Use fictional or anonymized examples; do not include personal or confidential information.
