�
�B�[D  �               @   s-   d  d l  m Z Gd d �  d e j � Z d S)�    )�modelsc               @   s�   e  Z d  Z e j d d � Z e j d d � Z e j d d � Z e j d d � Z e j d d � Z	 e j d d � Z
 e j �  Z e j �  Z e j d d � Z e j �  Z d d �  Z d S)�EmployeeInfo�
max_length�   �   �2   c             C   s   |  j  S)N)�
First_Name)�self� r
   �:C:\Users\Anu\Desktop\EmployeeManagement\employee\models.py�__str__   s    zEmployeeInfo.__str__N)�__name__�
__module__�__qualname__r   �	CharFieldZ	User_NameZPasswordZRoler   Z	Last_NameZEmail�IntegerFieldZPhone_NumberZEmployee_Id�AddressZPin_Coder   r
   r
   r
   r   r      s   r   N)�	django.dbr   �Modelr   r
   r
   r
   r   �<module>   s   