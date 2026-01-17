# GLM-4.7 - Installation and Configuration for Low-End PCs

This repository contains automated scripts to install and configure the GLM-4.7 model on machines with limited resources.

## 📋 Minimum Requirements

### Minimum Hardware (CPU Only)

- **RAM**: 32GB+ (64GB+ recommended)
- **Disk**: 200GB+ free space (SSD recommended)
- **CPU**: Modern multi-core processor

### Recommended Hardware (with GPU)

- **GPU**: 8GB+ VRAM (16GB+ recommended)
- **RAM**: 64GB+ (128GB+ recommended)
- **Disk**: 300GB+ free space (NVMe SSD recommended)
- **CUDA**: Compatible with CUDA 11.8+ or 12.1+

## 🎯 Available Model Versions

GLM-4.7 is available in various quantizations for different hardware capabilities:

| Version | Size | Minimum RAM | Minimum VRAM | Recommended Use |
|---------|------|-------------|--------------|-----------------|
| **UD-Q2_K_XL** (2-bit) | ~135GB | 128GB | 24GB | Powerful machines with GPU |
| **Q4_K_M** (4-bit) | ~200GB | 64GB | 16GB | Moderate machines |
| **Q4_K_S** (4-bit) | ~180GB | 48GB | 12GB | Modest machines |
| **Q5_K_M** (5-bit) | ~240GB | 80GB | 20GB | Best quality |

## 🚀 Quick Start

### Windows (PowerShell)

```powershell
# 1. Install dependencies
.\scripts\install.ps1

# 2. Download model (choose appropriate version)
.\scripts\download-model.ps1 -Version "Q4_K_S"

# 3. Run the model
.\scripts\run-llamacpp.ps1
```

### Linux/Mac (Bash)

```bash
# 1. Install dependencies
chmod +x scripts/install.sh
./scripts/install.sh

# 2. Download model (choose appropriate version)
chmod +x scripts/download-model.sh
./scripts/download-model.sh Q4_K_S

# 3. Run the model
chmod +x scripts/run-llamacpp.sh
./scripts/run-llamacpp.sh
```

## 📁 Repository Structure

```
.
├── README.md                 # This file
├── scripts/
│   ├── install.sh            # Linux/Mac installation
│   ├── install.ps1           # Windows installation
│   ├── download-model.sh     # Model download (Linux/Mac)
│   ├── download-model.ps1    # Model download (Windows)
│   ├── run-llamacpp.sh       # Run with llama.cpp (Linux/Mac)
│   ├── run-llamacpp.ps1      # Run with llama.cpp (Windows)
│   ├── run-ollama.sh         # Run with Ollama (Linux/Mac)
│   └── run-ollama.ps1        # Run with Ollama (Windows)
├── config/
│   ├── hardware-config.yaml  # Hardware configuration
│   └── model-config.json     # Model settings
└── models/                   # Directory for downloaded models
```

## ⚙️ Configuration

### 1. Configure Hardware

Edit `config/hardware-config.yaml` with your machine specifications:

```yaml
hardware:
  gpu:
    available: true
    vram_gb: 8
    cuda_arch: "75"  # For RTX 2060, 2070, 2080
  ram_gb: 32
  cpu_cores: 8
  disk_space_gb: 500
```

### 2. Choose Model Version

Based on your hardware, choose the appropriate version:

- **Very low-end PC (32GB RAM, no GPU)**: Use `Q4_K_S` or consider smaller models
- **Moderate PC (64GB RAM, 8-16GB GPU)**: Use `Q4_K_M`
- **Powerful PC (128GB+ RAM, 24GB+ GPU)**: Use `UD-Q2_K_XL` or `Q5_K_M`

## 🔧 Execution Methods

### Option 1: llama.cpp (Recommended for limited hardware)

`llama.cpp` offers better control over CPU/GPU offloading and quantization.

**Advantages:**

- Intelligent offloading support
- Lower memory usage
- Better for limited hardware

### Option 2: Ollama (Simpler)

Ollama is easier to use, but may be less efficient on limited hardware.

**Advantages:**

- Simpler installation
- More user-friendly interface
- Automatic model management

## 📝 Usage Examples

### Run with small context (saves memory)

```bash
./scripts/run-llamacpp.sh --ctx-size 4096 --threads 4
```

### Run CPU-only

```bash
./scripts/run-llamacpp.sh --cpu-only
```

### Run with partial CPU offloading

```bash
./scripts/run-llamacpp.sh --gpu-layers 10
```

## 🐛 Troubleshooting

### Error: "Out of memory"

- Reduce `--ctx-size` (context size)
- Use a more quantized version of the model
- Reduce `--gpu-layers` to offload more to CPU

### Error: "CUDA not found"

- Check if CUDA is installed: `nvidia-smi`
- Recompile llama.cpp with CUDA support

### Model too slow

- Increase `--threads` (number of CPU threads)
- Use more GPU layers if you have available VRAM
- Consider using a lighter version of the model

## 📚 Additional Resources

- [Official GLM-4.7 Documentation](https://huggingface.co/zai-org/GLM-4.7)
- [llama.cpp GitHub](https://github.com/ggerganov/llama.cpp)
- [Ollama Documentation](https://ollama.ai/docs)
- [Quantized models on Hugging Face](https://huggingface.co/bartowski/zai-org_GLM-4.7-GGUF)

## 📄 License

This repository contains installation and configuration scripts. The GLM-4.7 model has its own license - consult the official repository.

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or pull requests.

## ⚠️ Warnings

- Large models may take a long time to download (100GB+)
- First run may be slow while the model loads
- Make sure you have enough disk space before downloading
- On very limited hardware, consider using smaller models or cloud services
