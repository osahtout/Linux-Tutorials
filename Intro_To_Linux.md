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

#### CTRL-ALT-functionKey   
#### Ubuntu uses VT-7 or CTRL-ALT-F7

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

#### locate
> locate zip | grep bin  
- will list all the files and directories with both zip and bin in their name. We will cover grep in much more detail later. Notice the use of | to pipe the two commands together.

#### find
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

# Chapter 9 processes


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

 <br>

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
## File Operation

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

