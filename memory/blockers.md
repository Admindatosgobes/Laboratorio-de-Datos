# Current Blockers

**Last updated:** 2026-03-17  
**Updated by:** Claude agent  

---

## 🚨 High Priority Blockers

### Blocker #1: Outdated Constants File
**Issue:** `src/constants.py` contains placeholder values, not approved assumptions  
**Impact:** NB 06-08 will fail or produce wrong results  
**Blocked tasks:** All demand modeling, optimization, grid analysis  
**Resolution:** Update constants.py with values from `references/assumptions.md`  
**Owner:** TBD (team meeting)  
**Est. fix time:** 1 hour  

### Blocker #2: Missing Rutas por Carretera Data
**Issue:** No segment-level traffic flow data downloaded  
**Impact:** Cannot build demand model (NB 06)  
**Blocked tasks:** All modeling work, optimization, outputs  
**Resolution:** Create and run `scripts/download_rutas.py`  
**Dependencies:** Need script framework (#4 in roadmap)  
**Owner:** TBD (team meeting)  
**Est. fix time:** 3-4 hours total  

### Blocker #3: Team Role Assignments Pending
**Issue:** No clear ownership of tasks, potential work conflicts  
**Impact:** Cannot start parallel execution, unclear accountability  
**Resolution:** Mar 18 team meeting to assign roles  
**Deadline:** Mar 18  

---

## 🔶 Medium Priority Blockers

### Blocker #4: Incomplete Pipeline Execution
**Issue:** NB 02-05 written but never executed  
**Impact:** Missing processed datasets for modeling  
**Blocked tasks:** Demand model needs processed road/IMD data  
**Dependencies:** Constants file update (#1)  
**Est. fix time:** 2-3 hours  

### Blocker #5: Incomplete Source Code
**Issue:** `src/geo_utils.py` and `src/optimization.py` have NotImplementedError stubs  
**Impact:** Cannot run NB 07-08  
**Resolution:** Implement missing functions (BallTree, Set Cover LP)  
**Est. fix time:** 6-8 hours  

---

## 🔵 Low Priority Blockers

### Blocker #6: Additional Data Sources Not Acquired
**Issue:** Missing elevation, weather, cross-border traffic data  
**Impact:** Less rich analysis, but not critical for core deliverables  
**Resolution:** Research and download during M1 phase  
**Est. fix time:** 4 hours  

### Blocker #7: No Coding Standards Established
**Issue:** No shared code style, potential inconsistency across team  
**Impact:** Code review friction, integration issues  
**Resolution:** Create `.claude/rules/` standards  
**Est. fix time:** 1 hour  

---

## 🟢 Resolved Blockers

### ✅ Data Structure Understanding (Resolved 2026-03-17)
**Issue:** Unclear how Rutas por Carretera files relate and join  
**Resolution:** Explored Ministry API, confirmed file formats and relationships  
**Result:** Clear data ingestion plan for NB 06  

### ✅ Assumption Uncertainty (Resolved 2026-03-16)
**Issue:** Many project parameters were placeholder values  
**Resolution:** Comprehensive research against official sources  
**Result:** 20 assumptions documented with sources in `references/assumptions.md`  

---

## Escalation Path

**For immediate blockers (#1-3):**
1. Raise in team meeting Mar 18
2. Assign owner with clear deadline
3. Check resolution in next standup

**For technical issues:**
1. Document in this file with specifics
2. Tag relevant team member
3. Add to sprint retrospective if pattern

**For external dependencies:**
1. Identify alternative approach
2. Document risk in `memory/project_state.md`
3. Escalate to team lead if timeline impact