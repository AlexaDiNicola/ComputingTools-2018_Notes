## Contents

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
[back to top](#contents)

### Getting help
- ``command --help``: brief help on ``command``
- ``man command``: manual page, i.e. extended help on ``command``

### Command history
- ``history \| tail -n 17``: list only the last 17 previously-entered commands
- ``!23``: repeat command 23 in the history
- ``^R text``: searches your history for the most recent command matching ``text``; press again to search back from there, etc.
- ``echo !$``: prints last word of previous command
- ``xargs``: after a pipe, passes the prev command’s output as an argument (not standard input)
- ``ls *.txt \| xargs cat``: prints (using cat) the contents of all text-files in current dir

### Special characters
- ``*``: wildcard, matches zero or more characters
- ``?``: wildcard, matches exactly one character
- ``\``: escape character (e.g. to cd into a folder with a space in its name)
- ``$(command)``: command substitution: pass the results of ``command`` as a variable
- ``/``: (as a file-operations argument, alone) the root directory
- ``""``: Lines in double-quotes are interpreted as strings, but variables in them are parsed.
- ``''``: Lines in single-quotes are interpreted strictly as strings — no parsing.

### Shortcut commands
- ``^A`` (Ctrl-A): move cursor to the start of the line
- ``^E``: move cursor to the end of the line
- ``^C``: stop/kill a running program, cancel current action
- ``^Z``: pause a running program
- ``bg``: resume in the background
- ``fg``: resume in the foreground
- ``jobs``: see list of currently-running jobs
- ``ps -u User``: list all running processes started by ``User``
- ``top``: see list of all processes, refreshed, with CPU & memory consumption
- ``kill -9 PID``: kill process ``PID``

-----

## File handling
[back to top](#contents)

- ``pwd``: “print working directory,” i.e. state your current location
- ``cd``: “change directory.” With no arguments, takes you to your home directory.
    - ``cd ../Folder/Subfolder``: go up one level, then into ``Subfolder``, which is in ``Folder``
    - ``cd -``: go to the previous directory (not “up”, but “back”)
- ``ls``: list files in the current directory (“listing”)
    - ``-a``: list all files, including hidden
    - ``-F``: add a type marker to file/directory names
    - ``-lh``: show details, with file sizes in more human-readable units
    - ``-R``: recursively list subdirectories
    - ``-t``: sort by modification time, newest first
    - ``-1``: one entry per line
    - ``-C``: multi-column (opposite of -1 flag)
    -  Sort files by:
        - [none]: name
        - ``-lS``: size
        - ``-lt``: time last modified
        - ``-ltu``: time last accessed (also ``-tu``, ``-u``)
        - ``-ltc``: time file status was last changed (also ``-tc``, ``-c``)
        - ``-r``: (in reverse order)
- ``mkdir -p zmays-snps/{data/seqs,scripts,analysis}``: Directory creation + brace expansion. Create a directory structure in one line: this one will make a folder ``zmays`` with subfolders ``data``, ``scripts``, and ``analysis``, and a sub-subfolder ``seqs`` in ``data``.
- ``mv filename``: move a file
- ``cp filename1 filename2 … filenameN dirname``: copies ``filename1`` through ``filenameN`` into ``dirname``
- ``rm filename``: remove (delete) a file or empty directory
	- ``rm -r``: delete a directory and (recursively) all files/dirs inside it
	- ``rm -f``: “force” removal without asking for confirmation for each file
	- ``rm -i``: ask, interactively, before deleting each individual file
    - ``rmdir dirname``: remove a directory, even if it has files
- ``chmod u+x headtail.sh``: grant the current user permission to execute headtail.sh
    - ``u, g, o, a``: user, group, other, all (whose permissions are we changing?)
    - ``+`` or ``-``: add or remove permissions (how are we changing them?)
    - ``r, w, x``: read, write, execute (which permissions are we changing?
- ``diff file1 file2``: return all lines where ``file1`` and ``file2`` are different
- ``cat 1 2``: concatenate ``1`` and ``2``

### Text editing
[back to top](#contents)

- ``open file``: use default program to open ``file``
- ``cat file`` : print the full text of ``file``
- ``less file``: print the text of ``file``, page by page. Name from “less is more.”
    - ``q``: quit
    - ``[enter]``: next line
    - ``[space]``: next “page”
    - ``/pattern``: search forward for ``pattern``
    - ``?pattern``: search backward for ``pattern``
    - ``n``: “next”, repeat previous search
- ``nano file``: open ``file`` in ``nano`` text editor
- ``head file``: print the top 10 lines of ``file``
  - ``tail -n 2 file``: print the last 2 lines of ``file``
- ``wc file``: word count. Returns # of lines, words, & characters in ``file`` (``-l``, ``-w``, ``-c``)
- ``touch file``: create a blank file called ``file``, or update timestamp if file already exists
- ``sort file``: sort the contents of ``file`` in alphabetical order
  - ``-n``: in numerical order
  - ``sort list.txt | uniq -c``: return unique lines from list.txt, each with number of appearances
- ``cut -f 1 Mus_musculus.bed``: extract first column (“field”) from Mus_musculus.bed
  - ``-f2``: get second field
  - ``-d``: change delimiter (default is tab)
- ``pandoc``: converts Markdown to PDF, HTML, TeX, possibly others
- ``tar -cf archive.tar foo bar``: create archive.tar from files foo and bar
  - ``tar -tvf archive.tar``: list all files in archive.tar, verbosely
  - ``tar -xf archive.tar``: extract all files from archive.tar

### Searching & regex
- ``find "and"``: search for files with names containing “and”
    - ``-type d``: find directories (``-type f``: find files)
    - ``-name pattern``: find filenames fitting ``pattern``
    - ``-d``: set depth: which directory levels will you search? (Default is just the current one.)
- ``grep "and" fish.txt``: within fish.txt, search for the string “and” (“grep” from “global/regular expression/print”)
    - ``-n``: line numbers
    - ``-i``: case-insensitive search
    - ``-w``: whole words
    - ``-v``: invert the search
    - ``-o``: return the match only
    - ``-E``: use Extended (not basic) regex
- ``man re_format``: regex help
    - ``.``: any one character
    - ``^``: beginning of line (only if placed first)
    - ``$``: end of line (only if placed last)
    - ``\``: turns off special meaning of next symbol
    - ``[aBc]``: anything in: a or B or c. Ranges: like [0-9], [a-z], [a-zA-Z]
    - ``[^aBc]``: anything but: a, B, c
    - ``\b``: word boundary (null string). also \< and \> for start/end boundaries. opposite: \B
    - ``+``: one or more of the previous
    - ``?``: zero or one of the previous
    - ``*``: zero or more of the previous
    - ``{4}``: 4 of the previous
    - ``{4,6}``: between 4 and 6 of the previous
    - ``{4,}``: 4 or more of the previous

---

## Shell scripting

- ``bash scriptname``: execute ``scriptname`` as a bash shell script
- ``{1..9}``: set of the integers 1-9
- ``tail -f file``: “follow” a ``file``, displaying its last few lines in realtime as the file is updated
- ``/dev/null``: “null device”, a black hole: redirect things here to delete them
- ``command &``: execute ``command`` in the background

### Pipes & redirection
- ``command > file``: save output of ``command`` as ``file``
    - ``command > file1 2> file2``: save output of ``command`` as ``file1`` and errors of same command as ``file2``
    - ``0>`` to save inputs, ``1>`` outputs, ``2>`` errors, ``&>`` errors + output
- ``>>``: instead appends output of command as new line(s) at end of file
- ``[line1] | [line2]``: uses output of ``line1`` as input to ``line2``

### Arithmetic
- ``echo ((++i))``: increment i, then print the new value
- ``echo ((i++))``: print value of i, then increment it
- ``((i+=1))``: increment variable i
- ``((i--))``: decrement variable i
- ``((i+=5))``: increase i by 5
- ``((i/=5))``: divide i by 5

### The basic loop
``for varname in listofinputs ; do command ; done
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
- ``git status``: shows which files have/haven't
- ``git add [file]``: stages a file (&/or its changes) for committing
- ``git rm [file]``: removes a file from Git tracking
- ``git mv [file1] [file2]``: renames/moves a file and updates Git records accordingly
- ``git commit -m "Message here"``: commits changes to the Git record, with commit description "Message here"
- ``git checkout -- .``: version control? undo prev. command?
- ``git clone``: copy the contents of a repository into a new folder in the current directory on my local machine. Must have read access to the repository.
    - e.g. ``git clone git@github.com:vsbuffalo/bds-files.git``

---

## Remote server commands
- ``ssh adinicola@submit-3.chtc.wisc.edu``: connect to my submit server
- ``cd /mnt/gluster/adinicola``: move to my gluster directory
- ``cd /home/adinicola``: move back to my home directory on the submit server
- ``scp [filename.txt] adinicola@transfer00.chtc.wisc.edu:/mnt/gluster/adinicola``: Copy to my gluster space
- ``scp [filename.txt] adinicola@submit-3.chtc.wisc.edu:/home/adinicola``: Copy to my submit server

### CHTC and HTCondor
- ``condor_submit [file].sub``: submit an HTCondor job, per the .sub file provided
- ``condor_q``: view submitted/running/idle/held jobs
    - ``condor_q -hold``: see why a job, or any/all of my jobs, is held
		(see also <http://research.cs.wisc.edu/htcondor/manual/current/12_Appendix_A.html#HoldReasonCode-job-attribute>)
    - ``condor_q -analyze [job ID]``: see diagnostic info on [job]
- ``condor_rm [job ID]``: flag a job for cancellation & removal
- ``condor_ssh_to_job [job ID]``: access files, etc., in a running job
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcyMjMzOTExOV19
-->