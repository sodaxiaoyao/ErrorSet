@echo off

::�����ļ�
mkdir %cd%\test\
md go..\

::�ı�λ��
cd /d %~d0

::ɾ���ļ�
rd /s /q %cd%\test\
rmdir /s /q %cd%\go..\

::������ݣ���>���ض������
echo "test" > test.txt

::��ʾ�ļ�����
type test.txt

::ѭ����� set(��ʼ����������β)
for /l %%i in (1,1,6) do (echo %%i)

::��ʾ��ǰĿ¼
dir

::���û�����ʾϵͳ��������
path %PATH%;

::����Ŀ¼��
tree

::�鿴����
tasklist


pause 