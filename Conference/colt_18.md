COLT18
========

Gates : http://www.learningtheory.org/colt2018/index.html

Time : 

## Awards

- Best Paper Award
*Algorithmic Regularization in Over-parameterized Matrix Sensing and Neural Networks with Quadratic Activations*
Yuanzhi Li, Tengyu Ma and Hongyang Zhang. 

We show that the (stochastic) gradient descent algorithm provides an implicit regularization effect in the learning of over-parameterized matrix factorization models and one-hidden-layer neural networks with quadratic activations. Concretely, we show that given <img src="https://latex.codecogs.com/gif.latex?\tilde{O}(dr^2)" title="\tilde{O}(dr^2)" /> random linear measurements of a rank r positive semidefinite matrix
<img src="https://latex.codecogs.com/gif.latex?X^*" title="X^*" />
, we can recover 
<img src="https://latex.codecogs.com/gif.latex?X^*" title="X^*" />
 by parameterizing it by 
<img src="https://latex.codecogs.com/gif.latex?UU^T" 的title="UU^T" />
 with 
<img src="https://latex.codecogs.com/gif.latex?U\in\mathbb{R}&space;^{d\times&space;d}" title="U\in\mathbb{R} ^{d\times d}" />
 and minimizing the squared loss, even if 
r
 is much less than 
d
. We prove that starting from a small initialization, gradient descent recovers 
<img src="https://latex.codecogs.com/gif.latex?X^*" title="X^*" />
 in 
<img src="https://latex.codecogs.com/gif.latex?\tilde{O}(\sqrt&space;r)" title="\tilde{O}(\sqrt r)" />
 iterations approximately. The results solve the conjecture of Gunasekar et al. 17 under the restricted isometry property. The technique can be applied to analyzing neural networks with quadratic activations with some technical modifications.

- Best Student Paper Awards
*Reducibility and Computational Lower Bounds for Problems with Planted Sparse Structure*

Matthew Brennan, Guy Bresler and Wasim Huleihel.

Recently, research in unsupervised learning has gravitated towards exploring statistical-computational gaps induced by sparsity. A recent line of work initiated in \cite{berthet2013complexity} has aimed to explain these gaps through reductions to conjecturally hard problems in computer science. However, the delicate nature of average-case reductions has limited the development of techniques and often led to weaker hardness results that only apply to algorithms robust to different noise distributions or that do not need to know the parameters of the problem. We introduce several new techniques to give a web of average-case reductions showing strong computational lower bounds based on the planted clique conjecture. Our new lower bounds include:
1. Planted Independent Set: We show tight lower bounds for recovering a planted independent set of size 
k
 in a sparse Erd\H{o}s-R\'{e}nyi graph of size 
n
 with edge density 
<img src="https://latex.codecogs.com/gif.latex?\tilde{O}(n^{-&space;\alpha})" title="\tilde{O}(n^{- \alpha})" />.

2. Planted Dense Subgraph: If 
p > q
 are the edge densities inside and outside of the community, we show the first lower bounds for the general regime 
<img src="https://latex.codecogs.com/gif.latex?q&space;=&space;\tilde{O}(n^{-&space;\alpha})" title="q = \tilde{O}(n^{- \alpha})" />
 and 
<img src="https://latex.codecogs.com/gif.latex?p&space;-&space;q&space;=&space;\tilde{O}(n^{-&space;\gamma})" title="p - q = \tilde{O}(n^{- \gamma})" />
where 
γ ≥ α
, matching the lower bounds predicted in \cite{chen2016statistical}. Our lower bounds apply to a deterministic community size 
k, resolving a question raised in \cite{hajek2015computational}.

3. Biclustering: We show strong lower bounds for Gaussian biclustering as a simple hypothesis testing problem to detect a uniformly at random planted flat k × k submatrix.
4. Sparse Rank-1 Submatrix: We show that sparse rank-1 submatrix detection is often harder than biclustering, and obtain two different tight lower bounds for these problems with different reductions from planted clique.
5. Sparse PCA: We give a reduction between rank-1 submatrix and sparse PCA to obtain tight lower bounds in the less sparse regime 
k≫√n, when the spectral algorithm is optimal over the natural SDP. This yields the first tight characterization of a computational barrier for sparse PCA over an entire parameter regime. We also give an alternate reduction recovering the lower bounds of \cite{berthet2013complexity} and \cite{gao2017sparse} in the canonical simple hypothesis testing variant of sparse PCA, the spiked covariance model.
6. New Models: We demonstrate a subtlety in the complexity of sparse PCA and planted dense subgraph by introducing two variants of these problems, biased sparse PCA and planted stochastic block model, and showing that they have different hard regimes than the originals. 
Our results demonstrate that, despite the delicate nature of average-case reductions, using natural problems as intermediates can often be beneficial, as is the case for reductions between deterministic problems. Our main technical contribution is to introduce a set of cloning techniques that maintain the level of signal in an instance of a problem while increasing the size of its planted structure. We also give algorithms matching our lower bounds and identify the information-theoretic limits of the models we introduce.


*Logistic Regression: The Importance of Being Improper
Dylan Foster, Satyen Kale, Haipeng Luo, Mehryar Mohri and Karthik Sridharan.  *ABSTRACT 

Learning linear predictors with the logistic loss --- both in stochastic and online settings ---is a fundamental task in learning and statistics, with direct connections to classification and boosting. Existing "fast rates" for this setting exhibit exponential dependence on the predictor norm, and Hazan et al. (2014) showed that this is unfortunately unimprovable. Starting with the simple observation that the logisic loss is 1-mixable, we design a new efficient improper learning algorithm for online logistic regression that circumvents the aforementioned lower bound with a regret bound exhibiting a doubly-exponential improvement in dependence on the predictor norm. This provides a positive resolution to a variant of the COLT 2012 open problem of mcmahan2012open when improper learning is allowed. This improvement is obtained both in the online setting and, with some extra work, in the batch statistical setting with high probability. We show that the improved dependency on predictor norm is also near-optimal. Leveraging this improved dependency on the predictor norm also yields the following applications: (a) we give algorithms for online bandit multiclass learning with the logistic loss with an
<img src="https://latex.codecogs.com/gif.latex?\tilde{O}(\sqrt&space;n)" title="\tilde{O}(\sqrt n)" />
 relative mistake bound across essentially all parameter ranges, thus providing a solution to the COLT 2009 open problem of Abernethy and Rakhlin (2009), and (b) we give an adaptive algorithm for online multiclass boosting with optimal sample complexity, thus partially resolving an open problem of Beygelzimer et al. (2015) and Jung et al. (2017). Finally, we give information-theoretic bounds on the optimal rates for improper logistic regression with general function classes, thereby characterizing the extent to which our improvement for linear classes extends to other parameteric or even nonparametric classes.