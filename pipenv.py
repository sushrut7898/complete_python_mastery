# pipnv is dependency manager
# pipnv uses pip and virtual env together

# pip3 install pipenv
# pipenv install package_name -> created virtual env and also installed the package in it
# pipenv --venv -> gives lication of the vitual env created by pipenv
# pipenv shell -> activates virtual environment created by pipenv
# exit -> to deactivate the virtual environment

# on creating env 2 files get creted Pipfile & Pipfile.lock
# pipfile -> source -> dev packages -> packages appl dependent on -> requirement
# pipfile.lock -> json file -> dependencies and exact version of everything in application
# pipenv install -> installs all the dependies or all missing dependencies required by our program or application
# pipenv install --ignore-pipfile -> this will ignore pipfile while installing versions and will install the latest compatible version
# pipenv graph -> gives list og all the installed depencencies
# pipenv uninstall package_name
# pipenv update --outdated -> updates all the outdated versions
# pipenv update package_name -> Updates the specific package

