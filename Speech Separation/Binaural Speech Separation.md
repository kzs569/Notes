# Paper Review (MC-DL,MB-PIT)

总结，这两篇文章都是为了解决双通道（即双麦克风阵列下），两讲话人方向夹角过小，或者两麦克风之间距离小，导致只使用空间信息无法准确做到speaker independent的盲分离，需要结合spatial and spectral features to overcome the 'spatial overlapping problem'



## Multi-Channel Deep Clustering : Discriminative Spectral and Spatial Embedding for Speaker-Independent Speech Separation.

**Two-Channel Deep Clustering**

In the proposed method we encode not only **spectral but also spatial information** into the embedding of each T-F unit by  including spatial features as additional inputs.

Since **spectral and spatial features can be complementary** in terms of their **sources of uncertainty and failure modes,** we expect their combination to show improved robustness relative to each type of feature in isolation.

- **narrowband approach**

The narrowband approach performs clustering **within each frequency band** **using spatial cues such as IPDs or ILDs.** The DUET algorithm assumes that the microphone pairs are placed sufficiently close to each other so that **phase-wrapping effects** can be neglected. 

  **It estimates the ITD of each T-F unit by directly dividing the phase difference by the angular frequency(相位差/角频率)**, and then performs clustering on the estimated ITDs and ILDs, and then performs clustering on the estimated ITDs and ILDs of all the T-F units.

  In contrast,  Sawada handles phase wrapping by clustering based ultimately on IPDs instead of ITDs.

It would be beneficial to perform clustering across all the frequencies and over all the T-F units, as some frequency bands may be particularly worse than others and most importantly, more T-F units would form stronger cluster patterns that could elicit better clustering results.

the following IPDs as additional features for model training:
$$
\begin{aligned} \operatorname{cosIPD}(t, f, p, q) &=\cos \left(\theta_{t, f, p, q}\right) \\ \operatorname{sinIPD}(t, f, p, q) &=\sin \left(\theta_{t, f, p, q}\right) \end{aligned}
$$

where $\theta_{t, f, p, q}=\angle x_{t, f, p}-\angle x_{t, f, q}$ is the phase difference between the STFT coefficients $x_{t,f,p}$ and $x_{t,f,q}$ at the time t and frequency f of the signals at microphones p and q.

The rationale is that for spatially-separated sources with different time delays, 
$$
\frac{x_{t, f, p}}{x_{t, f, q}}=\frac{\left|x_{t, f, p}\right|}{\left|x_{t, f, q}\right|} e^{\theta_{t}, f, p, q}
$$

should naturally form clusters within each frequency band due to the speech sparsity property.


> 理由是，对于具有不同时间延迟的空间分离源，由于语音稀疏性，它应该在每个频带内自然形成簇

For a given source, the cosIPD and sinIPD features at different frequency bands are very
different, so we combine them with spectral features that can help resolve the ambiguity.

- **wideband approach**
The wideband approach avoids the IPD ambiguity by enumerating a set of potential time delays.
GCC-PHAT:
$$
\operatorname{GCC}(t, f, p, q, \tau)=\cos \left(\theta_{t, f, p, q}-\frac{2 \pi f}{N} \tau\right)
$$

Our approach avoids a separate sound localization module by enumerating a set of potential time delays. When a hypothesized time delay matches the observed phase difference, it appears as a peak in the derived spatial feature. **The entire set of GCC coefficients encodes all the direction information of each source** and hence could be useful for deep clustering.

The GCC features have a much higher dimension than the spectral features. If each dimension of these two features is normalized to unit variance, more importance will be implicitly placed on the GCC features.

## MULTI-BAND PIT AND MODEL INTEGRATION FOR IMPROVED MULTI-CHANNEL SPEECH SEPARATION

- Learning with Spatial Features

However, no investigation has been conducted on performance variability created by a change in relative location of multiple simultaneous speakers, particularly **when two speakers or more are closely located**.

frequency normalized IPD 
$$
\frac{1}{2 \pi f} a r g\left[\frac{Y_{p}(f, t)}{Y_{q}(f, t)}\right]
$$
for each T-F bin, which has been utilized in [13] for avoiding frequency permutation issue after feature clustering.

In practice, it increases the feature discrimination and avoids failure in the case of location ambiguity that two speakers? directions are symmetric with respect to a certain microphone pair.

Unfortunately, even equipped with spectral features, we found out that multi-channel PIT does not perform well in spatial overlapping scenarios as illustrated in Table 1 (schemes 1 vs. 2-5) when the two speakers’ directions are less than $15^{\circ}$ apart from each other.

features:

1. IPD
2. cosIPD
3. sinIPD
4. generalized cross-correlation, GCC

main disadvantage : **estimated phase difference is the potential phase wrapping in high frequencies, particularly when the microphone spacing is not sufficiently small.**

The occurrence of phase wrapping is common when the microphone spacing exceeds $\lambda_{min}=2$, half of the minimum wavelength of the speech signal.

This motivates us to split the full-band input features (log power spectra + IPDs) into multiple frequency subbands.

