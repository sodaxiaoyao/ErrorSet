@echo off

::���÷���
rem sc config ������ start= AUTO    (�Զ�)
rem sc config ������ start= DEMAND  (�ֶ�)
rem sc config ������ start= DISABLED(����)

::��������
rem net start ������

::�رշ���
net stop ������

::ɾ������
sc delete ������ 

::��ѯ����
sc query ������ 

pause