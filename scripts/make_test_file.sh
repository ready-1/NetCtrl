#!/bin/zsh

# Check if correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <size in GB> <output filename>"
    exit 1
fi

# Assign arguments to variables
size_gb=$1
output_file=$2

# Validate size is a positive number
if ! [[ "$size_gb" =~ ^[0-9]+(\.[0-9]+)?$ ]] || (( $(echo "$size_gb <= 0" | bc -l) )); then
    echo "Error: Size must be a positive number"
    exit 1
fi

# Convert GB to bytes (1GB = 1073741824 bytes)
size_bytes=$(echo "$size_gb * 1073741824" | bc | cut -d'.' -f1)

# Create the file using dd command
echo "Creating file of size ${size_gb}GB..."
dd if=/dev/zero of="$output_file" bs=1M count=$(($size_bytes / 1048576)) status=progress

# Check if file was created successfully
if [ $? -eq 0 ]; then
    echo "File '$output_file' created successfully!"
    ls -lh "$output_file"
else
    echo "Error creating file"
    exit 1
fi
