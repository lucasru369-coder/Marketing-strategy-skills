# Skill Maintenance Policy

This document defines a lightweight process for keeping the repository reliable and reusable.

## Scope

Apply this policy to every independent skill, template, example, and helper script.

## Skill quality requirements

Each skill should make the following clear:

- **Purpose:** the problem it is designed to solve.
- **When to use:** suitable scenarios and boundaries.
- **Inputs:** information required to produce a useful result.
- **Workflow:** ordered steps that can be followed consistently.
- **Outputs:** expected deliverables and their structure.
- **Quality checks:** how to evaluate completeness and usefulness.
- **Limitations:** assumptions, risks, and situations requiring human review.

## Change types

| Change | Examples | Review focus |
|---|---|---|
| Editorial | Clarify wording, fix typos | Accuracy and consistency |
| Template | Add or revise a worksheet | Completeness and ease of use |
| Workflow | Change steps or decision logic | Reproducibility and edge cases |
| Tooling | Add scripts or automated checks | Input validation, tests, safe defaults |
| Structural | Rename or move skills | Links, navigation, discoverability |

## Contribution checklist

Before committing a change:

- [ ] Keep examples fictional and clearly labeled.
- [ ] Remove personal, confidential, and customer-identifying information.
- [ ] Use neutral sample names, dates, and figures.
- [ ] Check Markdown headings, tables, and relative links.
- [ ] Keep each skill focused on one coherent responsibility.
- [ ] Explain new inputs, outputs, and assumptions.
- [ ] Add or update tests when executable code changes.
- [ ] Avoid presenting estimates or illustrative figures as facts.

## Review cadence

Review the repository periodically, and whenever a workflow or external platform changes materially.

A maintenance review should check:

1. Broken links and outdated references.
2. Duplicate or conflicting instructions across skills.
3. Missing inputs or unclear deliverables.
4. Examples that no longer match the workflow.
5. Scripts that lack validation or test coverage.

## Versioning approach

Use a simple semantic versioning convention when releases are introduced:

- **Major:** incompatible changes to a skill's expected inputs, outputs, or workflow.
- **Minor:** backward-compatible capabilities, templates, or examples.
- **Patch:** clarifications, corrections, and non-breaking improvements.

Individual skills may evolve independently. Document meaningful changes in their own changelog or release notes when needed.
