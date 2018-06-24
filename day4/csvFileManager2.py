import csv
class CsvFileManager2:
    @classmethod
    def read(cls):
        path=r'D:\zhuchunyan\selenium7day\data\testdata.csv'
        file=open(path,'r')
        #通过csv代码库读取打开的csv文件,获取文件中的数据
        data_table=csv.reader(file)
        #for循环,item每一行
        for item in data_table:
            print(item)

#如果想测试这个方法
if __name__ == '__main__':
    # csvr=CsvFileManager2()
    # csvr.read()
#如果在方法上面加classmethod 表示这个方法可以直接用类调用,直接用CsvFileManager2.read(),不用实例化对象了,省略上面两步
    CsvFileManager2.read()