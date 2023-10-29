import PySimpleGUI as sg
import os
import shutil
import sys

from docutils.nodes import entry

version = __version__ = "2.4"

"""

Installs Upload to PyPI quickly and easily

1.0 24-Oct-2023 - Let the fun begin!
1.6 24-Oct-2023 - Added back the test for input element event so folder is checked
2.0 28-Oct-2023 - It all sorta works!  

To upload to PyPI (at least on Python 3.6 this works)...
Make sure working folder is the one with setup.py
    python setup.py sdist bdist_wheel
    python -m twine upload -u USERNAME -p PASSWORD dist/*


"""


setuppy_template = """

import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
name="<#-NAME-#>",
version="<#-VERSION-#>",
author="<#-AUTHOR-#>",
author_email="<#-AUTHOR_EMAIL-#>",
install_requires=[<#-INSTALL_REQUIRES-#>],
description="<#-DESCRIPTION-#>",
long_description=readme(),
long_description_content_type="text/markdown",
license='Free To Use But Restricted',
keywords="<#-KEYWORDS-#>",
url="<#-URL-#>",
# packages=setuptools.find_packages(),
packages=[<#-PACKAGES-#>],
python_requires="<#-PYTHON_REQUIRES-#>",
classifiers=[
    <#-CLASSIFIERS-#>
],
package_data={"": ["*.ico", "LICENSE.txt", "README.md"]},
entry_points={'gui_scripts': [
    <#-ENTRY POINTS-#>
    ]
    },
)

"""

import re

alpha_num_order = lambda string: ''.join([format(int(x), '05d') if x.isdigit() else x for x in re.split(r'(\d+)', string)])


def fill_in_setup_py_template(window:sg.Window, values:dict):
    # print(f'In fill in setup... values dict = {values}')
    lines = setuppy_template.split("\n")
    new_lines = lines.copy()
    # for line in new_lines:
        # sg.cprint(line, colors='white on blue')
    # Loop through the values dictionary
    for key, item in values.items():
        # print(f'processing key {key}')
        # Special cases
        # Install requires - find ',' then put each entry in quotes
        # for each item in the values dictionary, scan the entire template to see what to fill in
        for i, line in enumerate(new_lines):
            token =  key_to_tag(key)
            while True:
                if token in line:
                    if key in ('-INSTALL_REQUIRES-', '-PACKAGES-'):
                        # print('found install requires')
                        requires_list = item.split(',')
                        oline = ''
                        for p in requires_list:
                            p = p.strip()
                            oline += f'"{p}",'
                        if oline.endswith(','):
                            oline = oline[:-1]
                        if key == '-INSTALL_REQUIRES-':
                            line = new_lines[i] = f'install_requires=[{oline}],'
                        elif key == '-PACKAGES-':
                            line = new_lines[i] = f'packages=[{oline}],'
                    else:
                        line = new_lines[i] = line.replace(token, item, 1)
                    # print(f'Found {token} in {line}.  New line:', new_lines[i])
                else:
                    break
    # Handle classifiers separately
    new_new_lines = []
    for line in new_lines:
        # sg.cprint(line, colors='white on blue')
        if '<#-CLASSIFIERS-#>' in line:
            for key, item in values.items():
                if isinstance(key, tuple):
                    if key[0] == '-CLASSIFIER-':
                        element = window[('-CLASSIFIER ROW-', key[1])]       # type: sg.Element
                        if element.visible:
                            new_new_lines.append(f'"{item}",')
            # Automatically add on these 3 classifiers
            if "Development Status :: 2 - Pre-Alpha" not in values.values():
                new_new_lines.append('"Development Status :: 2 - Pre-Alpha",')
            if "Development Status :: 3 - Alpha" not in values.values():
                new_new_lines.append('"Development Status :: 3 - Alpha",')
            if "Topic :: Multimedia :: Graphics" not in values.values():
                new_new_lines.append('"Topic :: Multimedia :: Graphics"')
        elif '<#-ENTRY POINTS-#>' in line:
            for key, item in values.items():
                if isinstance(key, tuple):
                    if key[0] == '-ENTRY POINT COMMAND-':
                        element = window[('-ENTRY POINT ROW-', key[1])]       # type: sg.Element
                        if element.visible:
                            # 'psgupgrade=PySimpleGUI.PySimpleGUI:_upgrade_entry_point',
                            command_text = f'"{item}={values["-NAME-"]}.{values["-NAME-"]}:{values[("-ENTRY POINT FUNCTION-", key[1])]}",'
                            # print(f'adding entry point: {command_text}')
                            new_new_lines.append(command_text)
        else:
            new_new_lines.append(line)

    new_setup = '\n'.join(new_new_lines)
    return new_setup
    # print(new_setup)


def remove_folders(main_folder):
    dist_folder = os.path.join(main_folder, 'dist')
    build_folder = os.path.join(main_folder, 'build')
    egg_folder = os.path.join(main_folder, os.path.basename(main_folder) + '.egg-info')
    try:
        shutil.rmtree(dist_folder, ignore_errors=True)
        shutil.rmtree(build_folder, ignore_errors=True)
        shutil.rmtree(egg_folder, ignore_errors=True)
    except Exception as e:
        print('Exception removing folders', e)
    print(f'Removed:\n{dist_folder}\n{build_folder}\n{egg_folder}')


def popup_yes_no_cancel(text):
    layout = [
        [sg.Text(text)],
        [sg.Push(), sg.B('Yes'), sg.B('No', bind_return_key=True, focus=True), sg.B('Cancel')],
    ]

    window = sg.Window('PyPI Package Uploader', layout, font='_ 12', icon=icon(), modal=True, keep_on_top=True, finalize=True)
    window['No'].set_focus()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'No', 'Cancel'):
            if event == sg.WIN_CLOSED:
                event = 'No'
            break
        elif event == 'Yes':
            break
    window.close()
    return event


def make_init_file(init_filename, package_name):
    # lines = [f'from .{package_name} import *']
    lines = [f'from .{package_name} import *']
    with open(init_filename, "w") as file:
        for line in lines:
            file.write(line + "\n")

# def make_main_file(main_filename, package_name):
#     lines = [f"from f.{package_name} import *",
#              'if __name__ == "__main__":',
#              '    main()',
#              ]
#     with open(main_filename, "w") as file:
#         for line in lines:
#             file.write(line + "\n")
#
def make_main_file(main_filename, package_name):
    lines = [
             'if __name__ == "__main__":',
             '    main()',
             ]
    with open(main_filename, "w") as file:
        for line in lines:
            file.write(line + "\n")

def make_setup_file(setup_filename, setup_text):
    with open(setup_filename, "w") as file:
        file.write(setup_text)


