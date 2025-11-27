## Tree for 
```
├── .gitignore
├── README.md
├── .github/
│   └── workflows/
│       ├── ci.yaml
│       └── cd.yaml
├── requirements.txt
├── calculator.py
└── test/
    └── test_calculator.py
```

## File: .gitignore
```
### Python template
solution/

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```
## File: README.md
```markdown
# Advanced Topics of Software Engineering: CI/CD

Welcome to the Python CI/CD Tutorial! This guide will walk you through enhancing a simple `Calculator` class, setting up a Continuous Integration and Continuous Deployment (CI/CD) pipeline on Github Actions, and ensuring your code meets high-quality standards through automated testing and code coverage.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Tutorial Steps](#tutorial-steps)
   1. [1. Clone the Repository](#1-clone-the-repository)
   2. [2. Create a Virtual Environment](#2-create-a-virtual-environment)
   3. [3. Install Requirements](#3-install-requirements)
   4. [4. Run Unit Tests Offline](#4-run-unit-tests-offline)
   5. [5. Fix the Bug in the Code](#5-fix-the-bug-in-the-code)
   6. [6. Push to Your Own Repository](#6-push-to-your-own-repository)
   7. [7. Check CI Results](#7-check-ci-results)
   8. [8. Write Additional Test Cases](#8-write-additional-test-cases)
   9. [9. Push Again and Check Coverage Report](#9-push-again-and-check-coverage-report)
   10. [10. Check the CD YAML File](#10-check-the-cd-yaml-file)
3. [Additional Resources](#additional-resources)
4. [Troubleshooting](#troubleshooting)
5. [Conclusion](#conclusion)

---

## Prerequisites

Before starting the tutorial, ensure you have the following installed on your machine:

* **Git**: Version control system. [Download Git](https://git-scm.com/downloads)
* **Anaconda**: Package and environment management system. [Download Anaconda](https://www.anaconda.com/download)
* **Python 3.8 in anaconda**: Programming language.
* **GitHub Account**: To host your repository and use GitHub Actions for CI/CD.
* **Code Editor**: Such as VS Code, PyCharm, or any preferred editor.

---

## Tutorial Steps

### 0. Fork the Repository

### 1. Clone the Repository

Begin by cloning the tutorial repository to your local machine.

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">gh repo clone your-username/Advanced-Topics-of-Software-Engineering
cd Advanced-Topics-of-Software-Engineering
</code></div></div></pre>

> **Note:** Replace `your-username` with your GitHub username. Make sure you have forked the repository.
> if you need to you are required to authorize your account when cloning the repo, please choose `SSH` way. (Need to create a new key on GitHub)

### 2. Create a Virtual Environment

Creating a virtual environment helps manage project-specific dependencies. 

Open "Anaconda Prompt":

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">conda create -n myenv python=3.8
</code></div></div></pre>

> **Note:** Replace `myenv` with your own environment name.


Activate the virtual environment:

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">conda activate myenv
</code></div></div></pre>

### 3. Install Requirements

Install the necessary Python packages using `pip`. Ensure you have a `requirements.txt` file in the repository.

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install --upgrade pip
pip install -r requirements.txt
</code></div></div></pre>

> **Tip:** If `requirements.txt` is not present, you can create one based on the dependencies used in the project.

### 4. Run Unit Tests Offline

Before making any changes, run the existing unit tests to ensure everything is working correctly.

<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">coverage run -m pytest
</code></div></div></pre>

You should see output indicating that all tests have passed. If there are any failures, review the test cases and the code to understand the issues.

### 5. Fix the Bug in the Code

For this tutorial, a deliberate bug has been introduced in the `Calculator` class. Your task is to identify and fix it.

### 6. Push to Your Own Repository

To implement CI/CD, you need to work on your own fork of the repository.

1. **Commit and Push Your Changes:**
   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git add calculator.py
   git commit -m "Fix bug"
   git push origin main
   </code></div></div></pre>

> **Note:** Replace `your-username` with your GitHub username.

### 7. Check CI Results

After pushing your changes, GitHub Actions will automatically trigger the CI workflow.

1. **Navigate to Your Repository on GitHub.**
2. **Go to the "Actions" Tab:**
   * Here, you can see the status of your CI workflows.
   * Ensure that all tests pass successfully.

> **Tip:** If the CI fails, review the error logs provided in the Actions tab to debug and fix the issues.

### 8. Write Additional Test Cases

To achieve over 90% code coverage, you need to write more comprehensive test cases.

1. **Open the Test File**
2. **Add Test Cases for Advanced Functions:**

   * Ensure that all methods in the `Calculator` class are tested, including edge cases.
3. **Run Tests Locally to Ensure They Pass:**

   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">coverage run -m pytest
   </code></div></div></pre>
4. **Check Code Coverage:**
   Ensure that your test coverage is above 90%. You can use `coverage.py` to check this.

   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">
   coverage report
   coverage html  # Generates an HTML report
   </code></div></div></pre>

### 9. Push Again and Check Coverage Report

After writing additional tests:

1. **Commit Your Test Cases:**
   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git add tests/test_calculator.py
   git commit -m "Add additional test cases for Calculator class"
   </code></div></div></pre>
2. **Push to GitHub:**
   <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git push origin main
   </code></div></div></pre>
3. **Verify Coverage Report:**
   * GitHub Actions should automatically run the CI workflow, including code coverage checks.
   * Navigate to the "Actions" tab to ensure that the coverage report is uploaded successfully.

### 10. Check the CD YAML File

Review the Continuous Deployment (CD) configuration to understand the deployment pipeline.

1. **Locate the CD Workflow File**
2. **Review the YAML Configuration**
3. **Understand Each Step**

## Conclusion

Congratulations! By completing this tutorial, you've:

* Enhanced a Python `Calculator` class with advanced features.
* Set up a virtual environment and managed dependencies.
* Implemented unit tests and achieved high code coverage.
* Configured a CI/CD pipeline using GitHub Actions to automate testing and deployment.

These skills are essential for modern software development, ensuring code quality, reliability, and streamlined deployment processes. Happy coding!
```
## File: requirements.txt
```
appnope==0.1.4
astroid==3.2.4
asttokens==2.4.1
attrs==24.2.0
backcall==0.2.0
beautifulsoup4==4.12.3
bleach==6.1.0
cachetools==5.5.0
certifi==2024.8.30
chardet==5.2.0
charset-normalizer==3.3.2
colorama==0.4.6
coverage==7.6.1
decorator==5.1.1
defusedxml==0.7.1
dill==0.3.8
distlib==0.3.8
docopt==0.6.2
exceptiongroup==1.2.2
executing==2.1.0
fastjsonschema==2.20.0
filelock==3.16.0
flake8==7.1.1
idna==3.8
iniconfig==2.0.0
ipython==8.12.3
isort==5.13.2
jedi==0.19.1
Jinja2==3.1.4
jsonschema==4.23.0
jsonschema-specifications==2023.12.1
jupyter_client==8.6.2
jupyter_core==5.7.2
jupyterlab_pygments==0.3.0
MarkupSafe==2.1.5
matplotlib-inline==0.1.7
mccabe==0.7.0
mistune==3.0.2
nbclient==0.10.0
nbconvert==7.16.4
nbformat==5.10.4
packaging==24.1
pandocfilters==1.5.1
parso==0.8.4
pexpect==4.9.0
pickleshare==0.7.5
pipreqs==0.5.0
platformdirs==4.3.2
pluggy==1.5.0
prompt_toolkit==3.0.47
ptyprocess==0.7.0
pure_eval==0.2.3
pycodestyle==2.12.1
pyflakes==3.2.0
Pygments==2.18.0
pylint==3.2.7
pyproject-api==1.7.1
pytest==8.3.3
python-dateutil==2.9.0.post0
pyzmq==26.2.0
referencing==0.35.1
requests==2.32.3
rpds-py==0.20.0
six==1.16.0
soupsieve==2.6
stack-data==0.6.3
tinycss2==1.3.0
tomli==2.0.1
tomlkit==0.13.2
tornado==6.4.1
tox==4.18.1
traitlets==5.14.3
typing_extensions==4.12.2
urllib3==2.2.3
virtualenv==20.26.4
wcwidth==0.2.13
webencodings==0.5.1
yarg==0.1.9
```
## File: calculator.py
```python
import math


class Calculator:
    def __init__(self):
        self.memory = None
        self.stack = []

    # Basic Operations
    def add(self, a, b):
        result = a + b
        self._push_stack(result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._push_stack(result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._push_stack(result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self._push_stack(result)
        return result

    # Advanced Operations
    def power(self, a, b):
        result = a ** (b)
        self._push_stack(result)
        return result

    def square_root(self, a):
        if a < 0:
            raise ValueError(
                "Can calculate square root only for non-negative values"
            )
        else:
            result = math.sqrt(abs(a))
            self._push_stack(result)
            return result

    def factorial(self, a):
        if a < 0:
            raise ValueError("Factorial is only for non-negative integers.")
        elif not isinstance(a, int):
            raise ValueError("Factorial is only defined for integers")
        else:
            result = math.factorial(int(a))
            self._push_stack(result)
            return result

    # Utility Functions
    def negate(self, a):
        """Returns the negation of a number."""
        result = -a
        self._push_stack(result)
        return result

    def absolute(self, a):
        """Returns the absolute value of a number."""
        result = abs(a)
        self._push_stack(result)
        return result

    def modulo(self, a, b):
        """Returns the modulo (remainder) of a by b. Raises on b == 0."""
        if b == 0:
            raise ValueError("Cannot modulo by zero.")
        result = a % b
        self._push_stack(result)
        return result

    def is_even(self, a):
        """Returns True if integer a is even. Requires integer input."""
        if not isinstance(a, int):
            raise ValueError("is_even requires integer input.")
        result = (a % 2) == 0
        self._push_stack(result)
        return result

    def gcd(self, a, b):
        """Returns the greatest common divisor of a and b."""
        result = math.gcd(a, b)
        self._push_stack(result)
        return result

    # Memory Functions
    def memory_store(self, value):
        self.memory = value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = None

    # Stack Functions
    def _push_stack(self, value):
        """Pushes a result onto the stack."""
        self.stack.append(value)

    def get_last_result(self):
        """Retrieves the last result from the stack."""
        if not self.stack:
            return None
        return self.stack[-1]

    def get_stack(self):
        """Returns the entire stack."""
        return self.stack

    def clear_stack(self):
        """Clears the result stack."""
        self.stack = []
```
## File: .github/workflows/ci.yaml
```yaml
name: ci
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

  workflow_dispatch:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install base dependencies - Ubuntu
        run: |
          python -m pip install --upgrade pip
          python -m pip install flake8

      - name: Check Python linting
        run: |
            flake8 . --count --show-source --statistics
  test:
    runs-on: ${{ matrix.platform }}
    needs: lint
    strategy:
      matrix:
        platform: [ubuntu-latest]
        python-version: [ '3.8', '3.9', '3.10']

    env:
      PY_COLORS: 1

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install base dependencies - Ubuntu
        run: |
          python -m pip install --upgrade pip
          python -m pip install -r requirements.txt

      - name: Run tests with coverage
        run: |
          coverage run -m pytest

      - name: Generate coverage report in XML
        if: matrix.python-version == '3.10'
        run: |
          coverage xml

      - name: Upload coverage report artifact
        if: matrix.python-version == '3.10'
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: coverage.xml
      
  check-coverage:
      runs-on: ubuntu-latest
      needs: test

      steps:
      - name: Download coverage report
        uses: actions/download-artifact@v4
        with:
          name: coverage-report

      - name: Upload coverage report to Codecov
        run: |
            echo "Uploading coverage report..."
```
## File: .github/workflows/cd.yaml
```yaml
name: cd
on:
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install -r requirements.txt

      - name: Build the application
        run: |
          # Commands to build or package your application
          echo "Building application..."

      - name: Deploy to production
        run: |
          # Replace this section with the actual deployment logic
          echo "Deploying application..."
          # For example, pushing Docker images or deploying to cloud
          # docker build -t my-app .
          # docker push my-app:latest

      - name: Post-Deployment Steps
        run: |
          echo "Deployment successful!"
```
## File: test/test_calculator.py
```python
import pytest
from calculator import Calculator


class TestCalculator:
    def test_add(self):
        calc = Calculator()
        assert calc.add(1, 2) == 3
        assert calc.get_stack() == [3]

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(4, 2) == 2

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 5) == 10

    def test_divide(self):
        calc = Calculator()
        assert calc.divide(10, 1) == 10

    def test_power(self):
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.get_last_result() == 8

    def test_square_root_negative_raises(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.square_root(-4)

    def test_factorial_requires_integer(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.factorial(4.5)
        assert calc.factorial(5) == 120

    def test_memory_store_and_clear(self):
        calc = Calculator()
        calc.memory_store(7)
        assert calc.memory_recall() == 7
        calc.memory_clear()
        assert calc.memory_recall() is None

    def test_get_last_result_and_clear_stack(self):
        calc = Calculator()
        calc.add(1, 1)
        calc.multiply(2, 3)
        assert calc.get_last_result() == 6
        calc.clear_stack()
        assert calc.get_stack() == []
        calc.add(2, 3)
        assert calc.get_last_result() == 5
```
