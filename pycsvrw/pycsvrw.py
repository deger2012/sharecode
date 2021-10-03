import csv
import pandas as pd

#csv文件的读写
class csv_rw:
    csv_init_data = csv_ini_reader();

    csv_file_path = csv_init_data['csv_file_path'];

    #读取csv文件并转换为json_list 
    def csv_reader():
        with open(csv_file_path) as csv_file:
            csv_data_list = list(csv.DictReader(csv_file));
        return csv_data_list;

    #根据需求将数据写入csv文件
    def csv_writer():
        #追加的方式将数据写入csv文件
        with open(csv_file_path, "a+", newline="") as data_file:
            #每行的各列的值，实际使用时需要修改
            row_data = [];
            row = csv.writer(data_file)
            row.writerow(h_data)

    #修改csv文件某一列的值
    def csv_modify_column_value():
        #delim_whitespace 如果是空格分隔符 ，delim_whitespace设置为True
        df = pd.read_csv(csv_file_path, delim_whitespace=False);
        #df.loc中condition是条件，按实际情况修改条件判断， column是要修改的csv列名，最后根据需求修改相关的值
        df.loc[(condition)), 'column'] = "1";
        df.to_csv(csv_file_path, index=False, sep=',');

    #csv模块配置文件
    def csv_ini_reader():
        ini_file = './csvsettings.ini';
        section = 'csvsettings';

        cfg = ConfigParser()
        # 读取文件内容
        cfg.read(ini_file);
        cfg_content = dict(cfg.items(section));
        return cfg_content;
