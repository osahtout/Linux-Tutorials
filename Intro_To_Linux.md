ctrl-alt-m to extract function  
alt-enter ->>>> for loop to   
crtl alt c ---> constant  
local history -> show history  

# Introduction to Linux

# Chapter 3

## Boot Process
      
1. power on
2. BIOS
3. MBR, master boot loader
4. Boot Loader
5. Kernal
6. Initial RAM disk
7. /sbin/init
8. Command Shell using getty
9. X Windows System

--------------------------

## Different types of filesystems supported by Linux:

* Conventional disk filesystems: ext2, ext3, ext4, XFS, Btrfs, JFS NTFS, etc.
* Flash storage filesystems: ubifs, JFFS2, YAFFS, etc.
* Database filesystems
* Special purpose filesystems: procfs, sysfs, tmpfs, squashfs, debugfs, etc
----------------------------------

## A comparison between filesystems in Windows and Linux is given in the accompanying table:

|   iii                   | Windows      | Linux          |
| :-----------            | :------:     | :-----------:  |
| partition               | Disk1        | /dev/sda1      |
| FileSystem type         | NTFS/VFAT    | ext2, ext3 ... |
| Mounting Parameters     | DriverLetter | MountPoint     |
| Base Folder (os location)| C:\          | /              |

-----------------------------------


## Distribution
* Server
    * RHEL/CentOS
    * Ubuntu Server
    * SLES
    * Debian
* Desktop
    * Ubuntu
    * Fedora
    * Linux Mint
    * Debian
* Embeded
    * Yocto
    * Open Embedded
    * Android

![File Hierarchy](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1d8c97abd237dcd44a5fe5464f6521ac/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/chapter01_The_Linux_Kernel_Distribution_Families_and_Individual_Distributions.png)

-----------------------------

## Package Managers
* Debian
    * apt-get
        * dpkg
* SUSE
    * zypper
        * rpm
* Red Hat
    * yum
        * rpm


![Package managers](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/b2cfd35138881e077bfc97915aed86b8/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/Package_Managers.png)

------------------------------------------

## File hierarchy

![File Hierarchy](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/66def40e2774fd96011565107706da2d/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/dirtree.jpg)



# Chapter 7

## Basic Utilities

* **cat**: used to type out a file (or combine files)
* **head**: used to show the first few lines of a file
* **tail**: used to show the last few lines of a file
* **man**: used to view documentation.

--------------------------------

## Most input lines entered at the shell prompt have three basic elements:

* Command
* Options
* Arguments.
    * [command] [options] [arguments]
    * shutdown -r now

---------------------------------

## Setting Up sudo

1. type **su** and hit _Enter_
2. enter password then _Enter_
3. Now, you need to create a configuration file to enable your user account to use sudo. Typically, this file is created in the  
 /etc/sudoers.d/ directory with the name of the file the same as your username. For example, for this demo, let’s say your username is  
 “student”. After doing step 1, you would then create the configuration file for “student” by doing this:  
 \# echo "student ALL=(ALL) ALL" > /etc/sudoers.d/student
4. Finally, some Linux distributions will complain if you do not also change permissions on the file by doing:  
   \# chmod 440 /etc/sudoers.d/student

---------------------------------

## Switch between virtual terminal (VT)


**CTRL-ALT-functionKey**  
**Ubuntu uses VT-7 or CTRL-ALT-F7**

-------------------------------

## To start or stop GUI
- $ sudo systemctl stop gdm (**or** sudo telinit 3)  
- $ sudo systemctl start gdm (**or** sudo telinit 5)

---------------------------------

## SSH

- One can also connect and log into remote systems via the Secure Shell (SSH) utility. For example, by typing  
ssh username@remote-server.com,  
 SSH would connect securely to the remote machine and give you a command line terminal window, using passwords  
  (as with regular logins) or cryptographic keys (a topic we will not discuss) to prove your identity.

------------------------

## Shutdown

- shutdown [-akrhPHfFnc] [-t sec] time [message]

| Options | Description |
| :---- | :----- |
|-a|Control access to the **shutdown** command using the control access file **/etc/shutdown.allow**. See Access Control below for more information. |
|-k|Do not shut down, but send the warning messages as if the shutdown were real. |
|-r|Reboot after shutdown. |
|-h|Instructs the system to shut down and then halt. |
|-P|(capital) Instructs the system to shut down and then power down. |
|-H|If **-h** is also specified, this option instructs the system to drop into boot monitor on systems that support it. |
|-f|Skip **fsck** after reboot. |
|-F| 	Force **fsck** after reboot. |
|-n|Don't call **init** to do the **shutdown** of processes; instruct shutdown to do that itself. **The use of this option is discouraged, and its results are not always predictable.** |
|-c|Cancel a pending shutdown. (This does not apply to "**shutdown now**", which does not wait before shutting down.) With this option, it is not possible to give the time argument, but you can still specify an explanatory message that will be sent to all users. |
|-t _sec_|Tell **init** to wait sec seconds between sending processes the warning and the kill signal, before changing to another runlevel. |
|_time_|The time argument specifies when to perform the shutdown operation. <br> The time can be formatted in different ways: <br> First, it can be an absolute time in the format hh:mm, in which hh is the hour (1 or 2 digits, from **0** to **23**) and mm is the minute of the hour (in two digits). <br> Second, it can be in the format +m, in which m is the number of minutes to wait. <br> Also, the **word** now is the same as specifying **+0**; it shuts the system down immediately. |
|_message_|A message to be sent to all users, along with the standard shutdown notification. |

-----------------------------

## Locating application
> which  
> whereis  

example:
- $ which diff  
  /usr/bin/diff

- $ whereis diff  
  diff: /usr/bin/diff /usr/share/man/man1/diff.1.gz /usr/share/man/man1p/diff.1p.gz

-----------------------------

## Access Directories
|Command | Results|
|:----- | :----|
| pwd| Displays the present working directory|
| cd ~ _or_ cd |Change to your home directory (shortcut name is ~ (tilde))|
|cd ..| Change to parent directory (..) |
|cd - | Changes to previous directory(- (minus))|

-----------------------------

## Absolute vs Relative path

- Absolute pathname  
An absolute pathname begins with the root directory and follows the tree, branch by branch, until it reaches the desired directory or file. Absolute paths always start with /.  
$ cd /usr/bin
- Relative pathname  
A relative pathname starts from the present working directory. Relative paths never start with /.  
$ cd ../../usr/bin


![File Hierarchy](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c9a79bc0bfc23d476b1c89380ca90aad/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch06_screen19.jpg)

-----------------------------

## Exploring File System

> tree -d

-----------------------------

## Hard Links
The **ln** utility is used to create hard links and (with the **-s** option) soft links, also known as symbolic links or symlinks. These two kinds of links are very useful in UNIX-based operating systems.  

> Hard link
**$ ln file1 file2**

Note that two files now appear to exist. However, a closer inspection of the file listing shows that this is not quite true.

**$ ls -li file1 file2**

38809 -rw-rw-r-- 2 student student 0 jan 6 09:18 file1  
38809 -rw-rw-r-- 2 student student 0 jan 6 09:18 file2

> soft link

**$ ln -s file1 file3**
**$ ls -li file1 file3**

38809 -rw-rw-r-- 2 student student 0 jan 6 09:18 file1  
38809 -rw-rw-r-- 2 student student 0 jan 6 09:18 file2  
38810 -rw-rw-r-- 2 student student 5 jan 6 09:22 file2

-----------------------------

## Viewing Files

|Command|usage|
|:------|:-----|
|cat|Used for viewing files that are not very long; it does not provide any scroll-back.|
|tac|  tac 	Used to look at a file backwards, starting with the last line.|
|less| Used to view larger files because it is a paging program. It pauses at each screen full of text, provides <br> scroll-back  capabilities, and lets you search and navigate within the file. Note: Use / to search for a pattern in the forward direction  and ? for a pattern in the backward direction. An older program named more is still used, but has fewer capabilities: "less is more".|
|tail| Used to print the last 10 lines of a file by default. You can change the number of lines by doing -n 15 or just -15 if <br> you wanted to look at the last 15 lines instead of the default.|
|head| The opposite of tail; by default, it prints the first 10 lines of a file.|
|vi| View, edit files|

-----------------------------

## Moving, Renaming or Removing

|Command|Usage|
|:------|:---|
|touch| create a file|
|touch -t|-t [mmddhhmm] myfile -t to timestamp|
|mv| Rename file or directory|
|rm| remove file|
|rm -rf| Remove directory and all its content|
|rm -f| forcefully remove a file|
|rm -i| interactively remove a file|
|mkdir| creates folder|
|rmdir| remove empty directory|

-----------------------------

## Searching Files

### Standard File streams

|Name|Symboblic Name|value|example|
|:----|:----|:----|:----|
|standard input| stdin |0|keyboard|
|standard output| stdout |1|terminal|
|standard error | stderr|2|log file|

### I/O

> intput from file
- $ do_something < input-file  

