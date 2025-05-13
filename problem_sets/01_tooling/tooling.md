# [Problem Set #1: Tooling](https://github.com/benbrastmckie/ModalHistory?tab=readme-ov-file#problem-sets)

> Problem Set #1: Tooling (due prior to class week 01)

This problem set consists of setting up your development environment and tools for the course.

## Requirements

- Install either [VSCodium](https://github.com/benbrastmckie/VSCodium), [NeoVim](https://github.com/benbrastmckie/.config), or an equivalent editor for writing in markdown, LaTeX, and using the model-checker.
- Install LaTeX on your machine if you have not already done so.
- Configure Git and learn how to push changes to repositories, adding an SSH key as needed.

This is an opportunity to upgrade your toolkit and gain experience with Git collaboration if you haven't used it before. No prior experience is required.

## Setup Instructions

### Editor Installation

Choose one of the following editors:

1. **VSCodium**: Follow the installation instructions [here](https://github.com/benbrastmckie/VSCodium)
2. **NeoVim**: Follow the configuration instructions [here](https://github.com/benbrastmckie/.config)
3. **Other**: Any editor that supports Markdown, LaTeX, and can access the terminal

### LaTeX Installation

Install a LaTeX distribution appropriate for your operating system:

- **Windows**: [MiKTeX](https://miktex.org/download) or [TeX Live](https://tug.org/texlive/windows.html)
- **macOS**: [MacTeX](https://tug.org/mactex/mactex-download.html)
- **Linux**: TeX Live via your package manager (e.g., `sudo apt install texlive-full` for Ubuntu)

### Git Configuration

1. Install Git if not already installed
2. Configure your identity:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
3. Generate and add an SSH key (recommended for secure communication with GitHub):
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```
4. Add the SSH key to your GitHub account (see GitHub documentation)

## Exercise: Practice Using Git

1. Clone this repository (if you haven't already)
2. Create a new branch for your work
3. Make some changes to a file
4. Stage and commit your changes
5. Push your changes to the remote repository

This exercise will help you become familiar with the Git workflow that we'll use throughout the course.