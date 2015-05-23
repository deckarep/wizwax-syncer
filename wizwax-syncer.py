#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sp
import os
import argparse
import shutil
import time
import sys

# tkinter junk
from Tkinter import Tk, BOTH, RIGHT, LEFT, W, E, N, S, DISABLED, NORMAL, END
from ttk import Frame, Button, Style, Entry
import tkFileDialog

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

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def source_open(self):
        my_dir = tkFileDialog.askdirectory()
        print my_dir
        self.updateEntry(self.sourceEntry, my_dir)

    def updateEntry(self, widget, msg):
        widget.delete(0, END)
        widget.insert(0, msg)

    def initUI(self):
        self.parent.title("WizWax Syncer 1.0")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(0, pad=5, weight=3)

        self.sourceEntry = Entry(self)
        self.sourceEntry.grid(row=0, column=0, padx=10, pady=10, sticky=W+E)
        self.updateEntry(self.sourceEntry, "Pick source folder...")

        sourceButton = Button(self, text="Source", command=self.source_open)
        sourceButton.grid(row=0, column=1, padx=10)

        destEntry = Entry(self)
        self.updateEntry(destEntry, "Pick destination folder...")
        destEntry.grid(row=1, column=0, padx=10, pady=10, sticky=W+E)

        destButton = Button(self, text="Destination", command=self.source_open)
        destButton.grid(row=1, column=1)

        syncButton = Button(self, text="Sync that Shiz", command=self.source_open)
        syncButton.grid(row=3, column=0, sticky=W+E, padx=10)


def main_gui():
    root = Tk()
    root.geometry("800x118+300+300")
    root.lift()
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    sp.call('clear', shell=True)
    # TODO: so Ronnie doesn't have to keep updating the folders, create a .wizwax config in home directory
    #banner()
    #main()
    if args.gui:
        main_gui()
