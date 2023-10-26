#  Copyright (c) 2023. Davi Pereira dos Santos
#  This file is part of the sortedness project.
#  Please respect the license - more about this in the section (*) below.
#
#  sortedness is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  sortedness is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with sortedness.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is illegal and it is unethical regarding the effort and
#  time spent here.
#
import numpy as np
import torch
import torch.optim as optim
from scipy.spatial.distance import cdist
from scipy.stats import rankdata
from torch import from_numpy, tensor
from torch.utils.data import Dataset, DataLoader

from sortedness.embedding.surrogate import cau, loss_function

pdist = torch.nn.PairwiseDistance(p=2, keepdim=True)


class Dt(Dataset):
    def __init__(self, X):
        self.size = X.shape[0]

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return idx


def balanced(X, symmetric, gamma=4, k=17, global_k="sqrt", alpha=0.5, smooothness_tau=1, neurons=30, epochs=100, batch_size=20, max_global_k=1000, seed=0, gpu=False, **kwargs):
    """
    >>> from sklearn import datasets
    >>> from sklearn.preprocessing import StandardScaler
    >>> from numpy import random, round
    >>> digits = datasets.load_digits()
    >>> X = digits.images.reshape((len(digits.images), -1))[:20]
    >>> rnd = random.default_rng(0)
    >>> rnd.shuffle(X)
    >>> X = StandardScaler().fit_transform(X)
    >>> X_ = balanced(X, False, epochs=2)
    >>> X_.shape
    (20, 2)


    Parameters
    ----------
    X
    symmetric
    gamma
    k
        number of nearest neighbors to consider for local order optimization
    global_k
        number of "neighbors" to sample for global order optimization
    alpha
        Parameter to balance between local and global. 0 is totally local. 1 is totally global.
    smooothness_tau
        Regularizer. Surrogate function tends to (non differentiable) Kendall tau when smooothness_tau tends to 0.
    neurons
    epochs
    batch_size
    seed
    gpu
    kwargs

    Returns
    -------

    """

    class M(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.encoder = torch.nn.Sequential(
                torch.nn.Linear(X.shape[1], neurons), torch.nn.ReLU(),
                torch.nn.Linear(neurons, 2)
            )
            self.decoder = torch.nn.Sequential(
                torch.nn.Linear(2, neurons), torch.nn.ReLU(),
                torch.nn.Linear(neurons, X.shape[1])
            )

        def forward(self, x):
            return self.encoder(x)

    torch.manual_seed(seed)
    if symmetric:
        print("warning: 'symmetric=True' not implemented")
    model = M()
    if gpu:
        model.cuda()

    X = X.astype(np.float32)
    n = X.shape[0]
    R = from_numpy(rankdata(cdist(X, X), axis=1)).cuda() if gpu else from_numpy(rankdata(cdist(X, X), axis=1))
    T = from_numpy(X).cuda() if gpu else from_numpy(X)
    w = cau(tensor(range(n)), gamma=gamma)

    optimizer = optim.RMSprop(model.parameters())
    model.train()
    loader = DataLoader(Dt(T), shuffle=True, batch_size=batch_size, pin_memory=gpu)
    with torch.enable_grad():
        for i in range(epochs):
            for idx in loader:
                encoded = model(T)
                expected_ranking_batch = R[idx]
                D_batch = pdist(encoded[idx].unsqueeze(1), encoded.unsqueeze(0)).view(len(idx), -1)
                loss, mu_local, mu_global, tau_local, tau_global = loss_function(D_batch, expected_ranking_batch, k, global_k, w, alpha, smooothness_tau, max_global_k)
                optimizer.zero_grad()
                (-loss).backward()
                optimizer.step()
    return model(T).detach().cpu().numpy().astype(float)
