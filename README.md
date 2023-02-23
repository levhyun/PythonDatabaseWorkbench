# PythonDatabaseWorkbench
Python Database Workbench for Koreans Using Socket Communication


<br><br>


### **Commands**
---
|Id|Name|Skill|
|:---:|:---:|:---:|
|SELECT|조회|데이터를 조회하는 기능|
|CREATE|생성|테이블을 생성하는 기능|
|USE|사용|데이터베이스를 지정하는 기능|
|INSERT|추가|데이터를 추가하는 기능|
|DELETE|삭제|데이터를 삭제하는 기능|
|ALTER|변경|데이터를 변경하는 기능|
---


<br><br>


### **Command Type**
---
**[조회]**
```
데이터베이스 조회 Pysql>조회 {옵션} [데이터베이스명]
테이블 조회 Pysql>조회 {옵션} [테이블명] [조건]
```
```
데이터베이스 조회 ex) 조회 -d [학교]
테이블 조회 ex) 조회 -t [교실] [class<5]
```
|Option|Skill|
|:---:|:---:|
|-d|데이터베이스를 조회하다|
|-t|테이블을 조회하다|

<br>

**[생성]**
```
데이터베이스 생성 Pysql>생성 {옵션} [데이터베이스명]
테이블 생성 Pysql>생성 {옵션} [테이블명] [속성명] [자료형]
```
```
데이터베이스 생성 ex) 생성 -d [학교] 
테이블 생성 ex) 생성 -t [grade,class,number,name,gender] [int,int,int,char,char]
```
|Option|Skill|
|:---:|:---:|
|-d|데이터베이스를 생성하다|
|-t|테이블을 생성하다|

<br>

**[사용]**
```
Pysql>사용 [데이터베이스명]
```
```
ex) 사용 [학교]
```

<br>

**[추가]**
```
Pysql>추가 [테이블명] [속성명] [값]
```
```
ex) 추가 [학생] [grade,class,number,name,gender] [1,2,3,test,male]
```

<br>

**[삭제]**
```
데이터베이스 삭제 Pysql>삭제 {옵션} [데이터베이스명]
테이블 삭제 Pysql>삭제 {옵션} [테이블명]
```
```
데이터베이스 삭제 ex) 삭제 -d [데이터베이스명]
테이블 삭제 ex) 삭제 -t [테이블명]
```
|Option|Skill|
|:---:|:---:|
|-d|데이터베이스를 삭제하다|
|-t|테이블을 삭제하다|

<br>

**[변경]**
```
Pysql>조회 [테이블명] [변경식] [조건]
```
```
ex) 조회 [학생] [gender=female]  [number<5]
```
---


<br><br>