multiple recurrent neural network towers are jointly trained to **generate individual subband embeddings **from the corresponding subband input features. Therefore, those subbands with reliable spatial features could leverage them to boost the embedding learning, while high frequency subbands learn to attend more on their spectral features. The dimension of each subband embedding remains the same as the  conventional full-band embedding’s. Without any change on the projection layer, subband embeddings are summed up to form a new embedding for the mask prediction.


## Proper Noun need to explain

**Intermicrophone phase difference,IPD**
$$
\operatorname{IPD}_{i, t,f}=\angle\left(\frac{Y_{i}(t,f)}{Y_{i^{\prime}}(t,f)}\right), i=2 \ldots M
$$

$$
=\angle Y_{j}(t, f)-\angle Y_{j^{\prime}}(t, f)+2 \ell \pi
$$

$$
\approx \angle H_{i^{\prime} j}(t, f) X_{i^{*}}(t, f)-\angle H_{i^{*} j^{\prime}}(t, f) X_{i^{*}}(t, f)+2 \ell \pi
$$

$$
=\angle H_{i^{*} j}(t, f)-\angle H_{i^{*} j^{\prime}}(t, f)+2 \ell^{\prime} \pi
$$

$$
=\angle \exp \left(\iota 2 \pi f \Delta_{\tau_{i j} /} / f_{\mathrm{s}}\right)=2 \pi f \Delta_{\tau_{i j} /} / f_{\mathrm{s}}+2 \pi \ell
$$

where y refers to the observed data in the frequency domain, M denotes the number of microphones being used, i  indexes the microphone, and t f indexes time-frequency bins. $y_{i,t,f}$ is the i-th channel complex spectrum of the mixture signal at time frame t and frequency bin $f . \angle(\cdot)$ outputs the angle of the input argument.

$$
\phi_{j j^{\prime}}(t, f)=2 \pi f \Delta_{\tau_{i j}^{\prime}} / f_{\mathrm{s}}+2 \pi \ell, \Delta_{\tau_{i j}^{\prime}}=f_sd_{jj^{\prime}}/c
$$

$$
\phi_{j j^{\prime}}(t, f)=2 \pi f d_{jj^{\prime}}/c
$$

$d_{jj^{\prime}}$是两个麦克风之间的距离，c是声音在空气中传播的速度

**Interaural level difference, ILD**
$$
\alpha_{j j^{\prime}}(t, f)=20 \log _{10}\left|C_{j j}(t, f)\right|
$$
where
$$
C_{j j}(t, f)=\frac{Y_{j}(t, f)}{Y_{j^{\prime}}(t, f)}
$$

**ITDs** correspond to the time location of the maximum in the cross-correlation pattern
$$
ITD=\frac{phase \ difference}{angular\ frequency}
$$


**IIDs** are computed based on the following formula:
$$
L_{i}=20 \log _{10} \frac{\sum_{t} l_{i}^{2}}{\sum_{t} r_{i}^{2}}
$$
where $s_i$ and $n_i$ refer to the output of the *i*th gammatone filter for speech and noise, respectively.

**Generalized Cross Correlation, GCC**
$$
\hat{\tau}_{\mathrm{GCC}}=\arg \max _{m} \Psi_{\mathrm{GCC}}[m]
$$
where
$$
\Psi_{\mathrm{GCC}}[m]=\sum_{k=0}^{K-1} \Phi[k] S_{\boldsymbol{x}_{0} \boldsymbol{x}_{1}} \mathrm{e}^{\mathrm{j} 2 \pi m k / K}
$$
is the generalized cross-correlation function(GCCF), $S_{\boldsymbol{x}_{0} \boldsymbol{x}_{1}}[k]=E\left\{\boldsymbol{X}_{0}[k] \boldsymbol{X}_{1}[k]^{*}\right\}$ is cross spectrum, '*' denotes the complex conjugate operator, $X[k]$ is the DFT of x[t], K is the length of DFT, and $\Phi[k]$ is a weighting function. $S_{\boldsymbol{x}_{0} \boldsymbol{x}_{1}}[k]$ is usually estimated by replacing the expected values by the corresponding instantaneous ones.

**DUET algorithms**



**phase-wrapping effects**



**spatial overlapping problem**



W-disjoint orthogonality



In addition, in single-channel source separation systems, the log magnitude of a mixture of signals is commonly approximated as the log magnitude of the most energetic signal, known as the log-max approximation.





- 语谱图

语谱图的横坐标是时间，纵坐标是频率，坐标点值为语音数据能量。由于是采用二维平面表达三维信息，所以能量值的大小是通过颜色来表示的，颜色深，表示该点的语音能量越强。

语谱图中有明显的一条条横方向的条纹，我们称为“声纹”，有很多应用。条纹的地方实际是颜色深的点聚集的地方，随时间延续，就延长成条纹，也就是表示语音中频率值为该点横坐标值的能量较强，在整个语音中所占比重大，那么相应影响人感知的效果要强烈得多。而一般语音中数据是周期性的，所以，能量强点的频率分布是频率周期的，即存在300Hz强点，则一般在n*300Hz点也会出现强点，所以我们看到的语谱图都是条纹状的。

