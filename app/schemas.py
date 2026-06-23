from pydantic import BaseModel

class MachineInput(BaseModel):

    Type: int

    Air_temperature_K: float

    Process_temperature_K: float

    Rotational_speed_rpm: float

    Torque_Nm: float

    Tool_wear_min: float

    Thermal_Stress_Index: float

    Wear_Efficiency: float

    Operational_Load_Index: float

    Temperature_Ratio: float

    Failure_Risk_Score: float