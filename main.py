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
        while len(filtered_names) != 3:
            filtered_names.append(' ')
        for i in range(3, 7):
            filtered_names.append(data[i])
        filtered_list.append(filtered_names)
    return filtered_list


def merge_same_data():
    filtered_list = create_filtered_list()
    for filtered_data in filtered_list:
        for reversed_data in filtered_list[::-1]:
            if filtered_data[:2] == reversed_data[:2] and filtered_data != reversed_data:
                for i in range(7):
                    if filtered_data[i]:
                        continue
                    else:
                        filtered_data[i] = reversed_data[i]
                filtered_list.remove(reversed_data)
    return filtered_list


def sub_phones():
    PHONE_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
    PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'
    result = []
    for i in merge_same_data():
        final_data = [i[0], i[1], i[2], i[3], i[4], re.sub(PHONE_PATTERN, PHONE_SUB, i[5]), i[6]]
        result.append(final_data)
    return result


def main():
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(sub_phones())


if __name__ == '__main__':
    main()
