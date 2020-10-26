# --------------
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = [ 'Hilary Mason','Carla Gentry','Corinna Cortes']

new_class = class_1 + class_2

print(new_class,end=' ')

courses = {'Math':65,'English':70,'History':80,'Frensch':70,'Science':60}

Total = 0
for i in courses.values():
    Total += i
print(Total)

percentage = (Total/500)*100

print(percentage)

mathematics= {'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,
              'Corinna Cortes':66,'Peter Warden':75}
topper=max(mathematics,key=mathematics.get)
print(topper)

last_name = topper.split(' ')[1]
first_name = topper.split(' ')[0]

certificate_name = (last_name + ' ' +first_name).upper()
certificate_name


