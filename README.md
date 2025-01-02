# Oneforall-IP-extraction
Oneforall批量扫描结束之后，可用此脚本提取文件夹下所有表中的ip

## 使用命令： ##
python IP_extraction.py -d csv -i 8 -o result.txt

- -d   指定文件夹，例如csv
- -i   指定ip在表格中的列数，例如onforall扫描之后的子域名，ip默认在第8列
- -o   将所有ip输出到result.txt

## 脚本演示： ##

首先将脚本和待提取ip的文件夹放在同目录下

![](https://raw.githubusercontent.com/xhmcc/Oneforall-IP-extraction/refs/heads/main/images/089be35bb16ae5597fd7cb80df377c9.png)

文件夹下为oneforall的子域名结果

![](https://raw.githubusercontent.com/xhmcc/Oneforall-IP-extraction/refs/heads/main/images/cdad5cca3c53620933e5bef7701c2e1.png)

-i指定第8行IP

![](https://raw.githubusercontent.com/xhmcc/Oneforall-IP-extraction/refs/heads/main/images/92ed5e12942fd483c5dba5fa8f2377d.png)

最后执行命令，提取IP

![](https://raw.githubusercontent.com/xhmcc/Oneforall-IP-extraction/refs/heads/main/images/9c7d9c0771e48738fc2d1ef59452e25.png)
