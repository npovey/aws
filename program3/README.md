  ####Directory Back up and Restore for the cloud

[TOC]

The project consists of two python programs. Backup.py and Restore.py One backs up and the other one restores the given directory. Must use python3 (not python).

 #### Assumptions

The user already set up it's keys and can connect to AWS and Azure from his/her computer. The program has backet hard coded "npovey2". Directories allways backed up to "npovey2"

#### Backup

1. Navigate to the directory with program3

```python
nps-MacBook-Air-2:Desktop np$ ls
fall_2019			text2 		cloud			program3		resume
```

2. Run the Backup.py file

```python
nps-MacBook-Air-2:Desktop np$ python3 program3/Backup.py text2
```

3. Output

```python
nps-MacBook-Air-2:Desktop np$ python3 program3/Backup.py text2
Created: text2/Backup.py
Created: text2/.DS_Store
Created: text2/makefile
Created: text2/README.md
Created: text2/texts/virus.txt
Created: text2/texts/Untitled.txt
Created: text2/hi/xc.txt
Created: text2/hi/bc.txt
Created: text2/hi/a.txt
nps-MacBook-Air-2:Desktop np$
```



#### Restore

1. Navigate to the directory with program3 folder

```python
nps-MacBook-Air-2:Desktop np$ ls
fall_2019			text2 		cloud			program3		resume
```

2. Run Restore.py MUST be outside program3

```python
nps-MacBook-Air-2:Desktop np$ python3 program3/Restore.py text2
```

3. Output

```python
nps-MacBook-Air-2:Desktop np$ python3 program3/Restore.py text2
Created: text2/.DS_Store
Created: text2/Backup.py
Created: text2/README.md
Created: text2/hi/a.txt
Created: text2/hi/bc.txt
Created: text2/hi/xc.txt
Created: text2/makefile
Created: text2/texts/Untitled.txt
Created: text2/texts/virus.txt
nps-MacBook-Air-2:Desktop np$ 
```

4. Output after backing up text2 folder after restoring

```python
nps-MacBook-Air-2:Desktop np$ python3 program3/Backup.py text2
Rewrote: text2/Backup.py
Rewrote: text2/.DS_Store
Rewrote: text2/makefile
Rewrote: text2/README.md
Rewrote: text2/texts/virus.txt
Rewrote: text2/texts/Untitled.txt
Rewrote: text2/hi/xc.txt
Rewrote: text2/hi/bc.txt
Rewrote: text2/hi/a.txt
```

#### Dependencies

```python
nps-MacBook-Air-2:Desktop np$ python3 --version
Python 3.7.6

nps-MacBook-Air-2:Desktop np$ uname -a
Darwin nps-MacBook-Air-2.local 18.7.0 Darwin Kernel Version 18.7.0: Tue Aug 20 16:57:14 PDT 2019; root:xnu-4903.271.2~2/RELEASE_X86_64 x86_64


```



#### Testing on local computer MacOS 

![before](/Users/np/Desktop/program3/images/before.png)

Ran the Backup.py from outside the program3 folder

```python
nps-MacBook-Air-2:Desktop np$ python3 program3/Backup.py text2
Created: text2/Backup.py
Created: text2/.DS_Store
Created: text2/makefile
Created: text2/README.md
Created: text2/texts/virus.txt
Created: text2/texts/Untitled.txt
Created: text2/hi/xc.txt
Created: text2/hi/bc.txt
Created: text2/hi/a.txt
nps-MacBook-Air-2:Desktop np$ 
```

Notice that npovey2 folder appeared.

![after](/Users/np/Desktop/program3/images/after.png)

Ran the same command the second time

```python
nps-MacBook-Air-2:Desktop np$ python3 program3/Backup.py text2
Already Backed Up: text2/Backup.py
Already Backed Up: text2/.DS_Store
Already Backed Up: text2/makefile
Already Backed Up: text2/README.md
Already Backed Up: text2/texts/virus.txt
Already Backed Up: text2/texts/Untitled.txt
Already Backed Up: text2/hi/xc.txt
Already Backed Up: text2/hi/bc.txt
Already Backed Up: text2/hi/a.txt
nps-MacBook-Air-2:Desktop np$ 

```

Edit Backup.py and try again

![local_folder](/program3/images/local_folder.png)

```python
nps-MacBook-Air-2:Desktop np$ python3 program3/Backup.py text2
Rewrote: text2/Backup.py
Rewrote: text2/.DS_Store
Already Backed Up: text2/makefile
Already Backed Up: text2/README.md
Already Backed Up: text2/texts/virus.txt
Already Backed Up: text2/texts/Untitled.txt
Already Backed Up: text2/hi/xc.txt
Already Backed Up: text2/hi/bc.txt
Already Backed Up: text2/hi/a.txt
nps-MacBook-Air-2:Desktop np$ 
```



