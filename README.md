# What is this project about?
Tasking Sheets is a functional proof of concept to provide a service for redundancy or large scale events by printing pager messages (decoded from Pagermon), achieved by monitoring an SQLite database for new entries - without needing to be connected to the internet

Once a new pager message is received, it is ingested and overlayed onto a template PDF, combining the pager message and any details on the template (i.e. reporting details (Vehicle Details, Crew, Weather, etc.)

The tasking sheet PDFs are automatically printed to a chosen printer to assist with incident management.

## __Project Status:__

### :white_check_mark: Monitoring & Saving

- [x] ~~SQLite database monitoring~~
- [x] ~~File watchdog~~
- [ ] Unit filtering

### :white_check_mark: PDF Creation & Overlay
- [x] ~~PDF file creation~~
- [x] ~~Database messages import to PDF~~
- [x] ~~Automatic PDF Printing~~

### :repeat: Application Functionality
- [x] ~~Application logging~~
- [x] ~~Config file~~
- [ ] Production testing
