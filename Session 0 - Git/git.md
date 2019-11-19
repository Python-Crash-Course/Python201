---
marp: true
# paginate: true
_class: lead
theme: base-theme

style: |
  section {
    font-family: Roboto;
    background-color: #ccc;
    color: darkslategrey;
  }
  h1 {
    text-align: center;
    font-family: Roboto;
    color: #EE7631;     
    font-size: 50pt;
    font-weight: bold;
  }
  h2 {
    font-family: Roboto;
    color: #EE7631;     
  }

  p {
    font-family: Roboto;
  }

   ul li ul li {  
     font-size: Roboto;
     font-size: 20pt;
  }

  section.center-content p {
    text-align: center;
  }

  section.small-table-text {
    font-size: 20pt;
  }

  pre {
    background-color: RGB(245, 245, 245);
    box-shadow: 0 4px 8px grey;
    line-height: 1.15;
    margin: 15px auto 30px auto;
    min-width: 60%;
    padding: 0.4em 0.6em;
  }

  .scaling-svg-container {
    position: relative; 
    height: 0; 
    width: 100%; 
    padding: 0;
    margin: 0;
  }

  .scaling-svg {
    position: absolute; 
    height: 100%; 
    width: 100%; 
    left: 0; 
    top: 0;
  }

backgroundImage: "linear-gradient(to left, lightgrey, white)"


---
<!-- footer: Python Crash Course 201 - Session 0 -->
<!-- _class: center-content -->
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg') -->
![bg left:40% 80%](img/Logos/Git_Logo.png)

# Git

Introduction and setup

---
<!-- _headingDivider: 1 -->
<!-- paginate: true -->

## What is Git?

* Most widely used version control technology in the world
* Created by Linus Thorvalds
* Free to use 
* Works best for text files, but can be used for other file types

---

## Git repositories

* A project is tracked as a ***Git repository***
* Tracking occurs via a hidden subdirectory called `.git/` inside the root directory
* A Git repository looks like any other directory on your system (except for the presence of `.git/`)

### Common ways to create Git repositories
1. Start tracking an existing *local* project by turning it into a Git repository 

2. `clone` a *remote* Git repository and starting tracking it *locally*  

A common place to host *remote* Git repositories is **GitHub**. 

---

## What is GitHub? 
Most people hear about GitHub before Git, so let's cover that briefly: 

* **GitHub** is a website that hosts Git repositories 

* Provides modern looking interface with many features for collaboration 

* **GitHub** started as a community maintained project and was so for many years 
* Acquired by Microsoft in 2018. 

* Free for basic usage

---

## Some things GitHub makes easy

* **Viewing version history** of projects tracked by Git 
* **Collaborating** on projects for both small and very large teams
* **Showcasing** projects and demonstrating their use 
* **Managing** projects with todo's, issues, milestones, releases etc.

To understand GitHub, one must first have a basic understanding of Git and version control in general.

Let's move on with that :rocket:

---
![bg right 90%](img/GitBasics/Distr_version_control.png)

## So again, what is Git?

* A **distributed version control system**

* **Which means:** 
  Everyone has a local `clone ` of the entire project and its history 

---

## Advantages of Git 
* Fast and light-weight
* Seamless collaborative work
* Work alone when needed and share when needed
* Almost impossible to lose work
* Supports workflows from very simple to very complex

---
<!-- _paginate: false -->
<!-- _class: center-content  -->
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg') -->
![bg right](img/Logos/Git_wallpaper.png)

# Git Basics

Commands and features

---
![bg right:25% 90%](img/GitBasics/Git_Bash.png)

## Git commands

Interaction with Git is performed via commands in ***Git Bash***

* Opens from inside your Git repository via right-click menu
* Interact with the repository by typing `git <command_name>`
* Many editors support common commands in GUI form

Initialize a Git repository inside a directory by typing

```css
git init
```
This will create the hidden `.git` folder in the current directory.

---

## Commit
The `git commit` command is the heart of Git.

