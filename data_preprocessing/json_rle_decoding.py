## RLE decoding

'''
json파일의 RLE 인코딩 방식을 면적값으로 디코딩하는 py파일 입니다.
'segmentation': {
     'counts': "e[`33l?2N2O0O1000O1000000000000000000001O0000000001N3M\\TS4",
     'size': [512, 512]  # 해당 마스크의 높이와 너비를 지정해야 합니다
 }
'''


# JSON 파일 로드
import json
json_file = '/USER/final_project/detectron2/output/inference/coco_instances_results.json'


from pycocotools import mask
import numpy as np

with open(json_file, 'r') as file:
    data = json.load(file)

# 면적 계산을 위한 딕셔너리 초기화
area_per_category = {}

# 각 인스턴스에 대한 RLE 디코딩 및 면적 계산 수행
for item in data:
    image_id = item['image_id']
    category_id = item['category_id']
    rle = {
        'counts': item['segmentation']['counts'],
        'size': item['segmentation']['size']
    }
    decoded_mask = mask.decode(rle)
    area = np.sum(decoded_mask)  # 마스크 내 1의 값을 가진 픽셀 수 계산

    # 결과 저장
    if image_id not in area_per_category:
        area_per_category[image_id] = {}
    if category_id not in area_per_category[image_id]:
        area_per_category[image_id][category_id] = 0
    area_per_category[image_id][category_id] += area

# 결과 출력
for image_id, categories in area_per_category.items():
    print(f"Image ID: {image_id}")
    for category_id, area in categories.items():
        print(f"  Category ID {category_id}: Area = {area}")






