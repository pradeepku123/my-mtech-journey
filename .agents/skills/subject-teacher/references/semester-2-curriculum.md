# Semester 2 — Class-by-Class Curriculum (BITS Pilani WILP M.Tech AIML)

> Teaching plan for **Semester 2 Core & Elective Subjects**.

---

## 🧠 Subject 1: Deep Neural Networks (Core)
**Folder**: `semesters/semester-2/deep-neural-networks/`  
**Total Classes**: 10 | **Professor Persona**: Prof. Andrej Karpathy

| Class | Topic | Key Goal |
|-------|-------|----------|
| 01 | Perceptrons & Multi-Layer Perceptrons | Linear neural networks, activation functions (ReLU, GELU) |
| 02 | Deep Feedforward Training & Backpropagation | Computation graphs, autograd engines, chain rule step-by-step |
| 03 | Optimization for Deep Networks | Momentum, RMSProp, Adam, AdamW, Learning rate warmup/decay |
| 04 | Regularization & Batch Norm | Dropout, Weight Decay, Batch Normalization, Layer Normalization |
| 05 | Convolutional Neural Networks (CNNs) | Convolution operation, pooling, receptive fields |
| 06 | Modern CNN Architectures & Transfer Learning | ResNet, EfficientNet, Transfer learning, Fine-tuning |
| 07 | Recurrent Neural Networks & LSTMs | Sequence modeling, BPTT, LSTMs, GRUs, Vanishing gradients |
| 08 | Attention Mechanisms & Encoder-Decoder | Bahdanau attention, Luong attention, Seq2Seq |
| 09 | Transformer Architecture Deep Dive | Scaled dot-product, Multi-head attention, Positional encodings |
| 10 | Vision Transformers (ViT) | Patchify, Patch embeddings, ViT vs CNN trade-offs |

---

## 🎮 Subject 2: Deep Reinforcement Learning (Core)
**Folder**: `semesters/semester-2/deep-reinforcement-learning/`  
**Total Classes**: 10 | **Professor Persona**: Prof. David Silver (DeepMind)

| Class | Topic | Key Goal |
|-------|-------|----------|
| 01 | MDP Foundations & Bellman Equations | States, Actions, Rewards, Bellman Optimality Equations |
| 02 | Dynamic Programming | Policy Evaluation, Policy Iteration, Value Iteration |
| 03 | Model-Free Prediction & Control | Monte Carlo methods, TD(0), SARSA, Q-Learning |
| 04 | Deep Q-Networks (DQN) | Value function approximation, Experience Replay, Target Networks |
| 05 | Advanced Q-Learning | Double DQN, Dueling DQN, Prioritized Experience Replay |
| 06 | Policy Gradient Methods | REINFORCE algorithm, Policy Gradient Theorem |
| 07 | Actor-Critic Architectures | Advantage Actor-Critic (A2C/A3C), Generalized Advantage Estimation |
| 08 | Continuous Control Algorithms | Deep Deterministic Policy Gradient (DDPG), Soft Actor-Critic (SAC) |
| 09 | Proximal Policy Optimization (PPO) | Clipped surrogate objective, PPO implementation |
| 10 | RLHF & LLM Alignment | Reward Modeling, PPO for LLM alignment, DPO comparison |

---

## 💬 Subject 3: Natural Language Processing (Elective 1)
**Folder**: `semesters/semester-2/natural-language-processing/`  
**Total Classes**: 10 | **Professor Persona**: Prof. Chris Manning (Stanford)

| Class | Topic | Key Goal |
|-------|-------|----------|
| 01 | Text Preprocessing & Subword Tokenization | Regex, Stemming, BPE, WordPiece, SentencePiece |
| 02 | Vector Space Models & Static Embeddings | TF-IDF, Word2Vec (Skip-Gram/CBOW), GloVe embeddings |
| 03 | N-gram & RNN Language Models | N-gram perplexity, Recurrent Language Models |
| 04 | Contextual Embeddings (ELMo, BERT) | Masked Language Modeling, Next Sentence Prediction, Fine-tuning |
| 05 | Named Entity Recognition & POS Tagging | Sequence labeling, CRF layers, BERT-NER |
| 06 | Information Extraction & Knowledge Graphs | Relation extraction, Entity linking, Knowledge Graph triples |
| 07 | Text Classification & Sentiment Analysis | Aspect-based sentiment analysis, Document classification |
| 08 | Machine Translation & Seq2Seq | Neural Machine Translation, BLEU/ROUGE metrics |
| 09 | Multilingual & Indic NLP | Cross-lingual representations, mBERT, XLM-R, IndicNLP |
| 10 | NLP Systems & Evaluation | Scalable NLP pipelines, Robustness, Bias & Fairness in NLP |

---

## 🤖 Subject 4: Large Language Models for Generative AI (Elective 2)
**Folder**: `semesters/semester-2/large-language-models-for-generative-ai/`  
**Total Classes**: 10 | **Professor Persona**: Prof. Andrew Ng / Chip Huyen

| Class | Topic | Key Goal |
|-------|-------|----------|
| 01 | Pre-trained LLM Architectures | Decoder-only transformers (Llama 3, Mistral, Qwen), RoPE |
| 02 | LLM Inference & Optimization | KV Cache, Quantization (AWQ, GPTQ, GGUF), vLLM |
| 03 | Efficient Fine-Tuning (LoRA & QLoRA) | PEFT methods, Rank decomposition, QLoRA 4-bit fine-tuning |
| 04 | Preference Alignment (RLHF & DPO) | Reward modeling, DPO loss, KTO, Alignment taxonomies |
| 05 | Prompt Engineering & Reasoning | CoT, Tree of Thoughts, ReAct prompting, System prompts |
| 06 | RAG Foundations | Chunking, Dense Retrieval, Vector DBs (FAISS, Chroma, Pinecone) |
| 07 | Advanced RAG Techniques | Hybrid search, Reciprocal Rank Fusion (RRF), Cross-encoder reranking |
| 08 | LLMs as Agents | Tool execution, Function calling schemas, Planning loops |
| 09 | Structured Output Generation | JSON mode, Instructor, Outlines, Pydantic validation |
| 10 | LLM Evaluation & Safety | Ragas framework, DeepEval, Red teaming, Jailbreak defenses |
