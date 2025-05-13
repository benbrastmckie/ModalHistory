# [Problem Set #1: Tooling](https://github.com/benbrastmckie/ModalHistory?tab=readme-ov-file#problem-sets)

Here is an outline of what is to come:

- Install a general purpose text editor (IDE) if you do not have one already.
- Install LaTeX if you have not already done so.
- Add an SSH key to your GitHub account.
- Configure Git and learn how to push changes to repositories, adding an SSH key as needed.
- Use Git to clone the repository and push changes.

This is an opportunity to upgrade your toolkit and gain experience with Git collaboration if you haven't used it before. No prior experience is required.

## Editor Installation

Install one of the following or equivalent for writing in markdown, LaTeX, as well as using the [model-checker](https://github.com/benbrastmckie/ModelChecker) to complete the final problem sets at the end of the course:

1. **VSCodium**: Follow the installation instructions [here](https://github.com/benbrastmckie/VSCodium)
2. **NeoVim**: Follow the configuration instructions [here](https://github.com/benbrastmckie/.config)
3. **Other**: Any editor that supports Markdown, LaTeX, and Python

### VSCodium

I have provided extensive installation instructions for how to install VSCodium [here](https://github.com/benbrastmckie/VSCodium).
You do not need to clone or fork that repository if you don't want to, but this is a good option if you have not already configured your editor.
Feel free to open an [issue](https://github.com/benbrastmckie/VSCodium/issues) in that repository if you run into any trouble.

Here is a brief overview:

1. **Download VSCodium**:
   - For Windows: Download the latest release from [VSCodium Releases](https://github.com/VSCodium/vscodium/releases)
   - For Mac: run `brew install --cask vscodium` in the terminal or download the latest release from [VSCodium Releases](https://github.com/VSCodium/vscodium/releases)
   - For Linux: Follow the [official installation guide](https://github.com/VSCodium/vscodium#installation)

1. **Essential Extensions**:
   - LaTeX Workshop
   - GitHub Pull Requests
   - Python

### NeoVim (Alternative)

Installing and learning to use NeoVim is a significant undertaking, so beware.
Nevertheless, you can find detailed installation instructions [here](https://github.com/benbrastmckie/.config).
If you go this route, feel free to open an [issue](https://github.com/benbrastmckie/.config/issues) in that repository if you run into any trouble.

## LaTeX Installation

Install a LaTeX distribution appropriate for your operating system if you have not already done so:

- **Windows**: [MiKTeX](https://miktex.org/download) or [TeX Live](https://tug.org/texlive/windows.html)
- **macOS**: [MacTeX](https://tug.org/mactex/mactex-download.html)
- **Linux**: TeX Live via your package manager (e.g., `sudo apt install texlive-full` for Ubuntu)

You can find resources for installing LaTeX [here](https://github.com/benbrastmckie/VSCodium/blob/master/docs/latex.md).
Follow these (or other) instructions to get LaTeX up and running on your machine in VSCodium (or equivalent).

### Trial Run

Once LaTeX is installed, create a `test_file.tex` document using the [template](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/problem_sets/01_pset/latex_template.tex).
Note that it is important to that your file has the extension `.tex` since otherwise VSCodium won't know that it is a LaTeX file.

Use VSCodium (or equivalent) to build the document, by clicking the green "play" button in the top right.
Click the "split screen" button just beside the "play" button to show the PDF.
Until you have put the `bst` and `bib` files in the right places, the document will not build, but you are close!
The aim of this trial is just to produce the errors so that you know that LaTeX is at least trying to do the right things.

You can find further resources for how to set up a LaTeX project in this [latex_example/README.md](../../final_projects/latex_example/).

### Adding Bib Support

To build your `tex` file, LaTeX will look for the bibliography citation style `bst` file and bibliography specified at the bottom of the template LaTeX file with:

```latex
  \bibliographystyle{../assets/bib_style} %%bib style found locally or in textmf/bibtex/bst
  \bibliography{../assets/modal_history} %%bib database found locally or in textmf/bibtex/bib
```

The easiest thing to do is to put the [`bib_style.bst`](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/assets/bib_style.bst) file in the `/texmf/bibtex/bst/` directory on your computer as explained [here](https://github.com/benbrastmckie/VSCodium/blob/master/docs/latex.md) so that you don't need to worry about always including a `bst` file in the same directory as your LaTeX file.
As for the bibliography, the path `../../assets/modal_history` included above specifies a sample bibliography that I have provided and will update as we go.

In order to get all the files in the right places and stay updated, the next step is to pull down the repository with Git.
This will streamline collaboration so that staying up to date becomes easy and you don't have to cut and paste or move around different versions of files.
To get Git working, you will need to add an SSH key.

### Writing LaTeX

Here are a few points to keep in mind to make the process of writing LaTeX documents easier:

1. SyncTex and BackSync
  - You can use `Cmd + click` (Mac) or `Ctrl + click` (Windows/Linux) on the PDF to find the same spot in the LaTeX.
  - You can also use `Ctrl + Alt + J` (Windows/Linux) or `Cmd + Alt + J` (Mac) to highlight the spot in the PDF corresponding to where the cursor is in the LaTeX document
2. Kill auxiliary files
 - You may need to delete auxiliary files when LaTeX builds fail or become corrupted
 - To clean auxiliary files in VSCodium:
   - Click the LaTeX Workshop icon in the left sidebar
   - Click the trash can icon labeled "Clean up auxiliary files"
   - Or use the Command Palette (`Ctrl+Shift+P`) and search for "Clean up auxiliary files"
   - This removes temporary files like .aux, .log, .synctex.gz but keeps your .tex and .pdf
   - These will be regenerated upon rebuilding the PDF
3. To use LaTeX snippets in VSCodium:
  - Type a backslash `\` followed by the command name (e.g., `\begin`)
  - VSCodium will show a dropdown list of matching snippets
  - Press `Tab` or `Enter` to insert the selected snippet
  - Common snippets include:
    - `\begin{document}` - Creates document environment
    - `\section{}` - Creates a new section
    - `\cite{}` - Creates citation
    - `\textit{}` - Creates italicized text
    - `\textbf{}` - Creates bold text
  - You can navigate between snippet placeholders using `Tab`
  - Create custom snippets in VSCodium:
    - Open Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
    - Type "Snippets: Configure User Snippets"
    - Select "latex.json"
    - Add your custom snippets following the JSON format
  - The LaTeX Workshop extension includes many built-in snippets
  - Type part of a command to see suggestions
  - Use `Ctrl+Space` to manually trigger suggestions

### Zotero (Optional)

Although optional, I recommend setting up [Zotero](https://www.zotero.org/) or equivalent if you have not already done so to help manage the readings and `.bib` info for each.
You can find installation instructions [here](https://github.com/benbrastmckie/VSCodium/blob/master/docs/zotero.md).
Shouldn't take more than a few minutes.

## Git

Here is a brief overview of the steps to be completed:

- Set up SSH authentication to be able to securely interact with GitHub repositories
- Use Git to pull down this repository onto your computer
- Add your name to the [`practice_git.md`](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/problem_sets/01_pset/practice_git.md) file on your computer
- Push your change up to the repository

> Feel free to complete these steps however you are comfortable, or by following the instructions below:

### Generate and Add an SSH Key

1. **Open VSCodium's Integrated Terminal**:
   - Press `Ctrl` together with the backtick or
   - Go to `Terminal → New Terminal` in the top menu

2. **Generate Your SSH Key**:
   - In the terminal, enter the following, substituting your email address (the one you used on GitHub):
     ```bash
     ssh-keygen -t ed25519 -C "your.github@email.com"
     ```
   - When asked for the file location, press Enter (uses default location)
   - When asked for a passphrase, either:
     - Press Enter twice for no passphrase (not recommended), or
     - Enter a secure passphrase

3. **Start the SSH Agent**:
   - For Mac/Linux, enter these commands in VSCodium's terminal:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```
   - For Windows, enter these commands:
   ```bash
   start-ssh-agent
   ssh-add C:\Users\YOUR_USERNAME\.ssh\id_ed25519
   ```

4. **Copy Your SSH Public Key**:
   - For Mac/Linux:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
   - For Windows:
   ```bash
   type C:\Users\YOUR_USERNAME\.ssh\id_ed25519.pub
   ```
   - Select and copy the entire output (starts with 'ssh-ed25519' and ends with your email)

5. **Add the Key to GitHub**:
   - Go to [GitHub.com](https://github.com) and sign in
   - Click your profile photo (top right) → Settings
   - Click "SSH and GPG keys" in the left sidebar
   - Click "New SSH key"
   - Title: Give it a name (e.g., "MyLaptop")
   - Key: Paste your copied public key
   - Click "Add SSH key"

6. **Test Your Connection**:
   In VSCodium's terminal:
   ```bash
   ssh -T git@github.com
   ```
   - If you see a warning about host authenticity, type 'yes'
   - You should see a message: "Hi username! You've successfully authenticated..."

### Troubleshooting SSH in VSCodium

- If commands aren't recognized:
  - Make sure Git is installed on your system
  - Try restarting VSCodium

- If you get permission errors:
  - For Windows: Run VSCodium as Administrator
  - For Mac/Linux: Check SSH agent is running: `ssh-add -l`

- If authentication fails:
  - Verify your key is listed in GitHub (Settings → SSH keys)
  - Make sure you're using SSH URLs for repositories (starts with `git@github.com:`)
  - Try verbose SSH test: `ssh -vT git@github.com`

Remember: Never share your private key (the file without .pub extension). Only share the public key (.pub file) with GitHub.

### Configure Git

1. **Add Two-Factor Authentication in GitHub**:
  - Go to GitHub Settings → Password and Authentication
  - Click "Enable two-factor authentication"
  - Choose your preferred 2FA method (authenticator app recommended)
  - Follow the setup wizard to configure your chosen method

2. **Initial Setup**:
  - Open VSCodium
  - Install the "GitHub Pull Requests and Issues" extension
  - Click the accounts icon in the bottom left corner
  - Sign in to GitHub when prompted
  - This will open a browser window where you will need to sign in
  - Enter the number provided in VSCodium

3. **Add Username and Email to Git**:
  - Open VSCodium's integrated terminal (`Ctrl + backtick` or View → Terminal)
  - Enter the following commands, replacing with your information:
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.github@email.com"
    ```
  - Use the same email address associated with your GitHub account
  - You can verify your settings with:
    ```bash
    git config --global user.name
    git config --global user.email
    ```

4. **Configure Git**
  - Open the terminal and enter the following command:
    ```bash
    git config --global merge.rebase false
    ```
  - This will tell Git how to integrate your changes.

5. **Clone the Repository**:
  - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open the command palette
  - Type "Git: Clone"
  - Select "Clone from GitHub"
  - Choose your private repository from the list
  - Select a folder on your computer where you want to save the repository locally
  - Click "Open" when prompted

### Using Git in VSCodium

1. **Making Changes**:
  - Use the explorer to find and open `problem_sets/01_pset/latex_template.tex` 
  - Try to build the file as before, confirming that it generates a PDF without errors
  - Once successful, open `problem_sets/01_pset/practice_git.md` using the explorer in VSCodium
  - Add your name to the list to practice using Git to contribute changes
  - Save the file (`Ctrl+S` or `Cmd+S`)

2. **Committing and Pushing Changes**:
  - Click the Source Control icon in the left sidebar (or press `Ctrl+Shift+G`)
  - You'll see your changed files under "Changes"
  - Hover over "Changes" and click the `+` icon to stage all changes
  - Type a commit message in the text box at the top
  - Click the ✓ (checkmark) icon to commit
  - Click `Sync Changes` or the `⋯` (three dots) menu and select "Push"

3. **Further Particulars**:   
  - Your changes are now on GitHub
  - You can verify by checking your repository on GitHub's website
  - It is good practice to always pull before pushing (or just click `Sync`)
  - If the remote repository changes, you can easily update by clicking the `Sync` button in the bottom left corner (two arrows in a circle)
  - Git has been set to ignore certain file types since we don't need to track all the auxiliary files for building LaTeX documents
  - If you are still feeling unsure of what Git does or what the workflow looks like, I recommend watching a short tutorial on YouTube

4. *Troubleshooting**:
  - If you get authentication errors, ensure you're signed into GitHub in VSCodium
  - If push fails, try pulling first using the "Pull" option in the ⋯ menu
  - Check the bottom status bar for any Git-related messages or errors

5. **Configuration**: (optional) 
  - VSCodium is highly configurable, so if there is something that you don't like, you can probably change it
  - For instance, color themes, autocompletion, snippets, keybindings, plugins, you name it
  - You can have a look through the settings if you like, though there is a lot to take in
  - Asking an LLM how to change the `settings.json` file to produce a specific change is another way
  - Don't want to mess with all that? No problem, it will be there if you ever feel inspired

## Exercise

Having set up all of these pieces there is one final exercise to check that everything is working

### Practice Using Git

1. Clone this repository (if you haven't already)
2. Create a new branch for your work
3. Make some changes to a file
4. Stage and commit your changes
5. Push your changes to the remote repository

This exercise will help you become familiar with the Git workflow that we'll use throughout the course
