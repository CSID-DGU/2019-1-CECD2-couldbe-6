## S13RNG - Random Number Generator Based on SHA-1 Hash Function
### Introduction
S13RNG는 기존의 문제점을 해결하고자 만든 새로운 Random Number 생성 방법입니다.

기존의 문제점: C언어 / Java의 선형 합동법, Python / C++의 메르센 트위스터 방법의 난수 예측이 가능함
### How To Generate
Set Seed and Modular, and Generate (Use Random)
### How To Use
Import S13RNG.py to your program
### How to Complie GUI (optional)
!!! Requires PyQt5, pyinstaller !!!

pyinstaller -F -w --clean --path "PyQt5 path" Project.py or UIInit.py

Project.py -> to run, need project.ui

UIInit.py -> no need project.ui
