#!/usr/bin/env bash


if [ -z "$(git status --porcelain)" ]; then 
  # Working directory clean
  echo "git working directory is clean."
  exit 0
else 
  # Uncommitted changes
  echo "git working directory is dirty,"
  echo "Files causing issues:"
  echo ""
  echo "$(git status --porcelain)"
  echo ""
  exit 1
fi
