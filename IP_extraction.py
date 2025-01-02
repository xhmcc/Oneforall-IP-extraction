# -*- coding: utf-8 -*-

import pandas as pd
import os
import argparse
import ipaddress

def extract_all_tables(csv_dir, column_index, output_file):
    # 获取指定目录下的所有 CSV 文件
    csv_files = [os.path.join(csv_dir, f) for f in os.listdir(csv_dir) if f.endswith('.csv')]

    # 所有 CSV 文件中指定列的值
    all_values = []

    # 读取每个 CSV 文件和提取指定列的值
    for csv_file in csv_files:
        # 读取 CSV 文件到 DataFrame
        df = pd.read_csv(csv_file, encoding='gbk')

        # 提取指定列的值到 Series
        column = df.iloc[:, column_index]

        # 将 Series 转换为列表
        values = column.tolist()

        # 将当前 CSV 文件的值添加到所有值的列表
        all_values += values

    # 去重
    all_values = set(all_values)

    # 去除无效 IP 地址，并过滤内网 IP 地址
    valid_ips = []
    for value in all_values:
        try:
            ip = ipaddress.ip_address(value)
        except ValueError:
            continue
        if ip.is_private:
            continue
        if ipaddress.ip_network('192.168.0.0/16').overlaps(ipaddress.ip_network(value)):
            continue
        if ipaddress.ip_network('172.16.0.0/12').overlaps(ipaddress.ip_network(value)):
            continue
        if ipaddress.ip_network('10.0.0.0/8').overlaps(ipaddress.ip_network(value)):
            continue
        valid_ips.append(str(ip))

    # 将所有值保存到文本文件中
    values_str = '\n'.join(valid_ips)
    with open(output_file, 'w', encoding='gbk') as f:
        f.write(values_str)

    print('Task End!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract column values from CSV files.')
    parser.add_argument('-d', '--dir', type=str, help='directory containing CSV files')
    parser.add_argument('-i', '--index', type=int, help='index of the column to extract')
    parser.add_argument('-o', '--output', type=str, help='output file name')
    args = parser.parse_args()

    if args.dir and args.index and args.output:
        extract_all_tables(args.dir, args.index, args.output)
    else:
        parser.print_help()