> output to file
- $ do_something > output-file

> Redirect stderr to a separate file
- $ do_something 2> error-file

> A special shorthand notation can send anything written to file descriptor 2 (stderr) to the same place as file descriptor 1 (stdout): 2>&1.
- $ do_something > all-output-file 2>&1
> bash permits an easier syntax for the above
- $ do_something >& all-output-file

-----------------------------

## Locate, find

### locate
> locate zip | grep bin  
- will list all the files and directories with both zip and bin in their name. We will cover grep in much more detail later. Notice the use of | to pipe the two commands together.

### find
> Searching for files and directories named gcc:
- $ find /usr -name gcc

>Searching only for directories named gcc:
- $ find /usr -type d -name gcc

> Searching only for regular files named gcc:
- $ find /usr -type f -name gcc


---------------------------------

## WildCard

|WildCard|Results|
|:----|:----|
|?| Matches any single character|
|*| matches any string of characters|
|[set]|Matches any character in the set of characters, for example [adf] will match any occurrence of "a", "d", or "f"|
|[!set]|Matches any character not in the set of characters|

-------------------------------------

# Chapter 9

**processes**


A process is simply an instance of one or more related tasks (threads) executing on your computer. It is not the same as a program or a command. A single command may actually start several processes simultaneously. Some processes are independent of each other and others are related. A failure of one process may or may not affect the others running on the system.

Processes use many system resources, such as memory, CPU (central processing unit) cycles, and peripheral devices, such as printers and displays. The operating system (especially the kernel) is responsible for allocating a proper share of these resources to each process and ensuring overall optimized system utilization.


|process type| Description | Example|
|:-----------|:------------|:-------|
|Interactive Processes|Need to be started by a user, either at a command line or through a graphical interface such as an icon or a menu selection. |bash, firefox, top |
|Batch Processes |Automatic processes which are scheduled from and then disconnected from the terminal. These tasks are queued and work on a FIFO (first-in, first-out) basis. |updatedb |
|Daemons |Server processes that run continuously. Many are launched during system startup and then wait for a user or system request indicating that their service is required. |httpd, xinetd, sshd |
|Threads |Lightweight processes. These are tasks that run under the umbrella of a main process, sharing memory and other resources, but are scheduled and run by the system on an individual basis. An individual thread can end without terminating the whole process and a process can create new threads at any time. Many non-trivial programs are multi-threaded. |firefox, gnome-terminal-server |
|Kernel Threads |Kernel tasks that users neither start nor terminate and have little control over. These may perform actions like moving a thread from one CPU to another, or making sure input/output operations to disk are completed. |kthreadd, migration, ksoftirqd |


----------------------------------

## Process Id (PID) and threads

| Id type| Description |
|:------| :------|
| Process ID (PID) |Unique Process ID number |
|Parent Process ID (PPID) |Process (Parent) that started this process. If the parent dies, the PPID will refer to an adoptive parent; on recent kernels, this is kthreadd which has PPID=2. |
|Thread ID (TID) |Thread ID number. This is the same as the PID for single-threaded processes. For a multi-threaded process, each thread shares the same PID, but has a unique TID. |

> Killing a process if PID pid  
 -$ kill -SIGKILL [pid] or kill -9 [pid]

--------------------

 ## User and group ID UID GID

 ![UID GID](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fbe122ffd13edf336ad978cddb953a7f/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch16_screen07.jpg)

 ---------------------------

 ## The ps Command (System V Style)
  >ps  
  >ps -ef -> all processes  
  >ps -eLf => every thread  
  >ps aux =>all users
  >ps axo specify attributes  
  >pstree --> displays processes in a tree form


-------------------------------

## top

>top command is like task manager  
- q to exit  

The **first** **line** displays a quick summary of what is happening in the system, including:

- How long the system has been up
- How many users are logged on
- What is the load average.

The **second** **line** output displays the total number of processes, the number of running, sleeping, stopped, and zombie processes.   

The **third line** output indicates how the CPU time is being divided between the users (us) and the kernel (sy) by displaying the percentage of CPU time used for each.  

The **fourth and fifth lines** of the top output indicate memory usage, which is divided in two categories:

- Physical memory (RAM) – displayed on line 4.
- Swap space – displayed on line 5.


Each line in the process list of the top output displays information about a process. By default,processes are ordered by highest CPU usage.

            Process Identification Number (PID)
            Process owner (USER)
            Priority (PR) and nice values (NI)
            Virtual (VIRT), physical (RES), and shared memory (SHR)
            Status (S)
            Percentage of CPU (%CPU) and memory (%MEM) used
            Execution time (TIME+)
            Command (COMMAND)


| Command | Output |
|:------| :------|
|t |Display or hide summary information (rows 2 and 3)|
|m |Display or hide memory information (rows 4 and 5) |
|A |Sort the process list by top resource consumers |
|r | Renice (change the priority of) a specific processes|
|k | Kill a specific process|
| f|Enter the top configuration screen |
| o|Interactively select a new sort order in the process list |

-------------------

## cron
> scheduling task  


|Field |Description|Values|
|:----|:---------|:-------|
|MIN |Minute  |0 to 59|
|HOUR |Hour field| 0 to 23|
|DOM | Day of the month| 1-31|
|MON| Month of the field| 1-12|
|DOW |Day of the week| 0-6 (0 is Dunday)|
|CMD | command |Command to be executed|

- example:  
>  \* \* \* \* /usr/local/bin/execute/this/script.sh  
woudl execute every mintute of every hour of every day of the month ...

> 30 08 10 06 * /home/sysadmin/full-backup  
will schedule a full-backup at 8.30 a.m., 10-June

----------

## Sleep

**sleep NUMBER[SUFFIX]**...

where SUFFIX may be:

- **s** for seconds (the default)
- **m** for minutes
- **h** for hours
- **d** for days.


# Chapter 10
 **File Operation**

----------

## mounting


The mount command is used to attach a filesystem (which can be local to the computer or, as we shall discuss, on a network) somewhere within the filesystem tree. The basic arguments are the device node and mount point. For example,

> $ sudo mount /dev/sda5 /home

will attach the filesystem contained in the disk partition associated with the /dev/sda5 device node, into the filesystem tree at the /home mount point. There are other ways to specify the partition other than the device node, such as using the disk label or UUID.

To unmount the partition, the command would be:

> $ sudo umount /home

only root users can umount


**NFS??**

-----------------------

## bin and sbin

![executible binaries](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0f4cc85473fc7a961b3bc98b87d33a24/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/lsbin.png)

![sbin](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/f60523278764a748d479ef923f75b0d7/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/lssbin.png)

-----------------------------

## var directory

The **/var** directory contains files that are expected to change in size and content as the system is running (var stands for variable), such as the entries in the following directories:

- System log files: /var/log
- Packages and database files: /var/lib
- Print queues: /var/spool
- Temporary files: /var/tmp.

--------------------------------

## The /etc Directory

The **/etc** directory is the home for system configuration files. It contains no binary programs, although there are some executable scripts. For example, **/etc/resolv.conf** tells the system where to go on the network to obtain host name to IP address mappings (DNS). Files like **passwd**, **shadow** and group for managing user accounts are found in the /etc directory. While some distributions have historically had their own extensive infrastructure under **/etc** (for example, Red Hat and SUSE have used **/etc/sysconfig**), with the advent of systemd there is much more uniformity among distributions today.

Note that **/etc** is for system-wide configuration files and only the superuser can modify files there. User-specific configuration files are always found under their home directory

--------------------------


## External drive (usb or portable)

> /run/media/student/myusbdrive.

|Directory Name|Usage|
|:----|:-----|
|/opt| 	Optional application software packages|
|/sys| 	Virtual pseudo-filesystem giving information about the system and the hardware Can be used to alter system parameters and for debugging purposes|
|/srv| 	Site-specific data served up by the system Seldom used|
|/tmp |	Temporary files; on some distributions erased across a reboot and/or may actually be a ramdisk in memory|
|/usr |	Multi-user applications, utilities and data|
|**dir /usr** | **usage**|
|/usr/include |	Header files used to compile applications|
|/usr/lib 	|Libraries for programs in /usr/bin and /usr/sbin|
|/usr/lib64 	|64-bit libraries for 64-bit programs in /usr/bin and /usr/sbin|
|/usr/sbin| 	Non-essential system binaries, such as system daemons|
|/usr/share| 	Shared data used by applications, generally architecture-independent|
|/usr/src| 	Source code, usually for the Linux kernel|
|/usr/local| 	Data and programs specific to the local machine. Subdirectories include bin, sbin, lib, share, include, etc.|
|/usr/bin| 	This is the primary directory of executable commands on the system|

--------------------------------

## Comparaing directories

> diff [options] [filename1] [filename2]

|diff Option 	|Usage|
|:---------|:--------|
|-c| Provides a listing of differences that include three lines of context before and after the lines differing in content|
|-r| 	Used to recursively compare subdirectories, as well as the current directory|
|-i |	Ignore the case of letters|
|-w |	Ignore differences in spaces and tabs (white space)|
|-q| 	Be quiet: only report if files are different without listing the differences|


