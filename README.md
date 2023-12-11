# 이어드림 스쿨 3기 스타트업 연계 프로젝트
#### DS 3팀 - 시간의 흐름에 따른 노후 인프라시설 건축물의 외관과 내부 Crack 감지 (소테리아에이트)
- Project Peroid : 23.11.08~23.12.15
- Team : 맘에들었조
- Member : 양태경, 김다현, 임승준, 이지윤, 이종은, 박정재

### Topic
- asdasd

### Stacks
<!--Table-->
|Category|Description|
|:--:|:--:|
|**Environment**|![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)|
|**Languag**e|![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
|**Storage**|![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)|
|**Deeplearning**|![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)|
|**ImageProcessing**|![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)|
|**Visualization**|![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)|
|**Communication**|![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)![Zoom](https://img.shields.io/badge/Zoom-2D8CFF?style=for-the-badge&logo=zoom&logoColor=white)|




### Modeling FrameWork
- mmdetection, detectron2, ultralytics

### Requirements




***
### Repository 
<!--Table-->
|Category|Description|
|:--:|:--:|
|ImageRetrieval|Cell2|
|DataProcessing|Cell2|
|Detectron2|Cell2|
|mmdetection|Cell2|
|yolov8|Cell2|

```bash
├── README.md
├── package-lock.json
├── package.json
├── strapi-backend : 
│   ├── README.md
│   ├── api : db model, api 관련 정보 폴더
│   │   ├── about
│   │   ├── course
│   │   └── lecture
│   ├── config : 서버, 데이터베이스 관련 정보 폴더
│   │   ├── database.js
│   │   ├── env : 배포 환경(NODE_ENV = production) 일 때 설정 정보 폴더
│   │   ├── functions : 프로젝트에서 실행되는 함수 관련 정보 폴더
│   │   └── server.js
│   ├── extensions
│   │   └── users-permissions : 권한 정보
│   ├── favicon.ico
│   ├── package-lock.json
│   ├── package.json
│   └── public
│       ├── robots.txt
│       └── uploads : 강의 별 사진
└── voluntain-app : 프론트엔드
    ├── README.md
    ├── components
    │   ├── CourseCard.js
    │   ├── Footer.js
    │   ├── LectureCards.js
    │   ├── MainBanner.js : 메인 페이지에 있는 남색 배너 컴포넌트, 커뮤니티 이름과 슬로건을 포함.
    │   ├── MainCard.js
    │   ├── MainCookieCard.js
    │   ├── NavigationBar.js : 네비게이션 바 컴포넌트, _app.js에서 공통으로 전체 페이지에 포함됨.
    │   ├── RecentLecture.js
    │   └── useWindowSize.js
    ├── config
    │   └── next.config.js
    ├── lib
    │   ├── context.js
    │   └── ga
    ├── next.config.js
    ├── package-lock.json
    ├── package.json
    ├── pages
    │   ├── _app.js
    │   ├── _document.js
    │   ├── about.js
    │   ├── course
    │   ├── index.js
    │   ├── lecture
    │   ├── newcourse
    │   ├── question.js
    │   └── setting.js
    ├── public
    │   ├── favicon.ico
    │   └── logo_about.png
    └── styles
        └── Home.module.css

```

<!--
```bash
├── README.md : 리드미 파일
│
├── strapi-backend/ : 백엔드
│   ├── api/ : db model, api 관련 정보 폴더
│   │   └── [table 이름] : database table 별로 분리되는 api 폴더 (table 구조, 해당 table 관련 api 정보 저장)
│   │       ├── Config/routes.json : api 설정 파일 (api request에 따른 handler 지정)
│   │       ├── Controllers/ [table 이름].js : api controller 커스텀 파일
│   │       ├── Models : db model 관련 정보 폴더
│   │       │   ├── [table 이름].js : (사용 X) api 커스텀 파일
│   │       │   └── [table 이름].settings.json : model 정보 파일 (field 정보)
│   │       └─── Services/ course.js : (사용 X) api 커스텀 파일
│   │ 
│   ├── config/ : 서버, 데이터베이스 관련 정보 폴더
│   │   ├── Env/production : 배포 환경(NODE_ENV = production) 일 때 설정 정보 폴더
│   │   │   └── database.js : production 환경에서 database 설정 파일
│   │   ├── Functions : 프로젝트에서 실행되는 함수 관련 정보 폴더
│   │   │   │   ├── responses : (사용 X) 커스텀한 응답 저장 폴더
│   │   │   │   ├── bootstrap.js : 어플리케이션 시작 시 실행되는 코드 파일
│   │   │   │   └── cron.js : (사용 X) cron task 관련 파일
│   │   ├── database.js : 기본 개발 환경(NODE_ENV = development)에서 database 설정 파일
│   │   └── server.js : 서버 설정 정보 파일
│   │  
│   ├── extensions/
│   │   └── users-permissions/config/ : 권한 정보
│   │ 
│   └── public/
│       └── uploads/ : 강의 별 사진
│
└── voluntain-app/ : 프론트엔드
    ├── components/
    │   ├── NavigationBar.js : 네비게이션 바 컴포넌트, _app.js에서 공통으로 전체 페이지에 포함됨.
    │   ├── MainBanner.js : 메인 페이지에 있는 남색 배너 컴포넌트, 커뮤니티 이름과 슬로건을 포함.
    │   ├── RecentLecture.js : 사용자가 시청 정보(쿠키)에 따라, 현재/다음 강의를 나타내는 컴포넌트 [호출: MainCookieCard]
    │   ├── MainCookieCard.js : 상위 RecentLecture 컴포넌트에서 전달받은 props를 나타내는 레이아웃 컴포넌트.
    │   ├── MainCard.js : 현재 등록된 course 정보를 백엔드에서 받아서 카드로 나타내는 컴포넌트 [호출: CourseCard]
    │   └── CourseCard.js : 상위 MainCard 컴포넌트에서 전달받은 props를 나타내는 레이아웃 컴포넌트
    │
    ├── config/
    │   └── next.config.js
    │
    ├── lib/
    │   └── ga/
    │   │   └── index.js
    │   └── context.js
    │
    ├── pages/
    │   ├── courses/
    │   │   └── [id].js : 강의 페이지
    │   ├── _app.js : Next.js에서 전체 컴포넌트 구조를 결정, 공통 컴포넌트(navbar, footer)가 선언되도록 customizing 됨.
    │   ├── _document.js : Next.js에서 전체 html 문서의 구조를 결정, lang 속성과 meta tag가 customizing 됨.
    │   ├── about.js : 단체 소개 페이지
    │   ├── index.js : 메인 페이지
    │   ├── question.js : Q&A 페이지
    │   └── setting.js : 쿠키, 구글 애널리틱스 정보 수집 정책 페이지
    │
    ├── public/
    │   ├── favicon.ico : 네비게이션바 이미지
    │   └── logo_about.png : about 페이지 로고 이미지
    │
    └── styles/
        └── Home.module.css

```
-->


***
### Acknowledgement
We refer to the following website to implement our models ("site")
