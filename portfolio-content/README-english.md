# Portfolio Content - Markdown Files

This folder contains the markdown files that are served by the backend for:

1. **Feeding the chat AI** - Contents in `portfolio-content/*.md` are automatically loaded and included in the system context for the AI
2. **Serving project markdowns** - Files in `portfolio-content/projects/{project_name}.md` are served via REST API for the frontend

## Structure

```
portfolio-content/
├── README.md (this file)
├── *.md (general markdowns for the AI - summaries, portfolio info, etc.)
└── projects/
    ├── {project-name}.md (markdowns specific to each project)
    └── ...
```

## How it works

### Markdowns for the AI

- `.md` files in the root of `portfolio-content/` are loaded automatically
- They are included in the AI system prompt when the chat is initialized
- Limit of 4000 characters per file (to avoid excessive tokens)

### Project Markdowns

- Files in `portfolio-content/projects/{project_name}.md`
- Served via endpoint: `GET /api/projects/{projectName}/markdown`
- The project name is normalized (lowercase, trim) before fetching the file
- Example: project "LoL-Matchmaking-Fazenda" fetches `lol-matchmaking-fazenda.md`

## Migration of Markdowns

The markdowns were migrated from `frontend/public/assets/portfolio_md/` to this folder in the backend because:

- They will be served dynamically by the backend in the future
- Enables access control and caching
- Facilitates updates without rebuilding the frontend

