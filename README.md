# IISc_volta_simulation
* Go to the parent directry of Volta to get the repository
```
https://github.com/botsync/volta   
```

* launch - contains the launch files for gazebo and robot spawning
* meshes - contains the updated meshes with reduced fazes
* urdf - contains the updated urdf file
* worlds - contains the gazebo world file

## Steps to launch volta on Gazebo
* Launch the gazebo world with
```
$ roslaunch IISc_volta_simulation gazebo.launch
```
* Spawn the robot on the gazebo world with
```
$roslaunch IISc_volta_simulation simulation.launch
```
* Start the simulation with a simple publish to cmd_vel
```
$ rostopic pub /cmd_vel geometry_msgs/Twist '{linear: {x: 1, y:0, z:0}, angular: {x:0, y:0, z:0}}'
```
