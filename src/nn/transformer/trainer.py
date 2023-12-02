
import torch
from torch import nn
from torch import optim

from src import Transformer


class Trainer():

    def __init__(self, src_vocab_size=5000, tgt_vocab_size=5000, d_model=512, num_heads=8, num_layers=6, d_ff=2048, max_seq_length=100, dropout=0.1, learning_rate=0.0001):
        self.src_vocab_size = src_vocab_size
        self.tgt_vocab_size = tgt_vocab_size
        self.d_model = d_model
        self.num_heads = num_heads
        self.num_layers = num_layers
        self.d_ff = d_ff
        self.max_seq_length = max_seq_length
        self.dropout = dropout
        self.learning_rate = learning_rate

    def run(self):
        transformer = Transformer(self.src_vocab_size, self.tgt_vocab_size, self.d_model, self.num_heads, self.num_layers, self.d_ff, self.max_seq_length, self.dropout)

        src_data = torch.randint(1, self.src_vocab_size, (64, self.max_seq_length))
        tgt_data = torch.randint(1, self.tgt_vocab_size, (64, self.max_seq_length))

        criterion = nn.CrossEntropyLoss(ignore_index=0)
        optimizer = optim.Adam(transformer.parameters(), lr=self.learning_rate, betas=(0.9, 0.98), eps=1e-9)

        transformer.train()
        for epoch in range(100):
            optimizer.zero_grad()
            output = transformer(src_data, tgt_data[:, :-1])
            loss = criterion(output.contiguous().view(-1, self.tgt_vocab_size), tgt_data[:, 1:].contiguous().view(-1))
            loss.backward()
            optimizer.step()
            print(f"Epoch: {epoch+1}, Loss: {loss.item()}")