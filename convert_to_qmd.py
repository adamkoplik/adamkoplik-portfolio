import os

projects_path = "projects"

for project_folder in os.listdir(projects_path):
    project_path = os.path.join(projects_path, project_folder)
    readme_path = os.path.join(project_path, "README.md")
    qmd_path = os.path.join(project_path, "index.qmd")

    if os.path.isfile(readme_path):
        with open(readme_path, "r") as readme_file:
            content = readme_file.read()

        title = project_folder.replace("-", " ").title()

        frontmatter = f"""---
title: "{title}"
format:
  html:
    page-layout: article
    toc: true
---

"""

        with open(qmd_path, "w") as qmd_file:
            qmd_file.write(frontmatter + content)

        print(f"Converted {readme_path} → {qmd_path}")

print("\n✅ All README.md files converted to index.qmd files.")
