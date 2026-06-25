---
description: "Task list for Análisis de Precios de Carburantes con GenAI implementation"
---

# Tasks: Análisis de Precios de Carburantes con GenAI

**Input**: Design documents from `specs/001-carburantes-ia/`  
**Prerequisites**: plan.md (required), spec.md (required)

**Organization**: Tasks grouped by user story (US0-US5) to enable independent implementation.

---

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story (US0, US1, US2, etc.)
- Include exact file paths

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and notebook structure

- [x] T001 Create notebook file `notebook/Analisis_Carburantes_v0_1.ipynb` in Colab-compatible format
- [x] T002 Create directory structure: `prompts/`, `posts/`, organize `prompts/` by functionality (ingesta/, limpieza/, visualizacion/, features/, modelado/)
- [x] T003 Initialize git tracking for notebook and prompts/ directory

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core setup that MUST complete before user stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [P] Add cell: Import libraries in `notebook/` (pandas, matplotlib, scikit-learn) with inline comments in Spanish
- [x] T005 [P] Add cell: Helper functions for Colab compatibility (ej: verificar entorno, descargar datos)
- [x] T006 Create `.gitignore` for notebook outputs and temporary files

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 0 - Documentación de Versión e Iteraciones (Priority: P0)

**Goal**: First cell displays notebook version and iteration counter

**Independent Test**: Execute cell. Verify output: "Versión: v0.1.0 | Iteración: 1"

- [x] T007 [US0] Create first cell in `notebook/`: metadata display with version (v0.1.0) and iteration (1)
- [x] T008 [US0] Add comment explaining why versioning matters in iterative analysis

**Checkpoint**: User Story 0 complete and visible 

---

## Phase 4: User Story 1 - Cargar y Formatear Datos Públicos (Priority: P1)

**Goal**: Dataset loaded from datos.gob.es with correct encoding and types

**Independent Test**: Run cell. Verify: dataframe exists, 11k+ rows, columns intact, no character corruption

- [x] T009 [P] [US1] Add cell: Download dataset from datos.gob.es (URL + error handling in Spanish)
- [x] T010 [US1] Add cell: Load CSV with ISO-8859-1 encoding and decimal separator handling
- [x] T011 [US1] Add cell: Explore dataset structure (`.info()`, `.head()`, `.dtypes()`, `.shape`)
- [x] T012 [US1] Create prompt file `prompts/ingesta/descargar_dataset.md` (prompt + result + reflection on what GenAI helped)
- [x] T013 [US1] Create prompt file `prompts/ingesta/explorar_estructura.md`

**Checkpoint**: User Story 1 complete - dataset loaded and explored

---

## Phase 5: User Story 2 - Limpiar y Normalizar Datos (Priority: P2)

**Goal**: Data validation functions and cleaning applied

**Independent Test**: Run validation. Verify: anomalies reported, brands normalized, coverage analysis shown

- [x] T014 [P] [US2] Add cell: Create function `validar_precios()` - report prices ≤0€ or >3€
- [x] T015 [P] [US2] Add cell: Create function `normalizar_marcas()` - unify brand name variations (REPSOL, Repsol, repsol → REPSOL)
- [x] T016 [P] [US2] Add cell: Create function `analizar_nulos()` - report null percentage per column
- [x] T017 [US2] Add cell: Execute all validation functions and display results
- [x] T018 [US2] Create prompt file `prompts/limpieza/validar_precios.md`
- [x] T019 [US2] Create prompt file `prompts/limpieza/normalizar_marcas.md`

**Checkpoint**: User Story 2 complete - data cleaned and validated

---

## Phase 6: User Story 3 - Análisis Exploratorio con Visualizaciones (Priority: P2)

**Goal**: 4 specific visualizations answering business questions

**Independent Test**: Generate 4 plots. Verify: all provinces shown, trend visible, geographic correlation clear, brand distribution shown

### Visualization Tasks

- [x] T020 [P] [US3] Add cell: Bar plot - Average price per province (pregunta: ¿qué provincia es más cara?)
- [x] T021 [P] [US3] Add cell: Line plot - Temporal evolution of prices (pregunta: ¿tendencia de precios?)
- [x] T022 [P] [US3] Add cell: Scatter plot - Geographic coordinates vs price (pregunta: ¿ubicación afecta precio?)
- [x] T023 [P] [US3] Add cell: Box plot - Price distribution by brand (pregunta: ¿marca afecta precio?)

### Visualization Documentation

- [x] T024 [US3] Create prompt file `prompts/visualizacion/precio_por_provincia.md`
- [x] T025 [US3] Create prompt file `prompts/visualizacion/evolucion_temporal.md`
- [x] T026 [US3] Create prompt file `prompts/visualizacion/ubicacion_vs_precio.md`
- [x] T027 [US3] Create prompt file `prompts/visualizacion/distribucion_por_marca.md`

**Checkpoint**: User Story 3 complete - EDA finished with 4 visualizations

---

## Phase 7: User Story 4 - Ingeniería de Variables Asistida (Priority: P3)

**Goal**: Create 3+ new features from existing data

**Independent Test**: Generate features. Verify: values correct, no nulls in derived columns, types appropriate

- [x] T028 [P] [US4] Add cell: Create `es_fin_de_semana` feature from date column
- [x] T029 [P] [US4] Add cell: Create `distancia_a_ref` feature from lat/long (distance to reference point)
- [x] T030 [P] [US4] Add cell: Create `region_geografica` feature (north/center/south) from coordinates

### Feature Engineering Documentation

