# Jupyter notebooks for Module 1 of the Computer Networks course
This repository contains the notebooks that are designed as part of the online networking course offered by the Centre for Networked Intelligence.
 
## Setting up the local environment
To run these notebooks on your local machine, make sure that you have python installed, preferably version 3.x.

#### Installing Virtualenv for python
The next step is to install [`python-virtualenv`](https://docs.python-guide.org/dev/virtualenvs/), this creates an isolated environment to run different packages.  To install virtualenv, use the following command, for Linux and Unix

```bash
pip3 install virtualenv
```

In Windows, you can install virtualenv using just `pip` instead of `pip3`.

#### Starting the virtualenv and installing packages
The last step, before getting started on the notebooks will be to start the virtualenv and install the packages which is done by running the following commands:
  1. `source network-algo-dev-env/bin/activate` will be the start the python virtual environment.
  2. `pip3 install -r requirements.txt` will install all the packages that are not present (these packages are available only within the virtual environment)
  3. `jupyter notebook` will start the jupyter notebook server, and the notebooks can be accessed from the `notebooks/` directory
  4. Once you are done, you can exit from the python virtual environment by typing `deactivate` 
  5. You can also delete the directory after the use and none of the packages installed will remain in your system.
  
## Running the notebooks in Google Colab
We list the steps to run the notebooks in google colab.
 1. Open google colab : https://colab.research.google.com/
 2. From File menu, select "Open notebook".
 3. Select the GitHub tab.
 4. In the search bar, paste the github link (the Github url for the notebook). For example, to open the notebook on Dijkstra, the github link is https://github.com/cni-iisc/module1_notebooks/blob/master/notebooks/1_dijkstra.ipynb
 5. Add the following two line to a cell on top of the notebook and execute:
           
           ``` 
           !git clone https://github.com/cni-iisc/computer-networks-course.git
           !ln -sf computer-networks-course/modules modules
           ```
  
