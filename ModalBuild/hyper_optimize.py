"""
基于损失函数，以及函数空间取得最优参数
"""
class hyper_opt(object):
    """
    """
    def __init__(self,loss_func,SpaceDic):
        self.loss_func=loss_func
        self.SpaceDic=SpaceDic
        self.__SpaceBuild()
    
    def __SpaceBuild(self,SpaceDic):
        """
        建立参数空间
        输入为参数空间Dictionary
        """
        from hyperopt import fmin, tpe, hp
        self.spaceparams={}
        self.choice={}
        for key in SpaceDic.keys():
            if self.SpaceDic[key]['type']=='choice':
                self.spaceparams.update({key:hp.choice(key,self.SpaceDic[key]['Content'])})
            if self.SpaceDic['type']=='uniform': 
                self.spaceparams.update({key:hp.uniform(key,*self.SpaceDic[key]['Content'])})#[0],self.SpaceDic[key]['Content'][1]
            if self.SpaceDic[key]['type']=='normal': 
                self.spaceparams.update({key:hp.normal(key,*self.SpaceDic[key]['Content'])}) #[0],self.SpaceDic[key]['Content'][1]

    def __fmin(self,params):
        """
        建立
        """
        from hyperopt import fmin, tpe, hp,STATUS_OK
        acc = self.loss_func(**params)
        return {'loss': -acc, 'status': STATUS_OK}

    def hyper_select(self):
        from hyperopt import fmin, tpe, hp,STATUS_OK,Trials
        self.trials=Trials()
        self.best=fmin(self.__fmin,self.spaceparams,algo=tpe.suggest, max_evals=1000, trials=self.trials)
        return self.best