def check_folder(folder, window: sg.Window):
    if os.path.isdir(folder):
        window['-STATUS-'].update('Valid folder')
    else:
        window['-STATUS-'].update('')
        window['-PACKAGE VER-'].update('')
        return

    package_name = os.path.basename(folder)
    window['-STATUS-'].update(f'Package name: {package_name}')
    program_folder = os.path.join(folder, package_name)
    init_name = os.path.join(program_folder, '__init__.py')
    program_name = os.path.join(program_folder, f'{package_name}.py')
    setup_name = os.path.join(folder, 'setup.py')
    if not os.path.exists(setup_name):
        return

    ver_from_program = get_ver_from_file(program_name)
    window['-PACKAGE VER-'].update(ver_from_program)
    window['-VERSION-'].update(ver_from_program)
    # print(program_name)
    make_init_file(init_name, package_name)
    make_main_file(os.path.join(program_folder, '__main__.py'), package_name)

    change_ver_in_setup(setup_name, ver_from_program)


def run_test(folder, window):
    package_name = os.path.basename(folder)
    program_folder = os.path.join(folder, package_name)
    program_name = os.path.join(program_folder, f'{package_name}.py')
    start_python_subproccess(program_name, folder, window)


def subprocess_thread(window, sp):
    window.write_event_value('-THREAD-', 'Python Subprocess Thread Started')
    for line in sp.stdout:
        oline = line.decode().rstrip()
        window.write_event_value('-THREAD-', oline)


def start_python_subproccess(command_line, cwd_folder, window: sg.Window):
    python_command = sys.executable  # always use the currently running interpreter to perform the pip!
    if 'pythonw' in python_command:
        python_command = python_command.replace('pythonw', 'python')
    python_command = 'python.exe'
    print(f'CWD forlder {cwd_folder}')
    print(f'Starting subprocess.  Python command = {python_command} command line = {command_line}')
    sp = sg.execute_command_subprocess(python_command, command_line, pipe_output=True, wait=False, cwd=cwd_folder)

    window.start_thread(lambda: subprocess_thread(window, sp), end_key='-THREAD DONE-')


def upload_part1(folder, window: sg.Window):
    remove_folders(folder)
    start_python_subproccess('setup.py sdist bdist_wheel', folder, window)


def upload_part2(folder, username, password, window: sg.Window):
    # for now DO NOT DO THE UPLOAD, signal that it completed instead
    start_python_subproccess(f'-m twine upload -u {username} -p {password} dist/*', folder, window)
    window.write_event_value('-THREAD DONE-', '-THREAD DONE-')

def get_ver_from_file(filename):
    if not filename:
        return ''
    if not os.path.exists(filename):
        return ''
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if 'version=' in line or 'version =' in line:
                if "'" in line:
                    quote = "'"
                elif '"' in line:
                    quote = '"'
                else:
                    print('*** NO VERSION QUOTE on version line in setup.py ***', line)
                    return ''
                quote_start = line.index(quote)
                quote_end = line.index(quote, quote_start + 1)
                version = line[quote_start + 1:quote_end]
                return version
    return ''


def change_ver_in_setup(setup_file, new_version):
    line_found = False
    with open(setup_file, 'r') as f:
        lines = f.readlines()
        # close the file after reading the lines.
        for i, line in enumerate(lines):
            if '    version' in line:
                lines[i] = f'    version="{new_version}",\n'
                line_found = True
                break
        if line_found:
            temp_file = os.path.join(os.path.dirname(setup_file), 'setup_new.py')
            with open(temp_file, 'w') as f:
                f.writelines(lines)
            shutil.copyfile(temp_file, setup_file)
            os.remove(temp_file)


def find_tag_in_string(tag:str, s:str):
    try:
        value = s[s.find(tag) + len(tag):s.find(tag) + len(tag) + 4]
    except:
        value = ''
    # print(value)
    return value


def key_to_tag(key):
    return f'<#{str(key).upper()}#>'


def get_list_from_quoted_list(value):
    start_index = value.find('[')
    # Find the index of the first ']' character
    end_index = value.find(']')
    # Use the index values to extract the string between the '[' and ']' characters
    value = value[start_index + 1:end_index]
    package_list = value.split(',')
    # print(package_list)
    value = ''
    if package_list:                # if more than 1 package found
        for p in package_list:
            p = p[1:-1]             # remove the quotes
            # print(f'package={p}')
            value += f'{p},'
        if value[-1] == ',':
            value = value[:-1]      # remove the last ","
    else:
        value = package_list
    return value


def load_from_setup(setup_file, values:dict, window:sg.Window):
    """
    Reads a setup.py file and creates a dictionary that will be used to fill in entire GUI Window with contents
    :param values:
    :param window:
    :return:
    """
    template_lines = setuppy_template.split("\n")
    new_template = []
    setup_dict = {}
    processing_classifiers = False
    processing_entry_points = False
    with open(setup_file, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            # If currently processing the classifier section
            if processing_classifiers:
                if ']' in line:
                    processing_classifiers = False
                else:
                    line = line.strip()
                    add_classifier(window, line)
            elif processing_entry_points:
                # Entry point format:  'psgissue=PySimpleGUI.PySimpleGUI:main_open_github_issue',
                if '}' in line:
                    processing_entry_points = False
                elif '=' in line:
                    line = line.strip()
                    if line.endswith(','):
                        line = line[:-1]        # if ends with a , then remove it
                    line = line[1:-1]       # remove the quotes
                    command = line.split('=',1)[0]       # Get the command
                    function = line[line.find(':')+1:]           # Everything after the : is the function
                    add_entry_point(window, command, function)
                    # print(f'entry point command = {command} function = {function}')
            elif '=' in line and not line.startswith('#') and not line.startswith('\"\"\"'):
                parm = line.split('=',1)[0].strip()       # Get the parameter name
                value = line.split('=',1)[1].strip()
                # Handle special case - Classifiers.  Look for lines until a "]" is found
                if parm == 'entry_points':       # entry_points is a special case
                    processing_entry_points = True
                if parm == 'classifiers':       # Classifiers is a special case
                    processing_classifiers = True
                elif parm in ('install_requires', 'packages'):
                    value = get_list_from_quoted_list(value)
                    setup_dict[parm.upper()] = value
                else:
                    # Loop through template
                    for l in template_lines:
                        tparm = l.split('=',1)[0].strip()
                        find_tag_in_string(key_to_tag(tparm.upper()), s=l)
                        if tparm == parm and parm not in setup_dict:
                            # print(f'Found {parm} in template')
                            if value.startswith('"') or value.startswith("'"):
                                value = value[1:-2]
                            setup_dict[parm.upper()] = value
            else:   # if not a parm line or other thing, add the line to the output unchanged
                new_template += line
    print(setup_dict)
    return setup_dict

def load_gui(window:sg.Window, setup_dict:dict):
    """
    Loops through all keys in the window.
    If a window's key is found in the setup dictionary, then fill it in with value from setup dictionary
    :param window:
    :param setup_dict:
    :return:
    """
    for key in window.key_dict.keys():
        # print(f'key = {key}')
        try:
            setup_key = key[1:-1]
            # print(f'setup key = {setup_key}')

            if setup_key in setup_dict.keys():
            # if key in setup_dict:
                window[key].update(setup_dict[setup_key])
                # print(f'updaing to {setup_dict[setup_key]}')
        except Exception as e:
            print(e)
            pass


def entry_point_row(item_num):
    row = [sg.pin(sg.Col([[sg.B(sg.SYMBOL_X, border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), k=('-DEL ENTRY POINT-', item_num), tooltip='Delete this item'),
                           sg.T(item_num, k=('-ID-', item_num)),
                           sg.T('Command:'), sg.In(size=(20, 1), k=('-ENTRY POINT COMMAND-', item_num)),sg.T('Function:'), sg.In(size=(20, 1), k=('-ENTRY POINT FUNCTION-', item_num)),
                           ]], k = ('-ENTRY POINT ROW-', item_num)))]
    return row


