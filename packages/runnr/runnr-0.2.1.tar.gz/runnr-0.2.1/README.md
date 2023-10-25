# runnr
runnr is an open-source command line interface tool for building, compiling & executing different programs & files.A single powerfull tool for developers to compile, open, build & interpret different programs.

runnr is currently in Beta stages [v0.x.x], most of the important features will be added in stable realease version [v1.x.x].
# Installation

[Link to PyPi](https://pypi.org/project/runnr/)

Install runnr with pip:
```bash
pip install runnr
```
    
# Documentation

- ## Config File:

Before starting to compiling & executing anything, lets take a look at runnr.conf file present at:-
```bash
Windows: C:\Users\<user-name>\runnr.conf
Unix-like: ~\.config\runnr.conf
```

>If config file is not present the try running: runnr --version

This runnr.conf is the main config file that runnr use to execute commands based on file-extension. Once the configuration is set for any file-extension runnr can execute and run it without any problem. As runnr is a config file based tool, it is very easy to use the same config file in different system only after setting it up once.

- ### Syntax of the config file:

```
(<extension>) :: <arguemnt1> = "<parameter1>",  <arguemnt2> = "<parameter2>", ....
```
All `<argument> = <parameter>` are separateed using ','. You can even comment in this config file using '#' and white Spaces are ignored automatically.

- Example:

```
#for adding support for .c files, we simply can write:-
(.c) :: COMPILER = "gcc", OUTPUT_FILENAME="$FILE"
```

The extension must be enclosed withing parenthese: "()". Then the respective arguments & parameters are writen after using argument separator: "::". The arguments must be separated using "," and every argument must have its value/parameter enclosed withing double qoutes: "".

- ## Supported Arguments:
As of version: v0.2.0 suppported aruments are:

```
1. COMPILER="<compiler-name>"
2. INTERPRETER="<interpreter-name>"
3. USE=<cli-program> : It is used for special arguments like "-open"
4. OUTPUT_FILENAME=<variables or name> : It is used for setting special output name.
```

- ### Output Name Values:
```
$FILE : It sets the output name to be same as input file name but without the extension.
$NONE : It is mostly used for interpreter based languages, as those don't have any compiled file.
        Using $NONE on compiled based languages, turns off generation of any custom output file.

<any-custom-name> : Creates an output file with the given name.
```
- Examples:
```
#for javascript
(.js)::INTERPRETER="node", OUTPUT_FILENAME="$NONE"
```

For interpreter based languages, it is optional to set "OUTPUT_FILENAME" argument.

- ## CLI Tool:
Now lets see how to interact with the runnr tool :- 

First lets see if it installed or not? : Simply Type-
```bash
$ runnr --version
v0.x.x
```

>If any error occurs then install runnr first.
>If it prompts to create config file, enter "Y". Then retry with the command.

Now if it is installed correctly, lets proceed with its usages:-

- ### Comiling or Interpreting a file:
runnr can compile or interpret different programs based on extensions from "runnr.conf" file. Now lets see some examples. Suppose we have "hello.py" & "hello.cpp" file with "Hello, World" printing program.

Then to run this files:
``` bash
$ runnr hello.py
Hello, World
```


```bash
$ runnr hello.cpp
Hello, World
```

It can execute different files based on .conf file.
* It is important to note that the file that is being compiled/interpreted must be the last argument, after any options.

- ### Only compiling not executing:
We can make runnr to only compile a programs but not execute it by using '-run' option.

Example:
```bash
$ runnr -run N hello.cpp
```

It outputs nothing as we set running after compilation to off. It just generates the binary executable file.

This option only works for compiled based programs like C, C++, rust. The "-run" option's parameter can be either "Y" or "N".

- ### Custom output file name for Compiled programs:

We can make runnr to output the compiled executable file-name as we want it to be instead of default set value from config.

Examples:
```bash
$ runnr -run N -out helloworld hello.cpp
$ ./helloworld
Hello, World
```
>Yes, we can use these different options and parameters all together.
So, "-out" option takes only one parameter that is the file name of the output file.

- ### More compiler arguments:
There may be some cases where we need to pass more compiler arguemnts to compile it. For example, in C++ we might need to tell the compiler to use C++11, as we have used 'auto' data-type in out program. 

This can be achieved by two ways:

- Parmanent:
Modifying the "runnr.conf" file for ".cpp" extension.

Examples:
```
#this will use C++11 std library
(.cpp)::COMPILER="g++ -std=c++11", OUTPUT_FILENAME="a.out"
```

- Temporary:
For single file use cases.

Examples:
```bash
$ runnr -param "-std=c++11" -out helloworld hello.cpp
```

"-param" takes the compiler arguemnt and directly pass it to the compiler. It is also a good practice to wrap them in "". "-param" can also be used to link to libaries too.

```bash
$ runnr -param -lm -out sqrt square_root.c
```

- ### Execuable file's command-line arguemnts:
You might write some programs that takes command line arguments directly, as runnr can compile and execute simultaneously, you might want to pass the necessary arguments to the program. This can be achieved by using "-args".

Suppose we have written a program which takes 2 number directly from command line like "./a.exe 5 7" & outputs its sum. Lets see how to do that with runnr.

Examples:

```bash
$ runnr -args "5 7" sum_2_no.c
12
```

Again it is necessary to wrap the arguments within "" as it containes spaces.

- ### Executing multiple files at once:
Multiple different or same files can be executed simultaneously using "-files" option.

```bash
$ runnr -run N -files hello.c hello.py hello.cpp sum.c
```

- By default all the input files gets executed. Use `-run N` to turn it off for compiled based language.
- If any custom output file-name in set in the config or by using `-out` option, it will be ignored and the executable output name will be same as of the file-name without the extension.
- After "-files" option all the arguments must be files.
- For using "-args" option, all the executable will recieve same command-line argument.
- "-param" option is ignored while using "-files", otherwise it will result in passing of same compiler/interpreter parameter to different compiler/interpreter. It is recommended to set these parameter options in config-file instead.
- Opening of multiple files using "-open" isn't implemented yet.

- ### Debug:

Sometimes developers need to see what is actually getting executed by runnr to find any error or mis-compilation of programs & executions. To solve this a particular option is to be used called "-debug".

Examples:
```bash
$ runnr -debug -out helloworld -param "-std=c++11" hello.cpp
runnr: debug: config: using config from /Users/aniket/.config/runnr.conf
runnr: debug: executed: g++ -std=c++11 -o helloworld hello.cpp
runnr: debug: run: ./helloworld
Hello, World
```

Using the "-debug" gives a detailed output of the underneath commands execution.

- ### Version:
To check the version of runnr:

```bash
$ runnr --version
v0.x.x
$ runnr -V
v0.x.x
```

- ### Help:

```bash
$ runnr --help
$ runnr -h
```

- ## Update:
Update runnr using `--update or -U` option. It uses pip to update itself.
```bash
$ runnr --update
$ runnr -U
```

# VERSION:
- Version rule :: `<major>.<minor>.<patches>`
>v0.2.1

# What's New in this Update:

1. Added help option "--help" or "-h".
2. Added "--update" or "-U" option to automatically update runnr using pip.
3. Added option "-files" for compiling/interpreting multiple files at once.
4. Fixed the issue where runnr detects the single argument as file with no extension.
5. Fixed the issue where runnr ignore cli arguments for interpreted languages.
6. Removed auto copying of "runnr.conf" while building the "setup.py".
7. Removed unnecessary boolean variables from runnr_flags and replaced them with string operations.