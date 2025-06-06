# Question Asked

GIT and Version Control

Could you answer these questions as if written by a 18 year old who is a newcomer to version control.

Identify key points for the answer.
Identify at least TWO CREDIBLE references (preferably from the internet) for each answer.

c.	What disruptions to collaborative work do you think could occur if company personnel were not given these specific instructions? 
d.	Why does the organisation need to give you these instructions as opposed to centrally configure them?

# Response

Looking at these questions about Git and version control! Let me tackle them from a fresh perspective since I'm still learning about all this stuff.Alright, let me break down these questions about Git and what happens when teams don't follow proper version control practices!

## c. What disruptions to collaborative work could occur if company personnel weren't given specific instructions?

**Key Points:**

**1. Merge Conflicts and Code Chaos**
Without proper Git instructions, team members would constantly create conflicts when trying to merge their work together. People would make "incompatible changes to a file" leading to merge conflicts, and honestly, as someone new to this, merge conflicts are terrifying enough when you know what you're doing!

**2. Lost Work and Overwritten Changes**
People might accidentally overwrite each other's code or lose important changes because they don't know the proper workflow for pulling, committing, and pushing changes in the right order.

**3. Inconsistent Commit Messages and History**
Without guidelines, you'd end up with commit messages like "stuff" or "fixed it" instead of meaningful descriptions. This makes it impossible to track what changes were made and why, which is super important for debugging later.

**4. Branch Management Disasters**
Teams might work directly on the main branch instead of using feature branches, creating a mess where unstable code gets mixed with working code. This leads to situations where "devs can use a graphical tool to resolve conflicts" but only if they understand the proper workflow first.

**References:**
1. NCEAS Arctic Research - Git Collaboration and Conflict Management: https://learning.nceas.ucsb.edu/2022-02-arctic/git-collaboration-and-conflict-management.html
2. GitKraken Blog - GitHub Collaboration Challenges: https://www.gitkraken.com/blog/github-collaboration-tools-gitkraken

## d. Why does the organization need to give you these instructions as opposed to centrally configuring them?

**Key Points:**

**1. Git's Multi-Level Configuration System**
Git actually works with different configuration levels - system, global, and local. Each level "overwrites values in the previous level, so values in .git/config trump those in [path]/etc/gitconfig". This means even if they set up system-wide configs, developers can still override them locally.

**2. Individual Accountability and Identity**
Each developer needs to set their own name and email for commits so there's proper attribution of who made what changes. Global level configuration is "user-specific, meaning it is applied to an operating system user", so this can't really be done centrally for everyone.

**3. Project-Specific Needs**
Different projects might need different settings. You can "set different values for different users or repositories" and "set different default branches for different repositories and users". A central configuration wouldn't be flexible enough for various project requirements.

**4. Learning and Understanding**
By making developers set up their own Git config, the organization ensures that everyone actually understands the basics of how Git works. If it was all done centrally, people might not learn the fundamental concepts they need to troubleshoot problems.

**References:**
1. Git Official Documentation - Git Configuration: https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration
2. W3Schools Git Config Guide: https://www.w3schools.com/git/git_config.asp?remote=github

Honestly, as someone just starting with version control, I can see how both of these issues would create major headaches for development teams. It's like trying to coordinate a group project where nobody knows the rules - chaos would definitely ensue!