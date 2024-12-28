# Wiki Pages
- [ ] Add a check for duplicate page names.
- [ ] adjust formatting of page content and bottom buttons
- [ ] implement better tagging

# Firmware Update Checker
- [ ] Add a check for firmware updates for all devices in the system.
        This will need to be a web scraper of some sort.  Not sure if this is possible.

# Network Device Management

## 1. Device List
- [ ] add a model for devices
        Model fields should include the following:
        - IP address
        - MAC address
        - hostname
        - device type
        - Make
        - Model
        - Version
        - Serial number
        - Location
        - Description
        - Status
        - Last seen
        - Last updated
        - Firmware version
- [ ] Add a form for adding new devices.
- [ ] Add a form for updating device information.
- [ ] Add a button to delete a device.
- [ ] Add a button to view device details.
- [ ] Add a button to update device firmware.
- [ ] Add a button to view device logs.

## 2. Device polling
- [ ] Figure out how to discover devices on the network.
        LLDP is available for some devices.
        Might be as simple as pinging the broadcast address.
- [ ] Create a background task to poll devices for updates.
        Need to look at load balancing and how often to poll.
        The bottleneck will not be on the server, but on the
        devices based on their response time.  Maybe it will be 
        best to have a thread for each device that polls on an interval.
        Might be better to spawn seperate docker workers to handle this.


## 99. Deployment
- [ ] Create a bootstrap script to set up the environment.
        - [ ] handle this ==> "sysctl -w vm.overcommit_memory=1" for redis and docker at the host level
              