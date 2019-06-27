
class DataClear(object):
    def __init__(self):
        pass
    
    def __GetData(self):
        import pandas as pd
        import numpy as np
        self.Df=pd.read_excel(r'DataCleat.xlsx',sheet_name='Sheet1',header=None)
    
    def __Clear(self,rateC,rateR):
        """
        目的：对数据进行清理去除空值与错误信息（-1）

        输入：rateC为列允许错误率；rateR为行允许错误率

        输出：清理后数据集（DataFrame）
        """
        del_cols=[]
        for cols in self.Df.columns:#对每列分析
            rownum,colnum=self.Df.shape
            Datacols=self.Df.loc[:,cols]
            nullnum=Datacols[(Datacols.isnull()) | (Datacols<=0)].shape[0]
            if (nullnum==0):
                pass
            else:
                rate=nullnum/rownum
                if (rate>rateC):#当超过预设列误差比例时
                    for rows in Datacols[(Datacols.isnull()) | (Datacols<=0)].index:#对列元素分析，看其错误率是否大于ratec
                        Datarows=self.Df.loc[rows,:]
                        nullnumC=Datarows[(Datarows.isnull()) | (Datarows<=0)].shape[0]
                        if(nullnumC/colnum>rateR):#如果大于ratec,认为该样本有误
                            self.Df=self.Df.drop([rows],axis=0) #删除样本
                    rownum,colnum=self.Df.shape
                    Datacols=self.Df.loc[:,cols]
                    nullnum=Datacols[(Datacols.isnull())| (Datacols<=0)].shape[0]
                    if (nullnum/rownum>rateC):#删除完后再判断是否仍然超过预设列误差比
                        self.Df=self.Df.drop([cols],axis=1) #删除该列     
                        del_cols.append(cols)
                else:
                    self.Df=self.Df.loc[(Datacols.notnull()) & (Datacols>0),:]
        return del_cols
    
    def __quantile_p(self,data, p):
        """
        目的：获得分为数
        输入：data数据集，p分位数
        输出：Q为对应分为数值
        """
        import math
        data.sort()
        pos = (len(data) + 1)*p
        pos_integer = int(math.modf(pos)[1])
        pos_decimal = pos - pos_integer
        Q = data[pos_integer - 1] + (data[pos_integer] - data[pos_integer - 1])*pos_decimal
        return Q
        
    def __RangeDeal(self,b,f=0):
        """
        目的：剔除异常数据，获取正常数据集的最大最小值
        输入：b为分位数取值,data数据集,f为偏差值
        输出：正常数据集的方差
        """
        import pandas as pd
        #取下1/4分位数FL以及3/4分位数为FU
        for col in self.Df.columns:
            column=self.Df.loc[:,col]
            data=column.values
            FL=self.__quantile_p(data,0.25)
            FU=self.__quantile_p(data,0.75)
            DF=FU-FL
            minF=FL-b*DF-f*FL
            maxF=FU+b*DF+f*FU
            Info=pd.Series([minF,maxF],index=['min','max'])
            if('All_Info' in vars()):
                All_Info=pd.concat([All_Info,Info],axis=1)
            else:
                All_Info=pd.DataFrame(Info)
        All_Info.columns=self.Df.columns
        self.DataRange=All_Info

    
    def __AbnormalDeal(self):
        for col in self.DataRange.columns:
            for row in self.Df[(self.Df.loc[:][col]<self.DataRange.loc['min'][col]) |( self.Df.loc[:][col]>self.DataRange.loc['max'][col])].index:
                self.Df=self.Df.drop([row],axis=0)


    def main(self):
        self.__GetData()
        Del_col=self.__Clear(0.1,0.5)
        print(Del_col)
        self.__RangeDeal(1.5,f=0.1)
        self.__AbnormalDeal()
        


if __name__=='__main__':
    import pandas as pd
    a=DataClear()
    
    a.main()
    print(a.DataRange)
