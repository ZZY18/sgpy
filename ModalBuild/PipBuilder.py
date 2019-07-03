class PiplineBuilder(object):
    def __init__(self):
        self.params
        self.X_train
        self.Y_train
    
    def Set_alg_select(self,alg_info):
        """
        解析alg_info中的信息，主要包括两块算法algorithm以及预处理
        """
        self.alg_prepro=alg_info.pop('preprocess',{'scaler':0,'dimension':0})
        self.algorithm=alg_info.pop('algorithm','svr')
        if (self.algorithm=='svr'):
            self.Pipline=SVMPipeline      
    
    def Set_Trains_Data(self,X_train,Y_train):
        self.X_train=X_train
        self.Y_train=Y_train
           
        
    def loss_func(self,params):
        """
        输入参数输出损失函数
        """
        self.params=params
        Pipline=self.Pipline(params,**self.alg_prepro)   
        from sklearn.model_selection import train_test_split,cross_val_score
        return  cross_val_score(Pipline, self.X_train, self.Y_train,cv=3).mean()    
    
    def Train_modal(self,params):
        """
        返回用于保存的训练模型
        """
        Pipline=self.Pipline(params,**self.alg_prepro)
        return Pipline.fit(self.X_train,self.Y_train)


def SVMPipeline(alg_params,scaler=0,dimension=0):
    """
    建立一个SVM通道模型
    分为两部分：1、算法参数 2、算法选择（标准化、降维）
    """
    from sklearn.preprocessing import StandardScaler,MinMaxScaler,MaxAbsScaler
    from sklearn.decomposition import PCA  
    from sklearn.svm import SVR
    from sklearn.pipeline import Pipeline      
    from sklearn.model_selection import train_test_split,cross_val_score
    pipe=[]
    #解析标准化
    if(scaler=='StandardScaler'):
        pipe.append(('sc',StandardScaler()))
    elif (scaler=='MinMaxScaler'):
        pipe.append(('mins',MinMaxScaler()))
    elif (scaler=='MaxAbsScaler'):
        pipe.append(('maxs',MaxAbsScaler()))
           
    #解析降维数据
    if dimension=='PCA':
        n_count=alg_params.pop('n_components',2)
        pipe.append(('pca',PCA(n_components=n_count)))
            
    #解析算法
    pipe.append(('svr',SVR(**alg_params)))
    return Pipeline(pipe)