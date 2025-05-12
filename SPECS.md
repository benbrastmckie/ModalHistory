# Repository Restructuring Specification

This document outlines a plan to integrate the contents of the `INTEGRATE/` directory into the main repository structure for the Modal History course.

## Current Structure Analysis

The repository is currently organized into:

1. Main content directories:
   - `1_modal_logic/` (00-02 weeks)
   - `2_intensional_semantics/` (03-06 weeks)
   - `3_counterfactual_conditionals/` (08-10 weeks)
   - `4_constitutive_explanation/` (12-14 weeks)

2. Content to be integrated from `INTEGRATE/`:
   - `readings/` - Weekly reading lists with notes
   - `problem_sets/` - Problem sets and student projects
   - `final_projects/` - Final project instructions and templates

## Integration Plan

### 1. Reading Lists and Notes

For each week, we'll integrate the readings information from `INTEGRATE/readings/XX_week.md` into the corresponding `X_module_name/XX_week/XX_week.md` file.

| Source | Destination | Notes |
|--------|-------------|-------|
| `INTEGRATE/readings/00_week.md` | `1_modal_logic/00_week/00_week.md` | Merge content, maintain existing lecture notes |
| `INTEGRATE/readings/01_week.md` | `1_modal_logic/01_week/01_week.md` | Merge reading list |
| `INTEGRATE/readings/02_week.md` | `1_modal_logic/02_week/02_week.md` | Merge reading list |
| `INTEGRATE/readings/03_week.md` | `2_intensional_semantics/03_week/03_week.md` | Merge reading list |
| `INTEGRATE/readings/04_week.md` | `2_intensional_semantics/04_week/04_week.md` | Merge reading list |
| `INTEGRATE/readings/05_week.md` | `2_intensional_semantics/05_week/05_week.md` | Merge reading list |
| `INTEGRATE/readings/06_week.md` | `2_intensional_semantics/06_week/06_week.md` | Merge reading list |
| `INTEGRATE/readings/08_week.md` | `3_counterfactual_conditionals/08_week/08_week.md` | Merge reading list |
| `INTEGRATE/readings/09_week.md` | `3_counterfactual_conditionals/09_week/09_week.md` | Merge reading list |
| `INTEGRATE/readings/10_week.md` | `3_counterfactual_conditionals/10_week/10_week.md` | Merge reading list |
| `INTEGRATE/readings/12_week.md` | `4_constitutive_explanation/12_week/12_week.md` | Merge reading list |
| `INTEGRATE/readings/13_week.md` | `4_constitutive_explanation/13_week/13_week.md` | Merge reading list |

For weeks that have special notes, we'll also integrate the content from `INTEGRATE/readings/notes/` into the appropriate week directories.

### 2. Problem Sets

Create a new top-level directory `problem_sets/` and organize the problem sets within, with a README.md at the root:

```
problem_sets/
├── README.md (renamed from collaboration.md)
├── 01_tooling/
│   ├── practice_git.md
│   ├── tooling.md
│   └── latex_template files...
├── 02_axiomatic_proofs/
│   ├── axiomatic_proofs.md
│   └── solution files...
...and so on
```

### 3. Final Projects

Create a new top-level directory `final_projects/` and move the contents, with a README.md at the root:

```
final_projects/
├── README.md (renamed from final_projects.md)
├── jupyter_example/
│   ├── README.md
│   └── exclusion_demo.ipynb
├── latex_example/
│   ├── README.md
│   ├── assets/
│   │   ├── bib_style.bst
│   │   ├── formatting.sty
│   │   ├── modal_history.bib
│   │   └── notation.sty
│   └── final_template.tex
└── miguel_final_pres_outline.md
```

### 4. Special Notes Directory

Create a new top-level directory `notes/` for the general notes that are not week-specific:

```
notes/
├── automated_reasoning.md
├── bit_vectors.md
└── lattice_theory.md
```

### 5. Update Main README.md

Update the main README.md by integrating content from INTEGRATE/README.md and adding:
- Links to problem sets directory
- Links to final projects directory
- Links to special notes

## Implementation Steps

1. **Create New Directories**:
   ```bash
   mkdir -p problem_sets
   mkdir -p final_projects
   mkdir -p notes
   ```

2. **Copy Week-Specific Reading Content**:
   - For each week, integrate the content from `INTEGRATE/readings/XX_week.md` into the corresponding `X_module_name/XX_week/XX_week.md` file.
   - Review each file to ensure proper merging (maintain existing lecture notes while adding reading lists).

3. **Move Problem Sets and Create README**:
   ```bash
   # Copy and rename collaboration.md to README.md in problem_sets directory
   cp INTEGRATE/problem_sets/collaboration.md problem_sets/README.md
   
   # For each problem set (01-08)
   mkdir -p problem_sets/01_tooling
   cp -r INTEGRATE/problem_sets/01_pset/* problem_sets/01_tooling/
   
   # Continue for remaining problem sets with appropriate naming
   ```

4. **Move Final Projects and Create README**:
   ```bash
   # Copy and rename final_projects.md to README.md in final_projects directory
   cp INTEGRATE/final_projects/final_projects.md final_projects/README.md
   
   # Copy the rest of the contents
   cp -r INTEGRATE/final_projects/* final_projects/
   # Remove the original file to avoid duplication
   rm final_projects/final_projects.md
   ```

5. **Move Special Notes**:
   ```bash
   cp -r INTEGRATE/readings/notes/* notes/
   ```

6. **Update Main README.md**:
   - Integrate content from INTEGRATE/README.md
   - Add links to new directories
   - Update course structure information
   - Keep the existing content and formatting where appropriate

7. **Verify Project Structure**:
   - Ensure all files have been properly moved
   - Check that all links within documents are still valid
   - Update any relative links as needed

8. **Remove INTEGRATE Directory** (after thorough verification):
   ```bash
   # Only after confirming everything is properly integrated
   rm -rf INTEGRATE/
   ```

## File Content Integration Details

For each week's content file, follow this pattern:
1. Preserve existing lecture notes in the destination file
2. Add reading list at the top of the file (if not already present)
3. Use consistent formatting across all files

## Main README.md Integration

When integrating INTEGRATE/README.md into the main README.md:
1. Keep the existing overview, course description, and module information
2. Add the problem sets section with links to the new problem_sets/README.md
3. Add the final projects section with links to the new final_projects/README.md
4. Update all internal links to point to the new directory structure

Example sections to add to main README.md:
```markdown
## Problem Sets

Eight problem sets to be completed collaboratively. See the [Problem Sets README](problem_sets/README.md) for details on collaboration and submission guidelines.

## Final Projects

The final project constitutes 40% of the grade for the formal track and 80% for the historical track. See the [Final Projects README](final_projects/README.md) for complete details and templates.
```

## Post-Integration Tasks

1. Review all links in the documents to ensure they point to the correct locations
2. Verify that all assets (images, etc.) are properly referenced
3. Test all repository navigation from the README.md file
4. Commit changes with a clear description of the restructuring