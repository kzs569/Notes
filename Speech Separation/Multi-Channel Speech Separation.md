# Multi-Channel Speech Separation

**Problem Description**

The problem of speech separation is formulated as estimating C sources, $s_{1}(t), \ldots, s_{c}(t) \in \mathrm{R}^{1 \times T}$ from the mixture waveform $x(t) \in \mathrm{R}^{1 \times T}$
$$
x(t)=\sum_{i=1}^{C} s_{i}(t)
$$
Taking the short-time Fourier transform(STFT) of both sides formulates the source separation problem in the T-F domain where the complex mixture spectrogram is the sum of the complex source spectrograms
$$
X(f, t)=\sum_{i=1}^{C} S_{i}(f, t)
$$
Where $X(f,t)$ and $S_i(f,t) \in \mathbb{C}^{F \times T}$. One common approach for recovering the individual sources, $S_i$, is to estimate a real-valued T-F mask for each source, $M_{i} \in \mathrm{R}^{F \times T}$





Generate_RIRs

Spatialize_mix(rir_dir, start_ind, stop_ind, fs, data_in_root, data_out_root, num_speakers, min_or_max, useparcluster)

