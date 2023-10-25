class runnr_ver:
    ver = 'v0.2.0'

    runnr_help = """
Usage:
    runnr [options] <file>

General Options:
    -h, --help                          Shows help.
    -V, --version                       Shows current runnr version.
    -U, --update                        Checks and update runnr using pip.
    -debug <other-options> <file>       Prints executed runnr commands.
    -run <Y/N> <file>              Sets running after compilation to on or off.
    -out <output-file-name> <file>      Sets output file name of the executable.
    -param <parameter> <file>           Passes additional configurations to the compiler/interpreter.
    -args <arguments> <file>            Passes additional command line arguments to the executable.
    -open <file>                        Opens a file in a program. (Uses "-open" configuration from runnr.conf)
    
"""