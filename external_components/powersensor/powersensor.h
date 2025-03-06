#pragma once

#include "esphome.h"
#include "EmonLib.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/core/component.h"

namespace esphome {
namespace powersensor {
	
	
class MyPowerSensor : public sensor::Sensor, public PollingComponent {
 public:
  EnergyMonitor emon1;
  EnergyMonitor emon2;
  EnergyMonitor emon3;
  EnergyMonitor emon4;

  Sensor *realpower_sensor1 = new Sensor();
  Sensor *realpower_sensor2 = new Sensor();
  Sensor *realpower_sensor3 = new Sensor();
  Sensor *realpower_sensor4 = new Sensor();

  MyPowerSensor() : PollingComponent(5000) {}

  void setup() override {
    // Initialisation des capteurs de courant
    emon1.mycurrent(34, 4.9);
    emon2.mycurrent(35, 4.9);
    emon3.mycurrent(36, 4.9);
    emon4.mycurrent(39, 4.9);

    // Enregistrer les capteurs pour ESPHome
		// register_sensor(realpower_sensor1);
		// register_sensor(realpower_sensor2);
		// register_sensor(realpower_sensor3);
		// register_sensor(realpower_sensor4);
  }

  void update() override {
    // Calcul et publication des valeurs
    realpower_sensor1->publish_state(emon1.mycalcIrms(1480) * 238.6);
    realpower_sensor2->publish_state(emon2.mycalcIrms(1480) * 238.6);
    realpower_sensor3->publish_state(emon3.mycalcIrms(1480) * 238.6);
    realpower_sensor4->publish_state(emon4.mycalcIrms(1480) * 238.6);
  }
};

}  // namespace empty_sensor
}  // namespace esphome