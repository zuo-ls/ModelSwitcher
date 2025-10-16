import inspect
from functools import partial

class ModulesGrouper:
    """
    Dynamiclly create a new class.
    """
    def get(self,name,kwargs):
        return getattr(self,name)(kwargs)
    
    def get_from_dict(self,cfg_dict):
        """
        cfg_dict: a dict of cfg. eg. {cfg_k:dict(a=1,b=2,c=3)}
        """
        return [self.get(k,v) for k,v in cfg_dict.items()][0]
    
    def init_module(self,module,kwargs):
        """
        init a module with given kwargs, check type of the module automatically.
        """
        # check module is a func or a class
        if inspect.isclass(module):
            return type(module.__name__,(module,),{})(**kwargs)
        elif inspect.isfunction(module):
            return partial(module,**kwargs)

def instantiate(cfg):
    """
    instantiate a class from a config.
    init a existed class.
    """
    module_path, cls_name = cfg.__target__.rsplit(".", 1)
    module = __import__(module_path, fromlist=[cls_name])
    cls = getattr(module, cls_name)
    return cls(**cfg.params)

# In YAML CONFIG 
"""
model_to_use:
    __target__: src.model.ModelClass
    params:
        in_dim: 512
"""
# model = instantiate(cfg.model_to_use)
# print(model)
