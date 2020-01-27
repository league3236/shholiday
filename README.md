# 사용방법

- pip 설치

```bash
#pip install shholiday
```


- 임시 사용

```python
from shholiday import holiday2020

daytuple = (1,1) # 1월 1일이 휴일인지 확인하고 싶을 때
nowholiday = holiday2020()
print(nowholiday.is_holiday(daytuple))
```

- 오늘 날짜가 휴일인지 확인 예시

```python
from shholiday import holiday2020
from datetime import  datetime

    
now = datetime.now()
daytuple = (str(now.month),str(now.day))

nowholiday = holiday2020()
print(nowholiday.is_holiday(daytuple))
```