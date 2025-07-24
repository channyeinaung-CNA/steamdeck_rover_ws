FROM ros:humble-ros-base

# Install GUI tools and essentials
RUN apt update && apt install -y \
    ros-humble-rviz2 \
    ros-humble-slam-toolbox \
    ros-humble-teleop-twist-keyboard \
    ros-humble-joy \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /ros2_ws

# Copy workspace (optional if you want to pull in source code)
# COPY ./ /ros2_ws/

# Environment setup
ENV DISPLAY=host.docker.internal:0.0
ENV ROS_DOMAIN_ID=42

# Default shell
CMD ["/bin/bash"]

