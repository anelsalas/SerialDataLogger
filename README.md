# SerialDataLogger
I need to connect to a serial port and be able to store data and plot it in the time and frequency domains.
  Requires Anaconda 3.7
  I've added a test hex file for the microchip Xpress board using pic16F1885
  
  To list Anaconda environments: conda info --envs
  
  To select an environment: conda activate py37
  
  To make sure conda is in your path, edit bashrc in your home path:
    vi ~/.bashrc and apend this to the end:
    . /opt/archiconda3/etc/profile.d/conda.sh
    
   Requires matplotlib:
   sudo apt-get install python3-matplotlib
   
    "sudo pip3 install serial" gave me an error:

   Error: ERROR: Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
   
   fixed using:
   sudo pip3 install --ignore-installed serial


