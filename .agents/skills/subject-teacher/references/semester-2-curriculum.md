# Semester 2 — Class-by-Class Curriculum

> Full teaching plan for all **6 Semester 2 subjects**.
> Updated Sep 2026: Added Generative AI & LLMs as dedicated subject (industry-critical).
> Each subject has a complete class-by-class breakdown with topics, sub-topics, and goals.

---

## 🧠 Subject 1: Deep Learning
**Folder**: `semesters/semester-2/deep-learning/`
**Total Classes**: 14 | **Difficulty**: High
**Professor Persona**: Prof. Andrej Karpathy (code-first, build from scratch)

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | Neural Network Intuition | Perceptron, MLP architecture, activation functions, forward pass | What IS a neural network? |
| 02 | Backpropagation from Scratch | Chain rule, computation graph, gradient flow, vanishing gradients | Build autograd by hand |
| 03 | Training Deep Networks | Loss functions, optimizers (Adam), learning rate scheduling, batch size | Make networks actually learn |
| 04 | Regularization in DL | Dropout, batch normalization, weight decay, data augmentation | Fight overfitting in deep nets |
| 05 | Convolutional Neural Networks | Convolution operation, pooling, receptive field, CNN architectures | Why CNNs dominate vision |
| 06 | Modern CNN Architectures | ResNet, VGG, EfficientNet, transfer learning, fine-tuning | Use pre-trained power |
| 07 | Recurrent Neural Networks | RNN, LSTM, GRU, vanishing gradient in RNNs, sequence modeling | Handle sequential data |
| 08 | Attention Mechanism | Self-attention, scaled dot-product attention, multi-head attention | The key to Transformers |
| 09 | Transformer Architecture | Encoder-Decoder, positional encoding, layer norm, BERT vs GPT | The architecture that changed AI |
| 10 | Generative Models — VAE | Latent space, encoder-decoder, reparameterization trick, ELBO | Learn data distributions |
| 11 | Generative Models — GAN | Generator, discriminator, adversarial training, mode collapse | Generate new data |
| 12 | Diffusion Models | Denoising score matching, DDPM, DDIM, Stable Diffusion architecture | Modern image generation |
| 13 | PyTorch Deep Dive | Custom datasets, DataLoader, custom nn.Module, GPU training loop | Production DL code |
| 14 | DL Project: End-to-End | Image classification → text generation mini-project with PyTorch | Build something real |

---

## 📝 Subject 2: Natural Language Processing
**Folder**: `semesters/semester-2/nlp/`
**Total Classes**: 12 | **Difficulty**: High
**Professor Persona**: Prof. Chris Manning (Stanford NLP)

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | NLP Foundations | Tokenization, stemming, lemmatization, POS tagging, text preprocessing | Clean text for ML |
| 02 | Text Representations I — Classic | Bag of Words, TF-IDF, n-grams, sparse representations | From words to numbers |
| 03 | Text Representations II — Word2Vec | Skip-gram, CBOW, negative sampling, GloVe, FastText | Dense word vectors |
| 04 | Language Models — N-gram | Bigram/trigram models, Markov assumption, smoothing techniques | Predict next word |
| 05 | Sequence Models for NLP | RNN for text, seq2seq, encoder-decoder, teacher forcing | Model text sequences |
| 06 | Attention in NLP | Bahdanau attention, self-attention for text, attention visualization | Focus on what matters |
| 07 | BERT & Pre-training | Masked LM, next sentence prediction, fine-tuning protocol, embeddings | The BERT revolution |
| 08 | GPT & Causal LMs | Autoregressive LM, GPT architecture, prompting, in-context learning | How ChatGPT works |
| 09 | Text Classification & NER | Fine-tuning BERT, token classification, CRF, span extraction | Core NLP tasks |
| 10 | Machine Translation | BLEU score, beam search, subword tokenization (BPE), multilingual models | Cross-language NLP |
| 11 | Information Retrieval & RAG | Dense retrieval, BM25, vector databases, RAG architecture | LLMs + your data |
| 12 | LLM Applications & Ethics | Prompt engineering, RLHF, hallucination, safety, evaluation | Use LLMs responsibly |

---

## 👁️ Subject 3: Computer Vision
**Folder**: `semesters/semester-2/computer-vision/`
**Total Classes**: 10 | **Difficulty**: High
**Professor Persona**: Prof. Fei-Fei Li (Stanford CS231n)

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | Image Fundamentals | Pixels, channels, color spaces, image as matrix, basic ops | See images as data |
| 02 | Classical CV — Filters & Edges | Convolution, Gaussian blur, Sobel/Canny edge detection, Hough | Pre-deep-learning CV |
| 03 | Feature Extraction — SIFT/HOG | Scale-invariant features, histogram of gradients, feature matching | Handcrafted features |
| 04 | Image Classification with CNNs | LeNet → AlexNet evolution, ImageNet challenge, benchmark datasets | CNNs for recognition |
| 05 | Object Detection | Sliding window, R-CNN family, YOLO, anchor boxes, IoU, NMS | Find AND localize objects |
| 06 | Semantic Segmentation | FCN, U-Net, DeepLab, pixel-wise classification, mIoU metric | Understand every pixel |
| 07 | Instance & Panoptic Segmentation | Mask R-CNN, Panoptic FPN, segment anything model (SAM) | Full scene understanding |
| 08 | Transfer Learning in CV | ImageNet pre-training, fine-tuning strategies, domain adaptation | Don't train from scratch |
| 09 | Vision Transformers (ViT) | Patch embedding, ViT architecture, DeiT, CLIP, DINO | Transformers in vision |
| 10 | CV Applications | Medical imaging, autonomous driving, visual regression testing (SDET bridge) | Real-world CV |

