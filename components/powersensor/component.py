import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import UNIT_WATT, DEVICE_CLASS_ENERGY, STATE_CLASS_MEASUREMENT

CODEOWNERS = ["@ton_nom"]  # Facultatif

powersensor_ns = cg.esphome_ns.namespace("powersensor")
MyPowerSensor = powersensor_ns.class_("MyPowerSensor", cg.PollingComponent)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(MyPowerSensor),
    cv.Required("update_interval", default="5000ms"): cv.positive_time_period_milliseconds,
}).extend(cv.polling_component_schema("5000ms"))

async def to_code(config):
    var = cg.new_Pvariable(config[cv.GenerateID()])
    await cg.register_component(var, config)
