trajopt is an optimization-based motion planning library written by John Schulman. The original document can be found in here:
http://rll.berkeley.edu/trajopt/doc/sphinx_build/html/#
### Changes we made in this repo
* it can be compiled as a catkin package through catkin_make
* add more cost and constraint functions
* add grabed objects into self collision ignore list

### Installation tips
trajopt requires OPENRAVE 0.9 and [Gurobi](http://www.gurobi.com/). There is an install instruction in the above trajopt document. http://rll.berkeley.edu/trajopt/doc/sphinx_build/html/install.html
Here, I list the installation steps which I followed.
* install OPENRAVE 0.9
  * ubuntu 12.04<br>
    `sudo apt-get -y install  libopenscenegraph-dev cmake libboost-all-dev libeigen3-dev python-numpy python3.2-dev`<br>
    `sudo add-apt-repository -y ppa:openrave/testing`<br>
    `sudo apt-get -y update`<br>
    `sudo apt-get -y install openrave`<br>
    `echo export LD_LIBRARY_PATH='${LD_LIBRARY_PATH}':/usr/lib >> ~/.bashrc`
  * ubuntu 14.04<br>
    Since there isn't a ppa for ubuntu 14.04, we have to build it from source. I used the following instruction: https://scaron.info/teaching/installing-openrave-on-ubuntu-14.04.html

* install Gurobi<br>
  * Download current version [gurobi 6.5.0](http://user.gurobi.com/download/gurobi-optimizer) into your ~/Downloads folder.<br>
  `cd ~/Downloads`<br>
  `tar xvfz gurobi6.5.0_linux64.tar.gz`<br>
  `sudo mv gurobi650 /opt/`<br>
  * Getting a license<br>
    go to http://www.gurobi.com/downloads/licenses/license-center and requrest an university lisence. Once you have a free university lisence,<br>
    `cd /opt/gurobi605/linux64/bin`<br>
    `./grbgetkey <LICENSE NUMBER GOES HERE>`<br>
  * Set GUROBI_HOME environment variable.<br>
    `echo export GUROBI_HOME="/opt/gurobi605/linux64" >> ~/.bashrc`<br>
* install trajopt
  * clone this repo to your catkin workspace
  * add openrave model folders into environment variable OPENRAVE_DATA.<br>
    for example, in my computer, `echo export OPENRAVE_DATA='${OPENRAVE_DATA}':~/traj_ws/src/trajopt/ >> ~/.bashrc`<br>
  * catkin_make

