# JIRA 2 Branch

Takes a JIRA issue and creates a git branch

```
Usage: jira2branch [OPTIONS] ISSUE_ID_OR_URL SOURCE_BRANCH

  Simple program that takes a JIRA issue ID and creates a new local and
  tracking remote branch

Options:
  -n, --name-only      Generates the branch name and prints it, no actual
                       branch will be created (default is False)
  -p, --push           Push newly created branch to remote (default is False)
  -t, --target PATH    Target repository (default is current directory)
  -r, --merge-request  Create merge request. Requires --push. (default is False)
  -c, --confirm        Request confirmation before creating the merge request (default is False)
  -d --dry-run         Dry run. Prints out the MR payload in JSON format but does not invoke the API 
  
  --preview (experimental) This toggles live preview ON when editing a merge request description. Requires vim being set as $EDITOR with markdown-preview.vim plugin installed

  --help               Show this message and exit.
```

- Branch naming format is as follows:
  - {CONVENTIONAL_COMMIT_PREFIX}/{ISSUE_ID}_{ISSUE_TITLE}

## Requirements

Requires Python 3.11

### Dev env

```
pip install poetry
poetry install
pip install dist/jira2branch-[VERSION]-py3-none-any.whl
```

Afterwards, your command should be available:

```
$ jira2branch WT3-227 develop
fix/WT3-227_some-jira-issue
```

### Credentials

JIRA credentials will be fetched from `[USER HOME]/.j2b/secrets.ini` with the following format:

```ini
[JIRA CREDENTIALS]

# url = 
# email = 
# username = 
# password = 
# token = 
```

WIP: GitLab credentials will also be required for automatic MR creation

#### Required fields

`url` and `email` are required.

Use either `username` + `password` or `token` depending on how access is configured

## Usage

`python main.py [JIRA_ISSUE_ID|JIRA_ISSUE_URL]`

### Examples

`python main.py WT3-227 develop`

`python main.py https://company.atlassian.net/browse/WT3-227 develop`
