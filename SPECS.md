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

For each week, we'll integrate the content from `INTEGRATE/readings/XX_week.md` into the corresponding `X_module_name/XX_week/XX_week.md` file, carefully synthesizing the content to maintain the full text of both files.

| Source | Destination | Merge Strategy |
|--------|-------------|----------------|
| `INTEGRATE/readings/00_week.md` | `1_modal_logic/00_week/00_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/01_week.md` | `1_modal_logic/01_week/01_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/02_week.md` | `1_modal_logic/02_week/02_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/03_week.md` | `2_intensional_semantics/03_week/03_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/04_week.md` | `2_intensional_semantics/04_week/04_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/05_week.md` | `2_intensional_semantics/05_week/05_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/06_week.md` | `2_intensional_semantics/06_week/06_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/08_week.md` | `3_counterfactual_conditionals/08_week/08_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/09_week.md` | `3_counterfactual_conditionals/09_week/09_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/10_week.md` | `3_counterfactual_conditionals/10_week/10_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/12_week.md` | `4_constitutive_explanation/12_week/12_week.md` | Create a true synthesis preserving all content from both files |
| `INTEGRATE/readings/13_week.md` | `4_constitutive_explanation/13_week/13_week.md` | Create a true synthesis preserving all content from both files |

**Critical content preservation guidelines:**

1. **True Synthesis Approach:**
   - Create a true synthesis of both files, preserving ALL content from both sources
   - Never compress paragraphs into bullet points or otherwise change the text format
   - Maintain the exact wording, tone, and style of all original content
   - Keep all paragraphs intact exactly as they appear in the original files

2. **Text Structure Preservation:**
   - Maintain all paragraph breaks and text flow as they exist in the original files
   - Preserve all headings, subheadings, and section organization
   - Keep all formatting (bold, italic, code blocks, etc.) exactly as it appears
   - Never condense or summarize content - each paragraph should remain unchanged

3. **Organization Strategy:**
   - Title and URL: Use the format from INTEGRATE/readings/XX_week.md
   - Introduction: Include the introduction paragraphs from BOTH files if they contain different information
   - Reading lists: Include ALL readings from both files, removing only exact duplicates
   - Lecture notes: Preserve all lecture notes, code samples, and examples exactly as they appear
   - Special sections: Include all special sections from both files, clearly organized

### 2. Problem Sets

INFO: This section is already largely complete.

```
problem_sets/
├── README.md (containing the full content from INTEGRATE/problem_sets/collaboration.md)
├── 01_tooling/
│   ├── practice_git.md
│   ├── tooling.md
│   └── latex_template files...
├── 02_axiomatic_proofs/
│   ├── axiomatic_proofs.md
│   └── solution files...
...and so on
```

**Problem Sets README.md Guidelines:**
* [x] Copy the ENTIRE content from INTEGRATE/problem_sets/collaboration.md into problem_sets/README.md
* [x] Do not modify, summarize, or reorganize the content - preserve it exactly as in the original file
* Update any internal links to reflect the new directory structure
* Consider adding a title at the top if one doesn't exist (e.g., "# Collaboration Guidelines")

### 3. Final Projects

INFO: This section is already largely complete.

