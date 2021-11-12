User.object.filter(name__exact="Amir")

User.object.filter(name__iexact="Sahebi")

User.object.filter(address__gt="2000-01-01")

User.object.filter(address__startswith="tehran")

User.object.exclude(address__startswith="tehran")

User.object.filter(id_in=[1,2,3,4])