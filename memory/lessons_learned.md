# Lessons Learned

**Purpose:** Capture what worked, what didn't, and patterns discovered for future reference.

---

## Project Setup & Research

### ✅ What Worked Well

**Comprehensive upfront assumptions research (2026-03-16)**
- Spending 6 hours researching all 20 assumptions with official sources
- Cross-validating against IEA, AFIR, CNMC, DGT publications
- Result: Solid foundation, no major assumption changes needed later

**Understanding data structure before coding (2026-03-17)**
- Exploring Ministry API, file formats, and relationships first
- Testing actual downloads and parsing sample files
- Result: Clear data ingestion plan, avoided architectural mistakes

**Creating structured roadmap early (2026-03-17)**
- Breaking 96 hours of work into 39 trackable issues
- Clear dependencies and effort estimation
- Result: Team has concrete plan, no ambiguity about scope

### ⚠️ What Could Be Improved

**Too much upfront planning detail**
- Could have started with basic download script sooner
- Risk of over-engineering before validating approach
- Lesson: Balance planning vs doing

---

## Technical Approaches

### ✅ What Worked Well

**Choosing official Ministry data over third-party wrappers**
- Rutas por Carretera vs pyspainmobility library
- Going directly to source avoided compatibility issues
- Result: More reliable, up-to-date data with official backing

**Shared memory system for agent coordination**
- CLAUDE.md + memory/ markdown files
- Git-tracked, human-readable, agent-accessible
- Result: Clear handoffs between agent sessions

### ⚠️ What Could Be Improved

**Constants file maintenance**
- Should have updated constants.py immediately after assumptions research
- Now it's a blocker for all notebook execution
- Lesson: Keep code and documentation in sync

---

## Data & Analysis

### ✅ What Worked Well

**Grid reality acceptance rather than avoidance**
- 87% of substations being Congested is the authentic constraint
- Making it the center of strategic narrative, not hiding it
- Result: Realistic business case for Iberdrola

**Three-tier spacing constraints (AFIR compliance)**
- 60km/100km/120km instead of binary TEN-T/non-TEN-T
- Direct mapping to regulation requirements
- Result: Defensible compliance story

### 🔄 Still Learning

**Set Cover LP complexity**
- Not yet implemented, potential debugging challenges ahead
- May need fallback to simpler greedy approach
- Watch: implementation complexity vs timeline pressure

---

## Collaboration & Process

### ✅ What Worked Well

**Structured documentation**
- references/assumptions.md, references/glossary.md
- Everything has sources and rationale
- Result: Easy to explain decisions to team/jury

### ⚠️ What Could Be Improved

**Early team coordination**
- Research phase was solo, team input could have been valuable
- Risk of too much individual direction-setting
- Lesson: Involve team in key architectural decisions

### 🔄 Still Learning

**Agent vs human task allocation**
- Which tasks benefit from agent assistance vs human judgment
- How to hand off work mid-stream between agents
- Balance automation vs human oversight

---

## Risk Management

### ✅ What Worked Well

**Identifying critical path early**
- Download script → demand model → optimization → outputs
- Clear priority ranking of tasks
- Result: Team knows what can't slip

**Multiple data source validation**
- Cross-checking IEA vs ANFAC vs DGT projections
- Using official sources over blog posts/wikis
- Result: Defensible assumptions under jury scrutiny

### ⚠️ Areas of Concern

**LP optimization complexity**
- Mathematical optimization is highest-risk technical component
- Single point of failure for core deliverable
- Mitigation: Plan fallback approach (greedy + post-hoc validation)

**Grid data interpretation**
- 87% congestion could be data artifact vs reality
- Need validation against independent sources
- Mitigation: Cross-check with CNMC publications

---

## Patterns for Future Projects

### Do More Of
1. **Upfront data exploration** — understand before architecting
2. **Official source preference** — government/NGO over commercial APIs
3. **Assumption documentation** — cite everything, explain reasoning
4. **Structured memory systems** — especially for multi-agent work

### Do Less Of
1. **Perfect planning** — start building sooner, iterate
2. **Solo decision-making** — involve team in key architectural choices
3. **Optimistic timeline estimates** — add buffer for debugging

### Watch For
1. **Technical debt accumulation** — keep constants/docs in sync
2. **Single points of failure** — especially complex algorithms
3. **External dependency risks** — have fallback plans

---

**Next retrospective:** After M1 (data acquisition complete)