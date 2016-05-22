#INTRODUCTION#
At Conversion Logic we process a lot of event-level data - enrichment, transformation, aggregation, and so forth. This coding exercise is a simplified, small-scale example of this type of processing. In production we do this at scale, on heavy-duty infrastructure - but the core concepts are similar.

#EVENT DATA#
For this exercise, consider a stream of incoming events representing users' online-advertising-related activities. These activities include ad impressions, clicks and conversions that we have observed (through a variety of means) and normalized into a common event format.

Each event contains the following fields:

* Timestamp: Event Time (UTC), in YYYY-MM-DD HH:MI:SS format
* Device ID: Unique ID for the user's device
* Username: Username, possibly blank if the user is not logged-in
* Channel: The media channel (display / video / mobile / search / social / email)
* Action: The user's action (impression, click)

This repository includes a sample of event data:

- UTF-8 encoded text file
- UNIX-style line-endings
- Comma-delimited CSV format

This repository also include a partial set of expected results for each of the problems below, based on the first 100 lines of the input file.

#DELIVERABLES#
For each of the following problems, we expect the following results:

- Code: written in Python, Java, Scala or JavaScript
- Tests: automated tests, written in a framework appropriate for the chosen language
- Output: the results of executing the code on the provided sample data
- Build Script / Dependencies: a build script and/or list of dependencies required to build and/or run the code
  - Java/Scala: Maven, Gradle or SBT
  - Python: requirements.txt
  - JavaScript: NPM
- Script: If producing the output requires more than "pipe the input file through the code and redirect to an output file", please include a shell script or a command in the build script.

To submit your deliverables for evaluation:

- Fork our Bitbucket repo
- Make your changes and commit them to your fork
- Submit a Bitbucket Pull Request


#CODE EXERCISES#

##1) Device ID-Channel Paths##
A user's exposure to an advertiser's ads constitutes a "path" - an ordered sequence of media events. For this exercise, we want to see the a basic sequence of Channels for all Device IDs, ordered by time.

Write a program to emit the Device ID-Channel paths for all Device IDs in the provided event log. The expected output format is:

    <Device ID>: <timestamp-ordered, comma-delimited list of channels>

For example, a device (1234) may have seen a display ad, then a video ad, then clicked on the display ad, then opened an email. The path for this device would be:

    1234: display,video,display,email



##2) Common Paths##
There will be many users who have the same Device ID-Channel Paths. This exercise builds upon (1) above, but instead of generating the path for each Device ID, we want to rank the unique Channel paths by frequency.

Write a program to emit the top-20 Channel Paths, sorted by frequency:

    <Frequency>: <timestamp-ordered, comma-delimited list of channels>

For example (only showing top-3):

    1000: display,video
    950: search
    100: mobile,search,display


##3) User-Channel Paths#
#A user may have multiple devices, so the path for that user should span all of the Device IDs observed for a user. In the sample log, we can consider the Username field to correspond to a single user (note that Username is not always populated, e.g. if the user is not logged-in at the time). 

Write a progra, to emit the sequence of Channels for all Device IDs associated with each Username, including events that happened while the user was not logged-in:

    <Username>: <timestamp-ordered, comma-delimited list of channels>

For example, a User (fred) may have seen a display ad on device A, then a video ad on device B, then clicked on a search ad on device A. Another user (mary) saw a video ad on device C, then a mobile ad on devices E and F. The expected output is:

    fred: display,video,search
    mary: video,mobile,mobile