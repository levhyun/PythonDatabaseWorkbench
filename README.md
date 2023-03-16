# PythonDatabaseWorkbench
Python Database Workbench for Koreans Using Socket Communication


<br><br>


### **Commands**
---
|Id|Name|Skill|
|:---:|:---:|:---:|
|SELECT,DESC|조회|데이터를 조회하는 기능|
|CREATE|생성|테이블을 생성하는 기능|
|INSERT|추가|데이터를 추가하는 기능|
|DELETE,DROP|삭제|데이터를 삭제하는 기능|
|ALTER,UPDATE|수정|데이터를 변경하는 기능|
---


<br><br>


### **Command Type**
---

<br>

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
테이블 생성 Pysql>생성 [테이블명] [속성] [자료형]
```
```
테이블 생성 ex) 생성 [교실] [grade,class,number,name] [int(100),int(100),int(100),char(100)]
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
테이블 삭제 Pysql>삭제 {옵션} [테이블명]
테이블 값 삭제 Pysql>삭제 {옵션} [테이블명] [조건]
```
```
테이블 삭제 ex) 삭제 -t [학교]
테이블 값 삭제 ex) 삭제 -r [학교] [class>4]
```
|Option|Skill|
|:---:|:---:|
|-t|테이블을 삭제하다|
|-r|테이블 값을 삭제하다|

<br>

**[수정]**
```
테이블 수정 - ADD Pysql> 수정 -t {모드} [테이블명] [속성] [자료형]
테이블 수정 - MODIFY Pysql> 수정 -t {모드} [테이블명] [속성] [자료형]
테이블 수정 - CHANGE Pysql> 수정 -t {모드} [원래속성명] [변경할속성명] [속성] [자료형]
테이블 수정 - DROP Pysql> 수정 -t {모드} [테이블명] [속성]
테이블 수정 - RENAME Pysql> 수정 -t {모드} [원래테이블명] [변경할테이블명]
테이블 값을 수정 Pysql> 수정 -r [테이블명] [변경식] [조건]
```
```
테이블 수정 - ADD ex) 수정 -t ADD [test2] [d] [int(64)]
테이블 수정 - MODIFY ex) comming soon
테이블 수정 - CHANGE ex) comming soon
테이블 수정 - DROP ex) comming soon
테이블 수정 - RENAME ex) comming soon
테이블 값을 수정 ex) 수정 -r [학생] [gender=female]  [number<5]
```
|Option|Skill|
|:---:|:---:|
|-t|테이블을 수정하다|
|-r|테이블 값을 삭제하다|

|Mod|Skill|
|:---:|:---:|
|ADD|칼럼을 추가한다|
|MODIFY|칼럼을 변경한다|
|CHANGE|칼럼 이름까지 변경한다|
|DROP|칼럼을 삭제한다|
|RENAME|테이블 이름을 변경한다|

<br>

---


<br><br>


