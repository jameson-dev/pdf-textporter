# What is this project about?
Tasking Sheets is intended as a proof of concept to provide a service for printing pager messages (decoded from Pagermon), achieved by monitoring an SQLite database for new entries

Once the database receives a new message, it is ingested and overlayed onto a PDF with the pager message and other reporting details (Vehicle Details, Crew, Weather, etc.)

An ability for automatically printing tasking sheets will be available to assist with incident management as a form of resilience/redundancy.

## __Project Status:__

### :white_check_mark: Monitoring & Saving

- [x] ~~SQLite database monitoring~~
- [x] ~~File watchdog~~

### :repeat: PDF Creation & Overlay
- [x] ~~PDF file creation~~
- [x] Database messages import to PDF
- [ ] Complete PDF Template
- [ ] PDF Printing

### :repeat: Application Functionality
- [x] ~~Application logging~~
- [x] ~~Config file~~
- [ ] Production testing
