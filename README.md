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
  * It may take upwards of 10-15 minutes to build your session for the first time (subsequent Binder launches are very quick)
  * We are limited to about 2GB of memory, so we must be careful about the data we generate
  * We are not able to scale the computational power at our disposal
  * Binder may shut down your session after ~10 minutes of inactivity
  * Any changes made during a Binder session will NOT be saved back to the original file
* Therefore, some best practices:
  * Make sure to continually interact with your Jupyter notebook to keep the session live, if you are making any changes
  * Periodically download your Jupyter notebook: File -> Download as -> Notebook (.ipynb)
  * To make your changes available in a future Binder session:
    * Download the notebook
    * Copy the notebook into your local repository (delete the old notebook and rename the file, if necessary)
    * Commit and push this change to the remote repository on GitHub
    * Your next Binder session will now build using the updated Jupyter notebook

### Project Overview

#### Step 1: Importing Data
In this workshop, we will use RideAustin data from 2016-2017 to build two models and forecast future values.  The raw data is saved in three CSV files, called Rides_DataA, Rides_DataB, and Weather_Data.  In order to simulate a typical data science workflow, I used SQLite to combine the three files into a single database file, called msda_workshop.  The msda_workshop database contains three tables with the same three names.  The first step of the project is to use SQLite's Python API to load this data into Pandas dataframes for inspection.  As we learn more about the data and refine our goals, we will edit this SQL code to manipulate and restructure the data.

#### Step 2: Preprocessing
As we explore the data, we'll collect a series of preprocessing steps that must be used to clean or reorganize our data.  This may also include some feature engineering, where additional features are generated from existing data.  Those steps will be refined and then combined into a single preprocessing function to convert our messy data into clean data.

#### Step 3: Model Testing
After preprocessing our data, we can experiment with a couple forecasting models.  With a time series project like this, typical cross validation methods are not available to us.  Instead, to evaluate the models' performance, we will use "Walk Forward Evaluation".  The Jupyter notebook contains some pre-built functions to streamline this process.  Here are some more details about the two models used here:
* Prophet ([documentation](https://facebook.github.io/prophet/))
  * Developed by Facebook to forecast internal metrics
  * Based on Time Series Decomposition model
  * Pros:
    * Very user-friendly
    * Great built-in output
    * Built specifically for time series forecasting
  * Cons:
    * Not very flexible
    * Performance may struggle when adding external regressors
* XGBoost ([documentation](https://xgboost.readthedocs.io/en/latest/))
  * Developed as research project, rose to prominence after winning multiple machine learning competitions
  * Based on Decision Trees
  * Pros:
    * Very fast
    * Highly tunable and applicable to many types of problems
    * Available in any platform
  * Cons:
    * Hyperparameters and underlying math are daunting
    * Any desired output must be custom-built







