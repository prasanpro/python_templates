#!/bin/bash

# Function to fetch GPS data from modem_status command
function fetch_gps_from_modem() {
    # Replace this command with the actual modem_status command to obtain GPS data
    modem_status_output=$(modem_status -gps)
    echo "$modem_status_output"
}

# Function to convert degrees, minutes, and seconds to decimal format
function dms_to_decimal() {
    degrees=$1
    minutes=$2
    seconds=$3

    # Calculate decimal degrees
    decimal=$(echo "scale=6; $degrees + $minutes / 60 + $seconds / 3600" | bc)
    echo "$decimal"
}

# Main script
gps_data=$(fetch_gps_from_modem)

# Check if GPS data is obtained successfully
if [ -z "$gps_data" ]; then
    echo "Error: Failed to obtain GPS data from modem_status."
    exit 1
fi


# Extract latitude, longitude, and direction information
latitude_d=$(echo "$gps_data" | grep -oE 'Lat: ([0-9]+) Deg' | awk '{print $2}')
latitude_m=$(echo "$gps_data" | grep -oE 'Min ([0-9]+) Sec' | awk '{print $2}')
latitude_s=$(echo "$gps_data" | grep -oE 'Sec ([0-9]+\.[0-9]+)' | awk '{print $2}')
longitude_d=$(echo "$gps_data" | grep -oE 'Lon: ([0-9]+) Deg' | awk '{print $2}')
longitude_m=$(echo "$gps_data" | grep -oE 'Min ([0-9]+) Sec' | awk '{print $2}')
longitude_s=$(echo "$gps_data" | grep -oE 'Sec ([0-9]+\.[0-9]+)' | awk '{print $2}')
direction_latitude=$(echo "$gps_data" | grep -oE 'N|S')
direction_longitude=$(echo "$gps_data" | grep -oE 'E|W')

# Convert degrees, minutes, and seconds to decimal format
latitude_decimal=$(dms_to_decimal "$latitude_d" "$latitude_m" "$latitude_s")
longitude_decimal=$(dms_to_decimal "$longitude_d" "$longitude_m" "$longitude_s")

echo "Latitude (Decimal): $latitude_decimal"
echo "Longitude (Decimal): $longitude_decimal"
echo "Direction Latitude: $direction_latitude"
echo "Direction Longitude: $direction_longitude"

# Calculate timezone using Python with lat, long, and direction
#timezone=$(python - <<EOF
#from tzwhere import tzwhere

#tz = tzwhere.tzwhere()
#latitude = $latitude_decimal
#longitude = $longitude_decimal
#direction = '$direction_latitude$direction_longitude'

#tz_name = tz.tzNameAt(latitude, longitude, forceTZ=True)
#if direction == 'S' or direction == 'W':
#    tz_name = 'Etc/GMT+' + tz_name

#print(tz_name)
#EOF
#)

#echo "Timezone: $timezone"
