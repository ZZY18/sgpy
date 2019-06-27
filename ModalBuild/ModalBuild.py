class ModalBuilder(object):

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    
    def __GetInfo(self):
        """
        确定基本信息
        主要是建模信息
        """
        pass
    
    def __SVMPipe(self):
        """
        建立一个SVM通道模型
        """
        pass
    
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