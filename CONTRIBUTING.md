# Contributing

Thanks for your interest in contributing to STL Viewer!

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/stl-viewer.git
   cd stl-viewer
   ```
3. Open `index.html` directly in a browser — no build step needed.

## Development Workflow

Since this is a single-file, no-build project, development is straightforward:

- Edit `index.html` directly
- Refresh the browser to see changes
- Use browser DevTools (F12) for debugging

For the Python STL generator:
```bash
pip install numpy
python scripts/generate_holder.py
```

## Submitting Changes

1. Create a descriptive branch:
   ```bash
   git checkout -b fix/gizmo-initialization
   # or
   git checkout -b feature/measurement-tool
   ```
2. Make your changes with clear, atomic commits:
   ```bash
   git commit -m "fix: move gizmo setup before animate() call"
   ```
3. Push and open a Pull Request against `main`

## Commit Message Convention

Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

| Prefix | Use for |
|--------|---------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `style:` | Formatting, no logic change |
| `refactor:` | Code restructuring |
| `perf:` | Performance improvement |
| `chore:` | Build process, tooling |

## Reporting Bugs

Please open a GitHub Issue with:
- Browser name and version
- Steps to reproduce
- Expected vs. actual behavior
- Console error output (if any)
- Sample STL file that reproduces the issue (if applicable)

## Code Style

- Vanilla JS — no frameworks, no npm
- Inline comments for non-obvious logic
- Keep the viewer as a **single self-contained HTML file**
- Test on Chrome, Firefox, and Safari before submitting

## License

By contributing, you agree your changes will be released under the [MIT License](LICENSE).
