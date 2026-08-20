# RUNBOOK — poojakira

## Overview
GitHub profile README repo. Content in `README.md` renders on your GitHub profile page.

## Edit Profile
1. Open `README.md` in any editor.
2. Update bio, skills, or stats sections.
3. Commit and push — GitHub renders changes immediately.

## Update Project Links
Edit the projects section in `README.md`:
```markdown
## Projects
- [project-name](https://github.com/poojakira/project-name) — Short description
- [another-repo](https://github.com/poojakira/another-repo) — Short description
```

## Add Badges/Shields
```markdown
![Python](https://img.shields.io/badge/Python-3.11-blue)
![AWS](https://img.shields.io/badge/AWS-Certified-orange)
```

## Deploy
Deployment is automatic. Push to `main` branch and GitHub renders the updated profile.

```bash
git add README.md
git commit -m "Update profile"
git push origin main
```

## Tips
- Keep README under 500 lines for fast rendering.
- Use GitHub-flavored markdown only (no custom HTML that GitHub strips).
- Test locally with a markdown previewer before pushing.
- Images: host in the repo under `assets/` or use external URLs.
