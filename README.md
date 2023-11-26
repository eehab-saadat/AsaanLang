# AsaanLang - Bringing Programming Home

AsaanLang is a custom-implemented programming language with Urdu/Hindi Latin-based syntax to accommodate native South Asian developer audiences. It is a transpiled programing language with its target language as Python to leverage its dynamically typed syntax and huge developer ecosystem.

## What's new?
- **Protected Branches:** The main branch is now protected from any direct commits. It is now impossible to change the main branch directly. It is necessary to submit the changes via a pull request (PR) which would now necessarily require a code review, and hence approval before any merges. The feedback of th code review would now be provided within the submitted PR if needed.
-  **GitHub Projects:** This is a built-in GitHub feature for requirements management and task status tracking. For this project, a Kanban-like board has been setup for maintaing and managing task backlog in conjunction with automation triggers provided by *GitHub Workflow*. For details and usage, refer to the `Projects` tab above (open the project's README when you're there to get more details on how to use it).

## Collaboration Guidelines

You must follow the following workflow guidelines to approve your changes to the final build aka stable production (aka the main branch) and hence collaborate.

1. **Review your assigned Issues** from the `Issues` tab on the top and check the checkboxes in the issue description to publicly track your progress on that task/issue, simultaneously as you work on its implementation. It is crucial for the progress to be transparent for efficient project progress tracking. To get a tabular view of the tasks backlog and status, refer to the `Projects` tab above.
2. Before starting working on an issue, **create a branch** and commit your changes to that branch. **Create one branch for one issue only**. Be sure to abide by branch naming convention. The branch name, although should be created with the name specified in your Issue, should be done in all lowercase, sould be short, meaningful and hyphen separated. E.g. "*add-playground*".
3. **Commit your changes to your branch** either in the case of showcasing your work for reference or updating your branch in consistency with the changes done at your local repository. **Adding a concise message to outline the commit theme is mandatory**. Sub-branches may be created in the case of a branch being dependant on the othr branch.
```sh
git commit -m "your message"
```
4. **Update your branch periodically** to stay in-sync with the main branch, especially whenever you observe a change done to the main repsitory to avoid future merge conflicts and to avoid using outdated code. If you are using Git, you may do this via:
```sh
git checkout your-branch # switching to your branch
git pull origin main # pull & merge remote main to local 
```
5. When your feature/task is completed and ready to be merged with the main branch, **submit a pull request (PR)**. Remember to include a meaningful title and description for your pull request. And **remember to include either *"fixes #n"* or *"resolves #n"* in your PR title**, where "*n*" is the Issue ID assigned to your Issue. For example: "*added playground page, resolves #3*" would automatically close Issue #3, submitting the associated pull request to be submitted for a **code review**.
6. The **code will then be reviewed** by the repository owner and feedback, if needed for the PR, would be given back for changes on the PR for code change & PR update, else it would be approved and **merged with the main**.

The process may then be iteratively used for every Issue resolved or feature added. 

## Coding Guidelines
Every collarborator is advised to write well indented and documented code. This includes writing explanatory code comments and docstrings for every function and class defined. Be sure to write efficient and concise code with meaningful names and type hints where possible. You can view the already submitted code for reference. A vscode extension was used to auto-generate docstrings in google formate, hence providing automation.

This would not only improve the code's readability and understandability but also improve the code's maintainibility and malleability.

## Introductory GitHub Guide
> For people new to GitHub, here's an attempt to sum it up for them to collaborate better.

We use Github to collaborate and maintain an effective workflow. This section provides easy-to-follow instructions for our team to work collaboratively and keep our work synced across the team by using Github.

To effectively cpntribute, you'll be using either the Github Desktop app or the Github CLI to follow through the following content. It's recommended to use the CLI as it easens redundant tasks and navigation but feel free to use whatever works with you.

[Here](https://uoftcoders.github.io/studyGroup/lessons/git/collaboration/lesson/)'s a good guide to get started with the CLI and for the App refer to [here](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop). Be sure to read [this](https://www.freecodecamp.org/news/how-to-use-git-and-github-in-a-team-like-a-pro/) and [this](https://medium.com/@jonathanmines/the-ultimate-github-collaboration-guide-df816e98fb67), along with the aforementioned gudes, before following through, to help stuff make sense.

### Issues
Issues are used to track todos, bugs, feature requests, and more. As issues are created, they’ll appear in the `Issues` section as a searchable and filterable list. Each issue has a label indicating its nature and can be assigned to the dedicated resource, who closes the issue once it's resolved.

### Branch, Commit & Push
There are multiple ways to do this so be sure to read the aforementioned guides before following along. Be sure to see the following section on pull requests before starting to work as well.

Once you're working on an issue, create a branch for it using a suitable and appropriate naming convention, as mentioned earlier.

Now, on your local device, switch to that branch, as mentioned in your relevant guide, and **commit** to it as you make progress through your feature(s). Be sure to include appropriate messages with the commit such as *"added the fully styled playground page, consistent with figma. backend integration pending"*. 

> **Note:** Remember to **ALWAYS** branch from the main branch, to keep up with updated code and to **NOT** work on the same file or place as others to avoid a crucial merge conflict.

### Pull Requests
Finally when you're done with your feature, submit a **pull request** (click [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) for more info) for your branch to be merged with the **main branch**, which is the trunk branch for stable, production-ready and deployable code. Be sure to include relevant name and description for this telling about what it's for and what issue it fixes such as *"added playground page, resolves #3"* where the `#3` indicates that it resolves the Issue with the ID of 3. 

### Code Reviews & Merge
The submitted pull request would then be submitted for code review to be done by the project administrator or merge master ([@eehab-saadat](https://github.com/eehab-saadat)) and merged with the main branch if no merge conflicts or problems are found. Relevant feedback would be provided via comments or in-built code review PR feedback otherwise.

Once the pull request is approved and merged with the main, the submitted branch would then be deleted by the merge master, after which you can start working on a new feature by just repeating through the aforementioned. That's it!

You can see the demo [here](https://medium.com/@jonathanmines/the-ultimate-github-collaboration-guide-df816e98fb67) for further info and illustration.

## Contact & Suggestions
Feel free to contact me in case of any queries or suggestions.