> diff3 [f1] [f2] [f3]

>diff -Nur originalfile newfile > patchfile

-------------------------------

## Backing up data

### rsync
 
 > back up project directories:  
- $ rsync -r project-X archive-machine:archives/project-X
- **-dry-run** to endure thhat it provides the right results 

> rsyn [sourcefile] [destinationfile]
- rsync --progress -avrxH  --delete sourcedir destdir

------------------------

## Compressing data

|Command| 	Usage|
|:-----|:------|
|gzip| 	The most frequently used Linux compression utility|
|bzip2| 	Produces files significantly smaller than those produced by gzip|
|xz| 	The most space-efficient compression utility used in Linux|
|zip| 	Is often required to examine and decompress archives from other operating systems|

<br>

### gzip

|Command| 	Usage|
|:----|:----|
|gzip *| 	Compresses all files in the current directory; each file is compressed and renamed with a .gz extension|
|gzip -r projectX| 	Compresses all files in the projectX directory, along with all files in all of the directories under projectX|
|gunzip foo| 	De-compresses foo found in the file foo.gz. Under the hood, the gunzip command is actually the same as gzip –d|

<br>

### bzip2
|Command| 	Usage|
|:----|:----|
|bzip2 *| 	Compresses all of the files in the current directory and replaces each file with a file renamed with a .bz2 extension|
|bunzip2 *.bz2| 	Decompresses all of the files with an extension of .bz2 in the current directory. Under the hood, bunzip2 is the same as calling bzip2 -d|

<br>

### xz
|Command| 	Usage|
|:----|:----|
|$ xz *| 	Compresses all of the files in the current directory and replaces each file with one with a .xz extension|
|xz foo| 	Compresses the file foo into foo.xz using the default compression level (-6), and removes foo if compression succeeds|
|xz -dk bar.xz 	| Decompresses bar.xz into bar and does not remove bar.xz even if decompression is successful|
|xz -dcf a.txt b.txt.xz > abcd.txt 	| Decompresses a mix of compressed and uncompressed files to standard output, using a single command|
|$ xz -d *.xz| 	Decompresses the files compressed using xz|


<br>

### zip

|Command| 	Usage|
|:----|:----|
|zip backup *| 	Compresses all files in the current directory and places them in the file backup.zip|
|zip -r backup.zip ~| 	Archives your login directory (~) and all files and directories under it in the file backup.zip|
|unzip backup.zip| 	Extracts all files in the file backup.zip and places them in the current directory|

<br>

### tar
|Command| 	Usage|
|:----|:----|
|$ tar xvf mydir.tar |	Extract all the files in mydir.tar into the mydir directory|
|$ tar zcvf mydir.tar.gz mydir |	Create the archive and compress with gzip|
|$ tar jcvf mydir.tar.bz2 mydir 	|Create the archive and compress with bz2|
|$ tar Jcvf mydir.tar.xz mydir |	Create the archive and compress with xz|
|$ tar xvf mydir.tar.gz 	|Extract all the files in mydir.tar.gz into the mydir directory <br>**Note**: You do **not** have to tell tar it is in gzip format|

<br>

> dd == disk destroyer

---------------------------

# Chapter 11

## nano


- CTRL-G  
Display the help screen.
- CTRL-O  
Write to a file.
- CTRL-X  
Exit a file.
- CTRL-R  
Insert contents from another file to the current buffer.
- CTRL-C  
Cancels previous commands.

<br>

## vi

>$ vim tutor for tutorial about vim

|Mode| 	Feature|
|:---|:----|
|Command| - By default, vi starts in Command mode. <br> - Each key is an editor command. <br> - Keyboard strokes are interpreted as commands that can modify file contents.|
|Insert |<br>  - Type i to switch to Insert mode from Command mode. <br>  - Insert mode is used to enter (insert) text into a file. <br>  - Insert mode is indicated by an “? INSERT ?” indicator at the bottom of the screen. <br>  - Press Esc to exit Insert mode and return to Command mode.|
|Line 	| <br>  -    Type : to switch to the Line mode from Command mode. Each key is an external command, including operations such as writing the file contents to disk or exiting.  <br>  -   Uses line editing commands inherited from older line editors. Most of these commands are actually no longer used. Some line editing commands are very powerful. <br>  -   Press Esc to exit Line mode and return to Command mode.|

<br>

|Command| 	Usage|
|:----|:----|
|vi myfile |	Start the vi editor and edit the myfile file|
|vi -r myfile |	Start vi and edit myfile in recovery mode from a system crash|
|:r file2 |	Read in file2 and insert at current position|
|:w |	Write to the file|
|:w myfile| 	Write out the file to myfile|
|:w! file2 |	Overwrite file2|
|:x or :wq |	Exit vi and write out modified file|
|:q |	Quit vi|
|:q! |	Quit vi even though modifications have not been saved|

<br>

|Key 	|Usage|
|:---|:---|
|arrow keys| 	To move up, down, left and right|
|j or [ret] |	To move one line down|
|k 	|To move one line up|
|h or Backspace |	To move one character left|
|l or Space |	To move one character right|
|0 |	To move to beginning of line|
|$ |	To move to end of line|
|w |	To move to beginning of next word|
|:0 or 1G |	To move to beginning of file|
|:n or nG |	To move to line n|
|:$ or G |	To move to last line in file|
|CTRL-F or Page Down 	|To move forward one page|
|CTRL-B or Page Up 	|To move backward one page|
|^l |	To refresh and center screen|

<br>

**search**

|Command| 	Usage|
|:----|:----|
|/pattern 	|Search forward for pattern|
|?pattern| 	Search backward for pattern|

|Key 	|Usage|
|:---|:---|
|n |	Move to next occurrence of search pattern|
|N| 	Move to previous occurrence of search pattern|

<br>

**keystrokes used when changing, adding, and deleting text**

|Key 	|Usage|
|:---|:---|
|a| 	Append text after cursor; stop upon Escape key|
|A |	Append text at end of current line; stop upon Escape key|
|i| 	Insert text before cursor; stop upon Escape key|
|I| 	Insert text at beginning of current line; stop upon Escape key|
|o| 	Start a new line below current line, insert text there; stop upon Escape key|
|O |	Start a new line above current line, insert text there; stop upon Escape key|
|r |	Replace character at current position|
|R |	Replace text starting with current position; stop upon Escape key|
|x |	Delete character at current position|
|Nx 	|Delete N characters, starting at current position|
|dw |	Delete the word at the current position|
|D |	Delete the rest of the current line|
|dd |	Delete the current line|
|Ndd or dNd |	Delete N lines|
|u |	Undo the previous operation|
|yy |	Yank (copy) the current line and put it in buffer|
|Nyy or yNy |	Yank (copy) N lines and put it in buffer|
|p |	Paste at the current position the yanked line or lines from the buffer.|

<br>

### emacs

|Key 	|Usage|
|:---|:---|
|emacs myfile |	Start emacs and edit myfile|
|CTRL-x i 	|Insert prompted for file at current position|
|CTRL-x s 	|Save all files|
|CTRL-x CTRL-w	|Write to the file giving a new name when prompted|
|CTRL-x CTRL-s 	|Saves the current file |
|CTRL-x CTRL-c |	Exit after being prompted to save any modified files|

<br>

|Key 	|Usage|
|:---|:---|
|arrow keys |	Use the arrow keys for up, down, left and right|
|CTRL-n |	One line down|
|CTRL-p 	|One line up|
|CTRL-f 	|One character forward/right|
|CTRL-b 	|One character back/left|
|CTRL-a 	|Move to beginning of line|
|CTRL-e 	|Move to end of line|
|Meta-f 	|Move to beginning of next word|
|Meta-b 	|Move back to beginning of preceding word|
|Meta-< 	|Move to beginning of file|
|Meta-g-g-n| 	Move to line n (can also use 'Esc-x Goto-line n')|
|Meta-> 	|Move to end of file|
|CTRL-v or Page Down| 	Move forward one page|
|Meta-v or Page Up 	|Move backward one page|
|CTRL-l| 	Refresh and center screen|

> **search**

|Key 	|Usage|
|:---|:---|
|CTRL-s |	Search forward for prompted pattern, or for next pattern|
|CTRL-r |	Search backwards for prompted pattern, or for next pattern|

> **working with emacs**

|Key 	|Usage|
|:---|:---|
|CTRL-o |	Insert a blank line|
|CTRL-d |	Delete character at current position|
|CTRL-k |	Delete the rest of the current line|
|CTRL-_ |	Undo the previous operation|
|CTRL- (space or CTRL-@)| 	Mark the beginning of the selected region. The end will be at the cursor position|
|CTRL-w |	Delete the current marked text and write it to the buffer|
|CTRL-y| 	Insert at current cursor location whatever was most recently deleted|


-------------------------


# Chapter 12

> whoami  
> who 

