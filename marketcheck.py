import os
import csv
import requests
import json

csv_header = [['MAKE', 'YEAR', 'MODEL']]


def write_direct_csv(lines, filename):
    with open(os.path.join(output_directory, filename), 'a', encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(lines)
    csv_file.close()


def write_csv(lines, filename):
    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    if not os.path.isfile(os.path.join(output_directory, filename)):
        write_direct_csv(lines=csv_header, filename=filename)
    write_direct_csv(lines=lines, filename=filename)


def api_request(make, year):
    headers = {
        'Host': 'marketcheck-prod.apigee.net'
    }
    url = 'http://api.marketcheck.com/v2/specs/car/terms?api_key={}&year={}&make={}&field=model'.format(year, make)
    res = requests.get(url=url, headers=headers)
    return res.text


def main():
    for year in range(2020, 2021, 1):
        for make in make_list:
            response = api_request(make.lower(), year)
            json_res = json.loads(response)
            print(json_res)
            if 'model' in json_res:
                json_res = json_res['model']
                for model in json_res:
                    line = [make, year, model]
                    print(line)
                    # write_csv(lines=[line], filename='Model_list.csv')


if __name__ == "__main__":
    output_directory = 'output'
    make_list = [
        'Acura',
        'Audi',
        'BMW',
        'Buick',
        'Cadillac',
        'Chevrolet',
        'Chrysler',
        'Dodge',
        'Fiat',
        'Ford',
        'GMC',
        'Honda',
        'Hyundai',
        'Infiniti',
        'Jeep',
        'Kia',
        'Lexus',
        'Lincoln',
        'Mazda',
        'Mercedes Benz',
        'Nissan',
        'RAM',
        'Subaru',
        'Toyota',
        'Volkswagen ',
        'Volvo'
    ]
    main()
