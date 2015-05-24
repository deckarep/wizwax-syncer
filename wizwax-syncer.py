#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess as sp
import os
import os.path
import argparse
import shutil
import time
import sys
import Queue
import threading
import datetime

# tkinter junk
from Tkinter import Tk, BOTH, RIGHT, LEFT, W, E, N, S, DISABLED, NORMAL, END, SUNKEN
from ttk import Frame, Button, Style, Entry, Label
import tkFileDialog
import tkMessageBox

wizwax_banner = """
                                                        @:@                                           +
    ,@@                 .'@@       @@`                 @;,@               @#`                `:@@,  :@;#;
    #,;#.        `,'@@@#':,#       @,@                @;,,@  #;          @;,@@         `:@@@@'::'+  @,,,;#;                          '@#@:`
   #,,,,@@    @@@+;:,,,,,,'@      ;;,@               ;+,,,@ #,#         :#,,,:#,   `@@@':,,,,,,,';  #,,,,,'#:                       `':,:'@@@@#'
  @:,,,,,:#, +',,,,,,,,,,,'@      @,,'              ,@,,,,#@:,':       `@,,,,,,@@  #,,,,,,,,,,,;'; #,,,,,,,,'@,                     .:,,,,,,,,:@
 +',,,,,,,,@@@;,,,,,,,,,,:'@      @+,,'            `@,,,,,';,,,@       #,,,,,,,,:#:#,,,,,,,,,,,'+;@,,,,,,,,,,,+:                    ::,,,,,,,,+@
 @:,,,,,,,,,,@',,,,,,,,,,''@      ++,,@            #,,,,,,:,,,,@.      @,,,,,,,,,,+#;,,,,,,,,,:'#@,,,,,,,,,,,,::                    ;,,,,,,,,,'@
 @',,,,,,,,,,,',,,,,,,,,,'#.     ::,',#            #';,,,,,,,,:+`      #;,,,,,,,,,,:',,,,,,,,,+#@,,,,,,,,,,,,,::     ;#@`           +,,,,,,,,,'@
 @''',,,,,:+';+',,,,,,:;+'@      @,,+,,:           #'':,,,,..,,+,     `++',,,,,,++;;',,,,,,:;;#+,,,,,,,,,,,,,,:,    `+,,@'          @,,,,,,,,,'@
 @'''+,,,,,'''+'.,,,,,''++;      @,.,;,@           #''+.,..,.,.,@     `++'',,,,,''''';,,,,,+''@,:'+'',,,,,,,,,:,    `@,,,'@         @,,,,,,,,:@
 @'''':....'''#'...,..''+#       @..,+,@           #'''...,......@     #+'''....;''''+....,'''@'''''',...,,,+++.    `#,,,,,@:       @,,:,,,,,;@
  @'''+....''++':.....''+@       +...,,:.          #'''....',.....@    @+''',...:'+'@'.....:''@''''''...,,,,;'+`     +,,,,,,+@      @,+:,,,,,'@
  #@+''...,#:.,#+..,..+'@       .:....#.@          #'''....'',.....@`   @@'':...,+..;'...,.,''#'''''+,,....,,'+`     #:,,.,,,,#.    @'':,.,..'+
    @#'....@..........#;,       ;,....,,@          @+''....'''......@     #';...,:....:..,..@;@+##@@@.......,'#`     @+,..,,,..+.   @'',.....':
     @'....,..........'`        @......@'`          @''....+'''.....:'@;   @;...:.....:.....@ #;`  `+....,...@#`     @'.....,:,:.   @''......+`
     `@...;...........:,        @......,+`          +';....+''''......',   @:.........,.....@      ,:........@       ,',.....''+,   ##@.....;#
      @..........,....:,        @....`..#`          ;',;+''+@+;..`....'`   #...;......,.....@      @..,......#        +'.....''+,    `@.....+@
     .;..........:....,;        #++...``.@          +'''+;,.`....``.;++    @..............`.@      @.........::       @'.....;'+:    `'.....'@
     ',..........;.....+        #''....`.@        `@,...........`.+''+@    @...`...``....``.@      @.`..+.....@       +':.....@@,    @.....:',
     @.......#...;.....+        #'+.....`@       '@............;''''''@   `+.....`,......`..@     @,``..'.....@       `++.....+`     @.....++
     @......++...:.....+        #'+:...`.@      @:..........;'+.;'''''#@@@@,......;.........@     @....:+:....+`       @',.....@    ',.....'@
    :;.....,'+..,:.....@        #+#;....;@    ,@......`.;+'',`....''+,...`@......+',...,....@    @,...`'++....,@       ;'+``..`:'   @.....''@`
   @@...,..+''..,:.....@         ;@'....'@    #;,.....,..,''+...........,@@......'',.,,,....@   `@....,'@'.....@@@@@@`  #':``...+. @.`````.`.+;
  `@,,,,,,,.:#,,,,,,,,,@;         ,+....+@    @'''',....,,.'',...,...,.,@,,,,,,,,,+,,,,,,,,,+@  @.....``:``````.....+;  @''.`....@;:..`.....+''
  @:,,,,,,,,;#,,,,,,,,,,@         .+....;@    @'''''+,,,,,,,:,,,,,,,,:+'@,,,,,,,,,@,,,,,,,,,;;..+.......:.......,,,,';   #''```...;.......,''''
  @,,,,,,,,,'#,,,,,,',:,@          +....,@    @''''''':,,,,,,,,,,,,;'''#;,,,,,,,,,#,,,,,,,;,:,@@,.......:.......,,,'';   #''+``......`..++''''@
 :',,:,,,::,@#,,::,,,,',',         +.....+    @'''''''';,:,:,,:,,''''''@,,,:,,,:,;#:,,:,,,,,:,@',,,.,++++++,....,;''@.    #''+``....`..'++''+@
 @::::::::''#+:::::::,:::@         #,,,.,@    @''''''''';::::::+''''''+#::::::::+'#::::::::,::@,,,,,;''''''',,,,:++'@     .#':........+'++'@@
 @::::::;'''##+::::::::::@      #@@@;,,,,#    @''''''''''::;:::;''''''@:::::::+'''#'+:::::::::@,,,,,+'''':,,,::,,:'#       @..,,,,,,,,,,#+#.
`+;;:::+''''@#;::;;;;::::@     .',;@',,::;;   @#'''''''''';;;;;;+'''''@':;::''''''#'::;;;;:::+;:::::#;;@::::::::::+:      @,,,,,,,:,,,:,,:@.
.+';;+''''''@+';;;;;;;;;;':    ;':::::::::@    `+@#''''''++';;;;;'''''@'+;;+''''''@++:;;;;;;;@:::::;+` @:;::::::::;@     #,::::::'+';::::::#@
.+''''''''+@,+''+;;;;;;;;;@    ;';::::;:;;#`      .@#''''+'''+;;;'''##@''+''''''@@@+'';;;;;;;@;:::::'; #'+';::;;::;;#   @::::::::;;+'+::::::;@
.+'''''''#'  #'''+;;;;+;+'@    ;'';;;;;;;;;@        ,#'''+''''+''+##' @''+''''#@` @@''';;;;;+#;;;;;;;@ #'''''+;;;;;;;@ +';;;;;;;;;;''''';;;;;;@
 #'''''@@    @''''';;;''''@    ;''';;;;;;;;@`         #''+'''''#'++   '#'+''+#:    #'''+;;;;'+;;;;;;+# #''''''+;;;;;;'#@';;;;;'++''''+++;;;;;;@
  #''+@`     @@'''''''+'''@    ;'''+''''''''@          #'+''''''+'@    ;#+'#@      #+'''+''''#'''''+'# #'''''''''''''''@'''++''''''#'''''''''+@
   ##;        `#'''#''+'''@     @'''''''''''@:         `#+'''''''+#     +@@         @@'''''''#'''+'''# `#@@+'''''''''''@'+''''''''''''++'''''+@
                #'''''@''#,      #''+++++++++:          @''''''''#+.     `           ;@''+''+++'+''''@     ;@@''++'''''@'+''''''+@#'''''''++++@
                 #''#+@@@        ,#'++#++'''':           #@+'''''+'@                  +#'''+@+''''''@@       .@''+++++++@+''+##@+` ''''''''''+@
                 .@''+@           @'+'''''''':            `@#''''''@                   @''##++'''''#,         @'''''''+##@@@@@     ###'''''''++
                  @''+@           `@+'''''''':               @''''+:                    #''#`#'''#@            #''''''''''#''@       :@#@+'''#,
                   #'+@            @+'''''''+,                @'''+,                    ++'# @''#:             `@'''''''''+''@          `;@#@#`
                   #+'@            ;+'''+##@@                  #''#`                     #'#  @@                +@#+''''''+'@,              `'
                    #'@             @@@;.                      .+'@                      @'#                       ,@@#+''+@,
                    @'@                                         @+#                       ##                           `'@#.
                    .@;                                         `@+                       @#
                     '                                                                    ..
"""

