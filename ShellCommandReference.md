## Contents:

- [Basic shell commands](#basic-shell-commands)
    - [Getting help](#getting-help)
    - [Command history](#command-history)
    - [Special characters](#special-characters)
    - [Environmental variables](#environmental-variables)
    - [Shortcut commands](#shortcut-commands)
- [File handling](#file-handling)
    - [Text editing](#text-editing)
    - [Searching & regex](#searching-&-regex)
- [Shell scripting](#shell-scripting)
    - [Pipes & redirection](#pipes-&-redirection)
    - [Arithmetic](#arithmetic)
    - [The basic loop](#the-basic-loop)
    - [Conditional statements](#conditional-statements)
- [Git and version control](#git-and-version-control)
- [Remote server commands](#remote-server-commands)
    - [CHTC and HTCondor](#chtc-and-htcondor)

---

## Basic shell commands

### Getting help
- ``[command] --help``: brief help on a command
- ``man [cmd]``: manual page, i.e. extended help on ``[cmd]``
- ``echo [var]``: print the value of a variable or string
- ``whoami``: print your username
- ``ps``: list running processes that were started from current terminal window
- ``ps -u [user]``: list all running processes started by [user]
- ``top``: show the most demanding processes currently running

### Command history
- ``history``: list previously-entered commands (long list!)
- ``history \| tail -n [num]``: list only the last [num] previous commands
- ``![num]``: repeat command [num] in the history
- ``[Ctrl-R] [text]``: searches your history for the most recent command matching [text]; press again to search back from there, etc.
- ``!$``: last word of the previous command (can be used in other commands)
- ``echo !$``: prints last word of previous command
- ``xargs``: after a pipe, passes the prev command’s output as an argument (not standard input)
- ``ls *.txt \| xargs cat``: prints (using cat) the contents of all text-files in current dir

### Special characters
- ``*``: wildcard, matches zero or more characters
- ``?``: wildcard, matches exactly one character
- ``\``: escape character (e.g. to cd into a folder with a space in its name)
- ``$``: denotes a variable
- ``$([cmd])``: command substitution: pass the results of `[cmd]` as a variable
- ``/``: (as a file-operations argument, alone) the root directory
- ``""``: Lines in double-quotes are interpreted as strings, but variables in them are parsed.
- ``''``: Lines in single-quotes are interpreted strictly as strings — no parsing.

### Environmental variables
- ``$PS1``: the prompt string. default $PS1 = “\h:\W \u\$”
- ``$PATH``: colon-separated list of paths to bin folders

```
parse_git_branch() { # defines a shell function: run "git branch" and extract branch name
   git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
PS1="\W \[\033[33m\]\$(parse_git_branch)\[\033[00m\]$ "
```

### Shortcut commands
- ``^A`` (Ctrl-A): move cursor to the start of the line
- ``^E``: move cursor to the end of the line
- ``^C``: stop/kill a running program, cancel current action
- ``^Z``: pause a running program
- ``bg``: resume in the background
- ``fg``: resume in the foreground
- ``jobs``: see list of currently-running jobs
- ``ps``: see list of currently-running processes. PID = process ID.
- ``top``: see list of all processes, refreshed, with CPU & memory consumption
- ``kill``: send a signal to a process
- ``kill -9 [PID]``: kill process [PID] 

---

## File handling
- ``pwd``: “print working directory,” i.e. state your current location
- ``cd``: “change directory.” With no arguments, takes you to your home directory.
    - ``cd .. ``: go to the parent directory (up one level)
    - ``cd [Folder]/[Subfolder]``: go into Subfolder, which is in Folder
    - ``cd ../[Folder]``: go up one level, then into Folder
    - ``cd /``: go to the root directory
    - ``cd ~``: go to your home directory
    - ``cd -``: go to the previous directory (not “up”, but “back”)
- ``ls``: list files in the current directory (“listing”)
    - ``ls [filename]``: list files matching this filename
    - ``ls *.txt``: list all text files in current directory
    - ``-a``: list all files, including hidden
    - ``-F``: add a type marker to file/directory names
    - ``-l``: show details: timestamps, permissions, people, etc.
    - ``-lh``: show details, with file sizes in more human-readable units
    - ``-Q``: put entry names in double quotes
    - ``-R``: recursively list subdirectories
    - ``-t``: sort by modification time, newest first
    - ``-1``: one entry per line
    - ``-C``: multi-column (opposite of -1 flag)
    -  Sort files by:
        - ``[none]``: name
        - ``-lS``: size
        - ``-lt``: time last modified
        - ``-ltu``: time last accessed (also ``-tu``, ``-u``)
        - ``-ltc``: time file status was last changed (also ``-tc``, ``-c``)
        - ``-r``: (in reverse order)
- ``mkdir [dirname]``: create a directory
- ``mkdir -p zmays-snps/{data/seqs,scripts,analysis}``: Brace expansion. Create a directory structure in one line: this one will make a folder ``zmays`` with subfolders ``data``, ``scripts``, and ``analysis``, and a sub-subfolder ``seqs`` in ``data``.
- ``mv [filename]``: move a file
- ``cp [filename]``: copy a file
- ``cp [filename1] [filename2] … [filenameN] [dirname]``: copies all those files into dirname
- ``rm [filename]``: remove (delete) a file or empty directory
	- ``rm -r``: delete a directory and (recursively) all files/dirs inside it
	- ``rm -f``: “force” removal without asking for confirmation for each file
	- ``rm -i``: ask, interactively, before deleting each individual file
- ``rmdir [dirname]``: remove a directory, even if it has files
- ``chmod [perm] [file]``: change permissions for ``[file]`` as per ``[perm]```
    - ``u, g, o, a``: user, group, other, all (whose permissions are we changing?)
    - ``+`` or ``-``: add or remove permissions (how are we changing them?)
    - ``r, w, x``: read, write, execute (which permissions are we changing?
    - e.g. ``chmod u+x headtail.sh``: grant the current user permission to execute headtail.sh
- ``diff [file1] [file2]``: return all lines where ``file1`` and ``file2`` are different
- ``cat [1] [2]``: concatenate ``1`` and ``2``
- ``exit``:

### Text editing
- ``open [filename]``: use default program to open [filename]
- ``cat [filename]`` : print the full text of a file
- ``less [filename]``: print the text of a file, page by page. Name from “less is more.”
    - ``q``: quit
    - ``[enter]``: next line
    - ``[space]``: next “page”
    - ``d``: down 1/2 page
    - ``b``: back 1 page
    - ``y``: back ("yp"?) 1 line
    - ``g``, ``<``: go to 1st line
    - ``4g``, ``4G``: go to 4th line
    - ``G``, ``>``: go to last line
    - ``/[pattern]``: search forward for [pattern]
    - ``?[pattern]``: search backward for [pattern]
    - ``n``: “next”, repeat previous search
    - ``-S``: don’t wrap text
- ``more [filename]``: like less but “shows more and more, one page at a time”. Less is better.
- ``nano [file]``: open ``[file]`` in ``nano`` text editor
- ``head [filename]``: print the first 10 lines of a file
  - ``head -n 3 [filename]``: print the first 3 lines of a file
  - ``tail -n 2 [filename]``: print the last 2 lines of a file
- ``wc [filename]``: word count. Returns # of lines, words, & characters in the file specified
  - ``-l``: counts lines only
  - ``-w``: counts words only
  - ``-c``: counts characters only
- ``touch [file]``: create a blank file called [file], or update timestamp if file already exists
- ``sort [file]``: sort the contents of [file] in alphabetical order
  - ``-n``: in numerical order
  - ``uniq``: filters out consecutive repeated lines. ``-c`` to get counts. e.g. ``sort list.txt | uniq -c``
- ``cut``: extract columns from a data file
  - ``cut -f 1 Mus_musculus.bed``: extract first column (“field”) from Mus_musculus.bed
  - ``-f2``: get second field
  - ``-c2``: get second column (synonymous with ``-f2``)
  - ``-d``: change delimiter (default is tab)
- ``pandoc``: converts Markdown to PDF, HTML, TeX, possibly others
- ``tar``: tarball compression program
  - ``tar -cf archive.tar foo bar``: create archive.tar from files foo and bar
  - ``tar -tvf archive.tar``: list all files in archive.tar, verbosely
  - ``tar -xf archive.tar``: extract all files from archive.tar

### Searching & regex
- ``find "and"``: search for files with names containing “and”
    - ``-type d``: find directories
    - ``-type f``: find files
    - ``-name [pattern]``: find filenames fitting [pattern]
    - ``-d``: set depth: which directory levels will you search? (Default is just the current one.)
    - ``-mtime``: return modified time
- ``grep "and" fish.txt``: within fish.txt, search for the string “and” (“grep” from “global/regular expression/print”)
    - ``-n``: line numbers
    - ``-i``: case-insensitive search
    - ``-w``: whole words
    - ``-v``: invert the search
    - ``-o``: return the match only
    - ``-E``: use Extended (not basic) regex
    - ``-P``: use Perl-like regex (GNU only)
    - ``--color``: colorize the results
- ``man re_format``: regex help
    - ``.``: any one character
    - ``^``: beginning of line (only if placed first)
    - ``$``: end of line (only if placed last)
    - ``\``: turns off special meaning of next symbol
    - ``[aBc]``: anything in: a or B or c. Ranges: like [0-9], [a-z], [a-zA-Z]
    - ``[^aBc]``: anything but: a, B, c
    - ``\w``: any word character: letter, number, or “_”. also [[:alnum:]_]. opposite: \W
    - ``\d``: any single digit. also [[:digit:]] or [0-9]. opposite: \D
    - ``\s``: any white space character: single space, \t (tab), \n (life feed) or \r (carriage return). also [[:space:]]. opposite: \S
    - ``\b``: word boundary (null string). also \< and \> for start/end boundaries. opposite: \B
    - ``+``: one or more of the previous
    - ``?``: zero or one of the previous
    - ``*``: zero or more of the previous
    - ``{4}``: 4 of the previous
    - ``{4,6}``: between 4 and 6 of the previous
    - ``{4,}``: 4 or more of the previous

---

## Shell scripting

- ``bash [scriptname]``: execute [scriptname] as a bash shell script
- ``{1..9}``: set of the integers 1-9
- ``tail -f [file]``: “follow” a file, displaying its last few lines in realtime as the file is updated
- ``/dev/null``: “null device”, a black hole: redirect things here to delete them
- ``[command] &``: execute [command] in the background

### Pipes & redirection
- ``[command] > [file]``: redirect output of [command] and save it as a textfile, [file]
    - ``[command] 0> [file]``: save inputs to [command] as [file]
    - ``[command] 1> [file]``: save outputs from [command] as [file]
    - ``[command] 2> [file]``: save errors from [command] as [file]
    - ``[command] > [file1] 2> [file2]``: save output as [file1] and errors of same command as [file2]
    - ``[command] &> [file]``: save errors-plus-output as [file]
    - ``[command] 2>> [file]``: append errors to [file]
- ``>>``: instead appends output of command as new line(s) at end of file
- ``[line1] | [line2]``: uses output of [line1] as input to [line2]

### Arithmetic
- ``((i++))``: increment variable i (set value of variable i to i+1)
- ``((i+=1))``: increment variable i
- ``((i--))``: decrement variable i
- ``((i+=5))``: increase i by 5
- ``((i/=5))``: divide i by 5
- ``echo ((++i))``: increment i, then print the new value
- ``echo ((i++))``: print value of i, then increment it

### The basic loop
``for [varname] in [listofinputs] ; do [command] ; done
- ``${varname}``: return variable string [varname], which was an argument (without the $)
- ``${varname:X:Y}``: return Y characters of varname, starting at position X

### Conditional statements
```
if [ $i -lt 800 ] # (the spaces after `[` and before `]` are REQUIRED)
then
  echo "i is less than 800"
else
  echo "i is not less than 800"
fi
```

```
if [ $# -lt 1 -o ! -f $1 -o ! -r $1 ]  # if number of args is less than one, OR if the first argument is not a file, OR if the first argument isn’t readable…
then
  echo "error: no argument, or no file, or file not readable"
  exit 1 # exit script with error code (1). 0 = successful exit
fi
```

#### Some conditional-test expressions:
- ``-z str``: string str is empty
- ``str1 = str2``: strings ``str1`` and ``str2`` are identical.
	- not identical: ``str1 != str2``
- ``int1 -eq int2``: integers ``int1`` and ``int2`` are equal.
	- not equal: `int1 -ne int2``
- ``int1 -lt int2``: integer int1 is less than int2.
	- greater than: ``int1 -gt int2``
- ``int1 -le int2``: integer int1 is less than or equal to int2.
	- greater or equal: ``int1 -ge int2``
- ``-d [thing]``: ``[thing]`` is a directory
- ``-f [thing]``: ``[thing]`` is a file
- ``-h [thing]``: ``[thing]`` is a link
- ``-e [thing]``: ``[thing]`` exists
- ``-r [file]``: ``[file]`` is readable
- ``-w [file]``: ``[file]`` is writable
- ``-x [file]``: ``[file]`` is executable
- ``-o, -a, !``: or, and, negation
- Use ``( )`` to group tests

---

## Git and version control
(needs to be updated)
- ``git status``: shows which files have/haven't been edited and/or staged for committing
- ``git add [file]``: stages a file (&/or its changes) for committing
- ``git rm [file]``: removes a file from Git tracking
- ``git mv [file1] [file2]``: renames/moves a file and updates Git records accordingly
- ``git commit``: commits changes to the Git record
- ``git checkout -- .``: *(version control? undo prev. command?)*
- ``git config``: 
- ``git clone``: copy the contents of a repository into a new folder in the current directory on my local machine. Must have read access to the repository.
    - e.g. ``git clone git@github.com:vsbuffalo/bds-files.git``

---

## Remote server commands
- ``ssh adinicola@submit-3.chtc.wisc.edu``: connect to my submit server
- ``cd /mnt/gluster/adinicola``: move to my gluster directory
- ``cd /home/adinicola``: move back to my home directory on the submit server
- ``^D (Ctrl+D)``: logout and quit ssh
- ``scp [filename.txt] adinicola@transfer00.chtc.wisc.edu:/mnt/gluster/adinicola``: Copy to my gluster space
- ``scp [filename.txt] adinicola@submit-3.chtc.wisc.edu:/home/adinicola``: Copy to my submit server
- ``cat ~/.ssh/id_rsa.pub``: view my private key
- ``/Users/Alexa/.ssh/id_rsa``: my private key
- ``/Users/Alexa/.ssh/id_rsa.pub``: my public key

### CHTC and HTCondor
<http://chtc.cs.wisc.edu/>
<http://research.cs.wisc.edu/htcondor/manual/current/2_5Submitting_Job.html>
<http://research.cs.wisc.edu/htcondor/manual/current/2_6Managing_Job.html>
- ``condor_submit [file].sub``: submit an HTCondor job, per the .sub file provided
- ``condor_q``: view submitted/running/idle/held jobs
    - ``condor_q -hold``: see why a job, or any/all of my jobs, is held
		(see also <http://research.cs.wisc.edu/htcondor/manual/current/12_Appendix_A.html#HoldReasonCode-job-attribute>)
    - ``condor_q -analyze [job ID]``: see diagnostic info on [job]
- ``condor_rm [job ID]``: flag a job for cancellation & removal
    - ``condor_rm [username]``: flag all [username]’s jobs for cancellation & removal
- ``condor_ssh_to_job [job ID]``: access files, etc., in a running job
- ``condor_check_userlogs [file].log``: check the given log(s) for errors
- ``condor_hold [job id]``: manually put a job on hold
- ``condor_release``: release a job from a manual hold
- ``condor_history``: see the jobs I’ve submitted in the past
- ``condor_status``: various useful queries (warning: needs arguments, or else output is loooooooong)
