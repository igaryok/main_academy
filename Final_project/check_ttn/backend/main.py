import string
import re
import requests


import google_api


def get_var(var, file):
    """
    return value of variable from settings file
    :param var: string with variable which value we want to get know
    :param file: string with path to settings file
    :return: string with value
    """
    value = None
    with open(file) as f:
        for line in f:
            if line.startswith("#"):
                continue
            if re.match(var, line):
                value = line.split("=")[1].strip()
                break

    return value


def convert_label(label):
    """
    convert label of column to number of column
    :param label: string with label
    :return: string with number
    """
    return string.ascii_uppercase.index(label)


def check_nova_poshta(api_key, ttns):
    url_nova_poshta = 'https://api.novaposhta.ua/v2.0/json/'

    params = {
        "apiKey": api_key,
        "modelName": "TrackingDocument",
        "calledMethod": "getStatusDocuments"
    }
    numbers_list = list(ttns)
    preload_list = []
    result = []
    counter = 0
    # Nova Poshta's API can return information about 100 TTN at once
    # so we must divide list if it more than 100
    while counter < len(numbers_list):
        if numbers_list[counter]:
            preload_list.append({"DocumentNumber": numbers_list[counter], "Phone": ""})
        if counter % 99 == 0 or counter == len(numbers_list) - 1:
            params["methodProperties"] = {"Documents": preload_list}
            resp = requests.post(url=url_nova_poshta, json=params)
            for item in resp.json()["data"]:
                result.append((item["Number"], item["Status"], item["StatusCode"]))
            preload_list.clear()

        counter += 1

    return result


def main(settings):
    """
    main function
    :param settings: string with folders name which includes files with settings
    alter.ini - main text-file with settings
    code.ini - text-file with TTN's status-code from API Nova Poshta
    :return: None
    """
    path_alter = settings+"/alter.ini"
    auth_var = (settings+"/"+get_var("CREDENTIAL", path_alter),
                get_var("SHEET", path_alter),
                get_var("WORKSHEET", path_alter))

    sheet = google_api.GoogleAPI(*auth_var)

    ttn_var = (convert_label(get_var("COL_TTN", path_alter)),
               convert_label(get_var("COL_WRITESYMBOL", path_alter)),
               int(get_var("START_ROW", path_alter)))

    data_sheet = sheet.get_all_ttn(*ttn_var)

    for key, item in data_sheet.items():
        print(key, item)

    current_status = check_nova_poshta(get_var("API_KEY", path_alter), data_sheet.keys())
    for item in current_status:
        print(item)

    symbol_var = settings+"/code.ini"
    for item in current_status:
        new = get_var(item[2], symbol_var).split(",")[0].strip()
        if not(new == data_sheet[item[0]][1]):
            print(new, data_sheet[item[0]][0])


if __name__ == '__main__':
    main("settings")
