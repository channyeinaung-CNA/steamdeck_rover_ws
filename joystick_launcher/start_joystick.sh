#!/bin/bash

# Set up outer environment (optional but safe)
source /opt/ros/humble/setup.bash
source ~/steamdeck_rover_ws/install/setup.bash
export DISPLAY=:0
export ROS_DOMAIN_ID=42

# Start joy_node
tmux has-session -t joy 2>/dev/null || \
tmux new-session -d -s joy "source /opt/ros/humble/setup.bash && source ~/steamdeck_rover_ws/install/setup.bash && ros2 run joy joy_node"

# Start joy_reader_node
tmux has-session -t joy_reader 2>/dev/null || \
tmux new-session -d -s joy_reader "source /opt/ros/humble/setup.bash && source ~/steamdeck_rover_ws/install/setup.bash && ros2 run joy_reader joy_reader_node"

# Wait for /scan topic
echo '[INFO] Waiting for /scan topic to appear...'
for i in {1..10}; do
  if ros2 topic list | grep -q /scan; then
    echo '[INFO] /scan detected, launching RViz2...'
    break
  fi
  sleep 1
done

# Start RViz2 in tmux using interactive shell (loads .bashrc with ROS env)
tmux has-session -t rviz 2>/dev/null || \
tmux new-session -d -s rviz "bash -i -c 'rviz2'"

# Attach to RViz2 session so user can see it
tmux attach-session -t rviz