---

## 🎮 Subject 4: Reinforcement Learning
**Folder**: `semesters/semester-2/reinforcement-learning/`
**Total Classes**: 10 | **Difficulty**: Very High
**Professor Persona**: Prof. David Silver (DeepMind, AlphaGo)

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | RL Framework | Agent, environment, state, action, reward, Markov property, MDP | The RL mental model |
| 02 | Bellman Equations | Value function, Q-function, Bellman optimality, dynamic programming | The math of RL |
| 03 | Model-Free: Monte Carlo | MC prediction, MC control, every-visit vs first-visit, exploration | Learn from experience |
| 04 | Temporal Difference Learning | TD(0), TD error, SARSA, on-policy vs off-policy | Bootstrap + learn online |
| 05 | Q-Learning & SARSA | Q-learning algorithm, convergence, tabular Q-table | Classic RL algorithms |
| 06 | Deep Q-Networks (DQN) | Neural Q-function, experience replay, target network, DQN tricks | RL meets deep learning |
| 07 | Policy Gradient Methods | REINFORCE, policy gradient theorem, baseline subtraction | Optimize policy directly |
| 08 | Actor-Critic Methods | A2C, A3C, advantage function, GAE, PPO | Combine value + policy |
| 09 | Advanced RL | DDPG, SAC, model-based RL, world models, offline RL | State-of-the-art RL |
| 10 | RL Applications | AlphaGo/AlphaFold walkthrough, game playing, robotics, AutoML | RL changes the world |

---

## ⚙️ Subject 5: MLOps
**Folder**: `semesters/semester-2/mlops/`
**Total Classes**: 12 | **Difficulty**: Medium (Pradeep's SDET background is a huge advantage!)
**Professor Persona**: Prof. Chip Huyen (Designing ML Systems author)

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | MLOps Overview | ML lifecycle, MLOps vs DevOps, maturity levels, team roles | See the full ML delivery picture |
| 02 | Data Versioning & Management | DVC, data lineage, feature stores (Feast), data contracts | Treat data like code |
| 03 | Experiment Tracking | MLflow, W&B, Neptune, tracking metrics/params/artifacts | Never lose an experiment |
| 04 | ML Pipelines | Kubeflow, Airflow, Prefect, ZenML, pipeline orchestration | Automate ML workflows |
| 05 | Model Training at Scale | Distributed training (PyTorch DDP), hyperparameter tuning (Optuna), Ray | Scale up training |
| 06 | Model Packaging & Serving | Docker containers, FastAPI + model, ONNX, TorchServe, BentoML | Deploy models as APIs |
| 07 | AWS SageMaker Deep Dive | Training jobs, endpoints, Pipelines, Model Registry — AWS bridge | Cloud ML deployment |
| 08 | CI/CD for ML | GitHub Actions ML workflows, automated testing for models, model cards | ML DevOps (Pradeep's world!) |
| 09 | Model Monitoring | Data drift, concept drift, Evidently AI, Grafana dashboards, alerts | Keep models healthy in production |
| 10 | ML Testing Strategies | Unit tests, integration tests, behavioral/metamorphic testing, property-based testing, shadow mode | SDET superpowers → ML quality |
| 11 | LLMOps — Serving LLMs | vLLM, TGI, quantization (GGUF/GPTQ), prompt versioning, eval pipelines | Serve LLMs in production |
| 12 | Feature Stores & Real-Time ML | Online vs offline features, Feast, Redis, latency optimization | Production feature engineering |
| 13 | MLOps Capstone | End-to-end: data → training pipeline → CI/CD → serving → monitoring + LLM endpoint | Build a complete production ML+LLM system |

---

## 🤖 Subject 6: Generative AI & Large Language Models
**Folder**: `semesters/semester-2/generative-ai-llms/`
**Total Classes**: 8 | **Difficulty**: Very High (most industry-relevant subject in 2025-2026)
**Professor Persona**: **Prof. Andrej Karpathy** (for architecture) + **Chip Huyen** (for production)
**Why Added**: Generative AI is now mandated in updated MTech AI/ML curricula across IITs/NITs. LLMs are the most in-demand skill in the industry.

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | Foundation Models & Scaling Laws | Pre-training at scale, scaling laws (Kaplan et al.), emergent abilities, GPT-4/Llama/Mistral overview | Understand the big picture |
| 02 | Prompt Engineering | Zero-shot, few-shot, chain-of-thought (CoT), ReAct, self-consistency, structured outputs | Get the most from LLMs |
| 03 | Fine-tuning LLMs | Supervised Fine-tuning (SFT), LoRA, QLoRA, PEFT, instruction tuning, dataset preparation | Customize LLMs for your domain |
| 04 | RLHF & Alignment | Human feedback, reward modeling, PPO on LLMs, Direct Preference Optimization (DPO), Constitutional AI | Make LLMs safe and helpful |
| 05 | RAG — Retrieval-Augmented Generation | Vector databases (Chroma, Pinecone, Weaviate), chunking strategies, re-ranking, Agentic RAG | LLMs + your own data |
| 06 | AI Agents & Tool Use | Function calling, tool-augmented LLMs, LangGraph, smolagents, ReAct agents, AutoGen | LLMs that take actions |
| 07 | Evaluation & Safety | LLM benchmarks (MMLU, HumanEval), hallucination detection, red-teaming, guardrails, Constitutional AI | Trustworthy LLMs |
| 08 | Multimodal AI | Vision-language models (LLaVA, GPT-4V, Gemini), text-to-image (DALL-E 3, SD3), audio AI | Beyond text-only LLMs |
