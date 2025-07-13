#!/bin/bash

echo "[INFO] Stopping joystick control..."

# Kill joy node session
tmux has-session -t joy 2>/dev/null && tmux kill-session -t joy && echo "[✓] joy stopped"

# Kill joy_reader node session
tmux has-session -t joy_reader 2>/dev/null && tmux kill-session -t joy_reader && echo "[✓] joy_reader stopped"

# Kill RViz2 session
tmux has-session -t rviz 2>/dev/null && tmux kill-session -t rviz && echo "[✓] rviz stopped"

echo "[INFO] All sessions stopped."
