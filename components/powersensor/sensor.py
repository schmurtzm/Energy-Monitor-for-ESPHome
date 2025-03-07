import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import UNIT_WATT, DEVICE_CLASS_ENERGY, STATE_CLASS_MEASUREMENT

powersensor_ns = cg.esphome_ns.namespace("powersensor")
MyPowerSensor = powersensor_ns.class_("MyPowerSensor", sensor.Sensor, cg.PollingComponent)

CONFIG_SCHEMA = sensor.sensor_schema({
    cv.GenerateID(): cv.declare_id(MyPowerSensor),
    cv.Optional("realpower_sensor1"): sensor.sensor_schema(),
    cv.Optional("realpower_sensor2"): sensor.sensor_schema(),
    cv.Optional("realpower_sensor3"): sensor.sensor_schema(),
    cv.Optional("realpower_sensor4"): sensor.sensor_schema(),
}).extend(cv.polling_component_schema("5000ms"))

async def to_code(config):
    var = cg.new_Pvariable(config[cv.GenerateID()])
    await cg.register_component(var, config)

    if "realpower_sensor1" in config:
        realpower_sensor1 = await sensor.new_sensor(config["realpower_sensor1"])
        cg.add(var.set_sensor1(realpower_sensor1))

    if "realpower_sensor2" in config:
        realpower_sensor2 = await sensor.new_sensor(config["realpower_sensor2"])
        cg.add(var.set_sensor2(realpower_sensor2))

    if "realpower_sensor3" in config:
        realpower_sensor3 = await sensor.new_sensor(config["realpower_sensor3"])
        cg.add(var.set_sensor3(realpower_sensor3))

    if "realpower_sensor4" in config:
        realpower_sensor4 = await sensor.new_sensor(config["realpower_sensor4"])
        cg.add(var.set_sensor4(realpower_sensor4))
