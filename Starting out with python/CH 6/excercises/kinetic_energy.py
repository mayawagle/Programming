#This program asks the user for the mass and velocity of
#an object. It then displays the object's Kinetic energy

#define the main:
def main():
    mass = float(input("Enter the object's mass in kgs: "))
    velocity = float(input("Enter the object's velocity in meters per second:  "))
    print(f"The object's kinetic energy is {format(kinetic_energy(mass,velocity), '.2f')}")

#define the kinetic_energy function
def kinetic_energy(mass,velocity):
    return 0.5 * mass * (velocity ** 2)

#run the main
main()