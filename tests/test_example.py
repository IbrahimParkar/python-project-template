"""Tests for the starter application."""

import pytest


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    """Check that the example command prints its greeting."""
    from python_project_template.__main__ import main

    main()

    assert capsys.readouterr().out == "Hello from python-project-template!\n"
