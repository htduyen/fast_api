# fast_api

# pyenv

    pyenv install <version python>
    pyenv versions

    pyenv virtualenv 3.10.5 <env>
    pyenv versions # check
    pyenv activate <env>

# Editorconfig

    Create: .editorcongig
    Add rules


# Linter, formater

    ## Black

        pdm add black

        black {source_file_or_directory}
    
    ## Isort

        pdm add isort

        pdm run isort <source_file_or_directory>

    ## Bandit: Bandit is a tool designed to find common security issues in Python code. To do this, Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files, it generates a report.

        pdm add bandit

        pdm run bandit <source_file_or_directory>


    # Flake8

        pdm add flake8


# PDM https://pdm.fming.dev/latest/usage/project/

    cd prject-name
    pdm init

    pdm info # Show the current Python environment

    ### Manage Dependencies

    ## Add dependencies

        pdm add requests
        pdm add requests==2.25.1

        pdm add -d pytest  # dev-dependencies
        pdm add -dG format black


    # Remove requests from the default dependencies
    
        pdm remove requests
    

    # Install package in pyproject.toml (as npm install, pip install -r requirement.txt)

        pdm install  # Delete __pypackages__ and do it
    
        pdm list --graph # Graph of dependences in projects


    # Export requirement.txt

        pdm export -o requirements.txt

    
    # Start application by pdm

        [tool.pdm.scripts]
        app = "flask run -p 8000"
        lint_bandit = "bandit -r"
        lint_flake8 = "flake8"

        pdm run app  # app must be mapping with app in pyproject.toml
        pdm run lint_bandit lint_flake8


#  Git

## HTTP

    sudo apt install libnss3-tools
    curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64"
    chmod +x mkcert-v*-linux-amd64
    sudo cp mkcert-v*-linux-amd64 /usr/local/bin/mkcert

    #  Generate cert file
    mkcert localhost 127.0.0.1 0.0.0.0

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
        ssl_keyfile="./localhost+2-key.pem",
        ssl_certfile="./localhost+2.pem"
    )

# SQLAlchemy

    1. Without orm_mode, if you returned a SQLAlchemy model from your path operation, it wouldn't include the relationship data.

    2. 