def classifier_row(item_num):
    row = [sg.pin(sg.Col([[sg.B(sg.SYMBOL_X, border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), k=('-DEL CLASSIFIER-', item_num), tooltip='Delete this item'),
                           sg.T(item_num, k=('-ID-', item_num)),
                           sg.Combo(classifier_list, size=(max_classifier_len, 20), readonly=True, k=('-CLASSIFIER-', item_num)),
                           ]], k = ('-CLASSIFIER ROW-', item_num)))]
    return row


def add_classifier(window:sg.Window, classifier):
    if classifier.endswith(','):
        classifier = classifier[:-1]
    classifier = classifier[1:-1]       # remove the quotes
    # get number of currently used classifier slots
    window['-CLASSIFIER FRAME-'].metadata += 1
    classifier_key = ('-CLASSIFIER-', window['-CLASSIFIER FRAME-'].metadata)
    window.extend_layout(window['-CLASSIFIER SECTION-'], [classifier_row(window['-CLASSIFIER FRAME-'].metadata)])
    window[classifier_key].update(classifier)


def add_entry_point(window:sg.Window, command, function):
    # get number of currently used classifier slots
    window['-ENTRY POINT FRAME-'].metadata += 1
    entry_point_command = ('-ENTRY POINT COMMAND-', window['-ENTRY POINT FRAME-'].metadata)
    entry_point_function = ('-ENTRY POINT FUNCTION-', window['-ENTRY POINT FRAME-'].metadata)
    window.extend_layout(window['-ENTRY POINT SECTION-'], [entry_point_row(window['-ENTRY POINT FRAME-'].metadata)])
    window[entry_point_command].update(command)
    window[entry_point_function].update(function)


