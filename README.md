# msda-workshop

## Project Introduction

### RideAustin Forecasting
In 2016, the city of Austin, TX attempted to apply new regulations for hiring rideshare drivers. The industry's two giants, Uber and Lyft, felt that the regulations were unnecessary and prohibitive, so they chose to leave the city altogether. In their wake, the community created a non-profit rideshare organization, called RideAustin, to provide a similar transportation service to Austin citizens. When the regulations were overturned less than one year later, Uber and Lyft swept back into the city, serving RideAustin a swift death.

Our goal is to act as a RideAustin data scientist in 2017, using historical rideshare data to forecast our future growth (assuming no policy revisions).  The data was obtained for free through data.world, a platform which allows data collection, sharing, manipulation, and analysis.  Sign up for a free account and visit this project's [data.world workspace](https://data.world/zbutton/msda-workshop-rideaustin "RideAustin Data") to view and interact with the raw data.

### GitHub Repo
This repository contains all the files you'll need for the workshop, including the following:
* This README - contains all the instructions needed for the workshop and beyond
* Jupyter notebook - will form the basis of the actual workshop
* Data files - will be processed and used for forecasting
* Configuration file - ensures that all necessary Python packages are installed correctly
* Forecasting package - the workshop's final product

### System Setup
In order to use this repository and/or follow along during the workshop, follow these setup steps:
* Gain basic familiarity with terminal/command line interface
  * Default is Terminal on macOS and cmd on Windows - feel free to install an alternative
   * My choice: iTerm2 on macOS Catalina
  * Example, navigate to some directory from root: `cd Documents/Dev/msda-workshop/examples`
  * Example, navigate UP one folder level: `cd ..`
  * Example, list files in current directory: `ls`
  * Example, execute Python file: `python examples/hello_world.py`
* Create a free GitHub account
* Install git on your machine ([instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
* Fork this repo into your account ([instructions](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo))

**OPTIONAL**, if you'd like to edit or run the forecasting package
* Clone your new repo to your machine ([instructions](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
  * In case you need to work with git-lfs (large file storage): documentation [here](https://git-lfs.github.com/) and [here](https://medium.com/@pavanskipo/how-to-use-git-lfs-large-file-storage-to-push-large-files-to-github-41c8db1e2d65)
* Install Anaconda ([instructions](https://docs.anaconda.com/anaconda/install/))
  * Alternative: Miniconda, a minimal installation of Anaconda ([instructions](https://docs.conda.io/en/latest/miniconda.html))
* Verify installation (`conda list`)
  * Create conda virtual environment using provided configuration file
  * Navigate to your repo's directory (ex. `cd Documents/Dev/msda-workshop`)
  * Create environment (`conda env create --file environment.yml`)
  * Verify environment creation (`conda env list`)
* Activate conda environment (`conda activate msda`)


## Workshop

### Working with Jupyter Notebook
If you cloned this repo to your machine, then you can open the "Forecasting - Workshop" notebook via the normal Jupyter workflow ([documentation here](https://jupyter.org/install)).  However, I have also made it available to the more casual attendee through a tool called [Binder](https://mybinder.readthedocs.io/en/latest/index.html).  Binder allows us to start a Jupyter environment directly from a GitHub repository, treating the repo like a normal file directory.  The package dependencies are all managed via the environment.yml file stored here, and any data files in this repository can be imported into Python.  To launch your Binder session, click the button below:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/zbutton314/msda-workshop/master)

A few more notes on Binder:
* If the above button fails for you, try visiting https://mybinder.org/ instead:
  * Enter https://github.com/zbutton314/msda-workshop into the "GitHub repository name or URL" field
  * Click "Launch"
* Binder is hosted securely in the cloud - this makes it possible for several people to easily launch their own Binder sessions from the same repo, but it does have a few implications:
  * We are limited to about 2GB of memory, so we must be careful about the data we generate
  * We are not able to scale the computational power at our disposal
  * 