**Git does the following when `git commit` is executed:**

* Saves your local staged changes to your local Git repository

* Takes a "picture" of what the repository files look like and stores it as a ***snapshot*** 

* Gives the snapsnot an ID so all files can be reverted to that state at *any* time

* Assigns the commit message you specify to snapshot 

Make a `commit` each time you want to record a snapshot of the project state by: 

```css
git commit -m "Commit message goes here"
```

---

![bg right:55% 90%](img/GitBasics/Snapshots_over_time.png)

## Commits over time
A `commit` records the state of all files, even unchanged ones.

Git creates a pointer to the previous version of unchanged files instead of saving it again.

---

## Status of files
![bg right:66% 90%](img/GitBasics/Status_of_files.png)
A file in a Git repository can have two states: 

* **Untracked** 
Grey operations
* **Tracked** 
Red operations

---

![bg right:40% 90%](img/GitBasics/Three_states.png)
## Three local states

A file that is **tracked** inside a Git repository can be in three states:

**1. Modified:**
File is modified and Git has detected it
  
**2. Staged**
File is in the staging area ready to be included in the next `commit`

**3. Comitted**
The file has been checked in and Git has taken a snapshot of the repository state

---
![bg right:40% 90%](img/GitBasics/gitignore_example.png)

## Ignoring files

It's quite common to have things inside a Git repository that you do not want to have version controlled.

The `.gitignore` file inside the repository controls what is being version controlled.

* Examples of files to ignore:

  * Excel files
  * Pictures or graphs
  * Dummy data sets for testing
  * Generated files

---
<!-- _paginate: false -->
<!-- _class: center-content -->
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg') -->
![bg right](img/Branching_and_Merging/Git_branching.PNG)

# Branching

The pinnacle of collaboration


---
![bg right:30% 85%](img/Branching_and_Merging/Branching_step1.svg)

## Branching illustrated 1/4
Branching is best explained by an example.

**Scenario:**

1. We have a main branch called `master` 
2. We just made a `commit` **C1** which made the code stable and ready for use by others.

The figure to the right depicts the scenario.

> **Note:** `HEAD` is a reference to the currently checked out commit

---
![bg right 90%](img/Branching_and_Merging/Branching_step2.svg)

## Branching illustrated 2/4

We want to keep developing and create a new feature.

***But*** we don't want to work directly in `master`. Others are using this branch and developing might temporarily bring it into a broken state. 

3. So we create a new branch called `feature` from Git Bash by typing
```css
git branch feature
```

---
![bg right 90%](img/Branching_and_Merging/Branching_step3.svg)

## Branching illustrated 3/4

We have created the branch, but the currently checked out commit (`HEAD`) is still `master`'s **C1**.

4. We switch to the new `feature` branch by
```css
git checkout feature
```
This switched us to the new `feature` branch with the same `commit` **C1** 

---
![bg right 90%](img/Branching_and_Merging/Branching_step4.svg)

## Branching illustrated 4/4

Now we want to start making the changes to implement our feature.

5. Change some file(s) and run 
```css
git commit
```

This creates a new `commit` **C2**.

*The **C2** `commit` might have made `master` unstable had it been done on that branch. But we are safe to experiment on our `feature` branch.* 

---
<!-- _paginate: false -->
<!-- _class: center-content -->
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg') -->
![bg right](img/Branching_and_Merging/Git_branching.PNG)

# Merging

Integrating changes from a branch

---

## Merging the `feature` branch

*Continuing from the previous branching example.* 

Our work on branch `feature` has been completed by `commit` **C2**. We want to `merge` it back into `master` so other can use it.

**We'll cover three different merging scenarios:**

1. **Automatic merge: Fast-forward** 
Branch `feature` has commits beyond **C1**, but `master` is unchanged at commit **C1**  

2. **Automatic merge: 3-way merge**
Both `feature` and `master` has new commits beyond **C1** which are not conflicting

