SOURCE_PATH = r'D:\Academy\Studying\Bootcamp\ITC Feb 23\Assignments\Python_1\Questions\ex2-alice.txt'
DESTINATION_PATH = r'D:\Academy\Studying\Bootcamp\ITC Feb 23\Assignments\Python_1\Solution'


def copaste(source, destination):
    """
    the function receives a path to a file (as an absolute path) and copies it to a given folder (as an
    absolute path). For example: copaste(r"C:/source_directory/test_file.txt", r"C:/dest_directory")
    This run should copy the file test_file.txt from folder C:/source_directory to the folder C:/dest_directory.
    :param source:
    :param destination:
    :return: None
    """
    file_name = source[-1*(1 + source[::-1].find('\\')):]
    mode_flag = ''
    try:
        file = open(source, 'rb')
        content = file.read()
        mode_flag = 'wb'
    except UnicodeDecodeError:
        file = open(source, 'rt')
        content = file.read()
        mode_flag = 'wt'
    finally:
        new_file = open(destination+file_name, mode_flag)
        new_file.write(content)
        file.close()
        new_file.close()


def main():
    copaste(SOURCE_PATH, DESTINATION_PATH)


if __name__ == '__main__':
    main()
