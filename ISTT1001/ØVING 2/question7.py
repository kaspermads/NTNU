from math import factorial as fact

def antall_gunstige(antall_batterier):
    return    ((fact(antall_batterier))/(fact(2)*fact((antall_batterier-2))))

def antall_mulige(antall_batterier):
    return    ((fact(antall_batterier))/(fact(2)*fact((antall_batterier-2))))

def betinget_sannsynlighet(antall_batterier):
    return (antall_gunstige(antall_batterier)/antall_mulige(antall_batterier))

print(antall_gunstige(10)/antall_mulige(12))
