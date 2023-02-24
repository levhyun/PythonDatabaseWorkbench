# PythonDatabaseWorkbench
Python Database Workbench for Koreans Using Socket Communication


<br><br>


### **Commands**
---
|Id|Name|Skill|
|:---:|:---:|:---:|
|SELECT|조회|데이터를 조회하는 기능|
|CREATE|생성|테이블을 생성하는 기능|
|INSERT|추가|데이터를 추가하는 기능|
|DELETE|삭제|데이터를 삭제하는 기능|
|ALTER|변경|데이터를 변경하는 기능|
---


<br><br>


### **Command Type**
---
**[조회]**
```
테이블 목록 조회 Pysql>조회 {옵션}
테이블 조회 Pysql>조회 {옵션} [테이블명] [속성명] [조건]
테이블 타입 조회 Pysql>조회 {옵션} [테이블명]
```
```
테이블 목록 조회 ex) 조회 -t
테이블 조회 ex) 조회 -r [교실] [*] [class<5]
테이블 타입 조회 ex) 조회 -a [교실]
```
|Option|Skill|
|:---:|:---:|
|-t|테이블 목록을 조회하다|
|-r|테이블 값을 조회하다|
|-a|테이블 타입을 조회하다|

<br>

**[생성]**
```
테이블 생성 Pysql>생성 [테이블명] [속성명] [자료형]
```
```
테이블 생성 ex) 생성 [교실] [grade,class,number,name] [int,int,int,char]
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
테이블 삭제 Pysql>삭제 [테이블명]
```
```
테이블 삭제 ex) 삭제 [학교]
```

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


