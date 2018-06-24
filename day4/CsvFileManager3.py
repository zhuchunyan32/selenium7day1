import csv
#每个测试用例对应着不同的csv文件
#每条测试用例都会打开一个csv文件,所以每次应该关闭该文件
class CsvFileManager3:
    @classmethod
    def read(cls):
        path=r'D:\zhuchunyan\selenium7day\data\testdata.csv'
        file=open(path,'r')
        try:  #try尝试执行以下代码
        #通过csv代码库读取打开的csv文件,获取文件中的数据
            data_table=csv.reader(file)
            #for循环,item每一行
            a=[2,3,4,5,6]
            a[6] #这时可能发生数据下标越界
            #如何保证程序执行过程中是否报错,都能正常关闭该文件
            for item in data_table:
                print(item)
                #方法最后添加close方法
        finally: #不论过程是否报错,都会执行以下代码
            file.close()
            print("file.close() method is execued")
#如果想测试这个方法
if __name__ == '__main__':
    # csvr=CsvFileManager2()
    # csvr.read()
#如果在方法上面加classmethod 表示这个方法可以直接用类调用,直接用CsvFileManager2.read(),不用实例化对象了,省略上面两步
    CsvFileManager3.read()