# 🧠 Deep Learning

> **Reference**: fast.ai + Deep Learning Book (Goodfellow et al.)  
> **Tools**: PyTorch, TensorFlow/Keras, Hugging Face

---

## 📋 Syllabus Coverage

### Neural Networks Fundamentals
- [ ] Perceptron & McCulloch-Pitts neuron
- [ ] Activation functions (Sigmoid, ReLU, GELU, Softmax)
- [ ] Forward propagation
- [ ] Backpropagation (chain rule)
- [ ] Loss functions (MSE, Cross-entropy, Huber)
- [ ] Gradient Descent variants (SGD, Adam, RMSProp)
- [ ] Vanishing / Exploding gradients

### Convolutional Neural Networks (CNN)
- [ ] Convolution operation
- [ ] Pooling (Max, Average)
- [ ] CNN architectures (LeNet, AlexNet, VGG, ResNet)
- [ ] Transfer Learning & Fine-tuning
- [ ] Object detection basics (YOLO, R-CNN)

### Recurrent Neural Networks
- [ ] RNN architecture & limitations
- [ ] LSTM & GRU
- [ ] Seq2Seq models
- [ ] Encoder-Decoder architecture

### Transformers & Attention (Modern DL)
- [ ] Self-Attention mechanism
- [ ] Multi-head attention
- [ ] Positional encoding
- [ ] The Transformer architecture
- [ ] BERT (bidirectional, pre-training)
- [ ] GPT (autoregressive, text generation)
- [ ] Vision Transformer (ViT)

### Regularization & Optimization
- [ ] Dropout
- [ ] Batch Normalization
- [ ] Learning rate scheduling
- [ ] Early stopping

---

## 💻 PyTorch Quick-Start Template

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Define model
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_size, output_size)
        )
    
    def forward(self, x):
        return self.layers(x)

# Training loop
model = SimpleNet(784, 256, 10)
optimizer = optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
```

---

## 🔗 Key Resources
- [fast.ai Practical DL](https://course.fast.ai/)
- [Andrej Karpathy's nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)
- [Distill.pub](https://distill.pub/) — Visual explanations
