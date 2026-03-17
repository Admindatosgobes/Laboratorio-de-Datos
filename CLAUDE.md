# Iberdrola EV Charging Network — Project Intelligence

## Identity
You are working on Team Greenlabs' solution for the IE Sustainability
Datathon March 2026 (Iberdrola challenge). The goal is to design an
optimal interurban EV charging network for Spain targeting 2027.

## Critical: Agent Protocol
Before starting ANY work:
1. Read @memory/project_state.md for current status
2. Read @memory/task_board.md for your assigned tasks
3. Read @memory/decisions_log.md for context on past decisions
4. Read @memory/blockers.md for known issues

After completing ANY significant work:
1. Update memory/task_board.md (move task status)
2. Update memory/project_state.md (what changed)
3. Log decisions in memory/decisions_log.md
4. Document issues in memory/blockers.md
5. Add learnings to memory/lessons_learned.md

## Project Structure
@memory/project_structure.md

## Key Parameters (DO NOT CHANGE without team approval)
- 150 kW per charger (MANDATED by datathon rules)
- Max station spacing: 60 km (TEN-T Core), 100 km (TEN-T Comprehensive), 120 km (general)
- Grid thresholds: >=5 MW Sufficient, 1-5 MW Moderate, <1 MW Congested
- Target: 2027 operational scenario
- EV projection: ~2.5M cumulative fleet by Dec 2027

## Deliverables
- File_1.csv: Global Network KPIs (single row)
- File_2.csv: Proposed Charging Locations
- File_3.csv: Friction Points (Moderate/Congested only)
- visualization/bi_map.html: Interactive map
- report/analytical_report.pdf: 3-5 page executive summary
- presentation/pitch.pdf: Max 5 min pitch

## Code Standards
@.claude/rules/code_standards.md

## Data Conventions
@.claude/rules/data_conventions.md