def banner():
    b = wizwax_banner.split("\n")
    for l in b:
        print l
        time.sleep(0.1)

    loader("Initializing system resources", 4, 0.4)
    loader("Registering pivot matrices for directory scan", 11, 0.2)
    loader("Increasing memory allocation table to 32 Mb", 13, 0.03)
    loader("Loading Skip List and Binary Search Space Partition Tree", 3, 0.4)
    loader("Installing XORG.org remote server management tool -- v2.34.8a [ Copyright 2008 - All Rights Reserved ]", 173, 0.1)

def loader(msg, num, interval=0.5):
    sys.stdout.write(msg)
    for x in xrange(num):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(interval)
    print ""

# First parse the args
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", help="The source flag is an absolute path of a directory to read from.")
parser.add_argument("-d", "--destination", help="The destination flag is an absolute path of a directory to write to.")
parser.add_argument("-v", "--verbose", action="store_true", help="Show more logging of what this app is doing.")
parser.add_argument("-n", "--noprompt", action="store_true", help="Don't prompt, just do it!")
parser.add_argument("-g", "--gui", action="store_true", help="Turn on GUI mode")
args = parser.parse_args()

def verbose(msg):
    if args.verbose:
        print msg

def main():
    print "This will began copying to the following folders:"

    print "\tSource Folder: " + args.source
    print "\tDestination Folder: " + args.destination
    print ''

    if not args.noprompt:
        print "Are you sure you want to continue? [y/n]"

        choice = raw_input().lower()
        if "n" in choice:
            print "Exiting."
            return

    files_copied = 0

    # Next walk the source dir
    for root, dirs, files in os.walk(args.source):
        for f in files:
            verbose("root: " + root)
            verbose("file: " + f)

            sub_path = root.replace(args.source, "")
            if len(sub_path) > 1 and sub_path[0] == os.sep:
                sub_path = sub_path[1:]

            # First check if destination directory exists, if not create that shit ya'll
            source_dir = os.path.join(args.destination, sub_path)
            verbose("source_dir: " + source_dir)

            if not os.path.exists(source_dir):
                verbose("Does not exist so creating: " + source_dir)
                os.makedirs(source_dir)

            # Now that directory is there, copy files that don't exist
            new_file_path = os.path.join(source_dir, f)
            if not os.path.exists(new_file_path):
                verbose("Does not exist, so copying: " + new_file_path)
                shutil.copyfile(os.path.join(root, f), new_file_path)
                files_copied +=1

    if files_copied > 0:
        print "Copied %d files successfully." % files_copied
    else:
        print "Copied 0 files. (No new files detected)"

    # Allow time to read the output.
    raw_input()

