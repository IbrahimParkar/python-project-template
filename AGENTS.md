# Repository instructions

This is the repository-level `AGENTS.md`. Nested `AGENTS.md` files, when
present, provide more specific instructions for their respective areas.

Access nested `AGENTS.md` files only when the task requires work in their
directory or their instructions are otherwise relevant.

After code updates, always update the relevant nested `AGENTS.md` when one is
present and the change affects that directory's behavior, structure, or
conventions.

## Project conventions

- Put importable application code under `src/` and automated tests under
  `tests/`.
- Keep dependencies and tool configuration in `pyproject.toml`; use `uv` to
  manage the environment and lockfile.
- Commit `uv.lock` updates when project metadata or dependencies change; CI
  installs with `uv sync --locked`.
- Keep secrets in an ignored local `.env` file. Update `.env.example` with
  variable names and safe placeholder values only.
- Add or update tests when changing behavior.
- Run `uv run pre-commit run --all-files` before completing code changes.

## Code writing rules

When a requested change conflicts with established industry conventions, explain
the conflict and its tradeoffs to the user before implementing it.

When generating or modifying Python code, keep documentation-complete public
APIs. Add a module docstring to every public Python module (the file's first
statement), and add a Google-style docstring to every public class, function,
and method. In particular, satisfy the following expectations:

- Public modules describe the module's responsibility.
- Public classes and functions describe their purpose.
- Functions and methods document parameters with `Args:`, the result with
  `Returns:` when they return a value, and failures with `Raises:` when callers
  need to handle specific exceptions.
- Omit docstrings only for private helpers whose names begin with `_`, or when
  a documented override already fully specifies the inherited contract.

Keep docstrings accurate when behavior or signatures change, and use concise
Google-style wording rather than duplicating implementation details.

When code orchestrates a multi-step workflow, add brief comments at the
important orchestration steps in that orchestration file. This applies to
workflow, pipeline, service-coordination, and API-service code. API service
handlers should comment each important step, such as validating input,
authorizing access, loading data, calling the service layer, transforming the
result, persisting changes, and returning the response. Comments should state
the step's purpose, dependency, or state transition. Do not add these step
comments throughout ordinary helpers or repeat what each individual line
already says.

## Exception ownership

Service-specific exceptions belong in the owning service package. They should
inherit from shared exceptions when they need common handling; keep shared
exception modules limited to errors that are meaningful across services.

## General chatting rules

For simple conversational questions, answer with only "yes" or "no" when
possible. Provide an explanation only when it is required for clarity,
correctness, or completing the requested task.

## Commit message rules

When asked for a commit message, inspect and include all current tracked changes and untracked files in the repository unless the user explicitly specifies otherwise.

For broad changes, use a concise subject followed by bullet points summarizing
the main work areas. Keep a single-line subject for small, focused changes.

Use these prefixes when suggesting commit messages:

- `feat` - New functionality.
- `fix` - Bug fix.
- `refactor` - Code restructuring without behavior change.
- `chore` - Maintenance or configuration.
- `docs` - Documentation changes.
- `test` - Test changes.
- `perf` - Performance improvement.
- `build` - Build system or dependency changes.
- `ci` - CI/CD configuration changes.
- `style` - Formatting-only changes.
- `revert` - Reverts a previous commit.
