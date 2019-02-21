# Raspberry Pie Reading Book
Writing is a form of information that has contributed greatly to the explosive growth of mankind. <br/>
However, there are people who have difficulty accessing information(Writing) that is visually provided, <br/>
such as illiterate or visually impaired. <br/>
In this Project, I tried to implement a system that converts non-standard documents to speech and outputs them. <br/>
글이란 인류가 폭발적으로 성장하는데 큰 기여를 한 정보 전달 형태다. <br/>
그러나 문맹, 시각장애인 등 시각적으로 제공되는 글에 대한 접근이 어려운 사람들은 우리 주변에 존재한다. <br/>
본 프로젝트는 이들을 위해 비정형화된 형태의 문서일지라도 음성으로 변환해서 출력해주는 시스템을 구현하고자 하였다. <br/><br/>

# 1. Setting up the Raspberry Pie for Development
```
A. Installing the USB Microphone / USB 마이크 설치하기 <br/>
(link) http://makeshare.org/bbs/board.php?bo_table=raspberrypi&wr_id=76
B. Configure and Test the Audio / 오디오 환경을 위한 설치 <br/>
(link) https://developers.google.com/assistant/sdk/guides/library/python/embed/audio
C. Recording a voice file with the extension raw / 확장명이 raw인 음성파일 녹화하기 <br/>
(link) https://github.com/larsimmisch/pyalsaaudio
```
# 2. 
(link) https://cloud.google.com/vision/docs/detecting-text?hl=ko 
```
def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    for text in texts:
        print('\n"{}"'.format(text.description))
detect_text(‘https://i.stack.imgur.com/t3qWG.png’)
```

