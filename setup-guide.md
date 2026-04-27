# Workspace Setup Guide: Work Computer

Follow this guide to integrate your personal "Brain" repository with your work environment. This setup allows you to leverage your entire personal knowledge base, use GitHub Copilot efficiently, and ensure you can take your notes with you when you leave—all while maintaining strict legal boundaries regarding company Intellectual Property (IP).

## Prerequisites
- **Git** is installed on your work computer.
- **VS Code** is installed.
- **GitHub Copilot** extension is installed and signed in.
- You have permission to use a personal GitHub SSH key or PAT to pull/push your `brain` repository on your work machine.

---

### Step 1: Clone the Repositories
Open your terminal on your work computer and navigate to your preferred projects directory (e.g., `D:\Projects\`).

1. Clone your company repository:
   ```bash
   git clone <company-repo-url> work-repo
   ```
2. Clone your personal Brain repository:
   ```bash
   git clone <your-personal-github-url>/brain brain
   ```

### Step 2: Configure Your Multi-Root Workspace
You want VS Code and Copilot to have context of both your work codebase and your full personal knowledge base.

1. Open VS Code.
2. Go to **File > Open Folder...** and select your company repository (`D:\Projects\work-repo`).
3. Go to **File > Add Folder to Workspace...**
4. Select the **entire root** `D:\Projects\brain\` folder and click **Add**.
5. Go to **File > Save Workspace As...** and save the file as `company-project.code-workspace` in a safe location (ensure it's ignored via `.gitignore` if saved inside your company repo).
6. From now on, open this `.code-workspace` file to launch your IDE. 
   *(Note: Because the root of `brain` is in the workspace, Copilot will automatically detect and follow `.github/copilot-instructions.md` without any extra configuration).*

### Step 3: The Daily Workflow & IP Safety

Your VS Code Explorer will now have two top-level folders:
- `work-repo` (Company IP)
- `brain` (Your Personal Knowledge Base)

**How to use it:**
- **Coding:** Write all actual software in `work-repo`. 
- **Strategizing & Logging:** Draft your professional posts, AI strategies, and daily logs in `brain/work/`. Keeping work-related notes in this specific folder organizes them cleanly.
- **Learning:** Access your `brain/learning/` materials directly alongside your code for quick reference.
- **Committing:**
  - Push code from `work-repo` to your company GitHub.
  - Push notes and strategies from `brain` to your personal GitHub.

> [!CAUTION] 
> **THE GOLDEN IP RULE:** You must **never** commit proprietary company source code, algorithms, API keys, or confidential architecture into any folder within the `brain` repository. The `brain` repo is for high-level strategy, personal task management, and learning. It is a legal boundary. All actionable company code belongs strictly in `work-repo`.

### Step 4: Offboarding
If you leave the company, simply delete the `D:\Projects\brain` folder off your work laptop on your last day. Because you've been pushing your notes to your personal GitHub, your entire professional journal, strategy drafts, and learning history comes with you safely and seamlessly.
