# What is this project about?
This Python app is intended as a proof of concept for providing a service for printing decoded pager messages (Pagermon) achieved by monitoring an SQLite database for new entries

Once the database receives a new message, this app will ingest them and present it on a printable/printed PDF with the pager message and other reporting details (Vehicle Details, Crew, Weather, etc.)


## __Project Status:__

### Monitoring & Saving

- [x] SQLite database monitoring
- [x] File watchdog

### PDF Creation & Overlay
- [x] PDF file creation
- [ ] Complete PDF Template
- [ ] Database messages imported to PDF
- [ ] PDF Printing

### Application Functionality
- [ ] Config file(s)
- [ ] Application logging
- [ ] Production testing


# Important Notes
- There is no promise this project will become production-ready. It is a learning experience and may experience significant tech debt

