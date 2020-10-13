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
  * Ex. Navigate to some directory from root: `cd Documents/Dev/msda-workshop/examples`
  * Ex. Navigate UP one folder level: `cd ..`
  * Ex. List files in current directory: `ls`
  * Ex. Execute Python file: `python examples/hello_world.py`
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
  * We have a constant amount of computational power at our disposal (not scalable)
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
After preprocessing our data, we can experiment with a couple forecasting models.  With a time series project like this, typical cross validation methods are not available to us.  Instead, to evaluate the models' performance, we will use "Walk Forward Evaluation".  The Jupyter notebook contains some pre-built functions to streamline this process.  Here are some more details about the two models we will use here:
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

#### Step 4: Code Cleanup
The final step is to put the pieces together into a single chunk of executable code.  My preference is to construct this in Jupyter, using separate cells for each step of the process (configuration, data import, preprocessing, model training, forecasting, etc.) This will make it easier to write our Python package later.  During this process, we will convert our model testing code into streamlined model build and forecasting code, and we will decide how to save all resulting data and display our results.  Note that this step is highly dependent on how our model will be used in a production environment, which is ultimately decided by the business requirements.  Here are a few common methods:
* Store forecast data (to database or text files)
* Send forecast data to API (to integrate with some other service)
* Create visualization of results (with dashboarding tool or web app)

## Forecasting Package

### Package Overview

* **\_\_init\_\_.py**
  * This file is empty, but it allows our code to be run as a Python _package_.  More explanation below in "How to Run Forecasting Package".
* **utils.py**
  * This file contains _utility functions_, which make the rest of the code easier to work with.
* **config.py**
  * This file contains any configuration settings, like filepaths for data exports or database credentials.
* **queries.py**
  * This file contains any query functions, which connect to a database and return the desired data.
* **preprocessing.py**
  * This file contains preprocessing functions, which clean and transform the data into our desired format.
* **model_build.py**
  * This file contains the model build functions, which fit our specified models to the data and save the results.
* **forecasting.py**
  * This file contains functions which load our saved models and fit them to future data.
* **run_forecaster.py**
  * This is our _\_\_main_\_\_ file, which imports and runs all the other modules in our package.  It's like our forecasting control center, and this is the file we'll actually execute when we want to run the package.
* **app.py**
  * This is the only file that isn't executed by run_forecaster.py.  When we run this file through Streamlit, it will import the latest forecast data and launch a simple web app to display our forecast accuracy.

### How to Run Forecasting Package
1. In order to run the package, you must use the msda conda virtual environment, created via the provided environment.yml file (instructions above in "System Setup").  In addition, navigate to the directory that contains your cloned repo.  Your terminal prompt must show something like this:
`(msda) zach.button@x86_64-apple-darwin13 msda-workshop %`
    * `(msda)` means that I have activated the msda conda environment.  If your prompt shows `(base)` or something else, run `conda activate msda`.
    * `msda-workshop %` means that my current working directory is msda-workshop, where I cloned the repo.  If your working directory does not match your repo location, use `cd file/path` to navigate to the correct folder.
  
2. From here, you should be able to use the Python interpreter, execute Python scripts, and run Streamlit apps.
    * Python Interpreter: Type `python` and hit Enter/Return to start the interpreter.  This Python shell accepts normal Python commands and package imports, useful for testing small bits of functionality.  There are multiple ways to exit the Python interpreter, depending on your system:
      * Ctrl+Z
      * Ctrl+D
      * `exit()`
    * Python Script: Type `python examples/hello_world.py` and hit Enter/Return to run the hello_world script.  This should print `Hello world!` to your terminal.
    * Streamlit App: Type `streamlit run examples/uber_pickups.py` and hit Enter/Return to run the example Uber web app, provided through Streamlit documentation.  This should open an interactive web app in your browser, showing Uber ride data.  Use Ctrl+Z in the terminal to exit back to the prompt.

3. To run the forecasting package, type `python -m forecasting.run_forecaster` and hit Enter/Return.  The files are structured as a _package_ (and therefore must be executed this way) so that one module can import other modules.  This is a much cleaner solution than including all our Python code in a single script.  The execution time will depend on your specific machine (mine takes around 30-40 seconds).  While this package is accomplishing quite a bit, there's not much to see here (that's what the web app is for).

4. To launch the Streamlit web app, type `streamlit run forecasting/app.py`.  By default, the app will show performance metrics and a forecast plot for each of the two models.  Additionally, you may view the raw forecast data by clicking a checkbox.


## Additional Ideas
The goals of this workshop go beyond the single live session.  I wanted to walk through a typical project workflow to demonstrate some potentially new techniques and explain a Data Scientist's thought process.  However, I also wanted to provide a launching pad for your own forecasting project, which would give you invaluable hands-on experience and a code repository to show off throughout your job search.  While you can't copy this repo and claim it as your work, I've provided some ideas below for how you can make it your own:
* **Different Target Variable**: Pick a different field from the raw data to use as your target to forecast.
* **Forecast Per Car Category**: Expand the current functionality to forecast for each car_category and store/display the results.
* **Change Goals**: Think of a new business goal for forecasting this data and modify the code to achieve it.
* **Model Tuning**: Spend some time researching the two models and then build a Grid Search or Cross Validation system to fine-tune their hyperparameters.
* **Feature Engineering**: Apply more robust feature engineering, using lags, differences, and rolling window functions on the various data features and evaluating their impact on the models.
* **Code Best Practices**: Exercise some coding best practices by adding logging, function documentation, and error handling to the existing code.
* **Different Models**: Experiment with model types other than Prophet and XGBoost to see if you can beat the existing forecast performance.
* **Web App**: Embellish the web app with additional features (plots/data, filters, buttons, etc) or aesthetics (formatting, design).

Better yet, create your own project from scratch!  You can follow the same steps outlined in this workshop.  Find publicly available data online, develop some business requirement ideas, explore with SQL and Python, start building some models, and store it all in your version controlled GitHub repo.
