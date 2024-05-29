from models import LinearModel, CNNModel, RNNModel
from model_grouper import ModelGrouper

class Encoder(ModelGrouper):
    def linearmodel(self,kwarg):
        return self.init_module(LinearModel, kwarg)
    def cnnmodel(self,kwarg):
        return self.init_module(CNNModel, kwarg)
    def rnnmodel(self,kwarg):
        return self.init_module(RNNModel, kwarg)

if __name__ == '__main__':
    config = {
        'linearmodel': dict(input_dim=10, output_dim=5),
    }
    enc1 = Encoder().get_from_dict(config)

    config = {
        'cnnmodel': dict(input_dim=10, output_dim=5),
    }
    enc2 = Encoder().get_from_dict(config)