**Creating Aliases**

You can create customized commands or modify the behavior of already existing ones by creating aliases. Most often, these aliases are placed in your **~/.bashrc** file so they are available to any command shells you create. unalias removes an alias.

Typing alias with no arguments will list currently defined aliases.

Please note there should not be any spaces on either side of the equal sign and the alias definition needs to be placed within either single or double quotes if it contains any spaces.

![alias example](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/97491d062822787b87a74f33ea868847/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/aliassuse.png)

-----------------

## Adding and Removing Users & Groups

Distributions have straightforward graphical interfaces for creating and removing users and groups and manipulating group membership. However, it is often useful to do it from the command line or from within shell scripts. Only the root user can add and remove users and groups.

Adding a new user is done with useradd and removing an existing user is done with **userdel**. In the simplest form, an account for the new user **bjmoose** would be done with:

> $ sudo useradd bjmoose

Note that for openSUSE, **useradd** is not in the normal user's PATH, so the command should be:

> $ sudo /usr/sbin/useradd bjmoose

which, by default, sets the home directory to **/home/bjmoose**, populates it with some basic files (copied from /etc/skel) and adds a line to **/etc/passwd** such as:

**bjmoose:x:1002:1002::/home/bjmoose:/bin/bash**

and sets the default shell to **/bin/bash**. Removing a user account is as easy as typing **userdel bjmoose**. However, this will leave the **/home/bjmoose** directory intact. This might be useful if it is a temporary inactivation. To remove the home directory while removing the account one needs to use the **-r** option to **userdel**.

Typing id with no argument gives information about the current user, as in:

> $ id  
uid=1002(bjmoose) gid=1002(bjmoose) groups=106(fuse),1002(bjmoose)

If given the name of another user as an argument, id will report information about that other user.

<br>

Adding a new group is done with **groupadd**:

> $ sudo /usr/sbin/groupadd anewgroup

The group can be removed with:

> $ sudo /usr/sbin/groupdel anewgroup

Adding a user to an already existing group is done with **usermod**. For example, you would first look at what groups the user already belongs to:

>$ groups rjsquirrel  
bjmoose : rjsquirrel

and then add the new group:

> $ sudo /usr/sbin/usermod -a -G anewgroup rjsquirrel

> $ groups rjsquirrel  
rjsquirrel: rjsquirrel anewgroup

These utilities update **/etc/group** as necessary. Make sure to use the **-a** option, for append, so as to avoid removing already existing groups. **groupmod** can be used to change group properties, such as the Group ID (gid) with the **-g** option or its name with then **-n** option.

Removing a user from the group is somewhat trickier. The -G option to usermod must give a complete list of groups. Thus, if you do:

>$ sudo /usr/sbin/usermod -G rjsquirrel rjsquirrel

>$ groups rjsquirrel  
rjsquirrel : rjsquirrel

only the _rjsquirrel_ group will be left.

-------------------------

|Task|Command|
|:---|:----|
|Show the value of a specific variable| 	echo $SHELL|
|Export a new variable value| 	export VARIABLE=value (or VARIABLE=value; export VARIABLE)|
|Add a variable permanently | 1- Edit ~/.bashrc and add the line export VARIABLE=value <br>2- Type source ~/.bashrc or just . ~/.bashrc (dot ~/.bashrc); or just start a new shell by typing  bash|


## History

Several associated environment variables can be used to get information about the history file. 

- _HISTFILE_  
The location of the history file. 
- _HISTFILESIZE_  
The maximum number of lines in the history file (default 500). 
- _HISTSIZE_  
The maximum number of commands in the history file. 
- _HISTCONTROL_  
How commands are stored. 
- _HISTIGNORE_  
Which command lines can be unsaved.

For a complete description of the use of these environment variables, see man bash.


|Key |	Usage|
|:----|:----|
|Up/Down arrow keys |	Browse through the list of commands previously executed|
|!! (Pronounced as bang-bang) |	Execute the previous command|
|CTRL-R |	Search previously used commands|
|**Syntax----------**|**Task----------**|
|! 	|Start a history substitution|
|!$ 	|Refer to the last argument in a line|
|!n |	Refer to the nth command line|
|!string 	|Refer to the most recent command starting with string|

<br>

>example  

$ history

1. echo $SHELL
2. echo $HOME
3. echo $PS1
4. ls -a
5. ls -l /etc/ passwd
6. sleep 1000
6. history

