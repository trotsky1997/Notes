

In Supervised Fine-Tuning (SFT) for language models, the cross-entropy loss function is commonly used. This function is defined for a single training example as follows:

\begin{equation}
\text{Cross-Entropy Loss} = - \sum_{c=1}^{M} y_{o,c} \log(p_{o,c})
\end{equation}

Here,$M $is the number of classes (in language models, this is often the vocabulary size),$y $is a binary indicator (0 or 1) if class label$c $is the correct classification for observation$o $, and$p $is the predicted probability of observation$o $being of class$c $.

In the context of language models, this loss function calculates the negative log probability of the correct word (or token) given the context provided by the preceding words (or tokens). The goal during training is to minimize this loss, which effectively increases the likelihood of the model predicting the correct next word in a sequence.