3. **Merge conflict**
Both `feature` and `master` has new commits beyond **C1** which are  conflicting

---
![bg right:48% 90%](img/Branching_and_Merging/Merging_fastforward.svg)

## Auto merge: Fast-forward

We can seamlessly merge branch `feature` into branch `master` from `commit` **C2**. 

This is because `mater` is unchanged since branch `feature` was created. 

```css
git checkout master
git merge feature
```

> **Note:** When doing `git merge <branch_name>` `HEAD` must be in the branch to `merge` *into*.

---
![bg right:48% 90%](img/Branching_and_Merging/Merging_3way.svg)
## Auto merge: 3-way merge

Branch `master` now has a `commit` **C3** after `feature` was created. Thus, both **C2** and **C3** has to be taken into account when merging.

If **C2** and **C3** has ***no competing changes***, Git is smart enough to perform an automatic `merge` by use of those two commits and their common ancestor **C1** (3-way).

```css
git checkout master
git merge master
```

---
![bg right:48% 90%](img/Branching_and_Merging/Merging_conflict.svg)
## Merge conflict

Suppose the `commits` **C2** and **C3** has conflicting changes. 

There is is no way for Git to know which change to keep during `merge`.

Thus, ***the user*** must 
1. resolve the `merge conflict` manually 
2. `commit` the changes
3. `merge` again 

---

## Summary: Branching

* Allows us to avoid working on the `master` branch  

* Everybody can work without overwriting work of others

* Work can be grouped logically into a branch for each sub project 

* Use branches for work that's experimental in nature (and might end up discarded)

* A branch creates a pointer to a commit ID (*not* a copy of the file system)

* Creating a branch is cheap ---> it's encouraged to do it often

* Main branch is by default called `master` :exclamation:
 
---

## Summary: Merging

* Allows us to feed work from branches back into the `master` (or other branches)

* Frees us from *a lot* of manual and error prone work 

* Provides a natural step for QA *(more on this when we get to GitHub)*

* A successful `merge` creates a new *merge commit* at the tip of the current branch

* After merging, the branch that was merged in can be deleted

* Basic merging can have three outcomes: 1. Fast-forward, 3-way merge or merge conflict

---
<!-- _paginate: false -->
<!-- _class: center-content -->
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg') -->
![bg right](img/Branching_and_Merging/Remote.jpg)

# Remotes

Sharing work with the world

---

## Sharing work

Up until now we have only talked about local operations

---
<!-- _paginate: false -->
<!-- _class: center-content -->
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg') -->
![bg right](img/Workflow/Collaboration.jpg)

# Workflow 

Some examples

---
<!-- _class: center-content -->
## Simple workflow example
![width:600pt](img/Workflow/Simple_workflow.svg)


---
<!-- _class: center-content -->
## Advanced workflow example (often referred to as Git Flow)
![width:750pt](img/Workflow/GitFlow.png)

---

## Git interface - _Git Bash vs. an editor_
Git Bash (the command line interface) is the original way of working with Git. It contains all the available commands and gives the user more control.

However, **all the popular editors have Git integration build in**, which includes the vast majority of functionality for basic users. It's arguably an easier way to get into the workflow for beginners. 

---
<!-- _paginate: false -->
<!-- _class: center-content -->
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg') -->
![bg right](img/GitBasics/Setup.jpg)

# Initial Git setup


---

## One time configurations

Open Git Bash from Windows start menu.

Setup up your global user name and email by typing the commands below.

```
git config --global user.name "John Doe"
```
```
git config --global user.email johndoe@example.com
```

This information will be tied to all `commit` actions that you do later on.

---
<!-- _paginate: false -->
<!-- _class: center-content -->
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg') -->
![bg right](img/VScode/vscode_wallpaper.jpg)

# Git in VS Code

Simplifying common commands 

---

## Start tracking a project
As previously stated, there are generally two scenarios from which a project is started

1. You want to start tracking an existing project of yours, which has not previously been under Git version control.