```
final_projects/
├── README.md (containing the full content from INTEGRATE/final_projects/final_projects.md)
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

**Final Projects README.md Guidelines:**
- [x] Copy the ENTIRE content from INTEGRATE/final_projects/final_projects.md into final_projects/README.md
- [x] Preserve the original formatting, structure, and all content
- Update any internal links to reflect the new directory structure

### 4. Special Notes Directory

Create a new top-level directory `notes/` for the general notes that are not week-specific, including links to these notes from the notes for relevant weeks:

```
notes/
├── automated_reasoning.md
├── bit_vectors.md
└── lattice_theory.md
```

### 5. Update Main README.md

Create a true synthesis of the existing main README.md and INTEGRATE/README.md to ensure that ALL content from both files is preserved and well-organized:

**Main README.md Integration Guidelines:**
- Apply the same true synthesis approach used for weekly content files
- Preserve ALL paragraphs from both README files exactly as they appear - no condensing or reformatting
- Maintain the existing structure of the main README.md while integrating new content from INTEGRATE/README.md
- Keep all content in its exact original format - paragraphs remain paragraphs, bullet points remain bullet points
- Integrate the Problem Sets section from INTEGRATE/README.md into the main README.md
- Add links to the new problem_sets/README.md, final_projects/README.md, and files in the notes/ directory where appropriate
- Update any internal links to reflect the new directory structure
- Organize the content logically, but never modify the content within sections

## Implementation Steps

1. **Create New Directories**:
   ```bash
   mkdir -p problem_sets
   mkdir -p final_projects
   mkdir -p notes
   ```

2. **Process Week-Specific Reading Content**:
   For each week, create a true synthesis by merging the content from `INTEGRATE/readings/XX_week.md` into the corresponding `X_module_name/XX_week/XX_week.md` file. Follow this approach:
   
   ```bash
   # Example for week 00
   # Step 1: Read both files completely to understand their structure and content
   # Step 2: Copy the title format from INTEGRATE file
   # Step 3: Include full introduction paragraphs from both files if they contain different information
   # Step 4: Merge reading lists, keeping all entries from both sources
   # Step 5: Preserve all lecture notes and other content from the destination file EXACTLY as-is
   # Step 6: Add any additional sections from the INTEGRATE file that aren't in the destination file
   ```
   
   **Important content preservation guidelines for each week's file**:
   
   - **NEVER convert paragraphs to bullet points or vice versa** - maintain the exact format of the original text
   - **Keep ALL content** from both files - this is a true synthesis, not a selective merge
   - **Preserve all paragraphs exactly as they appear** - maintain their original structure and wording
   - **Organize logically** - place related sections together, but don't modify the content within sections
   - **Maintain all formatting** - preserve all markdown formatting, including bold, italic, and code blocks

3. **Move Problem Sets and Create README**:
   ```bash
   # Copy the full content from collaboration.md to README.md in problem_sets directory
   cp INTEGRATE/problem_sets/collaboration.md problem_sets/README.md
   
   # For each problem set (01-08), create appropriate directory and copy content
   mkdir -p problem_sets/01_tooling
   cp -r INTEGRATE/problem_sets/01_pset/* problem_sets/01_tooling/
   
   mkdir -p problem_sets/02_axiomatic_proofs
   cp -r INTEGRATE/problem_sets/02_pset/* problem_sets/02_axiomatic_proofs/
   
   # Continue for remaining problem sets with appropriate naming
   ```

4. **Move Final Projects and Create README**:
   ```bash
   # Copy the full content from final_projects.md to README.md in final_projects directory
   cp INTEGRATE/final_projects/final_projects.md final_projects/README.md
   
   # Copy all other final_projects content
   cp -r INTEGRATE/final_projects/* final_projects/
   
   # Remove the original file to avoid duplication
   rm final_projects/final_projects.md
   ```

5. **Move Special Notes**:
   ```bash
   cp -r INTEGRATE/readings/notes/* notes/
   ```

6. **Update Main README.md**:
   Create a true synthesis of the main README.md and INTEGRATE/README.md:
   
   ```bash
   # Step 1: Read both README files completely to understand their structure and content
   # Step 2: Create a draft that combines both files, preserving ALL content from both
   # Step 3: Organize sections logically but DO NOT modify content within sections
   # Step 4: Add sections for problem sets and final projects with links to their README files
   # Step 5: Update all paths to point to the new directory structure
   # Step 6: Verify that ALL paragraphs from both files are preserved exactly as they appear
   ```

7. **Verify Project Structure**:
   - Ensure all files have been properly moved and merged
   - Check that all links within documents are updated to point to the correct locations
   - Test all repository navigation from the README.md file
   - Verify that no content was lost during the integration process

8. **Remove INTEGRATE Directory** (after thorough verification):
   ```bash
   # Only after confirming everything is properly integrated
   rm -rf INTEGRATE/
   ```

## Weekly Content Integration Details

For each week's content file, follow this specific pattern for true synthesis:

1. **Title and Introduction**:
   - Use the title format from INTEGRATE/readings/XX_week.md: `# [Week XX: Title](URL)`
   - Include introduction paragraphs from BOTH files if they contain different information
   - Place them in sequence with appropriate spacing - do not condense or merge paragraphs
   - Maintain any problem set references in the original format

2. **Reading List**:
   - Include all readings from both files, removing only exact duplicates
   - Preserve the formatting of bold items for primary readings
   - Maintain the chronological ordering if present

3. **Lecture Notes and Content**:
   - Preserve ALL existing lecture notes, section headings, and content in the main directory's XX_week.md file
   - Never modify paragraphs or convert between paragraphs and bullet points
   - Maintain all formatting features like bold emphasis and code blocks
   - Preserve all image references exactly as they appear
   - Keep all text in its original format - do not condense, summarize, or restructure content

4. **Special Sections**:
   - Include all special sections from both files
   - Organize them logically within the document, but preserve their internal structure
   - If sections with the same title appear in both files, combine them while preserving all content

5. **Synthesis Approach**:
   - This is a true synthesis - the goal is to include ALL content from both files
   - Organize the sections logically, but never modify the content within sections
   - Think of this as combining two documents, not editing or summarizing them

## Main README.md Integration

When updating the main README.md, apply the true synthesis approach:

1. **True Synthesis Approach for README.md**:
   - Create a true synthesis of both README files, preserving ALL content from both sources
   - Never compress paragraphs into bullet points or vice versa
   - Maintain the exact wording, tone, and style of all original content in both files
   - Keep all paragraphs intact exactly as they appear in the original files
   - Preserve all section headings and organization from the main README.md
   - Integrate additional content from INTEGRATE/README.md into logical locations

2. **README.md Content Integration**:
   - Maintain the existing title, description, and overview sections from main README.md
   - Preserve the course modules and weekly sections exactly as they appear
   - Add the Problem Sets section from INTEGRATE/README.md with links to the new problem_sets/README.md
   - Enhance the Final Projects section with content from INTEGRATE/README.md
   - Add links to the notes/ directory where relevant
   - Keep all original paragraphs exactly as they appear - no condensing or modifying content

3. **Organization and Links**:
   - Update all links to point to the new directory structure
   - Ensure any references to the INTEGRATE directory are removed or updated
   - Organize sections logically but NEVER modify the content within each section
   - Think of this as combining two documents, not editing or summarizing them
