# 이어드림 스쿨 3기 스타트업 연계 프로젝트
### DS 3팀 - 시간의 흐름에 따른 노후 인프라시설 건축물의 외관과 내부 Crack 감지 (소테리아에이트)
- Project Peroid : 23.11.08~23.12.15
- Team : 맘에들었조
- Member : 양태경, 김다현, 임승준, 이지윤, 이종은, 박정재

## Topic
- instance segmentation, image retrieval



## Modeling Framework
- detectron2, ultralytics


## Requirements
you need to install our requirment packages
```python
$ pip install -r requirements.txt
```

## 소개
### 1. 문제 정의
콘크리트 내의 이상징후(철근노출, Bleeding)은 구조물 성능 감소로 인한 안전성 저하, 수분 침투에 의한 철근 부식, 외관 해침으로 인한 불안감 유발 등의 원인이 된다.

콘크리트 구조물에서의 이상징후 관리를 위해서는 정기적인 육안 검사를 통해 균열의 위치, 폭, 길이와 같은 정보를 취득하고 이를 정보화된 형태로 관리하여야 한다. 

일본을 비롯한 다수의 국가에서 건설된 인프라의 노후화가 이상 기후 등으로 인해 가속화가 되고 있어, 균열이 예상보다 빠르게 진전되고 있는 상황이다.

### 2. 문제 해결의 필요성
일반적으로 건설 구조물들은 규모가 크고 접근성이 높지 않아 육안 검사를 이용한 구조물의 손상 탐지에 많은 비용과 시간이 요구되고 있는 실정이다. 

안전 진단 입력이 직접 장비(초음파 등)을 이용하여 건물을 전역적으로 탐색해야 하나, 중대재해 안전 진단을 위한 예산과 인력의 부족한 상황이기 때문에 이를 세부적으로 확인하는데 어려움이 있다. 

soteria8에서는 이상징후를 사전에 진단할 수 있는 로보틱스 촬영 기반 컴퓨터 비전 안전진단 솔루션(이하 ’스마트 솔루션’)을 제시하고 이를 통해 손쉽게 포착한다면 경제적인 효과를 거둘 수 있을 것으로 예상된다.


### 3. 문제 접근 방법
(1) 로보틱스 장비로 <font color="red">사람이 탐색하기 어려운 구조물</font>에 대한 데이터 확보<br>
(2) 1차 : 촬영한 영상에 대하여 위험이 있는 <font color="red">이상징후 포착 및 기록</font><br>
(3) 일정시간 이후 : 같은 구역의 **2차적으로 촬영된 영상**에 대하여 이상징후의 <font color="red">진전 여부 탐지</font><br>

![Alt text](https://github.com/jeongjae96/soteria8-crack-detection/blob/main/images/workflow.jpg?raw=true)


> 1.이전 촬영 영상과 일정 시간이 지난 뒤의 촬영 영상(비교군)을 input으로 설정합니다.<br>
> 2.각 영상을 frame단위로 slicing하여 segmentation model의 입력값으로 넣습니다.<br>
> 3.탐지된 이상징후(철근노출,bleeding)현상의 frame을 matching합니다 (ImageRetrieval)<br>
> 4.매칭된 이상징후의 면적 비교를 통해 이상징후의 진전 여부를 판단합니다.


### 3. 훈련 데이터 명세

yolo-v8모델의 훈련 데이터 정보는 아래와 같습니다.<br><br>
|DataSet|Num total|TrainSet|ValidSet|Instances|
|:--:|:--:|:--:|:--:|:--:|
후가공데이터|712|569|143|499(150,307,42)|

<br>
cf) instances : 전체(철근노출,화이트블리딩,레드블리딩)<br><br>
AI hub의 건물 균열 탐지 오픈소스 <a href="https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=162">데이터</a>
 중 test환경과 유사한 이미지를 선별하여 라벨링하여 사용하였습니다.<br>


### 4. 모델 


yolo-v8 [best.pt](https://drive.google.com/file/d/18uMUQbhpCTUYfNQVFi3A95VYFdwdd27z/view)
훈련된 모델의 가중치를 사용하기 위해 다운로드가 필요합니다.

### 5. 벤치마크 정보
<img src="https://github.com/jeongjae96/soteria8-crack-detection/blob/main/images/yolo_benchmark.jpg?raw=true" width="750px" height="400px">

<br>
모든 클래스에 대해 전반적으로 우수한 성능을 보이는 xlarge모델 선택 이후 Augmentation 및 hyper-parameter tunning 진행

### 6. Image Retrieval


### 7. 최종 결과물 예시
<img src="https://github.com/jeongjae96/soteria8-crack-detection/blob/main/images/report_sample.jpg?raw=true"
width="675px" height="350px">



### 8. Further Experiment
https://github.com/jeongjae96/soteria8-crack-detection/blob/main/images/further_experiment.jpg?raw=true


<br>
<br>





<!--T
### Stacks

|Category|Description|
|:--:|:--:|
|**Languag**e|![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
|**Storage**|![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)|
|**Deeplearning**|![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)|
|**ImageProcessing**|![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)|
|**Environment**|![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)|
|**Communication**|![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)![Zoom](https://img.shields.io/badge/Zoom-2D8CFF?style=for-the-badge&logo=zoom&logoColor=white)|
-->








***
### Directory
<!--Table-->
|Category|Description|
|:--:|:--:|
|yolo|cell2|
|frame_matching|cell2|
|demo.py|Cell2|
|results.txt|Cell2|



***
### Acknowledgement
We refer to the following website to implement our models ("site")
