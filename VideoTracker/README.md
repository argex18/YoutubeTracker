# The scripts in this repository use the Youtube API to create a tracker for Youtube.
# In this first version of the repository, it just provides the functions to detect the upload of new videos by part of your subscriptions and the putting of likes.
# I think to further extend it by adding new functions of which the tasks will be able to vary, from the comments management to the direct upload of new videos to the platform. 

# REQUISITES TO USE THE SCRIPT:
    
    1) Youtube API installed among your Python packages.
       Link to download them: https://developers.google.com/youtube/v3/quickstart/python

    2) Python 2.7 or Python 3.5+

    3) An OAuth 2.0 client ID to submit an authorized request that retrieves          information about your own YouTube channel.
       In case you didn't have one, i'd highly recommend you to read the official Google documentation: https://developers.google.com/youtube/v3/quickstart/python#step_1_set_up_your_project_and_credentials

# HOW TO USE THE SCRIPTS:

    You can choose to run the entire script by clicking on the main.py file or you may just want to use a single function present in the package.
# WARNING: NOT ALL MODULES OF THE PACKAGE ARE RUNNABLE WITHOUT THE MAIN FILE.
    Anyway, regardless of that, to run a module or the entire script you can simply double-click on that one or you can digit via console:
    // python module_you_want_to_run.py 

    It will be asked you to insert the path of your client secret file.
    This one is that you had previously downloaded when creating your credentials file. Make sure to accurately digit it.
# WARNING: AN ERROR IN THIS PHASE WILL CAUSE THE SCRIPT TO STOP WORKING. 
    Once started, the script will run in background and perform a cycle of operations every 10 minutes. The coders who want to change the time will simply have to change the value of the sleep function in main.py