# Assembly Sequencing and Motion Planning for Grasshopper

![Reachability data with shell and robot silhouette](https://github.com/swilcock0/asamp/blob/main/asamp/resources/image.png?raw=true)


## Activating the Python remote procedure calls in Grasshopper
Install COMPAS_FAB as per [these instructions](https://gramaziokohler.github.io/compas_fab/latest/getting_started.html) to allow the connection from Grasshopper to ROS. It's recommended to install [Anaconda to allow](https://www.anaconda.com/) for building virtual Python environments. Having installed Anaconda, for Rhino 7 the commands should be 

```bash
conda config --add channels conda-forge
conda create -n research compas_fab
conda activate research
python -m compas_rhino.install -v 7.0
```

## Package installation
Once COMPAS_FAB is installed, the package is ready to be installed:

```bash
cd <package_base>
pip install -r requirements.txt
pip install .
```

Once installed, test by running 

```bash
python
>>> import asamp
>>> asamp.__version__
0.1
```

Restart Rhino if open and open the examples/CleanPaper.gh file.

## Using ROS functions
A version of ROS will be required running in parallel. One solution is to use a Docker image as indicated by [COMPAS_FAB](https://gramaziokohler.github.io/compas_fab/latest/backends/ros.html), ie. running `docker run -p 9090:9090 -t gramaziokohler/ros-base roslaunch rosbridge_server rosbridge_websocket.launch`. Personally I prefer a Virtual Machine as it provides a more persistent system with better inbuilt display capabilities and have been testing using VMWare with Ubuntu16.04, ROS Kinetic and Moveit installed.


