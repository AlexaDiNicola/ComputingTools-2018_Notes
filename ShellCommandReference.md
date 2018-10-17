## Contents:

- [Background information](#background-information)
- [Basic shell commands](#basic-shell-commands)
    - [Getting help](#getting-help)
    - [Command history](#command-history)
    - [Special characters](#special-characters)
    - [Shortcut commands](#shortcut-commands)
    - [Environmental variables](#environmental-variables)
- [File handling & navigation](#file-handling-&-navigation)
    - [Text editing](#text-editing)
    - [Searching & regex](#searching-&-regex)
    - [Text processing](#text-processing)
    	- [awk](#awk)
	- [tmux][#tmux]
- [Shell scripting](#shell-scripting)
    - [Pipes & redirection](#pipes-&-redirection)
    - [Arithmetic](#arithmetic)
    - [The basic loop](#the-basic-loop)
    - [Conditional statements](#conditional-statements)
    	- [Conditional examples](#conditional-examples)
    	- [Some conditional-test expressions](#some-conditional-test-expressions)
- [Git: collaboration & version control](#git-collaboration-and-version-control)
	- [Local repository commands](#local-repository-commands)
	- [Github sync and collaboration](#github-sync-and-collaboration)
- [Remote server commands](#remote-server-commands)
	- [SSH and SCP](#ssh-and-scp)
	- [Getting external data](#getting-external-data)
    - [CHTC and HTCondor](#chtc-and-htcondor)

---


## Background information

- Signals sent to running processes:
	- SIGKILL: kill process
	- SIGHUP: hang up. Not as strong as SIGKILL, but stronger than SIGINT.
	- SIGINT: interrupt process
	- SIGTSTP: stop process. Like Ctrl-Z, as in sleep.


---


## Basic shell commands


### Getting help

- ``[command] --help``: brief help on a command
- ``man [cmd]``: manual page, i.e. extended help on ``[cmd]``
- ``echo [var]``: print the value of a variable or string
- ``whoami``: print your username
- ``hostname``: print this computer's name/address
- ``ps``: list running processes that were started from current terminal window
- ``ps -u [user]``: list all running processes started by [user]
- ``top``: show the most demanding processes currently running

### Command history

- ``history``: list previously-entered commands (long list!)
- ``history \| tail -n [num]``: list only the last [num] previous commands
- ``![num]``: repeat command [num] in the history
- ``[Ctrl-R] [text]``: searches your history for the most recent command matching [text]; 
  press again to search back from there, etc.
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


### Environmental variables

- ``$PS1``: the prompt string. default $PS1 = “\h:\W \u\$”
- ``$PATH``: colon-separated list of paths to bin folders

```
parse_git_branch() { # defines a shell function: run "git branch" and extract branch name
   git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
PS1="\W \[\033[33m\]\$(parse_git_branch)\[\033[00m\]$ "
```

---


## File handling & navigation

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
- ``mkdir -p zmays-snps/{data/seqs,scripts,analysis}``: Brace expansion. Create a directory 
  structure in one line: this one will make a folder ``zmays`` with subfolders ``data``, 
  ``scripts``, and ``analysis``, and a sub-subfolder ``seqs`` in ``data``.
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
- ``exit``: quits current program
- ``pushd [path]``: *...*
	- ``popd [path]``: *...*

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
- ``touch [file]``: create a blank file called [file], or update timestamp if file already 
  exists
- ``sort [file]``: sort the contents of [file] in alphabetical order
  - ``-n``: in numerical order
  - ``uniq``: filters out consecutive repeated lines. ``-c`` to get counts. e.g. 
    ``sort list.txt | uniq -c``
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
    - ``-d``: set depth: which directory levels will you search? (Default is just the 
      current one.)
    - ``-mtime``: return modified time
- ``grep "and" fish.txt``: within fish.txt, search for the string “and” (“grep” from 
  “global/regular expression/print”)
    - ``-n``: line numbers
    - ``-i``: case-insensitive search
    - ``-w``: whole words
    - ``-v``: invert the search
    - ``-o``: return the match only
    - ``-E``: use Extended (not basic) regex
    - ``-P``: use Perl-like regex (GNU only)
    - ``--color``: colorize the results
    - ``-B 3``: include the 3 lines before each result
    - ``-A 2``: include the 2 lines after each result
- ``man re_format``: regex help
    - ``.``: any one character
    - ``^``: beginning of line (only if placed first)
    - ``$``: end of line (only if placed last)
    - ``\``: turns off special meaning of next symbol
    - ``[aBc]``: anything in: a or B or c. Ranges: like [0-9], [a-z], [a-zA-Z]
    - ``[^aBc]``: anything but: a, B, c
    - ``\w``: any word character: letter, number, or “_”. also [[:alnum:]_]. opposite: \W
    - ``\d``: any single digit. also [[:digit:]] or [0-9]. opposite: \D
    - ``\s``: any white space character: single space, \t (tab), \n (life feed) or \r 
      (carriage return). also [[:space:]]. opposite: \S
    - ``\b``: word boundary (null string). also \< and \> for start/end boundaries. 
      opposite: \B
    - ``+``: one or more of the previous
    - ``?``: zero or one of the previous
    - ``*``: zero or more of the previous
    - ``{4}``: 4 of the previous
    - ``{4,6}``: between 4 and 6 of the previous
    - ``{4,}``: 4 or more of the previous

### Text processing

- ``sed``: *...*
	- e.g. ``sed 's///g' file.txt``: *...*
- ``bioawk``: like ``awk`` (see below), but for biology data formats
- Parameter expansion: use ``${variable_name extra stuff}``, as below.
```
var="coolname.txt.pdf.md"
i=3678
echo "var=$var and i=$i"
echo "substrings of parameter values: ${i:1} and ${var:4:5}" # :offset:length
echo "strip from the end: ${var%.*}"  # strips shortest occurrence
echo "strip from the end: ${var%%.*}" # strips longest  occurrence
echo "strip from beginning: ${var#*.}"  # strips shortest occurrence
echo "strip from beginning: ${var##*.}" # strips longest  occurrence
echo "substitute: ${var/cool/hot}"
echo "delete:     ${var/cool}"
```

#### awk

``awk '/pattern/ { action }' filename``: *...*

- ``awk`` is a programming language in itself. It works on tabular data.
- Patterns:
	- ``A ~ B``: if A matches regex pattern B
	- ``A !~ B``: if A doesn't match regex pattern B
	- Combine patterns with and ``&&``, or ``||``
	- Special patterns: BEGIN, END
	- Special variables: 
		- ``$0``: entire record (line)
		- ``$1``: first field (columns)’s value
		- ``$2``:  second field’s value, etc.
		- NR = current record (line) number
		- NF = number of fields (columns) on current line
- can do arithmetic operations on field values, standard comparisons (``<=``, ``==`` etc.)
- extra fields can be printed
- new variables can be introduced, modified, used (no ``$`` to use them, unlike shell 
  language)
- Actions: ``if``, ``for``, ``while`` statements can be used
- many built-in functions, like ``exit``, ``sub(regexp, replacement, string)``, 
  ``substr(string, i, j)``, and ``split(string, array, delimiter)``
- By default, inputs are assumed to be tab-delimited. For a csv file, change to comma with 
  ``-F","``
- Examples from Cécile's class notes, using ``example.bed`` from **[...?]**:
	- ``awk  '{ print $0 }' example.bed``: This is like ``cat``. Since there's no pattern, 
	  it defaults to true.
	- ``awk '{ print $2 "\t" $3 }' example.bed``: This works like ``cut -f2,3``.
	- ``awk '$3 - $2 > 18' example.bed``: prints lines (default action) if feature length > 18
	  (bed 0-based)
	- ``awk '$1 ~ /chr1/ && $3 - $2 > 10' example.bed``: prints lines if feature length > 18 
	  *and* feature is on chromosome 1
	- Using variables:
		- ``threshold=18 ; awk '$3 - $2 > $threshold' example.bed``: This throws an error 
		  because ``$`` is reserved for awk fields. You can't use shell variables within 
		  the ``awk`` program.
		- ``awk -v t=$threshold '$3 - $2 > t' example.bed``: The ``-v`` option lets you 
		  define variables within ``awk``, including using shell variables to define ``awk`` 
		  variables.
	- Combining a pattern with an action: ``awk '$1 ~ /chr2|chr3/ { print $0 "\t" $3 - $2 }' example.bed`` 
	  prints the whole line, a tab, and then the difference between the third and second 
	  field. (In context, this prints the name, beginning position, ending position, and 
	  length for all genes on chromosomes 2 and 3.)
	- ``awk 'BEGIN{ s = 0 }; { s += ($3-$2) }; END{ print "mean: " s/NR };' example.bed``: 
	  Calculates and prints the mean feature length, for all the genes in the file:
		1. starts with variable ``s``, value 0
		2. on each line, adds the difference between columns 3 and 2 (i.e. the gene length) 
		   to ``s``
		3. at the end, divides ``s`` (now the sum of all genes' lengths) by NR (the number 
		   of lines/rows in the input) to get the average gene length
		4. then prints "mean:  " and the value of that average
	- ``awk 'NR >= 3 && NR <= 5' example.bed``: prints lines 3, 4, and 5 only
	- ``awk -F "\t" '{print NF; exit}' Mus_musculus.GRCm38.75_chr1.bed``: number of columns 
	  (fields) on 1st line
	- ``grep -v "^#" Mus_musculus.GRCm38.75_chr1.gtf | awk -F "\t" '{print NF; exit}'``: 
	  removes the header (lines that start with #) in a gtf file, then pipes the results to 
	  determine how many columns there are in the actual *data*

A multiline ``awk`` command:
```
awk '/Lypla1/ { feature[$3] += 1 };
    END { for (k in feature)
    print k "\t" feature[k] }' Mus_musculus.GRCm38.75_chr1.gtf  | column -t
```
1. First pattern-action pair. For every line that matches ``/Lypla1/``, add the third 
   column to ``feature``, or increment the relevant value in ``feature`` if that third 
   column is already represented.
	- Note that ``feature`` is an array (because square brackets), AKA a dictionary (in 
	  Python) or hash (in Perl). It consists of a set of keys (~names), each of which has 
	  an associated numerical value.
	- Line ends in a semicolon, which ends the first pattern-action pair.
2. Second pattern-action pair: No pattern. Start a ``for`` loop over the keys in ``feature``.
3. Finish the ``for`` loop by printing the value, a tab, and then the key.
4. After finishing the loop, pipe the ``awk`` output to ``column`` for easier viewing.


### tmux
(probably a better practice than using multiple SSH windows or tabs)

- ``tmux new-session -s sessname``
- ``tmux list-sessions``
	- ``detach``
	- ``attach``

- Keyboard shortcuts, assuming you're using Cécile's preferred ``.tmux.conf``:
	- ``^a d``: detach
	- ``^a c``: create new window
	- ``^a |`` or ``^a -``: splits window vertically or horizontally (depends on config file)
	- ``^a n`` or ``^a p``: go to next or previous window
	- ``^a`` left arrow: go to left pane. other arrows for right, top, bottom panes
	- ``^a ?``: list all key sequences
	- ``^a &``, ``exit`` or ``logout``: kill current window
	- ``^a x``: kill current pane


---


## Shell scripting

- ``bash [scriptname]``: execute [scriptname] as a bash shell script
- ``{1..9}``: set of the integers 1-9
- ``tail -f [file]``: “follow” a file, displaying its last few lines in realtime as the 
	file is updated
- ``/dev/null``: “null device”, a black hole: redirect things here to delete them
- ``[command] &``: execute [command] in the background

### Pipes & redirection

- ``[command] > [file]``: redirect output of [command] and save it as a textfile, [file]
    - ``[command] 0> [file]``: save inputs to [command] as [file]
    - ``[command] 1> [file]``: save outputs from [command] as [file]
    - ``[command] 2> [file]``: save errors from [command] as [file]
    - ``[command] > [file1] 2> [file2]``: save output as [file1] and errors of same 
    	command as [file2]
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

#### Conditional examples

```
if [ $i -lt 800 ] # (the spaces after [ and before ] are REQUIRED)
then
  echo "i is less than 800"
else
  echo "i is not less than 800"
fi

if [ $# -lt 1 -o ! -f $1 -o ! -r $1 ]  # if number of args is less than one, OR if the first argument is not a file, OR if the first argument isn’t readable…
then
  echo "error: no argument, or no file, or file not readable"
  exit 1 # exit script with error code (1). 0 = successful exit
fi
```

#### Some conditional-test expressions

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
 - ``||``: or
 - ``&&``: and
- Use ``( )`` to group tests

---


## Git: collaboration & version control

### Local repository commands

- ``git init``: turns the current folder into a new, empty Git repository
- ``git config``: *[?]*
- ``git status``: shows which files have/haven't been edited and/or staged for committing
- ``git add [file]``: stages a file (&/or its changes) for committing
	- ``git add -A``: stages all un-staged changes for committing
- ``git rm [file]``: removes a file from Git tracking
- ``git mv [file1] [file2]``: renames/moves a file and updates Git records accordingly
- ``git commit``: commits changes to the Git record
	- ``git commit --amend``: change commit messsage (only) for the last commit. DO NOT USE 
	  if you've already pushed it to Github! (Just generally never delete things you've 
	  already pushed. It's rude to your collaborators.)
- ``git checkout [commit] -- filename``: pull the version of ``filename`` from ``[commit]``
	- e.g. ``git checkout 832eabda4cb -- readme.md`` pulls ``readme.md`` from commit 832eabda4cb
	- ``git checkout --`` (without a filename) pulls the whole project
	- ``git checkout --track origin/readme-changes``: pulls info on branch ``readme-changes``
- ``git revert``: revert changes, create a new commit.
	- ``git revert HEAD``: create a new commit whose actions cancel the actions of the 
		previous commit
	- ``git revert HEAD~1``: ditto, but revert to the second-to-last commit (erasing both 
		the previous commit and the one before)
- Don't use ``git reset`` or ``git rebase`` unless you know exactly what you're doing: they 
  change the git history and will mess up your collaborators. Even if you know what you're 
  doing, don't use them after pushing the affected commits.
- ``git stash``: creates something like a temporary snapshot, to save changes that are not 
	ready for a commit when you need to get back to the previous commit.
	- Example use: you made changes, working from the master branch, and realize that these 
	  changes will need to be committed on a different branch. ``git stash`` will temporarily 
	  save those changes and back out to the previous commit. You can then create the new 
	  branch and switch to it: ``git checkout -b mybranch``, then do ``git stash pop`` to 
	  bring those changes back (but now on the desired branch).

### Github sync and collaboration

- ``git clone``: copy the contents of a repository into a new folder in the current directory on my local machine. Must have read access to the repository.
    - e.g. ``git clone git@github.com:vsbuffalo/bds-files.git``
- ``git pull``:
- ``git push origin branchname``: push current local commit to ``branchname`` in the 
	original Github repository
	- ``git push -u origin branchname``: remember this branch and keep me on it
- ``git branch``: lists all currently-existing branches (the asterisk shows which branch 
	I'm currently on)
	- ``git branch branchname``: creates a new branch called ``branchname``
	- ``git branch -d branchname``: deletes the branch called ``branchname``
	- ``git branch -vv``: list all existing branches "very verbosely", i.e. show latest 
		commit with message for each branch
- ``git fetch --all``: pull down everything new from this repository, incl. branches *and* 
	files


---


## Remote server commands

- ``nohup [command] &``: "no hangup." Executes ``[command]`` in the background, divorced 
	from the current shell process, and insulates it from SIGHUP. This way the process 
	won't stop if this shell is closed, I log out, the computer sleeps, etc.
- ``shasum [thing]``: get the SHA checksum for ``[thing]`` (a file, string, etc)
- ``md5 [thing]``: get the MD5 checksum for ``[thing]``
- SSH keys:
	- ``cat ~/.ssh/id_rsa.pub``: view my private key
	- ``~/.ssh/id_rsa``: my private key
	- ``~/.ssh/id_rsa.pub``: my public key
- ``less -S ~/.ssh/known_hosts``: show the local machine's list of hostnames. Each line is a 
	machine I've logged onto.


### SSH and SCP

- ``ssh username@hostname``: Secure SHell. connect to ``hostname`` with ``username``
	- If ``username`` isn't specified, defaults to your username on the local machine.
	- ``hostname``: print the host's name/address
	- ``^D (Ctrl+D)``: logout and quit ssh
	- ``ssh adinicola@submit-3.chtc.wisc.edu``: connect to my CHTC submit server
- ``scp``: Secure Copy Protocol (or just Secure CoPy). Like SSH, but for file transfers.
	- ``scp username@hostname:path/of/filename.txt localpath/``: Using my credentials as
		``username@hostname``, copy ``filename`` from the remote server (specifically,
		relative to the remote machine, from ``~/path/of/``) to ``./localpath`` on my machine.
	- ``scp -p``: preserve timestamps
	- NB a slight difference between ``cp`` and ``scp``:
		- ``cp -r log/ target/path/`` copies **only the content** of the ``log/`` directory
		- ``cp -r log target/path/`` copies the directory itself **and** its content
		- ``scp``, on the other hand, **doesn't have this subtlety.**

### Getting external data

- ``wget``: *...*
	- *...*
	- *...*
- ``curl``: Like ``wget``, but instead of *saving* the external file to disk, writes it to 
	stdout.
	- It can use ``sftp`` among other protocols (more than ``wget``)
	- It can follow redirected pages with ``--location``
	- Some options:
		- ``-O``, ``-o``: *...*
		- ``--limit-rate``: Limit download speed, to avoid getting kicked off websites for 
			suspected DOS
		- ``-I`` or ``--head``: to get header only. On ftp files: file size
		- ``-s``: Silent, with no progress meter and no error messages
		- ``-#``: Display only a simple progress bar and no progress meter

### CHTC and HTCondor

<http://chtc.cs.wisc.edu/>
<http://research.cs.wisc.edu/htcondor/manual/current/2_5Submitting_Job.html>
<http://research.cs.wisc.edu/htcondor/manual/current/2_6Managing_Job.html>
- Navigating the Condor servers:
	- ``cd /mnt/gluster/adinicola``: move to my gluster directory
	- ``cd /home/adinicola``: move back to my home directory on the submit server
	- ``scp [filename.txt] adinicola@transfer00.chtc.wisc.edu:/mnt/gluster/adinicola``: 
		Working from my local machine, copy to my gluster space
	- ``scp [filename.txt] adinicola@submit-3.chtc.wisc.edu:/home/adinicola``: Working 
		from my local machine, copy to my submit server
- ``condor_submit [file].sub``: submit an HTCondor job, per the .sub file provided
	- ``condor_submit [file].sub --dryrun out.txt``: "dry run" a Condor job, saving the 
		resulting parameters to ``out.txt``.
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
- ``condor_status``: various useful queries (warning: needs arguments, or else output is 
	loooooooong)
