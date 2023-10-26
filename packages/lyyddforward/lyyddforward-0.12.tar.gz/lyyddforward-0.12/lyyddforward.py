import configparser
import pandas as pd
from pypinyin import lazy_pinyin


def get_config_value(config, section, option):
    try:
        value = config.get(section, option)
        return value
    except (configparser.NoSectionError, configparser.NoOptionError):
        return ""


# 解析 INI 配置文件
def parse_ini_config(ini_config_file):
    ini_config = configparser.ConfigParser()
    ini_config.read(ini_config_file, encoding="utf-8")
    return ini_config


def get_pinyin(chinese_words):
    pinyin = "".join(lazy_pinyin(chinese_words, errors='ignore'))
    return pinyin


def create_dataframe_from_ini(ini_config):
    data = []
    for section in ini_config.sections():

        tmp_list = []
        for col in ['from_group_name', 'from', 'to', 'prefix', 'fromuser']:
            tmp_list.append(get_config_value(ini_config, section, col))

        print(tmp_list)
        data.append(tmp_list)

    print(data)
    #print(data[:5])
    df = pd.DataFrame(data, columns=['from_group_name', 'from', 'to', 'prefix', 'fromuser'])
    df['pinyin'] = df['from_group_name'].apply(lambda x: get_pinyin(x))
    return df


if __name__ == '__main__':
    cfg_path = r'D:\UserData\resource\ddForward'
    ini_config_file = cfg_path + "/" + "ddForward.ini"
    ini_config = parse_ini_config(ini_config_file)
    df = create_dataframe_from_ini(ini_config)
    # 打印 DataFrame
    print(df[:5])
