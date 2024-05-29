import torch

class LinearModel(torch.nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearModel, self).__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)

class CNNModel(torch.nn.Module):
    def __init__(self, input_dim, output_dim, kernel_size=5):
        super(CNNModel, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 20, kernel_size)
        self.conv2 = torch.nn.Conv2d(20, 50, kernel_size)

    def forward(self, x):
        x = torch.nn.functional.relu(self.conv1(x))
        return torch.nn.functional.relu(self.conv2(x))

class RNNModel(torch.nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim=100):
        super(RNNModel, self).__init__()
        self.rnn = torch.nn.RNN(input_dim, hidden_dim)
        self.fc = torch.nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x, _ = self.rnn(x)
        return self.fc(x)
