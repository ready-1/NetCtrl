# Django File Manager Implementation To-Do List

## 1. Setup and Installation
- [ ] Clone the Django File Manager repository or extract the relevant components.
- [ ] Configure `MEDIA_URL` and `MEDIA_ROOT` in `settings.py`.
- [ ] Add file manager URLs to the project’s `urls.py`.

## 2. Basic Integration
- [ ] Set up file manager views for uploading, listing, and deleting files.
- [ ] Test file uploading and ensure files are saved in the `MEDIA_ROOT` directory.
- [ ] Verify file accessibility via the browser.

## 3. UI Customization
- [ ] Adjust templates to match your project’s look and feel (e.g., Bootstrap 5).
- [ ] Add navigation links to integrate the file manager with the existing wiki.

## 4. Testing and Debugging
- [ ] Verify file manager functionality with various file types (e.g., images, PDFs, binaries).
- [ ] Test edge cases like large file uploads and invalid formats.

## 5. Enhancements
- [ ] Integrate `django-taggit` for tagging files.
- [ ] Add views and filters to browse files by tags or categories.
- [ ] Add tagging functionality to the file upload form.
- [ ] Update templates to display tags and allow filtering by them.

## 6. Documentation
- [ ] Write a brief guide on how to use the file manager.
- [ ] Document any customizations or additional features.


# Wiki Pages
- [ ] Add a check for duplicate page names.
- [ ] adjust formatting of page content and bottom buttons

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
