There are 2 log files start.log and end.log that contain start and end data of the best lap for each racer of Formula 1 
- Monaco 2018 Racing. (Start and end times are fictional, but the best lap times are true). Data contains only the 
- first 20 minutes that refers to the first stage of the qualification.
Q1: For the first 20 minutes (Q1), all cars together on the track try to set the fastest time. The slowest seven cars 
- are eliminated, earning the bottom grid positions. Drivers are allowed to complete as many laps as they want during 
- this short space of time.
Top 15 cars are going to the Q2 stage. 
If you are so curious, you can read the rules here https://www.thoughtco.com/developing-saga-of-formula1-qualifying-1347189
The third file abbreviations.txt contains abbreviation explanations.
Hint:
SVF2018-05-24_12:02:58.917
SVF - racer abbreviation 
2018-05-24 - date
12:02:58.917 - time
App print report that shows the top 15 racers and the rest after underline, for example:
1. Daniel Ricciardo      | RED BULL RACING TAG HEUER     | 1:12.013
2. Sebastian Vettel      | FERRARI                       | 1:12.415
3. ...
------------------------------------------------------------------------
16. Brendon Hartley      | SCUDERIA TORO ROSSO HONDA     | 1:13.179
17. Marcus Ericsson      | SAUBER FERRARI                | 1:13.265
The application has a command-line interface and you can to have a few parameters. 
E.g.
python report.py --files <folder_path> --asc | --desc  shows list of drivers and optional order (default order is asc)
python report.py --files <folder_path> --driver “Sebastian Vettel”  shows statistic about driver 
