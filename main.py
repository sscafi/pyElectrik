import math

class PhysicsSimulator:
    def __init__(self):
        self.constants = {
            "g": 9.81,  # gravitational acceleration (m/s^2)
            "e": 1.602e-19,  # elementary charge (C)
            "ε0": 8.854e-12,  # vacuum permittivity (F/m)
            "μ0": 4 * math.pi * 1e-7,  # vacuum permeability (H/m)
        }

        self.electrical_components = {
            "Resistor": {"symbol": "R", "units": "Ω"},
            "Capacitor": {"symbol": "C", "units": "F"},
            "Inductor": {"symbol": "L", "units": "H"},
        }

        self.electrical_laws = {
            "Ohm's Law": {"equation": "V = I * R", "description": "Relates voltage, current, and resistance"},
            "Kirchhoff's Voltage Law": {"equation": "ΣV = 0", "description": "States that the sum of voltage changes around a closed loop is zero"},
            "Kirchhoff's Current Law": {"equation": "ΣI = 0", "description": "States that the sum of current entering a node is equal to the sum of current leaving a node"},
        }

        self.electrical_circuits = {
            "Series RC Circuit": {"components": ["R", "C"], "equation": "V = V0 * e^(-t/RC)"},
            "Parallel RL Circuit": {"components": ["R", "L"], "equation": "I = I0 * e^(-t/LR)"},
        }

    def simulate_circuit(self, circuit_name, values):
        circuit = self.electrical_circuits[circuit_name]
        components = circuit["components"]
        equation = circuit["equation"]

        print(f"Simulating {circuit_name} circuit:")
        print(f"Components: {', '.join(components)}")
        print(f"Equation: {equation}")

        # Simulate the circuit by plugging in the given values
        result = eval(equation, {"V0": values["V0"], "I0": values["I0"], "R": values["R"], "C": values["C"], "L": values["L"], "t": values["t"]})

        print(f"Result: {result:.2f} {self.electrical_components[components[0]]['units']}")

    def list_components(self):
        print("Available electrical components:")
        for component in self.electrical_components.keys():
            print(f"- {component} ({self.electrical_components[component]['symbol']})")

    def list_laws(self):
        print("Available electrical laws:")
        for law in self.electrical_laws.keys():
            print(f"- {law} ({self.electrical_laws[law]['equation']})")

    def list_circuits(self):
        print("Available electrical circuits:")
        for circuit in self.electrical_circuits.keys():
            print(f"- {circuit}")

def main():
    simulator = PhysicsSimulator()

    while True:
        print("Physics Simulator")
        print("---------------")
        print("1. List electrical components")
        print("2. List electrical laws")
        print("3. List electrical circuits")
        print("4. Simulate a circuit")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            simulator.list_components()
        elif choice == "2":
            simulator.list_laws()
        elif choice == "3":
            simulator.list_circuits()
        elif choice == "4":
            circuit_name = input("Enter the circuit name: ")
            values = {}
            for component in simulator.electrical_circuits[circuit_name]["components"]:
                value = float(input(f"Enter the value of {component}: "))
                values[component] = value
            values["t"] = float(input("Enter the time: "))
            simulator.simulate_circuit(circuit_name, values)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()