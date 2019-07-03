

class ModalBuilder(object):

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    
    def __GetInfo(self):
        """
        确定基本信息
        主要是建模信息
        """
        pass
    
    def __SVMPipe(self,params):
        """
        建立一个SVM通道模型
        """
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA  
        from sklearn.svm import SVR
        from sklearn.pipeline import Pipeline      
        from sklearn.model_selection import train_test_split,cross_val_score
        pipe=[]
        #解析标准化
        if self.BuildInfo['scaler']=='StandardScaler':
            pipe.append(('sc',StandardScaler()))
            
        #解析降维数据
        if self.BuildInfo['Dimension']['algorithm']=='PCA':
            pipe.append(('dr',PCA(n_components=self.BuildInfo['Dimension']['n_components'])))
            
        #解析算法
        # if self.BuildInfo['Regression']['algorithm']=='SVR':
        pipe.append(('svr',SVR(**params)))
        self.pipe=Pipeline(pipe)

    
    def __SpaceBuild(self):
        """
        Space空间建立
        """
        from hyperopt import fmin, tpe, hp
        self.spaceparams={}
        self.choice={}
        for key in self.params.keys():
            if self.params[key]['type']=='choice':   
                self.choice.update({key:self.params[key]['Content']})
                self.spaceparams.update({key:hp.choice(key,self.params[key]['Content'])})
            if self.params[key]['type']=='uniform': 
                self.spaceparams.update({key:hp.uniform(key,self.params[key]['Content'][0],self.params[key]['Content'][1])})
            if self.params[key]['type']=='normal': 
                self.spaceparams.update({key:hp.normal(key,self.params[key]['Content'][0],self.params[key]['Content'][1])}) 

    def __fmin(self):
        """
        建立最小化函数
        """
        pass
    
    def modalBuild(self):
        """
        寻优和模型保存
        """
        pass