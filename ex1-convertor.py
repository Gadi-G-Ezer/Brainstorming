import csv
import sys

METER_TO_FEET_CONVERSION = 3.28084


def get_content(path: str):
    """
    function receives path to csv file and return its content as a list of lists.
    i.e. each element in the list represent a single row of which value is given by a list.
    :param path: string
    :return content: list
    """
    try:
        with open(path, 'r') as f:
            content = [row for row in csv.reader(f)]
    except FileNotFoundError as error:
        print('Error: ', error)
        sys.exit(1)
    except OSError as error:
        print('Error: ', error)
        sys.exit(1)
    except BaseException as error:
        print('Error: ', error)
        sys.exit(1)
    else:
        return content


def content_validation_and_preparation(content: list):
    """
    function verifies the following:
        1) list is not empty
        2) list contains lists
        3) list elements contain single value
        4) list elements contains number
    and return list of lists that contains floats in the following form: [[meter, feet], [meter, feet],...]
    :param content: list
    :return meter_feet_data_list: list
    """
    meter_feet_data_list = []

    if not content:
        raise FileExistsError("File is empty!")
    elif not isinstance(content, list):
        raise TypeError('Given input should be a list!')
    elif not all((True if isinstance(element, list) else False for element in content)):
        raise TypeError('c, should be lists!')
    elif not all((True if len(element) == 1 else False for element in content)):
        raise SystemError('Expect to contain single value within an element of the given lists!')

    for index, element in enumerate(content):
        try:
            if index == 0 and not str(element[0]).isdigit():
                meter_feet_data_list.append([element[0], 'feet'])
            else:
                meter_feet_data_list.append([float(element[0]), float(element[0])*METER_TO_FEET_CONVERSION])
        except ValueError('Numerical values are required!') as error:
            print('Error: ', error)
            sys.exit(1)

    return meter_feet_data_list


def fit_to_feet(path:str, content: list):
    try:
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(content)
    except BaseException as error:
        print("It's not you, It's us :( \n", error)
    else:
        print(f'The new file is ready at: {path}')


def main():
    if len(sys.argv) != 2:
        raise SystemError('Missing path to CSV file!')

    print(sys.argv[1])
    source_path = sys.argv[1]
    new_path = source_path[:-4] + '_new.csv'

    content = get_content(source_path)
    list_values = content_validation_and_preparation(content)
    fit_to_feet(new_path, list_values)


if __name__ == '__main__':
    main()








