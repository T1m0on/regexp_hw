import csv
import re


def read_csv():
        with open("phonebook_raw.csv", encoding='utf-8') as f:
            rows = csv.reader(f, delimiter=",")
            return list(rows)


def create_filtered_list():
    filtered_list = []
    for data in read_csv():
        filtered_names = list(filter(None, re.split(r'\s', ' '.join(data[0:3]))))
        if data[5]:
            filtered_names.append(data[5])
        if filtered_names in filtered_list or len(filtered_names) < 4:
            continue
        else:
            filtered_list.append(filtered_names)
    return filtered_list


def sub_phones():
    PHONE_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
    PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'
    result = []
    for i in create_filtered_list():
        final_names = [i[0], i[1], i[2], re.sub(PHONE_PATTERN, PHONE_SUB, i[3])]
        result.append(final_names)
    return result


def main():
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(sub_phones())


if __name__ == '__main__':
    main()
