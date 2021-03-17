import requests
import json


# Создания локального файла логов
def get_log_file(url_l):
    response = requests.get(url_l)
    log_file_name = 'nginx_logs.txt'
    logs = open(log_file_name, 'w')
    logs.close()

    with open(log_file_name, 'a') as f_logs:
        for el in response.text:
            f_logs.write(el)

    return log_file_name


# Создание списка кортежей
def get_list_truple(file_name):
    list_truple = open('truple_list.json', 'w')
    list_truple.close()

    with open(file_name) as f:
        with open('truple_list.json', 'r+') as lt:
            for el in f.readlines():
                el = el.replace('"', '').split()
                trp = (el[0], el[5], el[6])
                json.dump(trp, lt)
                lt.write('\n')
    return 'truple_list.json'


# Поиск спамера
def find_spam(f_json):
    dict_ip_count = {}
    spam_ip = []
    count = 0
    with open(f_json, 'r') as lt:
        for el in lt.readlines():
            el = json.loads(el)
            if el[0] in dict_ip_count:
                dict_ip_count[el[0]] = dict_ip_count.get(el[0]) + 1
                if dict_ip_count[el[0]] > count:
                    count = dict_ip_count.get(el[0])
                    spam_ip = (el[0], count)
            else:
                dict_ip_count[el[0]] = 1

    return spam_ip


url_logs = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
get_f = get_log_file(url_logs)
get_t = get_list_truple(get_f)
f_spam = find_spam(get_t)
print(f_spam)
