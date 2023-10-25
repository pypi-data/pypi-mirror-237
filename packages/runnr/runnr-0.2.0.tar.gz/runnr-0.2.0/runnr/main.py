import sys
from os import system
from .runnr_parser import runnr_parser
from .runnr_flags import runnr_flags
from .runnr_ver import runnr_ver

ver = runnr_ver()

#command line arguments
argc = len(sys.argv)
argv = sys.argv

class runnr():
    #intialises the runnr
    def __init__(self):
        self.test_argv()
        self.parser = runnr_parser()
        self.flags = runnr_flags()
        self.parser.init()
        self.setup_cli_param()

        if self.flags.l_file_names:
            for file in self.flags.l_file_names:
                print(f'runnr: file: {file}')
                self.split_extension(file)
                self.build_commands(file)
                print()
            exit(0)

        self.split_extension()
        self.build_commands()
        exit(0)

    #function to test if there is any argument or not
    #parameters: none
    #returns: none
    def test_argv(self) -> None:
        if argc <= 1:
            print('runnr: error: no input file')
            exit(1)

    #function to return the output name & its command if it compiled based language else list of empty strings
    #parameters: configuration row for the given extension : dictionary
    #returns: [file_name_without_extension, file_name_with_output_command] : [str, str]
    def output_name(self, configs : [dict]) -> [str]:
        if configs['type'] == 'c':
            if self.flags.l_file_names:
                if self.flags.s_custom_output_file_name:
                    print('runnr: warning: "-out" option does not work while using "-files".')

                return [f'{self.flags.s_file_name}', f'-o {self.flags.s_file_name}']
            
            if self.flags.s_custom_output_file_name:
                return [f'{self.flags.s_custom_output_file_name}', f'-o {self.flags.s_custom_output_file_name}']
            
            match configs['out']:
                case '$FILE':
                    return [f'{self.flags.s_file_name}', f'-o {self.flags.s_file_name}']

                case '$NONE':
                    return ['', '']
                
                case _:
                    return [f"{configs['out']}", f"-o {configs['out']}"]
        else:
            return ['', '']

    #function to return the arguments for compiler/interpreter
    #parameters: none
    #returns: arguments : str
    def executor_param(self) -> str:
        if self.flags.s_extra_param:
            if self.flags.l_file_names:
                print('runnr: warning: "-param" option does not work while using "-files".')
                return ''
            
            return self.flags.s_extra_param
        else:
            return ''

    #function to execute the executable file if it is compiled based language and show the ran command if debug is set
    #parameters: output_file_name : str, status_of_previous_ran_code : int
    #returns: none
    def execute(self, output_name : str ,status : int) -> None:
        if output_name and not status:
            if sys.platform == 'win32':
                if self.flags.s_extra_args:
                    if self.flags.b_debug_mode:
                        print(f'runnr: debug: run: ".\\{output_name} {self.flags.s_extra_args}"')

                    system(f'.\\{output_name}  {self.flags.s_extra_args}')
                else:
                    if self.flags.b_debug_mode:
                        print(f'runnr: debug: run: ".\\{output_name}"')
                    system(f'.\\{output_name}')

            elif sys.platform in ['darwin', 'linux']:
                if self.flags.s_extra_args:
                    if self.flags.b_debug_mode:
                        print(f'runnr: debug: run: "./{output_name} {self.flags.s_extra_args}"')
                        
                    system(f'./{output_name} {self.flags.s_extra_args}')
                else:
                    if self.flags.b_debug_mode:
                        print(f'runnr: debug: run: "./{output_name}"')
                    system(f'./{output_name}')

    #function to iterate over all the arguments and set the parameters
    #parameters: none
    #returns: none
    def setup_cli_param(self) -> None:
        self.check_first_param()

        i = 1
        while(i < argc - 1):
            match argv[i]:
                case '-run':
                    if argv[i + 1] == 'Y':
                        self.flags.b_run_after_compilatiion = True
                    elif argv[i + 1] == 'N':
                        self.flags.b_run_after_compilatiion = False
                    else:
                        print(f'runnr: error: invalid parameter "{argv[i + 1]}" for option "-run"');
                        exit(1)
                     
                    i += 1

                case '-debug':
                    if not self.flags.b_debug_mode:
                        self.flags.b_debug_mode = True
                    else:
                        print('runnr: error: multiple use of option "-debug"')
                        exit(1)

                case '-out':
                    if not self.flags.s_custom_output_file_name:
                        self.flags.s_custom_output_file_name = argv[i + 1]
                        i += 1
                    else:
                        print('runnr: error: multiple use of option "-out"')
                        exit(1)

                case '-param':
                    if not self.flags.s_extra_param:
                        self.flags.s_extra_param = argv[i + 1]
                        i += 1
                    else:
                        print('runnr: error: multiple use of option "-param"')
                        exit(1)

                case '-args':
                    if not self.flags.s_extra_args:
                        self.flags.s_extra_args = argv[i + 1]
                        i += 1
                    else:
                        print('runnr: error: multiple use of option "-args"')
                        exit(1)

                case '-files':
                    self.flags.l_file_names = argv[i+1:]
                    return

                case _:
                    if argv[i][0] == '-':
                        print(f'runnr: error: bad option: "{argv[i]}"')
                        exit(1)
        
            i += 1
    
    #function to check first and only parameter
    #parameters: none
    # returns: none    
    def check_first_param(self) -> None:
        if argv[1] in ['--version', '-V']:
            print(f'{ver.ver}')
            exit(0)

        if argv[1] in ['--help', '-h']:
            print(ver.runnr_help)
            exit(0)

        if argv[1] in ['--update', '-U']:
            system('pip install --upgrade runnr')
            exit(0)

        if argv[1] == '-open':
            if argc == 2:
                print('runnr: error: no input file for "-open"')
                exit(1)

            for rows in self.parser.runnr_config_table:
                if rows['extension'] == argv[1]:
                    system(f"{rows['executor']} {argv[argc - 1]}")
                    exit(0)

            print(f'runnr: error: no config for "-open" found in "{self.parser.path_of_config}"')
            exit(1)

        if argc == 2 and argv[1][0] == '-':
            print(f'runnr: error: bad option: "{argv[1]}"')
            exit(1)

    #function to split the name by '.' dot
    #parameters: none
    #returns: none
    def split_extension(self , filename = argv[argc - 1]) -> None:
        index = filename.rfind('.')

        if index == -1:
            print(f'runnr: error: input file "{filename}" has no extension')
            exit(1)

        self.flags.s_file_name = filename[:index]
        self.flags.s_extension = filename[index:]

    #function to build the final command based on all the configs
    #parameters: none
    #returns: none
    def build_commands(self,filename = argv[argc - 1]) -> None:
        config : dict = self.parser.runnr_get_extension_config(self.flags.s_extension)
        if not config:
            print(f'runnr: error: file format is not found in "{self.parser.path_of_config}". Please add it to use it.')
            exit(1)

        [output_name, output_command_w_name] = self.output_name(config)
        args_for_i = self.flags.s_extra_args if self.flags.s_extra_args and config['type'] == 'i' else ''
        command = f"{config['executor']}{self.executor_param()} {filename} {output_command_w_name}{args_for_i}"

        if self.flags.b_debug_mode:
            print(f'runnr: debug: config: using config from "{self.parser.path_of_config}"')
            print(f'runnr: debug: executed: "{command}"')
        
        status = system(command)

        if self.flags.b_run_after_compilatiion:
            self.execute(output_name,status)