�
)@�['  �               @   s3   d  d l  m Z m Z Gd d �  d e j � Z d S)�    )�
migrations�modelsc               @   s  e  Z d  Z d Z g  Z e j d d d d e j d d d d d d	 d
 d � f d e j	 d d � f d e j	 d d � f d e j	 d d � f d e j	 d d � f d e j	 d d � f d e j	 d d � f d e j
 �  f d e j
 �  f d e j	 d d � f d e j
 �  f g � g Z d S)�	MigrationT�name�EmployeeInfo�fields�id�auto_created�primary_key�	serializeF�verbose_name�ID�	User_Name�
max_length�2   �Password�   �Role�   �
First_Name�	Last_Name�Email�Phone_Number�Employee_Id�Address�Pin_CodeN)�__name__�
__module__�__qualname__�initial�dependenciesr   �CreateModelr   �	AutoField�	CharField�IntegerField�
operations� r&   r&   �KC:\Users\Anu\Desktop\EmployeeManagement\employee\migrations\0001_initial.pyr      s   	'r   N)�	django.dbr   r   r   r&   r&   r&   r'   �<module>   s   