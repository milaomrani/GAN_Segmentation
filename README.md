# Document Image Segmentation Challenge

This repository contains scripts for training a multi-label segmentation model designed to identify and segment various elements within document images, such as characters, pages, and ornaments. The implementation is based on the paper from ICPR 2021, titled "Segmentation of Generative Adversarial Network."

## Getting Started

### Step 1: Generative Adversarial Networks (GANs)

The GAN implementation will be added to this repository soon.

### Step 2: Testing with Sample Images

To test the segmentation model with sample images, follow these steps:

1. Ensure you have the required datasets ready.

2. Run the following command:

```bash
python segmentation.py --imgDIR ./TrainingImages/1.jpg --Train 25
```

#### Optional Arguments

- `--train`: Specify the number of training epochs (default value is 25).

## Contributors

- [Milad Omrani]