$ !1   (Execute command #1 above)
echo $SHELL
/bin/bash
$ !sl   (Execute the command beginning with "sl")
sleep 1000
$

-------------------------------------

## Command line shortcuts

|Keyboard Shortcut |	Task|
|:----|:----|
|CTRL-L 	|Clears the screen|
|CTRL-D 	|Exits the current shell|
|CTRL-Z 	|Puts the current process into suspended background|
|CTRL-C 	|Kills the current process|
|CTRL-H 	|Works the same as backspace|
|CTRL-A 	|Goes to the beginning of the line|
|CTRL-W 	|Deletes the word before the cursor|
|CTRL-U 	|Deletes from beginning of line to cursor position|
|CTRL-E 	|Goes to the end of the line|
|Tab 	|Auto-completes files, directories, and binaries|

----------------------------------------------------

## File Permission

>Files have three kinds of permissions: read (r), write (w), execute (x). These are generally represented as in rwx. These permissions affect three groups of owners: user/owner (u), group (g), and others (o).

|user|group|others|
|:---:|:----:|:----:|
|rwx:| rwx: |rwx|  
| u:   |g:   |o|

<br>


- **4 if read permission is desired**
- **2 if write permission is desired**
- **1 if execute permission is desired.**

>**Thus, 7 means read/write/execute, 6 means read/write, and 5 means read/execute.**

<br>

|COmmand |	Shortcut|
|:----|:----|
|chown 	|Used to change user ownership of a file or directory|
|chgrp 	|Used to change group ownership|
|chmod |	Used to change the permissions on the file, which can be done separately for owner, group and the rest of the world (often named as other)|

>example:  

```
$ ls -l somefile  
  -rw-rw-r-- 1 student student 1601 Mar 9 15:04 somefile
$ chmod uo+x,g-w somefile
$ ls -l somefile  
  -rwxr--r-x 1 student student 1601 Mar 9 15:04 somefile
```

```
$ chmod 755 somefile
$ ls -l somefile
-rwxr-xr-x 1 student student 1601 Mar 9 15:04 somefile
```

--------------------

# Chapter 13

## Manipulating files

### Cat (or to Concatenate)

> $ cat [filename]  
- displays content of file

<br>

> $ tac   
-  print or writes the lines of the file in reverse

<br>

> \>\>  
- appends lines (or files) to an existing file.

<br>

|Command 	|Usage|
|:------|:----|
|cat file1 file2 |	Concatenate multiple files and display the output; i.e. the entire content of the ||first file is followed by that of the second file|
|cat file1 file2 > newfile |	Combine multiple files and save the output into a new file|
|cat file >> existingfile |	Append a file to the end of an existing file|
|cat > file |	Any subsequent lines typed will go into the file, until CTRL-D is typed|
|cat >> file |	Any subsequent lines are appended to the file, until CTRL-D is typed|

<br>

> cat > [filename] << EOF.  
- creates new file, enter input. to finish type **EOF**



### Working with larger files

> $ less [somefile]  
$ cat [somefile] | less  
head –n 5 [somfile] -> firts five lines  
$ tail -n 15 [somefile] -> last 15 lines  
$ tail -f [somefile] -> montior growing file 


### Viewing compress files

|Command 	|Desctiption|
|:------|:----|
|$ zcat compressed-file.txt.gz| 	To view a compressed file|
$ zless somefile.gz <br> or <br>$ zmore somefile.gz |	To page through a compressed file|
|$ zgrep -i less somefile.gz| 	To search inside a compressed file|
|$ zdiff file1.txt.gz file2.txt.gz| 	To compare two compressed files|

------------------------

## sed and awk

### sed
>String maniputlaiton in a file


|Command 	|Usage|
|:---|:---|
|sed s/pattern/replace_string/ file 	|Substitute first string occurrence in every line|
|sed s/pattern/replace_string/g file 	|Substitute all string occurrences in every line|
|sed 1,3s/pattern/replace_string/g file| 	Substitute all string occurrences in a range of lines|
|sed -i s/pattern/replace_string/g file| 	Save changes for string substitution in the same file|

<br>

> example
```
sed -e 's/01/JAN/' -e 's/02/FEB/' -e 's/03/MAR/' -e 's/04/APR/' -e 's/05/MAY/' \
    -e 's/06/JUN/' -e 's/07/JUL/' -e 's/08/AUG/' -e 's/09/SEP/' -e 's/10/OCT/' \
    -e 's/11/NOV/' -e 's/12/DEC/'
```

------------------------------

### awk

awk has the following features:

- It is a powerful utility and interpreted programming language.
- It is used to manipulate data files, retrieving, and processing text.
- It works well with fields (containing a single piece of data, essentially a column) and records (a collection of fields, essentially a line in a file).

<br>

|Command 	|Usage|
|:---|:---|
|awk ‘command’  file 	|Specify a command directly at the command line|
|awk -f scriptfile file 	|Specify a file that contains the script to be executed|
|-----|-----|
|awk '{ print $0 }' /etc/passwd |	Print entire file|
|awk -F: '{ print $1 }' /etc/passwd 	|Print first field (column) of every line, separated by a |space
|awk -F: '{ print $1 $7 }' /etc/passwd |	Print first and seventh field of every line|

--------------------------------

## File Manipulation Utilities

### sort

|Syntax |	Usage|
|:---|:----|
|sort \<filename> |	Sort the lines in the specified file, according to the characters at the beginning of each line| 
|cat file1 file2 \| sort |	Combine the two files, then sort the lines and display the output on the terminal|
|sort -r \<filename>| 	Sort the lines in reverse order|
|sort -k 3 \<filename> 	|Sort the lines by the 3rd field on each line instead of the beginning|

> **-u** or **uniq** to check unique values. Removes duplicates
- sort file1 file2 | uniq > file3
- sort file | uniq
- sort -u file1 file2 > file3
- uniq -c filename -> to count the number of duplicate entires

-----------------------

### paste

> paste can create a new file with all colunm from the old files

![paste example](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/0c746d1cc41ea999719d5cdad330d97b/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch12_screen27.jpg)
![paste example](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/da3d180e87ba8b70a3312fca74ecf815/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch12_screen30.jpg)


paste accepts the following options:

1. **-d** delimiters, which specify a list of delimiters to be used instead of tabs for separating consecutive values on a single line.   
Each delimiter is used in turn; when the list has been exhausted, paste begins again at the first delimiter.
2. **-s**, which causes paste to append the data in series rather than in parallel; that is, in a horizontal rather than vertical fashion

--------------------

### join

> enhanced version of pastes

> First checks if files share common fields and joins them without duplicate

----------------------

### split

> **split** is used to break up (or split) a file into equal-sized segments for easier viewing and manipulation, and is generally used only on relatively large files

> default is 1000 lines. Original file unchanged

- example :   

```
We will apply split to an American-English dictionary file of over 99,000 lines:

> $ wc -l american-english
99171 american-english

where we have used wc (word count, soon to be discussed) to report on the number of lines in the file. Then, typing:

> $ split american-english dictionary

will split the American-English file into 100 equal-sized segments named 'dictionaryxx. The last one will of course be somewhat smaller.
```

-----------------

## grep

> grep  scans files for specified patterns and can be used with regular expressions, as well as simple strings, as shown in the table:

|Command| 	Usage|
|:----|:-----|
|grep [pattern] \<filename>| 	Search for a pattern in a file and print all matching lines|
|grep -v [pattern] \<filename> |	Print all lines that do not match the pattern|
|grep [0-9] \<filename> 	|Print the lines that contain the numbers 0 through 9|
|grep -C 3 [pattern] \<filename> |	Print context of lines (specified number of lines above and below the pattern) for matching the pattern. Here, the number of lines is specified as 3|

-----------------------------------


## tr

> The tr utility is used to translate specified characters into other characters or to delete them. The general syntax is as follows:

> $ tr [options] set1 [set2]

> cat file | tr [options] set1 [set2]

|Command 	|Usage|
|:----|:----|
|$ tr a-z A-Z	|Convert lower case to upper case|
|$ tr '{}' '()' < inputfile > outputfile 	|Translate braces into parenthesis|
|$ echo "This is for testing" \| tr [:space:] '\t' |	Translate white-space to tabs|
|$ echo "This   is   for    testing" \| tr -s [:space:]| Squeeze repetition of characters using -s|
|$ echo "the geek stuff" \| tr -d 't' |	Delete specified characters using -d option|
|$ echo "my username is 432234" \| tr -cd [:digit:]| 	Complement the sets using -c option|
|$ tr -cd [:print:] < file.txt |	Remove all non-printable character from a file|
|$ tr -s '\n' ' ' < file.txt |	Join all the lines in a file into a single line|

---------------------------------------

## wordcount

>print number words:  wc file  or wc -w filename  
>print number of lines:  wc -f filename   
>print number of bytes: wc -c filename   

---------------------

# Chapter 14

TODO: summurize these paragraphs

----------------------

## Networking 

A network is a group of computers and computing devices connected together through communication channels, such as cables or wireless media. The computers connected over a network may be located in the same geographical area or spread across the world.

A network is used to:

- Allow the connected devices to communicate with each other
- Enable multiple users to share devices over the network, such as printers and scanners
- Share and manage information across computers easily.

Most organizations have both an internal network and an Internet connection for users to communicate with machines and people outside the organization. The Internet is the largest network in the world and can be called "the network of networks".

------------------------

### IP address

Devices attached to a network must have at least one unique network address identifier known as the IP (Internet Protocol) address. The address is essential for routing packets of information through the network.

Exchanging information across the network requires using streams of small packets, each of which contains a piece of the information going from one machine to another. These packets contain data buffers together with headers which contain information about where the packet is going to and coming from, and where it fits in the sequence of packets that constitute the stream. Networking protocols and software are rather complicated due to the diversity of machines and operating systems they must deal with, as well as the fact that even very old standards must be supported.

------------------

### IPv4 vs IPv6

There are two different types of IP addresses available: IPv4 (version 4) and IPv6 (version 6). IPv4 is older and by far the more widely used, while IPv6 is newer and is designed to get past limitations inherent in the older standard and furnish many more possible addresses.

IPv4 uses 32-bits for addresses; there are only 4.3 billion unique addresses available. Furthermore, many addresses are allotted and reserved, but not actually used. IPv4 is considered inadequate for meeting future needs because the number of devices available on the global network has increased enormously in recent years.

IPv6 uses 128-bits for addresses; this allows for 3.4 X 1038 unique addresses. If you have a larger network of computers and want to add more, you may want to move to IPv6, because it provides more unique addresses. However, it can be complex to migrate to IPv6; the two protocols do not always inter-operate well. Thus, moving equipment and addresses to IPv6 requires significant effort and has not been quite as fast as was originally intended. We will discuss IPv4 more than IPv6 as you are more likely to deal with it.

One reason IPv4 has not disappeared is there are ways to effectively make many more addresses available by methods such as NAT (Network Address Translation).  NAT enables sharing one IP address among many locally connected computers, each of which has a unique address only seen on the local network. While this is used in organizational settings, it also used in simple home networks. For example, if you have a router hooked up to your Internet Provider (such as a cable system) it gives you one externally visible address, but issues each device in your home an individual local address.

ipv4 -> 32-bits -> 4.3b unique addresses
ipv6 -> 128-bits -> 3.4e38 unique addresses

---------------------------------

#### decoding IPv4

A 32-bit IPv4 address is divided into four 8-bit sections called octets.

Example:  
IP address →   172  .   16  .   31  .     46  
Bit format → 10101100.00010000.00011111.00101110

Note: Octet is just another word for byte.

Network addresses are divided into five classes: A, B, C, D and E. Classes A, B and C are classified into two parts: Network addresses (Net ID) and Host address (Host ID). The Net ID is used to identify the network, while the Host ID is used to identify a host in the network. Class D is used for special multicast applications (information is broadcast to multiple computers simultaneously) and Class E is reserved for future use. In this section you will learn about classes A, B and C.

----------------------------------

##### Class A

Class A addresses use the first octet of an IP address as their Net ID and use the other three octets as the Host ID. The first bit of the first octet is always set to zero. So you can use only 7-bits for unique network numbers. As a result, there are a maximum of 126 Class A networks available (the addresses 0000000 and 1111111 are reserved). Not surprisingly, this was only feasible when there were very few unique networks with large numbers of hosts. As the use of the Internet expanded, Classes B and C were added in order to accommodate the growing demand for independent networks.

Each Class A network can have up to 16.7 million unique hosts on its network. The range of host address is from 1.0.0.0 to 127.255.255.255.

Note: The value of an octet, or 8-bits, can range from 0 to 255. 


![class A address](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/1867a1e02d2827251e50b65a03bcaa1b/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch11_screen07.jpg)

----------------------------

##### Class B

Class B addresses use the first two octets of the IP address as their Net ID and the last two octets as the Host ID. The first two bits of the first octet are always set to binary 10, so there are a maximum of 16,384 (14-bits) Class B networks. The first octet of a Class B address has values from 128 to 191. The introduction of Class B networks expanded the number of networks but it soon became clear that a further level would be needed.

Each Class B network can support a maximum of 65,536 unique hosts on its network. The range of host address is from 128.0.0.0 to 191.255.255.255

![Class B Adress](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/7e40d0c228a2ac28dd4e1e9af18ba3ce/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch11_screen08.jpg)

----------------------------

##### Class C

Class C addresses use the first three octets of the IP address as their Net ID and the last octet as their Host ID. The first three bits of the first octet are set to binary 110, so almost 2.1 million (21-bits) Class C networks are available. The first octet of a Class C address has values from 192 to 223. These are most common for smaller networks which don't have many unique hosts.

Each Class C network can support up to 256 (8-bits) unique hosts. The range of host address is from 192.0.0.0 to 223.255.255.255.

![class C Address](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/376a6fe8144e0d5799f331a803e1d33d/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch11_screen09.jpg)

----------------------------

### IP Address Allocation


Typically, a range of IP addresses are requested from your Internet Service Provider (ISP) by your organization's network administrator. Often, your choice of which class of IP address you are given depends on the size of your network and expected growth needs. If NAT is in operation, such as in a home network, you only get one externally visible address!

You can assign IP addresses to computers over a network either manually or dynamically. Manual assignment adds static (never changing) addresses to the network. Dynamically assigned addresses can change every time you reboot or even more often; the Dynamic Host Configuration Protocol (DHCP) is used to assign IP addresses.

------------------------

### Name Resolution

Name Resolution is used to convert numerical IP address values into a human-readable format known as the hostname. For example, 104.95.85.15 is the numerical IP address that refers to the hostname whitehouse.gov. Hostnames are much easier to remember!

Given an IP address, you can obtain its corresponding hostname. Accessing the machine over the network becomes easier when you can type the hostname instead of the IP address.

You can view your system’s hostname simply by typing hostname with no argument.

Note: If you give an argument, the system will try to change its hostname to match it, however, only root users can do that.

The special hostname localhost is associated with the IP address 127.0.0.1, and describes the machine you are currently on (which normally has additional network-related IP addresses).

-----------------------

## Network Configuration Files

Network configuration files are essential to ensure that interfaces function correctly. They are located in the /etc directory tree. However, the exact files used have historically been dependent on the particular Linux distribution and version being used.

For Debian family configurations, the basic network configuration files could be found under /etc/network/, while for Fedora and SUSE family systems one needed to inspect /etc/sysconfig/network. 

Modern systems emphasize the use of Network Manager, which we briefly discussed when we considered graphical system administration, rather than try to keep up with the vagaries of the files in /etc. While the graphical versions of Network Manager do look somewhat different in different distributions, the nmtui utility (shown in the screenshot) varies almost not at all, as does the even more sparse nmcli (command line interface) utility. If you are proficient in the use of the GUIs, by all means, use them. If you are working on a variety of systems, the lower level utilities may make life easier.

-----------------------

### Network Interface

Network interfaces are a connection channel between a device and a network. Physically, network interfaces can proceed through a network interface card (NIC), or can be more abstractly implemented as software. You can have multiple network interfaces operating at once. Specific interfaces can be brought up (activated) or brought down (de-activated) at any time.

Information about a particular network interface or all network interfaces can be reported by the ip and ifconfig utilities, which you may have to run as the superuser, or at least, give the full path, i.e. /sbin/ifconfig, on some distributions. ip is newer than ifconfig  and has far more capabilities, but its output is uglier to the human eye. Some new Linux distributions do not install the older net-tools package to which ifconfig belongs, and  so you would have to install it if you want to use it.

------------------------

### IP utility

To view the IP address:
>$ /sbin/ip addr show


To view the routing information:
>$ /sbin/ip route show

ip is a very powerful program that can do many things. Older (and more specific) utilities such as ifconfig and route are often used to accomplish similar tasks. A look at the relevant man pages can tell you much more about these utilities.

---------------

### ping

_ping_ is used to check whether or not a machine attached to the network can receive and send data; i.e. it confirms that the remote host is online and is responding.

To check the status of the remote host, at the command prompt, type _ping_ \<hostname>.

_ping_ is frequently used for network testing and management; however, its usage can increase network load unacceptably. Hence, you can abort the execution of _ping_ by typing CTRL-C, or by using the -c option, which limits the number of packets that _ping_ will send before it quits. When execution stops, a summary is displayed.

---------------------

### route

A network requires the connection of many nodes. Data moves from source to destination by passing through a series of routers and potentially across multiple networks. Servers maintain routing tables containing the addresses of each node in the network. The IP routing protocols enable routers to build up a forwarding table that correlates final destinations with the next hop addresses.

One can use the route utility or the newer ip route command to view or change the IP routing table to add, delete, or modify specific (static) routes to specific hosts or networks. The table explains some commands that can be used to manage IP routing:

|Task|Command|
|:----|:----|
|Show current routing table|$ route -n _or_ ip route|
|add statid route|$ route add -net address _or_ ip route add|
|Delete static route|$ route del -net address _or_ ip route del|

---------------

### traceroute

traceroute is used to inspect the route which the data packet takes to reach the destination host, which makes it quite useful for troubleshooting network delays and errors. By using traceroute, you can isolate connectivity issues between hops, which helps resolve them faster.

To print the route taken by the packet to reach the network host, at the command prompt, type traceroute \<address>.

------------------------

### More Networking tool

|Networking Tools|Description|
|:-------|:----------|
|ethtool |	Queries network interfaces and can also set various parameters such as the speed|
|netstat 	|Displays all active connections and routing tables. Useful for monitoring |performance and troubleshooting|
|nmap |	Scans open ports on a network. Important for security analysis|
|tcpdump |	Dumps network traffic for analysis|
|iptraf |	Monitors network traffic in text mode|
|mtr |	Combines functionality of ping and traceroute and gives a continuously updated display|
|dig |	Tests DNS workings. A good replacement for host and nslookup|

----------------

## Internet Browsers

The common graphical browsers used in Linux are:

- Firefox
- Google Chrome
- Chromium
- Konqueror
- Opera.

|Non-Graphical Browsers |	Description|
|:----|:------|
|Lynx|	Configurable text-based web browser; the earliest such browser and still in use|
|ELinks|	Based on Lynx. It can display tables and frames|
|w3m|	Another text-based web browser with many features|

-------------------

### wget

Sometimes, you need to download files and information, but a browser is not the best choice, either because you want to download multiple files and/or directories, or you want to perform the action from a command line or a script. wget is a command line utility that can capably handle the following types of downloads:

- Large file downloads  
- Recursive downloads, where a web page refers to other web pages and all are downloaded at once  
- Password-required downloads  
- Multiple file downloads.  

To download a web page, you can simply type wget \<url>, and then you can read the downloaded page as a local file using a graphical or non-graphical browser.

-----------------

### curl

Besides downloading, you may want to obtain information about a URL, such as the source code being used. curl can be used from the command line or a script to read such information. curl also allows you to save the contents of a web page to a file, as does wget.

You can read a URL using curl <URL>. For example, if you want to read http://www.linuxfoundation.org, type curl http://www.linuxfoundation.org.

To get the contents of a web page and store it to a file, type curl -o saved.html http://www.mysite.com. The contents of the main index file at the website will be saved in saved.html.

----------------------------

## FTP 

### File Transfer Protocol

When you are connected to a network, you may need to transfer files from one machine to another. File Transfer Protocol (FTP) is a well-known and popular method for transferring files between computers using the Internet. This method is built on a client-server model. FTP can be used within a browser or with stand-alone client programs.  

FTP is one of the oldest methods of network data transfer, dating back to the early 1970s. As such, it is considered inadequate for modern needs, as well as being intrinsically insecure. However, it is still in use and when security is not a concern (such as with so-called anonymous FTP) it can make sense. However, many websites, such as kernel.org, have abandoned its use.

----------------

### FTP Clients

FTP clients enable you to transfer files with remote computers using the FTP protocol. These clients can be either graphical or command line tools. Filezilla, for example, allows use of the drag-and-drop approach to transfer files between hosts. All web browsers support FTP, all you have to do is give a URL like ftp://ftp.kernel.org where the usual http:// becomes ftp://.

Some command line FTP clients are:

- ftp
- sftp
- ncftp
- yafc (Yet Another FTP Client).

FTP has fallen into disfavor on modern systems, as it is intrinsically insecure, since passwords are user credentials that can be transmitted without encryption and are thus prone to interception. Thus, it was removed in favor of using rsync and web browser https access for example. As an alternative, sftp is a very secure mode of connection, which uses the Secure Shell (ssh) protocol, which we will discuss shortly. sftp encrypts its data and thus sensitive information is transmitted more securely. However, it does not work with so-called anonymous FTP (guest user credentials).

--------------------

## SSH

> ip --brief addr show

### Executing Commands Remotely

Secure Shell (SSH) is a cryptographic network protocol used for secure data communication. It is also used for remote services and other secure services between two devices on the network and is very useful for administering systems which are not easily available to physically work on, but to which you have remote access.

To login to a remote system using your same user name you can just type ssh some_system and press Enter. ssh then prompts you for the remote password. You can also configure ssh to securely allow your remote access without typing a password each time.

If you want to run as another user, you can do either ssh -l someone some_system or ssh someone@some_system. To run a command on a remote system via SSH, at the command prompt, you can type ssh some_system my_command.

---------------

### Copying Files Securely with scp

We can also move files securely using Secure Copy (scp) between two networked hosts. scp uses the SSH protocol for transferring data.

To copy a local file to a remote system, at the command prompt, type scp \<localfile> \<user@remotesystem>:/home/user/ and press Enter.

You will receive a prompt for the remote password. You can also configure scp so that it does not prompt for a password for each transfer.

--------------------------

# Chapter 15

**Shell Scripting**

## Command Shell Choices

The command interpreter is tasked with executing statements that follow it in the script. Commonly used interpreters include:
- /usr/bin/perl
- /bin/bash
- /bin/csh-
- /usr/bin/python
- /bin/sh.

Wide choices of shells in **/etc/shells**:

- /bin/sh
- /bin/bash
- /bin/tcsh
- /bin/csh
- /bin/ksh
- /bin/zsh

default: bash shell

--------------

## Shell scripts

\#!/bin/bash  
find . -name "*.c" -ls

The #!/bin/bash in the first line should be recognized by anyone who has developed any kind of script in UNIX environments. The first line of the script, that starts with #!, contains the full path of the command interpreter (in this case /bin/bash) that is to be used on the file. As we have noted, you have quite a few choices for the scripting language you can use, such as /usr/bin/perl, /bin/csh, /usr/bin/python, etc.

-------------------

## Simple Bash Script

Displays a one line message on the screen. Either type:

>$ cat > hello.sh  
  \#!/bin/bash  
  echo "Hello Linux Foundation Student"

and press ENTER and CTRL-D to save the file, or just create hello.sh in your favorite text editor. Then, type chmod +x hello.sh to make the file executable by all users.

You can then run the script by typing ./hello.sh or by doing:

>$ bash hello.sh  
  Hello Linux Foundation Student

**Note**: If you use the second form, you do not have to make the file executable.

---------------

## Interactive Example Using bash Scripts

The user will be prompted to enter a value, which is then displayed on the screen. The value is stored in a temporary variable, name. We can reference the value of a shell variable by using a $ in front of the variable name, such as $name. To create this script, you need to create a file named getname.sh in your favorite editor with the following content: 

>\#!/bin/bash  
\# Interactive reading of a variable  
echo "ENTER YOUR NAME"  
read name  
\# Display variable input  
echo The name given was :$name

Once again, make it executable by doing **chmod +x getname.sh**.

In the above example, when the user types ./getname.sh and the script is executed, the user is prompted with the string  ENTER YOUR NAME. The user then needs to enter a value and press the Enter key. The value will then be printed out.

**Note**: The hash-tag/pound-sign/number-sign (#) is used to start comments in the script and can be placed anywhere in the line (the rest of the line is considered a comment). However, note the special magic combination of #!, used on the first line, is a unique exception to this rule.

---------------------


## Viewing Return Values

As a script executes, one can check for a specific value or condition and return success or failure as the result.   
Success: 0  
Failure: non-zero

example:  

>$ ls /etc/logrotate.conf  
/etc/logrotate.conf  
>
>$ echo $?  
0

In this example, the system is able to locate the file /etc/logrotate.conf and ls returns a value of 0 to indicate success. When run on an non-existing file, it returns 2. Applications often translate these return values into meaningful messages easily understood by the user.

--------------------

## Syntax and Special Characters


|Character| 	Description|
|:---|:-----|
|\#| 	Used to add a comment, except when used as \#, or as #! when starting a script|
|\\| 	Used at the end of a line to indicate continuation on to the next line|
|;| 	Used to interpret what follows as a new command to be executed next|
|$| 	Indicates what follows is an environment variable|
|>| 	Redirect output|
|>>| 	Append output|
|<| 	Redirect input|
|\|| 	Used to pipe the result into the next command|


>Other special characters and character combinations and constructs that scripts understand, such as:
- (..)
- {..}
- [..]
- &&
- ||
- '
- "
- $((...))

----------------------------


### Splitting Long Commands Over Multiple Lines

>\

example:  
>$~/> cd $HOME  
$~/> sudo apt-get install autoconf automake bison build-essential  
    chrpath curl diffstat emacs flex gcc-multilib g++-multilib \   
    libsdl1.2-dev libtool lzop make mc patch \  
    screen socat sudo tar texinfo tofrodos u-boot-tools unzip \  
    vim wget xterm zip   

It's all one command split for better understanding

------------------------

### Putting Multiple Commands on a Single Line

three commands in the following example will all execute, even if the ones preceding them fail:

>$ make ; make install ; make clean

<br>

However, you may want to abort subsequent commands when an earlier one fails. You can do this using the && (and) operator as in:

>$ make && make install && make clean

<br>

If the first command fails, the second one will never be executed. A final refinement is to use the || (or) operator, as in:

>$ cat file1 || cat file2 || cat file3

In this case, you proceed until something succeeds and then you stop executing any further steps.

------------------------

### Input/Output Redirection

 to output to file: > 
> $ free > /tmp/free.out

to append to a file: >>

<br>

to input from file: <
>$ wc < /etc/passwd  
49  105 2678 /etc/passwd  
>  
>$ wc /etc/passwd  
49  105 2678 /etcpasswd  
>
>$ cat /etc/passwd | wc
49  105 2678


--------------------

### Built-In Shell Commands

Shell scripts execute sequences of commands and other types of statements. These commands can be: 

- Compiled applications. ex: rm, ls, vi ...
- Built-in bash commands. ex: cd, echo, pwd ...
- Shell scripts or scripts from other interpreted languages, such as perl and Python.

> $ help

|Compiled applications|build in bash commands|other scripts|
|:-----|:----:|------:|
|rm|cd||
|ls|pwd||
|df|echo||
|vi|read||
|gzip|logout||
||printf||
||let||
||ulimit||

<br>

![helpbash](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/79040611925a7890d2337fb896445e08/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/helpbash.png)

----------------------------


### Script parameters

|Parameter| 	Meaning|
|:-------|:---------|
|$0| 	Script name|
|$1| 	First parameter|
|$2, $3, etc.| 	Second, third parameter, etc.|
|$* |	All parameters|
|$# |	Number of arguments|

-------------------------

>Example

![example paramteres](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a7d08ff7b0604bb8bd5d324cc162d17f/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/scriptparams.png)

- $0 prints the script name: param.sh
- $1 prints the first parameter: one
- $2 prints the second parameter: two
- $3 prints the third parameter: three
- $* prints all parameters: one two three four five
- The final statement becomes: All done with param.sh


------------------------------
### Command Substitution

To substitute the result of a command as a portion of another command can be done in two ways:

- By enclosing the inner command in $( )
- By enclosing the inner command with backticks (`)

>  $ ls /lib/modules/$(uname -r)/

-----------------

### Environment Variables

Most scripts use variables containing a value, which can be used anywhere in the script. These variables can either be user or system-defined. Many applications use such environment variables (already covered in some detail in Chapter 12: User Environment) for supplying inputs, validation, and controlling behavior.

As we discussed earlier,  some examples of standard environment variables are HOME, PATH, and HOST. When referenced, environment variables must be prefixed with the $ symbol, as in $HOME. You can view and set the value of environment variables. For example, the following command displays the value stored in the PATH variable:

>$ echo $PATH

However, no prefix is required when setting or modifying the variable value. For example, the following command sets the value of the MYCOLOR variable to blue:

>$ MYCOLOR=blue

You can get a list of environment variables with the env, set, or printenv commands.

### Exporting Environment Variables

While we discussed the export of environment variables in the section on the "User Environment", it is worth reviewing this topic in the context of writing bash scripts.

By default, the variables created within a script are available only to the subsequent steps of that script. Any child processes (sub-shells) do not have automatic access to the values of these variables. To make them available to child processes, they must be promoted to environment variables using the export statement, as in:

>export VAR=value

or

>VAR=value ; export VAR

While child processes are allowed to modify the value of exported variables, the parent will not see any changes; exported variables are not shared, they are only copied and inherited.

Typing export with no arguments will give a list of all currently exported environment variables.

## Functions

A function is a code block that implements a set of operations. Functions are useful for executing procedures multiple times, perhaps with varying input variables. Functions are also often called subroutines. Using functions in scripts requires two steps:

1. Declaring a function
2. Calling a function.

The function declaration requires a name which is used to invoke it. The proper syntax is:

    function_name () {
       command...
    }

For example, the following function is named display:

    display () {
       echo "This is a sample function"
    }

The function can be as long as desired and have many statements. Once defined, the function can be called later as many times as necessary. In the full example shown in the figure, we are also showing an often-used refinement: how to pass an argument to the function. The first argument can be referred to as $1, the second as $2, etc.

-------------------------

# Try ch. 15 problems and solutions

---------------------------

## if/elif/else Statement

In compact form, the syntax of an if statement is:

>if TEST-COMMANDS; then CONSEQUENT-COMMANDS; fi


>if:

```
if condition  
then  
        statements  
else  
       statements  
fi
```

- example"

```
if [ -f "$1" ]
then
    echo file "$1 exists" 
else
    echo file "$1" does not exist
fi
```

>elif

```
if [ sometest ] ; then
    echo Passed test1 
elif [ somothertest ] ; then
    echo Passed test2 
fi
```

--------------

### Testing for files

You can use the if statement to test for file attributes, such as:

- File or directory existence
- Read or write permission
- Executable permission.

 example:
```
if [ -x /etc/passwd ] ; then
    ACTION
fi
```

the if statement checks if the file /etc/passwd is executable, which it is not. Note the very common practice of putting:
```
; then
```
on the same line as the if statement.

You can view the full list of file conditions typing:
```
man 1 test.
```


|Condition| 	Meaning|
|:------|:---------|
|-e file 	|Checks if the file exists.|
|-d file 	|Checks if the file is a directory.|
|-f file| 	Checks if the file is a regular file (i.e. not a symbolic link, device node, directory, etc.)|
|-s file |	Checks if the file is of non-zero size.|
|-g file |	Checks if the file has sgid set.|
|-u file |	Checks if the file has suid set.|
|-r file |	Checks if the file is readable.|
|-w file |	Checks if the file is writable.|
|-x file |	Checks if the file is executable.|

--------------------------------

## boolean

Boolean expressions return either TRUE or FALSE. We can use such expressions when working with multiple data types, including strings or numbers, as well as with files. For example, to check if a file exists, use the following conditional test:

>[ -e \<filename> ]

Similarly, to check if the value of number1 is greater than the value of number2, use the following conditional test:

>[ $number1 -gt $number2 ]

The operator -gt returns TRUE if number1 is greater than number2.

<br>

- You can use the if statement to compare strings using the operator == (two equal signs). The syntax is as follows:
```
if [ string1 == string2 ] ; then
   ACTION
fi
```
--------------------------

### Numerical tests

|Operator| 	Meaning|
|:-----|:-----|
|-eq| 	Equal to|
|-ne |	Not equal to|
|-gt |	Greater than|
|-lt |	Less than|
|-ge |	Greater than or equal to|
|-le |	Less than or equal to|

-----------------------

### Arithmetic Expressions

Arithmetic expressions can be evaluated in the following three ways (spaces are important!):

- Using the expr utility  
expr is a standard but somewhat deprecated program. The syntax is as follows:  
                .  
expr 8 + 8  
echo $(expr 8 + 8)

- Using the $((...)) syntax   
This is the built-in shell format. The syntax is as follows:  
.  
echo $((x+1))
- Using the built-in shell command let. The syntax is as follows:  
let x=( 1 + 2 ); echo $x

In modern shell scripts, the use of expr is better replaced with var=$((...)).

------------------------------

# Chapter 16

## bash string manipulation

|Operator| 	Meaning|
|:----|:----|
|[[ string1 > string2 ]] |	Compares the sorting order of string1 and string2.|
|[[ string1 == string2 ]] |	Compares the characters in string1 with the characters in string2.|
|myLen1=${#string1} |	Saves the length of string1 in the variable myLen1.|

### part of string

At times, you may not need to compare or use an entire string. To extract the first n characters of a string we can specify: 
>${string:0:n}  


 Here, 0 is the offset in the string (i.e. which character to begin from) where the extraction needs to start and n is the number of characters to be extracted.

To extract all characters in a string after a dot (.), use the following expression:
> ${string#*.}.

## case statement

The **case** statement is used in scenarios where the actual value of a variable can lead to different execution paths. **case** statements are often used to handle command-line options.

Some of the advantages of using the case statement:

- It is easier to read and write.
- It is a good alternative to nested, multi-level if-then-else-fi code blocks.
- It enables you to compare a variable against several values at once.
- It reduces the complexity of a program.

```
case expression in
   pattern1) execute commands;;
   pattern2) execute commands;;
   pattern3) execute commands;;
   pattern4) execute commands;;
   * )       execute some default commands or nothing ;;
