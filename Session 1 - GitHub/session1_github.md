# GitHub

<***Image here***>

## Recap form Session 1

GitHub is a website that hosts Git repositories.

<***Recap here...***>

## Remotes - sharing work

Up until now we have only talked about local operations. I.e. operations where each person works alone on a local machine.

## GitHub features and remote nomenclature

### Pull Request

### ```push```

### `clone`

With Git, you can `clone` a remote repository to your local machine and start version controlling it by

```markdown
git clone <url_to_remote_repo>
```

### Forking

**Imagine this scenario:** You see a cool project on GitHub that you are interested in. You would like to access the code to play around with it yourself, maybe you want to use it as basis for your own project. ***But***, you don't want to affect the existing project.

You could `clone` the repository and do some changes locally, but where do you go from there? A `push` to the remote repo would affect the existing project, which is not what you want.

This is where **Forking** comes in. **Forking** a repository means to copy it to your own remote repository. You can now `clone` your own repository and `push` without affecting the existing one that you forked from.

This does not hinder the possibility of merging your new code into the existing project though. You can submit a *Pull Request* from your own repository to let the maintainer know that you have a potential contribution.
This is a common way to contribute to projects where you are not part of the "core team". If you see a bug, you can fix it yourself this way if you're up for it.

*See more about forking [here](https://help.github.com/en/github/getting-started-with-github/fork-a-repo).*

### `origin`

**The *main* remote repository is called `origin`.**

When you connect your local repository to a remote one, it's standard to name the remote one `origin`. If you `clone` a project from an url, Git will automatically set the name of the remote repository to `origin`.

`origin` is the default name for a main remote repository just as `master` is the default name for the main branch.
It's possible (but not common) to rename the main remote to something else, just like `master` can be renamed.

You can have more than one remote repository. An example of this could be when *forking* a project. You will have your own fork as the *main* remote repository, i.e. `origin`. The existing project that you forked from could be called `upstream`.

### `origin/master`

**The `master` branch in the remote repository is called `origin/master`.**

You have an `origin/master` on your local machine. This a branch that is ***read-only***. You can't write directly to a remote repository. It's a so-called *bare repository*, which has no working tree (editable files). Changes have to be done locally and `pushed` to the remote.

This implies that if you checkout `origin/master`, or any other remote branch for that matter, you will be in ***detached head*** state. *Detached head* means that what's currently checked out is not a local branch.  

Other branches in the remote repository will have the name `origin/branch_name`

## Common Git operations with remote

```markdown
git push -u origin master
```

## Visualizing a two-person workflow

<***Insert diagram with two different machines and a remote repo. Each machine should periodically push and pull from master to share and retrieve updated work.***>

## GitHub features

### Pull requests

### Issues

## Exercises

Before starting these exercises, you should have a ***local Git repository*** created for version controlling the contents this we develop for this course.
If you don't have that yet, please do the [Session 1 exercises](https://github.com/Python-Crash-Course/Python201/blob/master/Session%200%20-%20Git/session0_git.md#exercises) before starting these.

## Exercise 1

***Create a GitHub account***

Go to [github.com](https://github.com/) and create an account if you don't already have one and log in.

## Exercise 2

***Create a remote repository***

1. Once logged in, go to the `+` sign in the upper right corner and choose *New repository*.

2. Give your repository a name and a description.

3. Choose whether you want your repository to be public or private.

4. We have already created a `README.md` and a `.gitignore` file in the Session 0 exercises, so don't check those boxes. If you'd like, you can add a licence to the repository to let people know under which circumstances they can use your code.

5. Click *Create repository*.

> There is an info icon if you are more curious which license to choose for your repository. If you want to add one but don't care which, just take MIT License. It's the most permissive one.

## Exercise 3

***Sync local repository with GitHub***

You should now see a clean repository that looks something like this

![alt text](img/clean_repo.png)

We will now `push` our local code this remote repository.

1. Click the green *Clone or download* button and copy the url.

2. `git remote add origin <url>`
***How about from vscode?***

3. `git`
***What is the state of their repos? do they have branches to push or just master?***

***When pushing, it will say that the remote contains work that you do not have locally => git pull and then git push***.

***Do this exercise yourself before to make sure what they go through***

## Exercise 4

***GitHub Learning Lab***
