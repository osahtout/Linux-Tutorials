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

<br>

## Different types of filesystems supported by Linux:

* Conventional disk filesystems: ext2, ext3, ext4, XFS, Btrfs, JFS NTFS, etc.
* Flash storage filesystems: ubifs, JFFS2, YAFFS, etc.
* Database filesystems
* Special purpose filesystems: procfs, sysfs, tmpfs, squashfs, debugfs, etc

<br>

## A comparison between filesystems in Windows and Linux is given in the accompanying table:

|   iii                   | Windows      | Linux          |
| :-----------            | :------:     | :-----------:  |
| partition               | Disk1        | /dev/sda1      |
| FileSystem type         | NTFS/VFAT    | ext2, ext3 ... |
| Mounting Parameters     | DriverLetter | MountPoint     |
| Base Folder (os location)| C:\          | /              |

<br>


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

<br>

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

<br>

## File hierarchy

![File Hierarchy](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/66def40e2774fd96011565107706da2d/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/dirtree.jpg)



# Chapter 7

## Basic Utilities

* **cat**: used to type out a file (or combine files)
* **head**: used to show the first few lines of a file
* **tail**: used to show the last few lines of a file
* **man**: used to view documentation.

<br>

## Most input lines entered at the shell prompt have three basic elements:

* Command
* Options
* Arguments.
    * [command] [options] [arguments]
    * shutdown -r now

## Setting Up sudo

1. type **su** and hit _Enter_
2. enter password then _Enter_
3. Now, you need to create a configuration file to enable your user account to use sudo. Typically, this file is created in the  
 /etc/sudoers.d/ directory with the name of the file the same as your username. For example, for this demo, let’s say your username is  
 “student”. After doing step 1, you would then create the configuration file for “student” by doing this:  
 \# echo "student ALL=(ALL) ALL" > /etc/sudoers.d/student
4. Finally, some Linux distributions will complain if you do not also change permissions on the file by doing:  
   \# chmod 440 /etc/sudoers.d/student

<br>

## Switch between virtual terminal (VT)

#### CTRL-ALT-functionKey   
#### Ubuntu uses VT-7 or CTRL-ALT-F7

<br>

## To start or stop GUI
- $ sudo systemctl stop gdm (**or** sudo telinit 3)  
- $ sudo systemctl start gdm (**or** sudo telinit 5)

<br>

## SSH  
- One can also connect and log into remote systems via the Secure Shell (SSH) utility. For example, by typing  
ssh username@remote-server.com,  
 SSH would connect securely to the remote machine and give you a command line terminal window, using passwords  
  (as with regular logins) or cryptographic keys (a topic we will not discuss) to prove your identity.

  <br>

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

<br>

## Locating application
> which  
> whereis  

example:
- $ which diff  
  /usr/bin/diff

- $ whereis diff  
  diff: /usr/bin/diff /usr/share/man/man1/diff.1.gz /usr/share/man/man1p/diff.1p.gz


## Access Directories
|Command | Results|
|:----- | :----|
| pwd| Displays the present working directory|
| cd ~ _or_ cd |Change to your home directory (shortcut name is ~ (tilde))|
|cd ..| Change to parent directory (..) |
|cd - | Changes to previous directory(- (minus))|

## Absolute vs Relative path

- Absolute pathname  
An absolute pathname begins with the root directory and follows the tree, branch by branch, until it reaches the desired directory or file. Absolute paths always start with /.  
$ cd /usr/bin
- Relative pathname  
A relative pathname starts from the present working directory. Relative paths never start with /.  
$ cd ../../usr/bin


![File Hierarchy](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/c9a79bc0bfc23d476b1c89380ca90aad/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch06_screen19.jpg)

<br>

## Exploring File System

> tree -d

<br>

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

<br>

## Viewing Files

|Command|usage|
|:------|:-----|
|cat|Used for viewing files that are not very long; it does not provide any scroll-back.|
|tac|  tac 	Used to look at a file backwards, starting with the last line.|
|less| Used to view larger files because it is a paging program. It pauses at each screen full of text, provides <br> scroll-back  capabilities, and lets you search and navigate within the file. Note: Use / to search for a pattern in the forward direction  and ? for a pattern in the backward direction. An older program named more is still used, but has fewer capabilities: "less is more".|
|tail| Used to print the last 10 lines of a file by default. You can change the number of lines by doing -n 15 or just -15 if <br> you wanted to look at the last 15 lines instead of the default.|
|head| The opposite of tail; by default, it prints the first 10 lines of a file.|
|vi| View, edit files|
<br>

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

<br>

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


<br>

## WildCard

|WildCard|Results|
|:----|:----|
|?| Matches any single character|
|*| matches any string of characters|
|[set]|Matches any character in the set of characters, for example [adf] will match any occurrence of "a", "d", or "f"|
|[!set]|Matches any character not in the set of characters|

<br>

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


<br>

## Process Id (PID) and threads

| Id type| Description |
|:------| :------|
| Process ID (PID) |Unique Process ID number |
|Parent Process ID (PPID) |Process (Parent) that started this process. If the parent dies, the PPID will refer to an adoptive parent; on recent kernels, this is kthreadd which has PPID=2. |
|Thread ID (TID) |Thread ID number. This is the same as the PID for single-threaded processes. For a multi-threaded process, each thread shares the same PID, but has a unique TID. |

> Killing a process if PID pid  
 -$ kill -SIGKILL [pid] or kill -9 [pid]

<br>

 ## User and group ID UID GID

 ![UID GID](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fbe122ffd13edf336ad978cddb953a7f/asset-v1:LinuxFoundationX+LFS101x+3T2018+type@asset+block/LFS01_ch16_screen07.jpg)

 <br>

 ## The ps Command (System V Style)
  >ps  
  >ps -ef -> all processes  
  >ps -eLf => every thread  
  >ps aux =>all users
  >ps axo specify attributes