- [x] T031 [US4] Create prompt file `prompts/features/crear_fin_semana.md`
- [x] T032 [US4] Create prompt file `prompts/features/distancia_punto_referencia.md`
- [x] T033 [US4] Create prompt file `prompts/features/region_geografica.md`

**Checkpoint**: User Story 4 complete - new features created and validated

---

## Phase 8: User Story 5 - Modelado y Predicción de Tendencias (Priority: P3)

**Goal**: Simple regression model with interpretable metrics

**Independent Test**: Train model. Verify: R² ≥ 0.5, RMSE reasonable (±0.X€), predictions in realistic range (1-2€/L)

### Model Implementation

- [x] T034 [US5] Add cell: Prepare data for modeling (X, y split, train/test 80/20)
- [x] T035 [US5] Add cell: Train simple regression model (scikit-learn LinearRegression)
- [x] T036 [US5] Add cell: Calculate metrics (R², RMSE, MAE) on test set
- [x] T037 [US5] Add cell: Generate 7-day price predictions
- [x] T038 [US5] Add cell: Interpret metrics in business language (Spanish, non-technical)

### Model Documentation

- [x] T039 [US5] Create prompt file `prompts/modelado/entrenar_modelo_regresion.md`
- [x] T040 [US5] Create prompt file `prompts/modelado/interpretar_metricas.md`

**Checkpoint**: User Story 5 complete - model trained and interpreted

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final refinement and documentation

- [ ] T041 Write post Markdown at `posts/Reflexion_GenAI_Analisis_Carburantes.md` with sections:
  - Problema (dataset, pregunta de negocio)
  - Proceso con GenAI (cómo cada fase usó prompts)
  - Aprendizajes (qué funcionó bien, qué sorpresas)
  - Limitaciones (del análisis, del modelo)
  - Guía de Uso del Repo (dónde notebook, dónde prompts/)
  - Extensiones sugeridas (qué mejoraría el análisis)

- [ ] T042 Validate notebook in new Colab session (fresh browser): 
  - Copy notebook URL
  - Open in incognito window
  - Run all cells start to finish
  - Verify execution <5 minutes
  - Verify no modifications needed

- [ ] T043 [P] Audit Spanish compliance:
  - [ ] All cell comments in Spanish
  - [ ] All output messages in Spanish
  - [ ] No English variable names
  - [ ] No English error messages

- [ ] T044 Code compactness audit:
  - [ ] Count active code lines (excludes markdown, comments)
  - [ ] Verify total ≤150 lines
  - [ ] Each cell does one clear thing
  - [ ] No duplicate code

- [ ] T045 Create README.md at repo root with:
  - Project overview (1-2 sentences)
  - How to run (link to notebook in Colab)
  - Directory structure explanation
  - License (MIT)

- [ ] T046 Final version bump: Update notebook metadata to v0.1.0 (final) if all tests pass

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-8)**: 
  - US0 (Phase 3): Depends on Foundational - runs first (metadata)
  - US1 (Phase 4): Depends on Foundational + US0 - blocks US2, US3, US4, US5
  - US2 (Phase 5): Depends on US1 - independent from US3/US4/US5
  - US3 (Phase 6): Depends on US1 - independent from US2/US4/US5  
  - US4 (Phase 7): Depends on US1 - independent from US2/US3/US5
  - US5 (Phase 8): Depends on US1 (can also use US4 features) - independent from US2/US3
- **Polish (Phase 9)**: Depends on all user stories - final phase

### Parallel Opportunities

**After Foundational (Phase 2) completes**:

```bash
# All these can run in parallel:
- US0 (Phase 3): Metadata cell
- US1 Phase 4 data load tasks (parallel)
- US2 Phase 5 cleaning functions (parallel)
- US3 Phase 6 visualization (parallel)
- US4 Phase 7 features (parallel)
```

**Within each User Story**:

- **US1**: T009, T010, T011 can run in parallel (different cells)
- **US2**: T014, T015, T016 can run in parallel (different functions)
- **US3**: T020, T021, T022, T023 can run in parallel (different plots)
- **US4**: T028, T029, T030 can run in parallel (different features)
- **US3/US2/US4**: Prompt creation (T024-T033) can all run in parallel

**Polish Phase**: All T041-T046 can run in parallel except T042 (validation) and T046 (final version)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: US0 (metadata)
4. Complete Phase 4: US1 (data loading)
5. **STOP and VALIDATE**: Test notebook in Colab. If passes, demo/commit.
6. Deploy/demo if ready

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add US0 → Metadata visible
3. Add US1 → Data loaded → Test independently → Deploy/Demo (MVP!)
4. Add US2 → Cleaned data → Test independently → Deploy/Demo
5. Add US3 → EDA visualizations → Test independently → Deploy/Demo
6. Add US4 → New features → Test independently → Deploy/Demo
7. Add US5 → Model ready → Full analysis → Deploy/Demo
8. Polish → Post + docs ready

Each story adds value without breaking previous stories.

### Parallel Team Strategy (if multi-person)

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: US1 (data loading)
   - Developer B: US2 (cleaning) + US3 (visualization)
   - Developer C: US4 (features) + US5 (model)
3. Stories complete and integrate independently
4. Team does Polish together

---

## Notes

- [P] = parallelizable (different files, no blocking dependencies)
- [Story] = maps to user story for traceability
- Each user story should be independently completable and testable
- Verify tests pass before moving to next story
- Commit after each story completion
- Use GenAI prompts for each analysis step (documented in `prompts/`)
