from django.db import models

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=15)
    dsg=models.CharField(max_length=20)
    salary=models.IntegerField()
    city=models.CharField(max_length=20,default="",null=True,blank=True)
    state=models.CharField(max_length=20,default="",null=True,blank=True)

    def __str__(self):
        return str(self.id)+'/'+self.name+'/'+self.email


"""
create table Employee(
    id int auto_increment primary key,
    name varchar(20) not null,
    email varchar(30) not null,
    phone varchar(15) not null,
    dsg varchar(20) not null,
    salary int not null,
    city varchar(20),
    state varchar(20)    
)

"""