class WizwaxApp(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        # How often to poll on the GUI thread and check the Queue, we don't need this to be super fast
        self.poll_interval = 200
        self.wizwax_filename = ".wizwax-syncer"
        self.sync_started = False

        self.saved_source_path = None
        self.saved_dest_path = None
        self.saved_last_sync = None

        self.queue = Queue.Queue()
        self.choose_source_message = "Choose source folder..."
        self.choose_dest_message = "Choose destination folder..."

        self.initUI()
        self.check_wizwax_file()
        self.poll_counter = 0
        self.ascii_spinner = ("/", "-", "\\", "|")


    def source_open(self):
        my_dir = tkFileDialog.askdirectory()
        self.saved_source_path = my_dir
        self.updateEntry(self.sourceEntry, my_dir)

    def dest_open(self):
        my_dir = tkFileDialog.askdirectory()
        self.saved_dest_path = my_dir
        self.updateEntry(self.destEntry, my_dir)

    def updateEntry(self, widget, msg):
        widget.delete(0, END)
        widget.insert(0, msg)

    def update_status_bar(self, msg):
        self.status.config(text=msg)
        self.status.update_idletasks()

    def check_wizwax_file(self):
        """
        Checks a two-line file in HOME directory called .wizwax-syncer to see if there is
        any default source/dest folders already used...
        """
        user_home_folder = os.path.expanduser("~")
        file_path = os.path.join(user_home_folder, self.wizwax_filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                results = content.split("\n")
                if len(results) >= 3: # We only care about the first two lines in the file
                    self.saved_source_path, self.saved_dest_path, self.saved_last_sync = results[0], results[1], results[2]

                    # We have what we need populate source/dest entry fields
                    self.updateEntry(self.sourceEntry, self.saved_source_path)
                    self.updateEntry(self.destEntry, self.saved_dest_path)
                    self.update_status_bar("Last Synced: " + self.saved_last_sync)

        if self.saved_last_sync is None:
            self.update_status_bar("Last Synced: Unknown")

    def initUI(self):
        self.parent.title("WizWax Syncer 1.0")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(0, pad=5, weight=3)

        self.sourceEntry = Entry(self)
        self.sourceEntry.grid(row=0, column=0, padx=10, pady=10, sticky=W+E)
        self.updateEntry(self.sourceEntry, self.choose_source_message)

        sourceButton = Button(self, text="Source", command=self.source_open)
        sourceButton.grid(row=0, column=1, padx=10)

        self.destEntry = Entry(self)
        self.updateEntry(self.destEntry, self.choose_dest_message)
        self.destEntry.grid(row=1, column=0, padx=10, pady=10, sticky=W+E)

        destButton = Button(self, text="Destination", command=self.dest_open)
        destButton.grid(row=1, column=1)

        syncButton = Button(self, text="Start Syncing Folders", command=self.kickoff_thread)
        syncButton.grid(row=3, column=0, columnspan=2, sticky=W+E, padx=10)

        self.status = Label(self, text="", relief=SUNKEN, anchor=W)
        self.status.grid(row=4, column=0, columnspan=2, sticky=W+E, padx=10, pady=5)


    def write_wizwax_file(self):
        """
        Creates or updates the .wizwax-syncer file in user's home directory with
        two lines, each line being the source/dest folder respectively
        """
        user_home_folder = os.path.expanduser("~")
        file_path = os.path.join(user_home_folder, self.wizwax_filename)
        # order of the lines matter
        lines = (self.saved_source_path, self.saved_dest_path)
        with open(file_path, "w") as f:
            for l in lines:
                f.write(l + "\n")

            # Last line is the date
            f.write(datetime.datetime.today().strftime("%a %b %d %I:%M:%S %p %Y"))

    # poll() is responsible for checking the synchronized queue for a result when finished.
    def poll(self):
        try:
            # We can't use the blocking get() call otherwise we block GUI thread.
            result = self.queue.get_nowait()

            # When we get a result, the kickoff_thread finished!
            # so update the .wizwaxfile
            self.write_wizwax_file()
            self.update_status_bar(result)
            self.sync_started = False
            self.poll_counter = 0
            # We don't want the poll timer to be rescheduled cause we're done!
            # so return early bitch
            return
        except Queue.Empty:
            # When we check the queue, if empty an 'Empty' exception is thrown (this is expected)
            # In here we can do an ascii spinner update
            self.update_status_bar("Syncing..." + self.ascii_spinner[self.poll_counter % len(self.ascii_spinner)])
            self.poll_counter += 1
            pass
        except:
            print "Unexpected error: ", sys.exc_info()[0]
            raise

        # Kick off poll again
        self.parent.after(self.poll_interval, self.poll)

    # kickoff_thread() does the actual file i/o work so as to not block the main thread
    def kickoff_thread(self):

        # First check that we should move forward
        if self.saved_source_path is None or self.saved_dest_path is None:
            tkMessageBox.showwarning("Error", "Please choose a source and destination path first.")
            return

        # Prevents user from kicking off multiple worker threads
        if self.sync_started:
            tkMessageBox.showwarning("Warning", "Syncing has already started uncle fucka.\nPlease wait!")
            return

        # Start polling on GUI main thread so we can receive a result from worker thread
        self.parent.after(self.poll_interval, self.poll)
        self.update_status_bar("Syncing started...(please wait)")

        def worker_thread():
            # WARNING: Do not reference UI in this worker thread, use the self.queue
            print "Worker thread started: sleeping for 15 seconds"
            # Simulate work with this sleepy thread
            # 1. Actual work goes here
            time.sleep(15)

            # 2. Anything left goes here
            # The queue could have something useful in it...but currently it's acting as just
            # a signal to the poller that we're done.
            self.queue.put("Syncing completed")

        # Notice it invokes the nested function
        t = threading.Thread(target=worker_thread)
        t.start()
        self.sync_started = True

def main_gui():
    root = Tk()
    root.geometry("800x138+300+300")
    root.lift()
    app = WizwaxApp(root)
    root.mainloop()

if __name__ == '__main__':
    sp.call('clear', shell=True)
    #banner()
    #main()
    if args.gui:
        main_gui()
