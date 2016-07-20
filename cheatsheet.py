# More can be found at http://rypress.com/tutorials/git/index

# The "only" difference between a usual directory and a Git-managed directory is the (hidden) .git directory.
# Four components: 1. the working directory; 2. the staged snapshot; 3. the committed snapshots; 
#                  4. development branches.   

git init
# Create a Git repository in the current folder.

git status
# View the status of each file in a repository.

git add <file>
# Stage a file for the next commit.
# Ex. 1: git add index.html
# Ex. 2: git add index.html orange.html

git commit
# Commit the staged files with a descriptive message.

git log
# View a repository’s commit history.
git log --oneline
git log --oneline index.html

git config --global user.name "<name>"
# Define the author name to be used in all repositories.

git config --global user.email <email>
# Define the author email to be used in all repositories.

git checkout <commit-id>
# View a previous commit.

git tag -a <tag-name> -m "<description>"
# Create an annotated tag pointing to the most recent commit.
# Note: so we could use "git checkout <tag-name>" in the future. 

git revert <commit-id>
# Undo the specified commit by applying a new commit.
# This works on the committed snapshots.

git reset --hard
# Reset tracked files to match the most recent commit.
# Also reset the contents on the disk.

git clean -f
# Remove untracked files.

git reset --hard / git clean -f
# Permanently undo uncommitted changes.
# This works on the working directory and the staged snapshot.

git branch
# List all branches.

git branch <branch-name>
# Create a new branch using the current working directory as its base.

git checkout <branch-name>
# Make the working directory and the HEAD match the specified branch.

git checkout -b <new-branch-name>
# Create and check out the new branch in a single step.

git merge <branch-name>
# Merge a branch into the checked-out branch.

git branch -d <branch-name>
# Delete a branch.

git rm <file>
# Remove a file from the working directory (if applicable) and stop tracking the file.

git mv <file0> <file1>
# Rename file0 as file1

git commit -a -m "<message>"
# Stage all tracked files and commit the snapshot using the specified message.

git branch -D <branch-name>
# Force the removal of an unmerged branch (be careful: it will be lost forever).

git rebase <new-base>
# Move the current branch’s commits to the tip of <new-base>, which can be either a branch name or a commit ID.

git rebase -i <new-base>
# Perform an interactive rebase and select actions for each commit.

git commit --amend
# Add staged changes to the most recent commit instead of creating a new one.

git rebase --continue
# Continue a rebase after amending a commit.

git rebase --abort
# Abandon the current interactive rebase and return the repository to its former state.

git merge --no-ff <branch-name>
# Force a merge commit even if Git could do a fast-forward merge.

git reflog
# Display the local, chronological history of a repository.

git reset --mixed HEAD~<n>
# Move the HEAD backward <n> commits, but don’t change the working directory.

git reset --hard HEAD~<n>
# Move the HEAD backward <n> commits, and change the working directory to match.

git log <since>..<until>
# Display the commits reachable from <until> but not from <since>.
# These parameters can be either commit ID’s or branch names.
git log HEAD~4..HEAD  # Ex.
git log -n 4  # Equivalent of the command above

git log --stat
# Include extra information about altered files in the log output.

git clone <remote-path>
# Create a copy of a remote Git repository.

git remote
# List remote repositories.
git remote -v

git remote add <remote-name> <remote-path>
# Add a remote repository.
# Ex.: git remote add mary ../marys-repo

git fetch <remote-name>
# Download remote branch information, but do not merge anything.

git merge <remote-name>/<branch-name>
# Merge a remote branch into the checked-out branch.

git branch -r
# List remote branches.

git push <remote-name> <branch-name>
# Push a local branch to another repository.

git push <remote-name> <tag-name>
# Push a tag to another repository.

git init --bare <repository-name>
# Create a Git repository, but omit the working directory.

git remote rm <remote-name>
# Remove the specified remote from your bookmarked connections.

git format-patch <branch-name>
# Create a patch for each commit contained in the current branch but not in <branch-name>. 
# You can also specify a commit ID instead of <branch-name>.

git am < <patch-file>
# Apply a patch to the current branch.

git archive <branch-name> --format=zip --output=<file>
# Export a single snapshot to a ZIP archive called <file>.

git bundle create <file> <branch-name>
# Export an entire branch, complete with history, to the specified file.

git clone <repo-dir> -b <branch-name>
# Re-create a project from a bundled repository and checkout <branch‑name>.

git stash
# Temporarily stash changes to create a clean working directory.

git stash apply
# Re-apply stashed changes to the working directory.

git diff <commit-id>..<commit-id>
# View the difference between two commits.

git diff
# View the difference between the working directory and the staging area.

git diff --cached
# View the difference between the staging area and the most recent commit.

git reset HEAD <file>
# Unstage a file, but don’t alter the working directory or move the current branch.

git checkout <commit-id> <file>
# Revert an individual file to match the specified commit without switching branches.

git config --global alias.<alias-name> <git-command>
# Create a shortcut for a command and store it in the global configuration file.

git cat-file <type> <object-id>
# Display the specified object, where <type> is one of commit, tree, blob, or tag.

git cat-file -t <object-id>
# Output the type of the specified object.

git ls-tree <tree-id>
# Display a pretty version of the specified tree object.

git gc
# Perform a garbage collection on the object database.

git update-index [--add] <file>
# Stage the specified file, using the optional --add flag to denote a new untracked file.

git write-tree
# Generate a tree from the index and store it in the object database. Returns the ID of the new tree object.

git commit-tree <tree-id> -p <parent-id>
# Create a new commit object from the given tree object and parent commit. Returns the ID of the new commit object.

