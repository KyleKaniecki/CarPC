
import obd
import os


class OBDManager():

    def __init__(self):

        self.obd_controller = obd.OBD("/dev/rfcomm0")

        self.first_commands = {"Speed": obd.commands.SPEED,
                               "RPM": obd.commands.RPM,
                               "Throttle Position": obd.commands.THROTTLE_POS,
                               "Engine Load": obd.commands.ENGINE_LOAD
                               }

        self.second_commands = {"Coolant Temp": obd.commands.COOLANT_TEMP,
                                "Air Intake Temp": obd.commands.INTAKE_TEMP,
                                "Barometric Pressure": obd.commands.BAROMETRIC_PRESSURE,
                                "Catalyst Temp": obd.commands.CATALYST_TEMP_B1S1
                                }

        self.third_commands = {"Fuel Level": obd.commands.FUEL_LEVEL,
                               "Run Time": obd.commands.RUN_TIME,
                               "Air Flow Rate": obd.commands.MAF,
                               "Timing Advance": obd.commands.TIMING_ADVANCE
                               }

    def queryAdapter(self, table=1):
        responses = {}

        if(table == 1):
            for key in self.first_commands.keys():
                resp = self.obd_controller.query(self.first_commands[key])

                if resp.value.units == "degC":
                    resp.value = resp.value.to('degF')
                elif resp.value.units == 'kph':
                    resp.value = resp.value.to('mph')

                responses[key] = ("%.2f " + str(resp.value.units)) % resp.value.magnitude

        elif(table == 2):
            for key in self.second_commands.keys():
                resp = self.obd_controller.query(self.second_commands[key])

                if resp.value.units == "degC":
                    resp.value = resp.value.to('degF')
                elif resp.value.units == 'kph':
                    resp.value = resp.value.to('mph')

                responses[key] = ("%.2f " + str(resp.value.units)) % resp.value.magnitude

        else:
            for key in self.third_commands.keys():
                resp = self.obd_controller.query(self.third_commands[key])
                
                if resp.value.units == "degC":
                    resp.value = resp.value.to('degF')
                elif resp.value.units == 'kph':
                    resp.value = resp.value.to('mph')

                responses[key] = ("%.2f " + str(resp.value.units)) % resp.value.magnitude

        return responses

    def celsius_to_fahrenheit(self, value):
        return int((value * 9.0 / 5.0) + 32)

    def connectToAdapter(self):
        return os.system("sudo rfcomm bind 00:1D:A5:00:04:A9")