def main():
    sg.theme('Neon Yellow 1')
    sg.theme_text_color(sg.theme_button_color_text())
    sg.theme_button_color((sg.theme_button_color_background(), sg.theme_button_color_text()))
    layout_tab_main = [
        [sg.T('Source Folder'), sg.In(setting='', k='-FOLDER-', enable_events=True), sg.FolderBrowse()],
        [sg.T(key='-STATUS-')],
        [sg.T(key='-PACKAGE VER-')],
        [sg.B('Upload'), sg.B('Make setup.py'), sg.B('Load Setup.py'), sg.B('Load Alternate Setup.py'), sg.Checkbox('Scramble Name', key='-SCRAMBLE-')]]
    def Item(text_label, key, tsize=15, isize=20, justification='r', default=''):
        return [sg.Text(text_label, size=tsize, justification=justification), sg.Input(default, size=isize, key=key)]
    tsize = 10


    layout_entry_points = [[sg.Col([[]], k='-ENTRY POINT SECTION-')],
                           [sg.T('+', enable_events=True, k='Add Entry Point', tooltip='Add Another Entry Point')]]

    layout_classifiers_points = [[sg.Col([[]], k='-CLASSIFIER SECTION-')],
                           [sg.T('+', enable_events=True, k='Add Classifier', tooltip='Add Another Entry Point')]]

    layout_package = [
                    [sg.Frame('The Basics', [
                    Item('Package Name:', '-NAME-', default=''),
                    Item('Version:', '-VERSION-'),
                    Item('Description:', '-DESCRIPTION-', isize=60),
                    Item('Author:', '-AUTHOR-', default=''),
                    Item('Author Email:', '-AUTHOR_EMAIL-', default=''),
                    Item('Python Requires:', '-PYTHON_REQUIRES-', default=''),
                    Item('Keywords:', '-KEYWORDS-'),
                    Item('License:', '-LICENSE-'),
                    Item('Project URL:', '-URL-', default=r''),
                    [sg.Text('Install Requires (List of packages. Use "," between each):')],
                    Item('Install Requires:', '-INSTALL_REQUIRES-'),
                    Item('Packages:', '-PACKAGES-'),
                    Item('Package Data:', '-PACKAGE_DATA-'),])],
                    # [sg.Frame('Classifiers', layout_classifiers_points, key='-CLASSIFIER FRAME-', metadata=0)],
                    [sg.Frame('Entry Points', layout_entry_points, key='-ENTRY POINT FRAME-', metadata=0)]
                    ]

    layout_tab_classifier = [sg.Frame('Classifiers', layout_classifiers_points, key='-CLASSIFIER FRAME-', metadata=0)],

    layout_tab_main += layout_package
    layout_tab_main += [[sg.Frame('Output', [[sg.Multiline(reroute_cprint=True, reroute_stdout=True, echo_stdout_stderr=True, autoscroll=True, write_only=True, size=(120, 20), font='Courier 12', auto_refresh=True, k='-OUTPUT-', expand_x=True, expand_y=True)]], expand_y=True, expand_x=True)]]
    layout_tab_main[-1] += [sg.Sizegrip()]
    layout_tab_setup = [[sg.T('PyPI Credentials')],
                        [sg.T('Login:', s=12, justification='r'), sg.Input(setting='', k='-LOGIN-', s=20)],
                        [sg.T('Password:', s=12, justification='r'), sg.Input(setting='', k='-PASSWORD-', password_char='*', s=20)],
                        ]
    # layout_tab_setup += [[sg.B('Save Settings'), sg.B('Restore Settings')]]


    layout = [
        [sg.Image(icon()), sg.Text(f'PySimpleGUI Application Distribution - PyPI Uploader\nVersion {version}', font='_ 16')],
        [sg.TabGroup([[sg.Tab('Upload', layout_tab_main), sg.Tab('Classifiers', layout_tab_classifier), sg.Tab('Settings', layout_tab_setup),]], expand_y=True, expand_x=True)]]

    window = sg.Window('psgup', layout, resizable=True, font='_ 12', right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, enable_close_attempted_event=True,
                       icon=icon(), finalize=True)
    window.set_min_size(window.size)
    window.metadata = 0

    folder = sg.user_settings_get_entry('-FOLDER-', '')
    check_folder(folder, window)
    upload1_started = upload2_started = False            # There are 2 upload parts
    loaded_from_setup = False
    # -------  EVENT LOOP ------
    while True:
        event, values = window.read()
        # sg.cprint(f'{event}',  c='white on purple', font='courier 12')
        # for key, item in values.items():
        #     sg.cprint(f'     {key} = {values[key]}', c='white on green', font='courier 12')
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit', sg.WIN_CLOSED):
            save = popup_yes_no_cancel('Exiting....\nSave settings?')
            if save != 'Cancel':
                if save == 'Yes':
                    sg.popup_quick_message('Saved settings', auto_close_duration=2, text_color=sg.theme_background_color(), background_color=sg.theme_text_color())
                    window.settings_save(values)
                window.close()
                break

        if event == '-THREAD DONE-':    # Thread Finished Event means either done or need to start part 2
            sg.cprint('Thread is done', c='white on red', font='default 12 italic bold')
            if upload1_started:        # if was doing part 1, now start part 2
                upload1_started = False
                print('SKIPPING PART 2!!!')
                upload2_started = True
                upload_part2(folder, values['-LOGIN-'], values['-PASSWORD-'], window)

            elif upload2_started:
                upload2_started = False
                # remove_folders(folder)
        elif event == '-THREAD-':       # Thread event means print text from thread
            sg.cprint(f'Thread {values["-THREAD-"]}', c='white on red', font='default 12 italic')
        if event == '-FOLDER-':
            folder = values['-FOLDER-']
            check_folder(folder, window)
        if event == 'Run Test':
            check_folder(folder, window)
            run_test(folder, window)
        if event == 'Upload':
            # make the setup file
            if values['-SCRAMBLE-']:
                pass        # scramble the name
            new_setup_contents = fill_in_setup_py_template(window, values)
            setup_filename = os.path.join(values['-FOLDER-'], 'setup.py')
            make_setup_file(setup_filename, new_setup_contents)

            upload1_started = True
            upload_part1(folder, window)
        if event == 'Make setup.py':
            new_setup_contents = fill_in_setup_py_template(window, values)
            setup_filename = os.path.join(values['-FOLDER-'], 'setup.py')
            make_setup_file(setup_filename, new_setup_contents)
        if event == 'Load Alternate Setup.py':
            if not loaded_from_setup:
                filename = sg.popup_get_file('setup.py file to load from?', history=True)
                if filename:
                    setup_dict = load_from_setup(filename, values,  window)
                    load_gui(window, setup_dict)
                    loaded_from_setup = True
            else:
                sg.popup_error('You have already loaded the information from the setup.py file.', 'Restart the program if you want to process another folder')

        if event == 'Load Setup.py':
            setup_filename = os.path.join(values['-FOLDER-'], 'setup.py')
            if not loaded_from_setup:
                setup_dict = load_from_setup(setup_filename, values,  window)
                load_gui(window, setup_dict)
                loaded_from_setup = True
            else:
                sg.popup_error('You have already loaded the information from the setup.py file.', 'Restart the program if you want to process another folder')
            window.refresh()
        if event == 'Add Entry Point':
            window['-ENTRY POINT FRAME-'].metadata += 1
            window.extend_layout(window['-ENTRY POINT SECTION-'], [entry_point_row(window['-ENTRY POINT FRAME-'].metadata)])
        if event == 'Add Classifier':
            window['-CLASSIFIER FRAME-'].metadata += 1
            window.extend_layout(window['-CLASSIFIER SECTION-'], [classifier_row(window['-CLASSIFIER FRAME-'].metadata)])
        if event[0] == '-DEL ENTRY POINT-':
            window[('-ENTRY POINT ROW-', event[1])].update(visible=False)
        if event[0] == '-DEL CLASSIFIER-':
            window[('-CLASSIFIER ROW-', event[1])].update(visible=False)
        # ------- Standard Right-Click Menu Handling -------
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, location=window.current_location(), no_buttons=True, no_sizegrip=True)
        # except Exception as e:
        #     sg.Print('WHOA!  Exception happened in event loop!', e)
    window.close()


def icon():
    return \
        b'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'


