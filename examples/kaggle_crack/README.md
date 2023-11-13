# [Kaggle Crack Dataset](https://www.kaggle.com/datasets/yatata1/crack-dataset)

Kaggle Crack Dataset을 이용해 crack 탐지를 먼저 진행해보고자 합니다.

## Data Structure

```
.
├── README.md
├── data
│   └── kaggle_crack
│       ├── Concrete
│       │   └── Concrete
│       │       ├── Negative
│       │       │   ├── Images
│       │       │   │   └── *.jpg
│       │       │   └── Mask
│       │       │       └── *.jpg
│       │       └── Positive
│       │           ├── Boxs
│       │           │   └── *.txt
│       │           ├── Images
│       │           │   ├── *.jpg
│       │           │   └── *.png
│       │           └── Masks
│       │               ├── *.jpg
│       │               └── *.png
│       └── Unity_Generation
└── examples
    └── kaggle_crack
        └── README.md
```