import PySimpleGUI as sg
import os
import shutil
import sys

version = __version__ = "1.0"

"""

Installs Upload to PyPI quickly and easily

1.0 24-Oct-2023 - Let the fun begin!

To upload to PyPI (at least on Python 3.6 this works)...
Make sure working folder is the one with setup.py
    python setup.py sdist bdist_wheel
    python -m twine upload -u USERNAME -p PASSWORD dist/*


"""

import re

alpha_num_order = lambda string: ''.join([format(int(x), '05d') if x.isdigit() else x for x in re.split(r'(\d+)', string)])


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
    lines = [f'from .{package_name} import *']
    with open(init_filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


def check_folder(folder, window: sg.Window):
    if os.path.isdir(folder):
        window['-STATUS-'].update('Valid folder')
    else:
        window['-STATUS-'].update('')
        return

    package_name = os.path.basename(folder)
    window['-STATUS-'].update(f'Package name: {package_name}')
    program_folder = os.path.join(folder, package_name)
    init_name = os.path.join(program_folder, '__init__.py')
    program_name = os.path.join(program_folder, f'{package_name}.py')
    setup_name = os.path.join(folder, 'setup.py')
    ver_from_program = get_ver_from_file(program_name)
    window['-PACKAGE VER-'].update(ver_from_program)
    print(program_name)
    make_init_file(init_name, package_name)
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


def upload(folder, window: sg.Window):
    remove_folders(folder)
    start_python_subproccess('setup.py sdist bdist_wheel', folder, window)


def upload_part2(folder, username, password, window: sg.Window):
    start_python_subproccess(f'-m twine upload -u {username} -p {password} dist/*', folder, window)


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


def main():
    sg.theme('Neon Yellow 1')
    sg.theme_text_color(sg.theme_button_color_text())
    sg.theme_button_color((sg.theme_button_color_background(), sg.theme_button_color_text()))
    layout_tab_main = [
        [sg.T('Source Folder'), sg.In(setting='', k='-FOLDER-', enable_events=True), sg.FolderBrowse()],
        [sg.T(key='-STATUS-')],
        [sg.T(key='-PACKAGE VER-')],
        [sg.B('Upload'), sg.B('Check'), sg.B('Exit'), ],
        [sg.Multiline(reroute_cprint=True, reroute_stdout=True, echo_stdout_stderr=True, write_only=True, size=(120, 20), font='Courier 12', auto_refresh=True, k='-OUTPUT-',
                      expand_x=True, expand_y=True, autoscroll_only_at_bottom=True)],
    ]
    layout_tab_main[-1] += [sg.Sizegrip()]
    layout_tab_setup = [[sg.T('PyPI Credentials')],
                        [sg.T('Login:', s=12, justification='r'), sg.Input(setting='', k='-LOGIN-', s=20)],
                        [sg.T('Password:', s=12, justification='r'), sg.Input(setting='', k='-PASSWORD-', password_char='*', s=20)],
                        ]
    # layout_tab_setup += [[sg.B('Save Settings'), sg.B('Restore Settings')]]

    layout = [
        [sg.Image(icon()), sg.Text(f'psgup - PyPI Package Uploader\nVersion {version}', font='_ 16')],
        [sg.TabGroup([[sg.Tab('Upload', layout_tab_main), sg.Tab('Settings', layout_tab_setup)]], expand_y=True, expand_x=True)]]

    window = sg.Window('psgup', layout, resizable=True, font='_ 12', right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, enable_close_attempted_event=True,
                       icon=icon(), finalize=True)
    window.set_min_size(window.size)

    folder = sg.user_settings_get_entry('-FOLDER-', '')
    check_folder(folder, window)
    upload_part1 = False
    # -------  EVENT LOOP ------
    while True:
        try:
            event, values = window.read()
            # sg.cprint(f'{event}\n{values}',  c='white on green', font='courier 12')
            if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit', sg.WIN_CLOSED):
                save = popup_yes_no_cancel('Exiting....\nSave settings?')
                if save != 'Cancel':
                    if save == 'Yes':
                        sg.popup_quick_message('Saved settings', auto_close_duration=2, text_color=sg.theme_background_color(), background_color=sg.theme_text_color())
                        window.settings_save(values)
                    window.close()
                    break

            if event == '-THREAD DONE-':
                sg.cprint('Thread is done', c='white on red', font='default 12 italic')
                if upload_part1:
                    upload_part1 = False
                    upload_part2(folder, values['-LOGIN-'], values['-PASSWORD-'], window)
            elif event == '-THREAD-':
                sg.cprint(f'Thread {values["-THREAD-"]}', c='white on red', font='default 12 italic')
            if event == 'Run Test':
                check_folder(folder, window)
                run_test(folder, window)
            if event == 'Upload':
                upload_part1 = True
                folder = values['-FOLDER-']
                upload(folder, window)

            # ------- Standard Right-Click Menu Handling -------
            if event == 'Edit Me':
                sg.execute_editor(__file__)
            elif event == 'Version':
                sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, location=window.current_location(), no_buttons=True, no_sizegrip=True)
        except Exception as e:
            sg.Print('WHOA!  Exception happened in event loop!', e)
    window.close()


def icon():
    return \
        b'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'


if __name__ == '__main__':
    main()