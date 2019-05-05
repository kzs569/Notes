## PyTorch常用代码段整理

```python
import collections
import os
import shutil
import tqdm
import numpy as np
import torch
import torchvision
```

## 基础配置

**检查PyTorch版本**

```python
torch.__version__
torch.version.cuda
torch.backends.cudnn.version()
torch.cuda.get_device_name(0)
```

**固定随机种子**

```python
torch.manual_seed(0)
torch.cuda.manual_seed_all(0)
```

**指定程序运行在特定的GPU卡上**

```python
CUDA_VISIBLE_DEVICES=0,1 python train.py #在命令行指定环境变量
os.environ['CUDA_VISIBLE_DEVICES']='0,1' #在代码中指定
```

**设置为cuDNN benchmark模式**

```python
torch.backends.cudnn.benchmark = True #Benchmark模式会提升计算速度，但是由于计算中有随机性，每次网络前馈结果略有差异
torch.backends.cudnn.deterministic = True
```

**清除GPU存储**

```python
torch.cuda.empty_cache() #pytorch内部
ps aux|grep python|kill -9 [pid] #命令行
nvidia-smi --gpu-reset -i [gpu_id] #重置没有被清空的GPU
```

## 张量处理

张量基本信息

```python
tensor.type()   # Data type
tensor.size()   # Shape of the tensor. It is a subclass of Python tuple
tensor.dim()    # Number of dimensions.
```

数据类型转换

```python
# Set default tensor type. Float in PyTorch is much faster than double.
torch.set_default_tensor_type(torch.FloatTensor)

# Type convertions.
tensor = tensor.cuda()
tensor = tensor.cpu()
tensor = tensor.float()
tensor = tensor.long()
```

torch.Tensor与np.ndarry转换

```python
# torch.Tensor -> np.ndarray.
ndarray = tensor.cpu().numpy()

# np.ndarray -> torch.Tensor.
tensor = torch.from_numpy(ndarray).float()
tensor = torch.from_numpy(ndarray.copy()).float()  # If ndarray has negative stride
```

**torch.Tensor与PIL.Image转换**

PyTorch中的张量默认采用N×D×H×W 的顺序，并且数据范围在 [0, 1]，需要进行转置和规范化。

```python
# torch.Tensor -> PIL.Image
image = PIL.Image.fromarray(
    torch.clamp(tensor * 255, min=0, max=255).byte().permute(1,2,0).cpu().numpy()
)
image = torchvision.transforms.functional.to_pil_image(tensor)

# PIL.Image -> torch.Tensor.
tensor = torch.from_numpy(np.asarray(PIL.Image.open(path))
    ).permute(2, 0, 1).float() / 255
tensor = torchvision.transforms.functional.to_tensor(PIL.Image.open(path))  # Equivalently way
```

**np.ndarray 与 PIL.Image 转换**

```python
# np.ndarray -> PIL.Image.
image = PIL.Image.fromarray(ndarray.astypde(np.uint8))

# PIL.Image -> np.ndarray.
ndarray = np.asarray(PIL.Image.open(path))
```

**从只包含一个元素的张量中提取值**

```python
value = tensor.item()
```

**张量形变**

张量形变常常需要用于将卷积层特征输入全连接层的情形。相比torch.view, torch.reshape可以自动处理输入张量不连续的情况。

```python
tensor = torch.reshape(tensor, shape)
```

**打乱顺序**

```python
tensor = tensor[torch.randperm(tensor.size(0))] #Shuffle the first dimension
```

**水平翻转**

```python
# Assume tensor has shape N*D*H*W.
tensor = tensor[:, :, :, torch.arange(tensor.size(3) - 1, -1, -1).long()]
```

**复制张量**

```python
# Operation                 |  New/Shared memory | Still in computation graph |
tensor.clone()            # |        New         |          Yes               |
tensor.detach()           # |      Shared        |          No                |
tensor.detach.clone()()   # |        New         |          No                |
```

**拼接张量**

注意torch.cat和torch.stack的区别在于torch.cat沿着给定的维度拼接，而torch.stack会新增一维。例如当参数是 3 个 10×5 的张量，torch.cat 的结果是 30×5 的张量，而 torch.stack 的结果是 3×10×5 的张量。

```python
tensor = torch.cat(list_of_tensors, dim=0)
tensor = torch.stack(list_of_tensors, dim=0)
```

**将整数标记转换成one-hot编码**

```python
N = tensor.size(0)
one_hot = torch.zeros(N, num_classes).long()
one_hot.scatter_(dim=1, index=torch.unsqueeze(tensor, dim=1), src=torch.ones(N, num_classes).long())
```

**得到非零/零元素**

```python
torch.nonzero(tensor)               # Index of non-zero elements
torch.nonzero(tensor == 0)          # Index of zero elements
torch.nonzero(tensor).size(0)       # Number of non-zero elements
torch.nonzero(tensor == 0).size(0)  # Number of zero elements
```

**张量扩展**

```python
# Expand tensor of shape 64*512 to shape 64*512*7*7.
torch.reshape(tensor, (64, 512, 1, 1)).expand(64, 512, 7, 7)
```

**矩阵乘法**

```python
# Matrix multiplication: (m*n) * (n*p) -> (m*p).
result = torch.mm(tensor1, tensor2)

# Batch matrix multiplication: (b*m*n) * (b*n*p) -> (b*m*p).
result = torch.bmm(tensor1, tensor2)

# Element-wise multiplication.
result = tensor1 * tensor2
```

**计算两组数据之间的两两欧式距离**

```python
# X1 is of shape m*d.
X1 = torch.unsqueeze(X1, dim=1).expand(m, n, d)
# X2 is of shape n*d.
X2 = torch.unsqueeze(X2, dim=0).expand(m, n, d)
# dist is of shape m*n, where dist[i][j] = sqrt(|X1[i, :] - X[j, :]|^2)
dist = torch.sqrt(torch.sum((X1 - X2) ** 2, dim=2))
```