esac
````

![example case](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/afb49c3ebe75ff82910621adb09a22c6/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch15_screen18.jpg)


-----------------------------

## Looping Construct

3 types:
- for
- while
- until

<br>

>example **for**
```
for variable-name in list
do
    execute one iteration for each item in the list until the list is finished
done
```

<br>

>example **while**
```
while condition is true
do
    Commands for execution
    ----
done
```

<br>

>example **until**
```
until condition is false
do
    Commands for execution
    ----
done
```


---------------------


## debug

> bash –x ./script_file,

- It traces and prefixes each command with the + character.
- It displays each command before executing it.
- It can debug only selected parts of a script (if desired) with:

```
set -x    # turns on debugging
...
set +x    # turns off debugging
```

## Creating Temporary Files and Directories

|Command 	|Usage|
|:----|:---|
|TEMP=$(mktemp /tmp/tempfile.XXXXXXXX)| 	To create a temporary file|
|TEMPDIR=$(mktemp -d /tmp/tempdir.XXXXXXXX)| 	To create a temporary directory|

>example
```
> $ ln -s /etc/passwd /tmp/tempfile

The password file will be overwritten by the temporary file contents.

To prevent such a situation, make sure you randomize your temporary file names by replacing the above line with the following lines:

> TEMP=$(mktemp /tmp/tempfile.XXXXXXXX)
> echo $VAR > $TEMP

```
### Discarding output with /dev/null