if __name__ == '__main__':
    sorted_classifiers = [
        "Development Status :: 1 - Planning",
        "Development Status :: 2 - Pre-Alpha",
        "Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "Development Status :: 6 - Mature",
        "Development Status :: 7 - Inactive",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Environment :: Console :: Framebuffer",
        "Environment :: Console :: Newt",
        "Environment :: Console :: svgalib",
        "Environment :: GPU",
        "Environment :: GPU :: NVIDIA CUDA",
        "Environment :: GPU :: NVIDIA CUDA :: 1.0",
        "Environment :: GPU :: NVIDIA CUDA :: 1.1",
        "Environment :: GPU :: NVIDIA CUDA :: 2.0",
        "Environment :: GPU :: NVIDIA CUDA :: 2.1",
        "Environment :: GPU :: NVIDIA CUDA :: 2.2",
        "Environment :: GPU :: NVIDIA CUDA :: 2.3",
        "Environment :: GPU :: NVIDIA CUDA :: 3.0",
        "Environment :: GPU :: NVIDIA CUDA :: 3.1",
        "Environment :: GPU :: NVIDIA CUDA :: 3.2",
        "Environment :: GPU :: NVIDIA CUDA :: 4.0",
        "Environment :: GPU :: NVIDIA CUDA :: 4.1",
        "Environment :: GPU :: NVIDIA CUDA :: 4.2",
        "Environment :: GPU :: NVIDIA CUDA :: 5.0",
        "Environment :: GPU :: NVIDIA CUDA :: 5.5",
        "Environment :: GPU :: NVIDIA CUDA :: 6.0",
        "Environment :: GPU :: NVIDIA CUDA :: 6.5",
        "Environment :: GPU :: NVIDIA CUDA :: 7.0",
        "Environment :: GPU :: NVIDIA CUDA :: 7.5",
        "Environment :: GPU :: NVIDIA CUDA :: 8.0",
        "Environment :: GPU :: NVIDIA CUDA :: 9.0",
        "Environment :: GPU :: NVIDIA CUDA :: 9.1",
        "Environment :: GPU :: NVIDIA CUDA :: 9.2",
        "Environment :: GPU :: NVIDIA CUDA :: 10.0",
        "Environment :: GPU :: NVIDIA CUDA :: 10.1",
        "Environment :: GPU :: NVIDIA CUDA :: 10.2",
        "Environment :: GPU :: NVIDIA CUDA :: 11",
        "Environment :: GPU :: NVIDIA CUDA :: 11.0",
        "Environment :: GPU :: NVIDIA CUDA :: 11.1",
        "Environment :: GPU :: NVIDIA CUDA :: 11.2",
        "Environment :: GPU :: NVIDIA CUDA :: 11.3",
        "Environment :: GPU :: NVIDIA CUDA :: 11.4",
        "Environment :: GPU :: NVIDIA CUDA :: 11.5",
        "Environment :: GPU :: NVIDIA CUDA :: 11.6",
        "Environment :: GPU :: NVIDIA CUDA :: 11.7",
        "Environment :: GPU :: NVIDIA CUDA :: 11.8",
        "Environment :: GPU :: NVIDIA CUDA :: 12",
        "Environment :: GPU :: NVIDIA CUDA :: 12 :: 12.0",
        "Environment :: GPU :: NVIDIA CUDA :: 12 :: 12.1",
        "Environment :: GPU :: NVIDIA CUDA :: 12 :: 12.2",
        "Environment :: Handhelds/PDA's",
        "Environment :: MacOS X",
        "Environment :: MacOS X :: Aqua",
        "Environment :: MacOS X :: Carbon",
        "Environment :: MacOS X :: Cocoa",
        "Environment :: No Input/Output (Daemon)",
        "Environment :: OpenStack",
        "Environment :: Other Environment",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Environment :: Web Environment :: Buffet",
        "Environment :: Web Environment :: Mozilla",
        "Environment :: Web Environment :: ToscaWidgets",
        "Environment :: WebAssembly",
        "Environment :: WebAssembly :: Emscripten",
        "Environment :: WebAssembly :: WASI",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Environment :: X11 Applications :: GTK",
        "Environment :: X11 Applications :: Gnome",
        "Environment :: X11 Applications :: KDE",
        "Environment :: X11 Applications :: Qt",
        "Framework :: AWS CDK",
        "Framework :: AWS CDK :: 1",
        "Framework :: AWS CDK :: 2",
        "Framework :: AiiDA",
        "Framework :: Ansible",
        "Framework :: AnyIO",
        "Framework :: Apache Airflow",
        "Framework :: Apache Airflow :: Provider",
        "Framework :: AsyncIO",
        "Framework :: BEAT",
        "Framework :: BFG",
        "Framework :: Bob",
        "Framework :: Bottle",
        "Framework :: Buildout",
        "Framework :: Buildout :: Extension",
        "Framework :: Buildout :: Recipe",
        "Framework :: CastleCMS",
        "Framework :: CastleCMS :: Theme",
        "Framework :: Celery",
        "Framework :: Chandler",
        "Framework :: CherryPy",
        "Framework :: CubicWeb",
        "Framework :: Dash",
        "Framework :: Datasette",
        "Framework :: Django",
        "Framework :: Django :: 1",
        "Framework :: Django :: 1.4",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django CMS",
        "Framework :: Django CMS :: 3.4",
        "Framework :: Django CMS :: 3.5",
        "Framework :: Django CMS :: 3.6",
        "Framework :: Django CMS :: 3.7",
        "Framework :: Django CMS :: 3.8",
        "Framework :: Django CMS :: 3.9",
        "Framework :: Django CMS :: 3.10",
        "Framework :: Django CMS :: 3.11",
        "Framework :: Django CMS :: 4.0",
        "Framework :: Django CMS :: 4.1",
        "Framework :: FastAPI",
        "Framework :: Flake8",
        "Framework :: Flask",
        "Framework :: Hatch",
        "Framework :: Hypothesis",
        "Framework :: IDLE",
        "Framework :: IPython",
        "Framework :: Jupyter",
        "Framework :: Jupyter :: JupyterLab",
        "Framework :: Jupyter :: JupyterLab :: 1",
        "Framework :: Jupyter :: JupyterLab :: 2",
        "Framework :: Jupyter :: JupyterLab :: 3",
        "Framework :: Jupyter :: JupyterLab :: 4",
        "Framework :: Jupyter :: JupyterLab :: Extensions",
        "Framework :: Jupyter :: JupyterLab :: Extensions :: Mime Renderers",
        "Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt",
        "Framework :: Jupyter :: JupyterLab :: Extensions :: Themes",
        "Framework :: Kedro",
        "Framework :: Lektor",
        "Framework :: Masonite",
        "Framework :: Matplotlib",
        "Framework :: MkDocs",
        "Framework :: Nengo",
        "Framework :: Odoo",
        "Framework :: Odoo :: 8.0",
        "Framework :: Odoo :: 9.0",
        "Framework :: Odoo :: 10.0",
        "Framework :: Odoo :: 11.0",
        "Framework :: Odoo :: 12.0",
        "Framework :: Odoo :: 13.0",
        "Framework :: Odoo :: 14.0",
        "Framework :: Odoo :: 15.0",
        "Framework :: Odoo :: 16.0",
        "Framework :: Opps",
        "Framework :: Paste",
        "Framework :: Pelican",
        "Framework :: Pelican :: Plugins",
        "Framework :: Pelican :: Themes",
        "Framework :: Plone",
        "Framework :: Plone :: 3.2",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 5.3",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: Core",
        "Framework :: Plone :: Distribution",
        "Framework :: Plone :: Theme",
        "Framework :: Pycsou",
        "Framework :: Pydantic",
        "Framework :: Pydantic :: 1",
        "Framework :: Pydantic :: 2",
        "Framework :: Pylons",
        "Framework :: Pyramid",
        "Framework :: Pytest",
        "Framework :: Review Board",
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library",
        "Framework :: Robot Framework :: Tool",
        "Framework :: Scrapy",
        "Framework :: Setuptools Plugin",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Extension",
        "Framework :: Sphinx :: Theme",
        "Framework :: Trac",
        "Framework :: Trio",
        "Framework :: Tryton",
        "Framework :: TurboGears",
        "Framework :: TurboGears :: Applications",
        "Framework :: TurboGears :: Widgets",
        "Framework :: Twisted",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 1",
        "Framework :: Wagtail :: 2",
        "Framework :: Wagtail :: 3",
        "Framework :: Wagtail :: 4",
        "Framework :: Wagtail :: 5",
        "Framework :: ZODB",
        "Framework :: Zope",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Zope :: 2",
        "Framework :: Zope :: 3",
        "Framework :: Zope :: 4",
        "Framework :: Zope :: 5",
        "Framework :: aiohttp",
        "Framework :: cocotb",
        "Framework :: napari",
        "Framework :: tox",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Religion",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: Aladdin Free Public License (AFPL)",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "License :: CeCILL-B Free Software License Agreement (CECILL-B)",
        "License :: CeCILL-C Free Software License Agreement (CECILL-C)",
        "License :: DFSG approved",
        "License :: Eiffel Forum License (EFL)",
        "License :: Free For Educational Use",
        "License :: Free For Home Use",
        "License :: Free To Use But Restricted",
        "License :: Free for non-commercial use",
        "License :: Freely Distributable",
        "License :: Freeware",
        "License :: GUST Font License 1.0",
        "License :: GUST Font License 2006-09-30",
        "License :: Netscape Public License (NPL)",
        "License :: Nokia Open Source License (NOKOS)",
        "License :: OSI Approved",
        "License :: OSI Approved :: Academic Free License (AFL)",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: Apple Public Source License",
        "License :: OSI Approved :: Artistic License",
        "License :: OSI Approved :: Attribution Assurance License",
        "License :: OSI Approved :: BSD License",
        "License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)",
        "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
        "License :: OSI Approved :: Common Development and Distribution License 1.0 (CDDL-1.0)",
        "License :: OSI Approved :: Common Public License",
        "License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)",
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
        "License :: OSI Approved :: Eiffel Forum License",
        "License :: OSI Approved :: European Union Public Licence 1.0 (EUPL 1.0)",
        "License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "License :: OSI Approved :: GNU Free Documentation License (FDL)",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "License :: OSI Approved :: Historical Permission Notice and Disclaimer (HPND)",
        "License :: OSI Approved :: IBM Public License",
        "License :: OSI Approved :: ISC License (ISCL)",
        "License :: OSI Approved :: Intel Open Source License",
        "License :: OSI Approved :: Jabber Open Source License",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: MIT No Attribution License (MIT-0)",
        "License :: OSI Approved :: MITRE Collaborative Virtual Workspace License (CVW)",
        "License :: OSI Approved :: MirOS License (MirOS)",
        "License :: OSI Approved :: Motosoto License",
        "License :: OSI Approved :: Mozilla Public License 1.0 (MPL)",
        "License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "License :: OSI Approved :: Mulan Permissive Software License v2 (MulanPSL-2.0)",
        "License :: OSI Approved :: Nethack General Public License",
        "License :: OSI Approved :: Nokia Open Source License",
        "License :: OSI Approved :: Open Group Test Suite License",
        "License :: OSI Approved :: Open Software License 3.0 (OSL-3.0)",
        "License :: OSI Approved :: PostgreSQL License",
        "License :: OSI Approved :: Python License (CNRI Python License)",
        "License :: OSI Approved :: Python Software Foundation License",
        "License :: OSI Approved :: Qt Public License (QPL)",
        "License :: OSI Approved :: Ricoh Source Code Public License",
        "License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)",
        "License :: OSI Approved :: Sleepycat License",
        "License :: OSI Approved :: Sun Industry Standards Source License (SISSL)",
        "License :: OSI Approved :: Sun Public License",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "License :: OSI Approved :: Universal Permissive License (UPL)",
        "License :: OSI Approved :: University of Illinois/NCSA Open Source License",
        "License :: OSI Approved :: Vovida Software License 1.0",
        "License :: OSI Approved :: W3C License",
        "License :: OSI Approved :: X.Net License",
        "License :: OSI Approved :: Zope Public License",
        "License :: OSI Approved :: zlib/libpng License",
        "License :: Other/Proprietary License",
        "License :: Public Domain",
        "License :: Repoze Public License",
        "Natural Language :: Afrikaans",
        "Natural Language :: Arabic",
        "Natural Language :: Basque",
        "Natural Language :: Bengali",
        "Natural Language :: Bosnian",
        "Natural Language :: Bulgarian",
        "Natural Language :: Cantonese",
        "Natural Language :: Catalan",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Chinese (Traditional)",
        "Natural Language :: Croatian",
        "Natural Language :: Czech",
        "Natural Language :: Danish",
        "Natural Language :: Dutch",
        "Natural Language :: English",
        "Natural Language :: Esperanto",
        "Natural Language :: Finnish",
        "Natural Language :: French",
        "Natural Language :: Galician",
        "Natural Language :: German",
        "Natural Language :: Greek",
        "Natural Language :: Hebrew",
        "Natural Language :: Hindi",
        "Natural Language :: Hungarian",
        "Natural Language :: Icelandic",
        "Natural Language :: Indonesian",
        "Natural Language :: Irish",
        "Natural Language :: Italian",
        "Natural Language :: Japanese",
        "Natural Language :: Javanese",
        "Natural Language :: Korean",
        "Natural Language :: Latin",
        "Natural Language :: Latvian",
        "Natural Language :: Lithuanian",
        "Natural Language :: Macedonian",
        "Natural Language :: Malay",
        "Natural Language :: Marathi",
        "Natural Language :: Nepali",
        "Natural Language :: Norwegian",
        "Natural Language :: Panjabi",
        "Natural Language :: Persian",
        "Natural Language :: Polish",
        "Natural Language :: Portuguese",
        "Natural Language :: Portuguese (Brazilian)",
        "Natural Language :: Romanian",
        "Natural Language :: Russian",
        "Natural Language :: Serbian",
        "Natural Language :: Slovak",
        "Natural Language :: Slovenian",
        "Natural Language :: Spanish",
        "Natural Language :: Swedish",
        "Natural Language :: Tamil",
        "Natural Language :: Telugu",
        "Natural Language :: Thai",
        "Natural Language :: Tibetan",
        "Natural Language :: Turkish",
        "Natural Language :: Ukrainian",
        "Natural Language :: Urdu",
        "Natural Language :: Vietnamese",
        "Operating System :: Android",
        "Operating System :: BeOS",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS 9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: MS-DOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 3.1 or Earlier",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Operating System :: Microsoft :: Windows :: Windows 95/98/2000",
        "Operating System :: Microsoft :: Windows :: Windows CE",
        "Operating System :: Microsoft :: Windows :: Windows NT/2000",
        "Operating System :: Microsoft :: Windows :: Windows Server 2003",
        "Operating System :: Microsoft :: Windows :: Windows Server 2008",
        "Operating System :: Microsoft :: Windows :: Windows Vista",
        "Operating System :: Microsoft :: Windows :: Windows XP",
        "Operating System :: OS Independent",
        "Operating System :: OS/2",
        "Operating System :: Other OS",
        "Operating System :: PDA Systems",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: AIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: BSD :: BSD/OS",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Operating System :: POSIX :: BSD :: NetBSD",
        "Operating System :: POSIX :: BSD :: OpenBSD",
        "Operating System :: POSIX :: GNU Hurd",
        "Operating System :: POSIX :: HP-UX",
        "Operating System :: POSIX :: IRIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: Other",
        "Operating System :: POSIX :: SCO",
        "Operating System :: POSIX :: SunOS/Solaris",
        "Operating System :: PalmOS",
        "Operating System :: RISC OS",
        "Operating System :: Unix",
        "Operating System :: iOS",
        "Programming Language :: APL",
        "Programming Language :: ASP",
        "Programming Language :: Ada",
        "Programming Language :: Assembly",
        "Programming Language :: Awk",
        "Programming Language :: Basic",
        "Programming Language :: C",
        "Programming Language :: C#",
        "Programming Language :: C++",
        "Programming Language :: Cold Fusion",
        "Programming Language :: Cython",
        "Programming Language :: D",
        "Programming Language :: Delphi/Kylix",
        "Programming Language :: Dylan",
        "Programming Language :: Eiffel",
        "Programming Language :: Emacs-Lisp",
        "Programming Language :: Erlang",
        "Programming Language :: Euler",
        "Programming Language :: Euphoria",
        "Programming Language :: F#",
        "Programming Language :: Forth",
        "Programming Language :: Fortran",
        "Programming Language :: Haskell",
        "Programming Language :: Java",
        "Programming Language :: JavaScript",
        "Programming Language :: Kotlin",
        "Programming Language :: Lisp",
        "Programming Language :: Logo",
        "Programming Language :: Lua",
        "Programming Language :: ML",
        "Programming Language :: Modula",
        "Programming Language :: OCaml",
        "Programming Language :: Object Pascal",
        "Programming Language :: Objective C",
        "Programming Language :: Other",
        "Programming Language :: Other Scripting Engines",
        "Programming Language :: PHP",
        "Programming Language :: PL/SQL",
        "Programming Language :: PROGRESS",
        "Programming Language :: Pascal",
        "Programming Language :: Perl",
        "Programming Language :: Pike",
        "Programming Language :: Pliant",
        "Programming Language :: Prolog",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: 2.3",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: IronPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: Stackless",
        "Programming Language :: R",
        "Programming Language :: REBOL",
        "Programming Language :: Rexx",
        "Programming Language :: Ruby",
        "Programming Language :: Rust",
        "Programming Language :: SQL",
        "Programming Language :: Scheme",
        "Programming Language :: Simula",
        "Programming Language :: Smalltalk",
        "Programming Language :: Tcl",
        "Programming Language :: Unix Shell",
        "Programming Language :: Visual Basic",
        "Programming Language :: XBasic",
        "Programming Language :: YACC",
        "Programming Language :: Zope",
        "Topic :: Adaptive Technologies",
        "Topic :: Artistic Software",
        "Topic :: Communications",
        "Topic :: Communications :: BBS",
        "Topic :: Communications :: Chat",
        "Topic :: Communications :: Chat :: ICQ",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Communications :: Chat :: Unix Talk",
        "Topic :: Communications :: Conferencing",
        "Topic :: Communications :: Email",
        "Topic :: Communications :: Email :: Address Book",
        "Topic :: Communications :: Email :: Email Clients (MUA)",
        "Topic :: Communications :: Email :: Filters",
        "Topic :: Communications :: Email :: Mail Transport Agents",
        "Topic :: Communications :: Email :: Mailing List Servers",
        "Topic :: Communications :: Email :: Post-Office",
        "Topic :: Communications :: Email :: Post-Office :: IMAP",
        "Topic :: Communications :: Email :: Post-Office :: POP3",
        "Topic :: Communications :: FIDO",
        "Topic :: Communications :: Fax",
        "Topic :: Communications :: File Sharing",
        "Topic :: Communications :: File Sharing :: Gnutella",
        "Topic :: Communications :: File Sharing :: Napster",
        "Topic :: Communications :: Ham Radio",
        "Topic :: Communications :: Internet Phone",
        "Topic :: Communications :: Telephony",
        "Topic :: Communications :: Usenet News",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Database :: Front-Ends",
        "Topic :: Desktop Environment",
        "Topic :: Desktop Environment :: File Managers",
        "Topic :: Desktop Environment :: GNUstep",
        "Topic :: Desktop Environment :: Gnome",
        "Topic :: Desktop Environment :: K Desktop Environment (KDE)",
        "Topic :: Desktop Environment :: K Desktop Environment (KDE) :: Themes",
        "Topic :: Desktop Environment :: PicoGUI",
        "Topic :: Desktop Environment :: PicoGUI :: Applications",
        "Topic :: Desktop Environment :: PicoGUI :: Themes",
        "Topic :: Desktop Environment :: Screen Savers",
        "Topic :: Desktop Environment :: Window Managers",
        "Topic :: Desktop Environment :: Window Managers :: Afterstep",
        "Topic :: Desktop Environment :: Window Managers :: Afterstep :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: Applets",
        "Topic :: Desktop Environment :: Window Managers :: Blackbox",
        "Topic :: Desktop Environment :: Window Managers :: Blackbox :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: CTWM",
        "Topic :: Desktop Environment :: Window Managers :: CTWM :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: Enlightenment",
        "Topic :: Desktop Environment :: Window Managers :: Enlightenment :: Epplets",
        "Topic :: Desktop Environment :: Window Managers :: Enlightenment :: Themes DR15",
        "Topic :: Desktop Environment :: Window Managers :: Enlightenment :: Themes DR16",
        "Topic :: Desktop Environment :: Window Managers :: Enlightenment :: Themes DR17",
        "Topic :: Desktop Environment :: Window Managers :: FVWM",
        "Topic :: Desktop Environment :: Window Managers :: FVWM :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: Fluxbox",
        "Topic :: Desktop Environment :: Window Managers :: Fluxbox :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: IceWM",
        "Topic :: Desktop Environment :: Window Managers :: IceWM :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: MetaCity",
        "Topic :: Desktop Environment :: Window Managers :: MetaCity :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: Oroborus",
        "Topic :: Desktop Environment :: Window Managers :: Oroborus :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: Sawfish",
        "Topic :: Desktop Environment :: Window Managers :: Sawfish :: Themes 0.30",
        "Topic :: Desktop Environment :: Window Managers :: Sawfish :: Themes pre-0.30",
        "Topic :: Desktop Environment :: Window Managers :: Waimea",
        "Topic :: Desktop Environment :: Window Managers :: Waimea :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: Window Maker",
        "Topic :: Desktop Environment :: Window Managers :: Window Maker :: Applets",
        "Topic :: Desktop Environment :: Window Managers :: Window Maker :: Themes",
        "Topic :: Desktop Environment :: Window Managers :: XFCE",
        "Topic :: Desktop Environment :: Window Managers :: XFCE :: Themes",
        "Topic :: Documentation",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Topic :: Education :: Testing",
        "Topic :: File Formats",
        "Topic :: File Formats :: JSON",
        "Topic :: File Formats :: JSON :: JSON Schema",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Arcade",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Games/Entertainment :: First Person Shooters",
        "Topic :: Games/Entertainment :: Fortune Cookies",
        "Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)",
        "Topic :: Games/Entertainment :: Puzzle Games",
        "Topic :: Games/Entertainment :: Real Time Strategy",
        "Topic :: Games/Entertainment :: Role-Playing",
        "Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games",
        "Topic :: Games/Entertainment :: Simulation",
        "Topic :: Games/Entertainment :: Turn Based Strategy",
        "Topic :: Home Automation",
        "Topic :: Internet",
        "Topic :: Internet :: File Transfer Protocol (FTP)",
        "Topic :: Internet :: Finger",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Internet :: WAP",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Internet :: WWW/HTTP :: Session",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
        "Topic :: Internet :: XMPP",
        "Topic :: Internet :: Z39.50",
        "Topic :: Multimedia",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
        "Topic :: Multimedia :: Graphics :: Capture",
        "Topic :: Multimedia :: Graphics :: Capture :: Digital Camera",
        "Topic :: Multimedia :: Graphics :: Capture :: Scanners",
        "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
        "Topic :: Multimedia :: Graphics :: Editors",
        "Topic :: Multimedia :: Graphics :: Editors :: Raster-Based",
        "Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Topic :: Multimedia :: Graphics :: Viewers",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: CD Audio",
        "Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Playing",
        "Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Ripping",
        "Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Writing",
        "Topic :: Multimedia :: Sound/Audio :: Capture/Recording",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
        "Topic :: Multimedia :: Sound/Audio :: Editors",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
        "Topic :: Multimedia :: Sound/Audio :: Mixers",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "Topic :: Multimedia :: Sound/Audio :: Players :: MP3",
        "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Capture",
        "Topic :: Multimedia :: Video :: Conversion",
        "Topic :: Multimedia :: Video :: Display",
        "Topic :: Multimedia :: Video :: Non-Linear Editor",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Office/Business :: Groupware",
        "Topic :: Office/Business :: News/Diary",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Printing",
        "Topic :: Religion",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Artificial Life",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Hydrology",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Oceanography",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Sociology",
        "Topic :: Sociology :: Genealogy",
        "Topic :: Sociology :: History",
        "Topic :: Software Development",
        "Topic :: Software Development :: Assemblers",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Disassemblers",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Java Libraries",
        "Topic :: Software Development :: Libraries :: PHP Classes",
        "Topic :: Software Development :: Libraries :: Perl Modules",
        "Topic :: Software Development :: Libraries :: Pike Modules",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Ruby Modules",
        "Topic :: Software Development :: Libraries :: Tcl Extensions",
        "Topic :: Software Development :: Libraries :: pygame",
        "Topic :: Software Development :: Localization",
        "Topic :: Software Development :: Object Brokering",
        "Topic :: Software Development :: Object Brokering :: CORBA",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Topic :: Software Development :: Testing :: BDD",
        "Topic :: Software Development :: Testing :: Mocking",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Topic :: Software Development :: Testing :: Unit",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Version Control",
        "Topic :: Software Development :: Version Control :: Bazaar",
        "Topic :: Software Development :: Version Control :: CVS",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Software Development :: Version Control :: Mercurial",
        "Topic :: Software Development :: Version Control :: RCS",
        "Topic :: Software Development :: Version Control :: SCCS",
        "Topic :: Software Development :: Widget Sets",
        "Topic :: System",
        "Topic :: System :: Archiving",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: System :: Archiving :: Compression",
        "Topic :: System :: Archiving :: Mirroring",
        "Topic :: System :: Archiving :: Packaging",
        "Topic :: System :: Benchmark",
        "Topic :: System :: Boot",
        "Topic :: System :: Boot :: Init",
        "Topic :: System :: Clustering",
        "Topic :: System :: Console Fonts",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Emulators",
        "Topic :: System :: Filesystems",
        "Topic :: System :: Hardware",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: System :: Hardware :: Mainframes",
        "Topic :: System :: Hardware :: Symmetric Multi-processing",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB)",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Audio",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Audio/Video (AV)",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Communications Device Class (CDC)",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Diagnostic Device",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Hub",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Human Interface Device (HID)",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Mass Storage",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Miscellaneous",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Printer",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Smart Card",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Vendor",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Video (UVC)",
        "Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Wireless Controller",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: System :: Networking :: Monitoring :: Hardware Watchdog",
        "Topic :: System :: Networking :: Time Synchronization",
        "Topic :: System :: Operating System",
        "Topic :: System :: Operating System Kernels",
        "Topic :: System :: Operating System Kernels :: BSD",
        "Topic :: System :: Operating System Kernels :: GNU Hurd",
        "Topic :: System :: Operating System Kernels :: Linux",
        "Topic :: System :: Power (UPS)",
        "Topic :: System :: Recovery Tools",
        "Topic :: System :: Shells",
        "Topic :: System :: Software Distribution",
        "Topic :: System :: System Shells",
        "Topic :: System :: Systems Administration",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
        "Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP",
        "Topic :: System :: Systems Administration :: Authentication/Directory :: NIS",
        "Topic :: Terminals",
        "Topic :: Terminals :: Serial",
        "Topic :: Terminals :: Telnet",
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
        "Topic :: Text Editors",
        "Topic :: Text Editors :: Documentation",
        "Topic :: Text Editors :: Emacs",
        "Topic :: Text Editors :: Integrated Development Environments (IDE)",
        "Topic :: Text Editors :: Text Processing",
        "Topic :: Text Editors :: Word Processors",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Fonts",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing :: Markup",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: LaTeX",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: SGML",
        "Topic :: Text Processing :: Markup :: VRML",
        "Topic :: Text Processing :: Markup :: XML",
        "Topic :: Text Processing :: Markup :: reStructuredText",
        "Topic :: Utilities",
        "Typing :: Stubs Only",
        "Typing :: Typed",
    ]
    classifier_list = sorted_classifiers
    max_classifier_len = len(max(classifier_list, key=len))
    main()