2. You want to `clone` an exiting project from elsewhere into your own workspace. This can e.g. be for the purpose of contributing to the project.

These two scenarios are demonstrated in _Visual Studio Code_ with the equivalent _Git Bash_ commands shown.


---
![bg right:60% 90%](img/VScode/git_init_from_vscode.png)

### 1. Start tracking your own project - _Visual Studio Code_
You want to create a new project and start tracking it with Git and GitHub. 
In order to do that, we need to have a 

**Git Bash command:**

```css
git init
```

---

7. Go the the directory in Windows where you want initiate the Git repository, right click and select _Git Bash Here_. 

---

8. Inside Git Bash type ```git init``` and presse enter. This initialises an empty Git repository inside that directory.

---

8. Create a `.gitigore` file inside the directory by typing `touch .gitignore` in Git Bash.
***WHAT TO PUT IN IT?. Is it better to link to a predefined `.gitignore file`?*** 


---

### 1. Start tracking your own project - _Git Bash_ 
Every comannd that exists in Git can be executed via the command line interface. All comamads start with `git`. 

> 1. Open Git Bash from desired directory. You can do so by right clicking inside the directory in Windowns and choosing _GitBash Here_ or by typing `cd path_to_desired_directory` inside Git Bash.  

---
<!-- _class: small-table-text -->

Aftewards, run commands below:

| Command in Git Bash                  | Desciption           |
| :----------------------------------- |:-------------|
| 2. ``git init``                      | _Initialize repository_ |
| 3. ``touch .gitignore``              | _Create `.gitignore` file in current directiry. Adjust contents to fit project. Alternatively, copy it from another project into your Git directory._      |
| 4. ``git add filename``        | _Adds `filename` to staging area ready to be comitted. Add all files by `git add .`_  |
| 5. ``git commit -m "First commit"``  |  _Choose custom commit message if desired_      |

---

## Clone existing project - _Visual Studio Code_

---

## Clone existing project - _Git Bash_

Open Git Bash in the directory of choice and type

```css
git clone <url_for_remote_repo>
```

---

## Normal workflow - _Demonstrated in Visual Studio Code_

Once you have a project setup properly with a local Git repository and a remote to push to, the standard workflow will be something like:

---

___TODO: If real fancy create a gif___


## What about non-text files?
**> TODO: Keep this in the back of the slide show so it can be skipped and people can review it later themselves.**

Non-text files are so-called ***binary files***. 

Imagine having an image in JPEG format:

***TODO:*** Show `master` and `branch` both modified with => Automatic merge not possible. 

---

So to sum up:

> Git can version control binary files, but it has some limitations.
> * Git cannot create meaningful ***diffs*** of binary files, which makes it hard to view changes from one commit to the next.  
> * As a consequence, Git cannot automatically ***merge*** two diverged branches, i.e. two branches that were both committed to after they split. In that case it must be manually chosen which branch is the right one to continue with. 

---

Recall that for text files, Git can automatically merge changes for diverged branches provided there are not conflicts. Conflicts occur if the branches to be merged were changed in the exact same place. In the case of a merge conflict with text files, resolving the conflict is done by comparing the two branches. The branches to be merged can easily be compared line by line e.g. in an editor. 

### Why is this not a PowerPoint?
PowerPoints (`.ppt`-flies) are binary


---
<!-- _class: small-table-text -->

## References

| Link     | Description      |
| :----| :---- |
| [Ressourcces to learn Git](https://try.github.io/) | _dddd_ |
| [Pro Git](https://git-scm.com/book/en/v2) | _Book on Git written by experts_ |
| [`.gitignore` examples](https://git-scm.com/book/en/v2) | _Good examples of `.gitignore` files for various languages_ |

---
---
<!-- _paginate: false -->
<!-- _class: center-content -->
<!-- _backgroundImage: url('https://marp.app/assets/hero-background.jpg') -->
![bg right](img/Exercises/Exercises.jpg)
# Exercises