>$ ls -lR /tmp > /dev/null

* the entire standard output stream is ignored, but any errors will still appear on the console.

> the entire standard output stream is ignored, but any errors will still appear on the console.

* this will dump both stdout and stderr

## Random data and numbers

> Using the $RANDOM environment variable

read https://en.wikipedia.org/wiki/FIPS_140-2

## challenge

Do you enjoy learning new skills? Would you like to get some extra experience under your belt and apply what you have learned to real world job tasks? The Mooqita project is here to change the way education and work are connected. We are NOT part of The Linux Foundation, but we are very happy to work with the course team to offer you a unique opportunity.

In this class we offer an additional homework assignment. It is a little more challenging than your regular assignments, and OPTIONAL. 

Solving the challenge will allow you to start building a portfolio on Mooqita and give you the chance to be connected with employers, for internships, full time positions, and paid projects.

Here's how this works:

Go to the challenge link, register your account, and start solving. Complete the additional assignment and engage in a peer review process. The challenge is more challenging and closer to real world work challenges or questions you might encounter in a job interview. Once you have done the challenge presented here, you can try out more of our challenges. You will not get paid to solve them, but you get extra practice through real world challenges. The companies will NOT get work for free through this.

More information is available at https://www.mooqita.org/.

Mooqita is new and we are still improving the platform. If you encounter problems, have questions, or want to give us feedback, please contact us via info@mooqita.org or open a ticket in our bug-tracker (https://github.com/Mooqita/worklearn/issues).

Hint: Using a bug-tracker is a very important part of a developer’s life, so give it a try. 

And here is your entry MooqitaChallenge (https://app.mooqita.org/app/solution?challenge_id=YKgnjCTtuD2AoAmu2).

We wish you a great time in this class and hope to hear from you!


# Chapter 7 printing

> Common UNIX Printing System (CUPS).

Important configuration files:
 * cupsd.conf
 * printers.conf
 
 > view the full list of configuration files by typing: **ls -l /etc/cups/**.
 
 > CUPS stores print requests as files under the **/var/spool/cups** directory

> Log files are placed in **/var/log/cups**  
$ sudo ls -l /var/log/cups


## Managing CUPS

$ systemctl status cups

$ sudo systemctl [enable|disable] cups

$ sudo systemctl [start|stop|restart] cups

## Printing from the Command-Line Interface

> CUPS provides two command-line interfaces, descended from the System V and BSD flavors of UNIX. This means that you can use either lp (System V) or lpr (BSD) to print. You can use these commands to print text, PostScript, PDF, and image files.
  
### using ip


|Command	|Usage|
|:---|:---|
|lp \<filename>	|To print the file to default printer|
|lp -d printer \<filename>|	To print to a specific printer (useful if multiple printers are available)|
|program [pipeline] lp echo string [pipeline] lp	|To print the output of a program|
|lp -n number \<filename>|	To print multiple copies|
|lpoptions -d printer	|To set the default printer|
|lpq -a	|To show the queue status|
|lpadmin	|To configure printer queues|

### Managing printing jobs

|Command	|Usage|
|:---|:----|
|lpstat -p -d	|To get a list of available printers, along with their status|
|lpstat -a	|To check the status of all connected printers, including job numbers|
|cancel job-id OR lprm job-id	|To cancel a print job|
|lpmove job-id newprinter	|To move a print job to new printer|

### Viewing PDF

Linux has many standard programs that can read PDF files, as well as many applications that can easily create them, including all available office suites, such as LibreOffice.

The most common Linux PDF readers are:

* Evince is available on virtually all distributions and the most widely used program.
* Okular is based on the older kpdf and available on any distribution that provides the KDE environment.
* GhostView is one of the first open source PDF readers and is universally available.
* Xpdf is one of the oldest open source PDF readers and still has a good user base. 