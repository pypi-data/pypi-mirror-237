# pip install cantera

# retenir cette bibliothèque qui est bien !

import cantera as ct
import CoolProp.CoolProp as CP

print(f"Using Cantera version: {ct.__version__}")

gas = ct.Solution("gri30.yaml")

# Set reactants state
gas.TPX = 298, 101325, "CH4:1, O2:2"
h1 = gas.enthalpy_mass
Y_CH4 = gas["CH4"].Y[0]  # returns an array, of which we only want the first element

# set state to complete combustion products without changing T or P
gas.TPX = None, None, "CO2:1, H2O:2"
h2 = gas.enthalpy_mass

LHV = -(h2 - h1) / Y_CH4 / 1e6
print(f"LHV = {LHV:.3f} MJ/kg")


water = ct.Water()
# Set liquid water state, with vapor fraction x = 0
water.TQ = 298, 0
h_liquid = water.h
# Set gaseous water state, with vapor fraction x = 1
water.TQ = 298, 1
h_gas = water.h

# Calculate higher heating value
Y_H2O = gas["H2O"].Y[0]
HHV = -(h2 - h1 + (h_liquid - h_gas) * Y_H2O) / Y_CH4 / 1e6
print(f"HHV = {HHV:.3f} MJ/kg")

print(HHV/LHV)

def heating_value(fuel):
    """Returns the LHV and HHV for the specified fuel"""
    gas.TP = 298, ct.one_atm
    gas.set_equivalence_ratio(1.0, fuel, "O2:1.0")
    h1 = gas.enthalpy_mass
    Y_fuel = gas[fuel].Y[0]

    # complete combustion products
    X_products = {
        "CO2": gas.elemental_mole_fraction("C"),
        "H2O": 0.5 * gas.elemental_mole_fraction("H"),
        "N2": 0.5 * gas.elemental_mole_fraction("N"),
    }

    gas.TPX = None, None, X_products
    Y_H2O = gas["H2O"].Y[0]
    h2 = gas.enthalpy_mass
    LHV = -(h2 - h1) / Y_fuel / 1e6
    HHV = -(h2 - h1 + (h_liquid - h_gas) * Y_H2O) / Y_fuel / 1e6

       # Calculate the density at standard conditions (298 K, 1 atm)
    if fuel=="C2H6":
        fuel="ethane"
    if fuel=="CH3OH":
        fuel="methanol" 
    rho = CP.PropsSI("D", "T", 273.15, "P", 101325, fuel)
    print(fuel)
    print(rho)
    # Convert LHV and HHV to kWh/Nm^3
    LHV_kWh_Nm3 = LHV * rho / 3.600  # Convert from MJ/kg to kWh/Nm^3
    HHV_kWh_Nm3 = HHV * rho / 3.600  # Convert from MJ/kg to kWh/Nm^3
    print(LHV_kWh_Nm3)
    print(HHV_kWh_Nm3)

    return LHV, HHV,LHV_kWh_Nm3,HHV_kWh_Nm3


fuels = ["H2", "CH4", "C2H6", "C3H8", "NH3", "CH3OH"]
print("fuel   LHV (MJ/kg)   HHV (MJ/kg)")
for fuel in fuels:
    LHV, HHV,LHV_kWh_Nm3,HHV_kWh_Nm3 = heating_value(fuel)
    print(f"{fuel:8s} {LHV:7.2f}      {HHV:7.2f}  {LHV_kWh_Nm3:7.2f}      {HHV_kWh_Nm3:7.2f}")