#!/bin/bash

# Define ANSI color codes
COLOR_RESET="\033[0m"
COLORS=(
    "\033[31m"  # Red
    "\033[32m"  # Green
    "\033[33m"  # Yellow
    "\033[34m"  # Blue
    "\033[35m"  # Magenta
    "\033[36m"  # Cyan
)

# Custom container-to-color mapping
declare -A CONTAINER_COLOR_MAP=(
    ["redis"]="${COLORS[0]}"  # Red
    ["web"]="${COLORS[1]}"   # Green
    ["db"]="${COLORS[2]}" # Yellow
)

# Function to get running containers
get_running_containers() {
    docker compose ps --services 2>/dev/null
}

# Main log monitoring loop
echo "Starting colorized Docker log viewer..."
while true; do
    # Get currently running containers
    CONTAINERS=($(get_running_containers))
    if [ ${#CONTAINERS[@]} -eq 0 ]; then
        echo "No containers are running. Waiting for containers to start..."
        sleep 2
        continue
    fi

    # Display active containers and their colors
    echo "Monitoring the following containers:"
    for container in "${CONTAINERS[@]}"; do
        if [[ -z "${CONTAINER_COLOR_MAP[$container]}" ]]; then
            # Assign a default color if not in the predefined map
            CONTAINER_COLOR_MAP["$container"]="${COLORS[$((RANDOM % ${#COLORS[@]}))]}"
        fi
        echo -e "${CONTAINER_COLOR_MAP[$container]}$container${COLOR_RESET}"
    done

    # Stream logs with colorization
    docker compose logs -f 2>/dev/null | while read -r line; do
        for container in "${!CONTAINER_COLOR_MAP[@]}"; do
            if [[ $line == *"$container"* ]]; then
                echo -e "${CONTAINER_COLOR_MAP[$container]}$line${COLOR_RESET}"
            fi
        done
    done

    sleep 2
done